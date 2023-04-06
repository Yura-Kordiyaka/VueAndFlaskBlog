<template>
  <div class="container_main">
    <div class="navbar">
      <div class="container">
        <h1 class="navbar-brand">It's user page</h1>
        <div class="navbar-wrap">
          <div class="navbar-menu">
            <ul>
                <li class="dropdown">
                <button class="dropdown-toggle" @click="isOpen = !isOpen">Category</button>
                <div v-if="isOpen" class="dropdown-menu">
                  <ul>
                    <li v-for="(item,index) in all_category" :key="index">
                      <button @click="GetPostWithCategory(item)">{{ item }}</button>
                    </li>
                  </ul>
                </div>
              </li>
              <li>
                <button @click="showAllPost">Show all Post</button>
              </li>
              <li>
                <button @click="showMyPost">Show my Post</button>
              </li>
              <li>
                <button @click="createPost">Crate Post</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="window_from_login" v-show="this.previousPath==='/Login'">
      <h3>successful login</h3>
      <button @click="Close">Close</button>
    </div>
    <div class="container_post" v-if="posts.length!==0">
      <div class="paginator">
        <a class="previous"
           @click.prevent="currentPage!==1 ? changePage(currentPage-1) : changePage(currentPage) ">
          Previous
        </a>
        <ul class="count_of_page">
          <li v-for="pageNumber in totalPages" :key="pageNumber">
            <a :class="{'active': pageNumber===currentPage }" @click.prevent="changePage(pageNumber)">
              {{ pageNumber }}
            </a>
          </li>
        </ul>
        <a class="next" @click.prevent="currentPage!==totalPages ? changePage(currentPage+1) : changePage(currentPage)">
          Next
        </a>
      </div>
      <div class="posts">
        <ul class="one_post">
          <li v-for="(post, index) in paginatedItems" :key="index">
            <div class="name_of_post">
              <h3>{{ post.name_of_post }}</h3>
            </div>
            <div class="text_of_post">
              <p>
                {{ post.text_of_post }}
              </p>
            </div>
            <div class="button_like_dislike">
              <button class="btn_like" v-if="post.user_id!==user_id" @click="AddLike(post.id)">
                <font-awesome-icon class="like" icon="fa-solid fa-thumbs-up"/>
                <span class="count_of_like">{{ post.like }}</span>
              </button>
              <button class="btn_like" v-else>
                <font-awesome-icon class="like" icon="fa-solid fa-thumbs-up"/>
                <span class="count_of_dislike">{{ post.like }}</span>
              </button>
              <button class="btn_dislike" v-if="post.user_id!==user_id" @click.prevent="AddDislike(post.id)">
                <font-awesome-icon class="dislike" icon="fa-solid fa-thumbs-down"/>
                <span class="count_of_dislike">{{ post.dislike }}</span>

              </button>
              <button class="btn_dislike" v-else>
                <font-awesome-icon class="dislike" icon="fa-solid fa-thumbs-down"/>
                <span class="count_of_dislike">{{ post.dislike }}</span>
              </button>
            </div>
            <div class="add_comment" v-if="user_id!==post.user_id">
              <textarea placeholder="live your comment" v-model="post.comment">
              </textarea>
              <button v-if="post.comment!==null && post.comment.length!==0"
                      @click.prevent="AddComent(post.id,post.comment,index)">Add Comment
              </button>
              <div v-if="comments_to_add['error'] && Number(comments_to_add['post_id'])===post.id">
                {{ comments_to_add['error'] }}
              </div>
            </div>
            <div>
            </div>
            <div class="category">
              <p><span>Category</span> {{ post.category }}</p>
            </div>
            <button class="btn_show_comment" @click.prevent="ShowComment(post.id)">Show Comment</button>
            <div class="show_comment" v-for="(comment,index) in all_comments_get" :key="index">
              <div class="container_comment" v-if="post.id===comment.post_id">
                <span class="who_add_comment"
                      v-if="who_add_comment[index].id===comment.user_id">{{
                    who_add_comment[index].name + ":  "
                  }}</span>
                <p class="what_add_to_comment">
                  {{ comment.text }}
                </p>
              </div>
              <div class="close_comment" v-if="all_comments_get.length!==0 && all_comments_get.length===index+1">
                <button v-if="post.id===comment.post_id" @click="CloseComment">Close Coment</button>
              </div>
            </div>
            <div class="edit_post" v-if="user_id===post.user_id">
              <button @click="EditPost(post.id)">Edit Post</button>
            </div>
          </li>
        </ul>
      </div>
    </div>

  </div>
  <router-view></router-view>
</template>

<script>
import axios from "axios";

// import '@fortawesome/fontawesome-free/css/all.css'
import "@/assets/userPage.css"
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

export default {
  name: "UserPage",
  components: {FontAwesomeIcon},
  data() {
    return {
      previousPath: this.$route.meta.previousPath,
      token: localStorage.getItem('token'),
      all_category: [],
      all_comments_get: [],
      comments_to_add: [],
      user_id: 0,
      select_category: '',
      posts: [],
      who_add_comment: [],
        isOpen: false,
      itemsPerPage: 10,
      currentPage: 1,
      template: [],
      CommentError: 'Comment must have length more then 10',
    }
  },
  created() {
    this.getAllCategory()
  },
  computed: {
    totalPages() {
      return Math.ceil(this.posts.length / this.itemsPerPage);
    },
    paginatedItems() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.posts.slice(startIndex, endIndex);
    },
  },
  methods: {
    Close() {
      this.previousPath = ' '
    },
    changePage(page) {
      this.currentPage = page;
    },
    async getAllCategory() {
      const response = await axios.get(`/GetAllCetegory`,)
      this.all_category = response.data.all_category
    },
    // async GetPostWithCategory() {
    //   const response = await axios.get(`/GetPostsWithConcreateCategory`, {params: {category: this.select_category}})
    //   this.posts = response.data.all_post
    //   this.user_id = JSON.parse(atob(this.token.split('.')[1]))
    //   this.user_id = Number(this.user_id.sub)
    //
    // },
    async GetPostWithCategory(name_category) {
      const response = await axios.get(`/GetPostsWithConcreateCategory`, {params: {category: name_category}})
      this.posts = response.data.all_post
      this.user_id = JSON.parse(atob(this.token.split('.')[1]))
      this.user_id = Number(this.user_id.sub)

    },
    async AddLike(post_id) {
      const response = await axios.post(`/AddLike`, null,
          {
            params: {
              post_id: post_id,
            },
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
          }
      )
      this.template = response.data.post
      for (let i = 0; i < this.posts.length; i++) {
        if (this.template.id === this.posts[i].id) {
          this.posts[i] = this.template
        }
      }
    },
    async AddDislike(post_id) {
      const response = await axios.post(`/AddDislike`, null, {
        params: {
          post_id: post_id,
        },
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      })
      this.template = response.data.post
      for (let i = 0; i < this.posts.length; i++) {
        if (this.template.id === this.posts[i].id) {
          this.posts[i] = this.template
        }
      }
    },
    async AddComent(id, text_of_comments, index) {
      const response = await axios.post(`/AddComent`, null, {
        params: {id: id, text_of_comment: text_of_comments},
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
      })
      this.posts[index].comment = ''
      this.comments_to_add = response.data
    },
    async ShowComment(id) {
      const response = await axios.get(`/ShowComment`, {params: {post_id: id}})
      this.all_comments_get = response.data.comment
      this.who_add_comment = response.data.who_add_comment
    },
    CloseComment() {
      this.all_comments_get = [];
    },
    EditPost(post_id) {
      this.$router.push(`/EditPost/${post_id}`)
    },
    showAllPost() {
      this.$router.push('/ShowAllPost')
    },
    showMyPost() {
      this.$router.push('/ShowMyPost')
    },
    createPost() {
      this.$router.push('/CreatePost')
    }
  },
  watch: {
    select_category() {
      this.GetPostWithCategory()
    }
  }

}
</script>

<style scoped>


</style>
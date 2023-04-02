<template>
  <div class="container_main">
    <div class="navbar">
      <div class="container">
        <h1 class="navbar-brand">My post</h1>
        <div class="navbar-wrap">
          <div class="navbar-menu">
            <ul>
              <li>
                <button @click="showAllPost">Show all Post</button>
              </li>
              <li>
                <button @click="showMyPost">Show my Post</button>
              </li>
              <li>
                <button @click="createPost">Crate Post</button>
              </li>
              <li>
                <button @click="UserPage">User page</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="container_post" v-if="my_post.length!==0">
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
              <button class="btn_like">
                <font-awesome-icon class="like" icon="fa-solid fa-thumbs-up"/>
                <span class="count_of_dislike">{{ post.like }}</span>
              </button>
              <button class="btn_dislike">
                <font-awesome-icon class="dislike" icon="fa-solid fa-thumbs-down"/>
                <span class="count_of_dislike">{{ post.dislike }}</span>
              </button>
            </div>
            <div>
            </div>
              <div class="category">
              <p><span>Category</span> {{post.category}}</p>
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
            <div class="edit_post">
              <button @click="EditPost(post.id)">Edit Post</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

import "@/assets/userPage.css"


export default {
  name: "ShowMyPost",
  components: {FontAwesomeIcon},
  data() {
    return {
      who_add_comment: [],
      my_post: [],
      all_comments_get: [],
      itemsPerPage: 10,
      currentPage: 1,
    }
  },
  async created() {
    this.getData()
  },
  computed: {
    totalPages() {
      return Math.ceil(this.my_post.length / this.itemsPerPage);
    },
    paginatedItems() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.my_post.slice(startIndex, endIndex);
    },
  },
  methods: {
    async getData() {
      const response = await axios.get(`/ShowMyPost`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      })
      this.my_post = response.data
    },
    changePage(page) {
      this.currentPage = page;
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
    },
    UserPage() {
      this.$router.push('/UserPage')
    }
  }
}
</script>

<style scoped>

</style>
<template>
  <div>
    <div class="paginator">
      <a class="previous"
         @click.prevent="currentPage!==1 ? changePage(currentPage-1) : changePage(currentPage) ">
        Previous
      </a>
      <ul>
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
    <div>
      <ul>
        <li v-for="(item, index) in paginatedItems" :key="index">
          <div>
            <h3>Name Post : {{ item.name_of_post }}</h3>
          </div>
          <h3>What about post</h3>
          <div>
            {{ item.text_of_post }}
          </div>
          <div v-if="user_id!==item.user_id">
            <textarea  v-model="comments_to_add[index]" @change="handleChange(index)" minlength="10">
            </textarea>
            <span v-if="CommentError">{{ CommentError }}</span>
            <br>
            <button @click.prevent="AddComent(item.id,comments_to_add[index])">Add Comment</button>
            <br>
          </div>
          <div>
            <button v-if="user_id!==item.user_id" @click="AddLike(item.id)">Add Like {{ item.like }}</button>
            <br>
            <button v-if="user_id!==item.user_id" @click="AddDislike(item.id)">Add Dislike {{ item.dislike }}</button>
          </div>
          <div v-if="user_id===item.user_id">
            <button @click="EditPost(item.id)">Edit Post</button>
          </div>
          <button @click.prevent="ShowComment(item.id)">Show Comment</button>
          <ul v-for="(items,index) in all_comments_get" :key="index">
            <div v-if="item.id===items.post_id">
              {{ items }}
            </div>
          </ul>
          <div v-if="all_comments_get.length!==0">
            <button @click="CloseComment">Close Coment</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ShowAllPost",
  components: {},
  data() {
    return {
      all_post: [],
      all_comments_get: [],
      comments_to_add: [],
      user_id: 0,
      token: localStorage.getItem('token'),
      itemsPerPage: 10,
      currentPage: 1,
      CommentError: ''
    }
  },
  created() {
    this.getData()
  },
  computed: {
    totalPages() {
      return Math.ceil(this.all_post.length / this.itemsPerPage);
    },
    paginatedItems() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.all_post.slice(startIndex, endIndex);
    },
  },
  methods: {
    async getData() {
      const response = await axios.get(`/ShowAllPost`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
      })
      this.all_post = response.data.all_post
      this.comments_to_add.length = response.data.all_post.length
      this.user_id = JSON.parse(atob(this.token.split('.')[1]))
      this.user_id = Number(this.user_id.sub)
      console.log(this.user_id)
    },
    changePage(page) {
      this.currentPage = page;
    },
    async AddLike(id) {
      const response = await axios.post(`/AddLike`, null, {params: {id: id}})
      this.all_post = response.data
    },
    async AddDislike(id) {
      const response = await axios.post(`/AddDislike`, null, {params: {id: id}})
      this.all_post = response.data
    },
    async AddComent(id, index_of_comments) {
      const response = await axios.post(`/AddComent`, null, {params: {id: id, text_of_comment: index_of_comments}})
      this.comments_to_add = response.data
    },
    async ShowComment(id) {
      const response = await axios.get(`/ShowComment`, {params: {post_id: id}})
      this.all_comments_get = response.data.comment
    },
    CloseComment() {
      this.all_comments_get = [];
    },
    EditPost(post_id) {
      this.$router.push(`/EditPost/${post_id}`)
    },
    // CheckComments(comments) {
    //   if (comments.length < 6) {
    //     this.CommentError = 'incorrect data'
    //   } else {
    //     this.CommentError = ''
    //   }
    // }
     handleChange(index) {
         console.log('Changed item:', this.comments_to_add[index])
       if(this.comments_to_add[index].length<6){
         this.CommentError='incorrect data'
       }else{
         this.CommentError=''
       }
    },
  },
  watch: {
    comments_to_add: {
      handler: function (value) {
        console.log(value)
      },
      deep: true
    }
  }
}
</script>

<style scoped>


.previous, .next {
  width: 100px;
  height: 50px;
  color: black;
}

.paginator {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50px;
}

.paginator ul {
  list-style: none;
  text-align: center;
}

.paginator ul li {
  float: left;
  margin-left: 10px;
}

.active {
  color: green;
  background: firebrick;
  text-decoration: underline;
}


.paginator li a {
  padding: 10px 10px 10px 10px;
  border: 2px solid yellow;
  border-radius: 10px;
}


.comments {
  margin-top: 10px;
}


.container {
  border-radius: 100px;
  margin: auto;

}

.container ul {
  list-style: none;
}


.container .name_post {
  margin-right: auto;
  margin-top: 14px;
  margin-left: auto;
  text-align: left;
  width: 40%;

}

.container .what_about_post {
  margin-right: auto;
  margin-left: auto;
  text-align: left;
  width: 40%;
  padding: 10px 10px 10px 10px;
}

.container .post_text {
  width: 40%;
  margin: auto;
  text-align: left;
  font-size: 0.8rem;
  letter-spacing: 1px;
  line-height: 1.5;
  height: 120px;
  border-radius: 5px;
  border: 1px solid #ccc;
  box-shadow: 1px 1px 1px #999;
}


.comments {
  width: 40%;
  margin-top: 10px;
  margin-left: auto;
  margin-right: auto;
}

.comments textarea {
  text-align: left;
  width: 90%;
  height: 10px;
  letter-spacing: 1px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  box-shadow: 1px 1px 1px #999;
  resize: none;
}

.btn_like, .btn_dislike {
  margin-top: 100px;
}

</style>
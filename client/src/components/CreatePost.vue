<template>
  <div class="container_main">
    <div class="navbar">
      <div class="container">
        <h1 class="navbar-brand">Create post</h1>
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
                <button @click="UserPage">User page</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <form class="forms">
      <div class="name_of_post">
        <label for="">Title of post</label>
        <input v-model="name_of_post" type="text" name="name_of_post" id="email" required>
        <span v-if="this.NameError">{{ NameError }}</span>
      </div>
      <div class="what_about_post">
        <label for="data_post">What about post</label>
        <textarea v-model="text_of_post" id="data_post" name="data_post" cols="30" rows="15">
      </textarea>
        <span v-if="this.TextPostError">{{ TextPostError }}</span>
      </div>
      <div class="category">
        <label for="category_of_post">Category of post</label>
        <input v-model="category_of_post" type="text" name="category_of_post" id="category" required>
        <span class="category_error" v-if="this.CategoryError">{{ CategoryError }}</span>
      </div>
      <button class="btn_to_create_post" @click.prevent="CreatePost">
        submit
      </button>
    </form>

  </div>
</template>

<script>
import axios from "axios";
import "@/assets/Create_post.css"


export default {
  name: "CreatePost",
  data() {
    return {
      name_of_post: '',
      text_of_post: '',
      category_of_post: '',
      status: '',
      token: localStorage.getItem('token'),
      NameError: '',
      CategoryError: '',
      TextPostError: ''
    }
  },
  methods: {
    async CreatePost() {
      if (this.CheckName() && this.CheckCategory() && this.CheckTextOfPost()) {
        const data = {
          name_of_post: this.name_of_post,
          text_of_post: this.text_of_post,
          category_of_post: this.category_of_post,
        }
        const response = await axios.post('/CreatePost', data, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
        })
        this.status = response.data.status
        if (this.status === 'successfully') {
          this.$router.push(`/UserPage`)
        }
      } else {
        alert('incorrect data')
      }
    },
    CheckName() {
      if (this.name_of_post.length < 5) {
        this.NameError = 'name of post must have length more then 5 '
        return false
      } else {
        this.NameError = ''
        return true
      }
    },
    CheckCategory() {
      if (this.category_of_post.length < 4) {
        this.CategoryError = 'category of post must have length more then 4 '
        return false
      } else {
        this.CategoryError = ''
        return true
      }
    },
    CheckTextOfPost() {
      if (this.text_of_post.length < 25) {
        this.TextPostError = 'text of post must have length more then 25 symbols'
        return false
      } else {
        this.TextPostError = ''
        return true
      }
    },
    showAllPost() {
      this.$router.push('/ShowAllPost')
    },
    showMyPost() {
      this.$router.push('/ShowMyPost')
    },
    UserPage() {
      this.$router.push('/UserPage')
    }
  },
  watch: {
    name_of_post(value) {
      console.log(value)
      this.CheckName()
    },
    category_of_post(value) {
      console.log(value)
      this.CheckCategory()
    },
    text_of_post(value) {
      console.log(value)
      this.CheckTextOfPost()
    }
  }
}


</script>

<style scoped>
textarea {
  resize: none;
}
</style>
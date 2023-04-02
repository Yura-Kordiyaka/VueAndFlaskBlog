<template>
  <div>
    <div class="navbar">
      <div class="container">
        <h1 class="navbar-brand">Edit post</h1>
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
    <div class="edit_concreate_post">
      <div class="name_of_concreate_post">
        <h3>{{ name }}</h3>
        <input v-model="name">
        <span v-if="name_error">{{name_error}}</span>
      </div>
      <div class="text_of_concreate_post">
        <p>
          {{ text }}
        </p>
        <textarea class="textarea_text" v-model="text">
      </textarea>
        <span v-if="text_error">{{text_error}}</span>
      </div>
      <div class="category_of_concreate_post">
        <h3>{{ category }}</h3>
        <input v-model="category">
        <span v-if="category_error">{{category_error}}</span>

      </div>
      <button class="btn_save_changes" @click.prevent="PostEditPost">Save changes</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import '@/assets/edit_post.css'

export default {
  name: "EditPost",
  data() {
    return {
      id: this.$route.params.id,
      name: '',
      text: '',
      category: '',
      name_error: '',
      text_error: '',
      category_error: '',
      post: [],
      status: '',
      previousPath: this.$route.meta.previousPath,
    }
  },
  created() {
    this.GetConcreatePost()
  },
  methods: {
    async GetConcreatePost() {
      const response = await axios.get(`/EditPost`, {params: {id: this.id}})
      this.post = response.data.post
      this.name = this.post.name_of_post
      this.text = this.post.text_of_post
      this.category = this.post.category
    },
    async PostEditPost() {
      if (this.CheckName() && this.CheckCategory() && this.CheckText()) {
        const data = {
          id: this.id,
          name_of_post: this.name,
          text_of_post: this.text,
          category_of_post: this.category,
        }
        const response = await axios.post(`/EditPost`, data)
        this.status = response.data.status
        if (this.status === 'successfully') {
          this.$router.push(`${this.previousPath}`)
        }
      } else {
        alert('incorrect data')
      }

    },
    CheckName() {
      if (this.name.length < 5) {
        this.name_error = 'name of post must have length more then 5 '
        return false
      } else {
        this.name_error = ''
        return true
      }
    },
    CheckText() {
      if (this.text.length < 25) {
        this.text_error = 'name of post must have length more then 25 '
        return false
      } else {
        this.text_error = ''
        return true
      }
    },
    CheckCategory() {
      if (this.category.length < 5) {
        this.category_error = 'name of post must have length more then 5 '
        return false
      } else {
        this.category_error = ''
        return true
      }
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
    },
  },

  watch: {
    name(value) {
      this.CheckName()
      console.log(value)
    },
    text(value) {
      console.log(value)
      this.CheckText()
    },
    category(value) {
      console.log(value)
      this.CheckCategory()
    },
  }
}
</script>

<style scoped>

</style>
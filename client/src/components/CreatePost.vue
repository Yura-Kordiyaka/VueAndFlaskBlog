<template>
  <div>
    <h1>Create post</h1>
    <form>
      <label for="name_of_post">Enter name of post: </label>
      <input v-model="name_of_post" type="text" name="name_of_post" id="email" required>
      <span v-if="this.NameError">{{ NameError }}</span>
      <br>
      <br>
      <label for="data_post">Review of W3Schools:</label>
      <textarea v-model="text_of_post" id="data_post" name="data_post" cols="30" rows="15">
      </textarea>
      <span v-if="this.TextPostError">{{ TextPostError }}</span>
      <br>
      <label for="category_of_post">Enter category of post: </label>
      <input v-model="category_of_post" type="text" name="category_of_post" id="category" required>
      <span v-if="this.CategoryError">{{ CategoryError }}</span>
      <button @click.prevent="CreatePost">
        submit
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

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
        this.NameError = 'name of post must have length more then 6 '
        return false
      } else {
        this.NameError = ''
        return true
      }
    },
    CheckCategory() {
      if (this.category_of_post.length < 5) {
        this.CategoryError = 'name of post must have length more then 6 '
        return false
      } else {
        this.CategoryError = ''
        return true
      }
    },
    CheckTextOfPost() {
      if (this.text_of_post.length < 30) {
        this.TextPostError = 'name of post must have length more then 6 '
        return false
      } else {
        this.TextPostError = ''
        return true
      }
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
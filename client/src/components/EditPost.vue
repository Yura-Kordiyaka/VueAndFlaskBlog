<template>
  <div>
    <h1>Edit Post</h1>
    <div>
      <h3>Name of Post {{ name }}</h3>
      <input v-model="name">
      <br>
      <br>
      <h3>Text </h3>
      <div>
        {{ text }}
      </div>
      <textarea v-model="text">
      </textarea>
      <br>
      <br>
      <h3>Category {{ category }}</h3>
      <input v-model="category">
    </div>
    <button @click.prevent="PostEditPost">Save changes</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EditPost",
  data() {
    return {
      id: this.$route.params.id,
      name: '',
      text: '',
      category: '',
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
    }
  },

}
</script>

<style scoped>

</style>
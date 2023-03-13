<template>
  <div>
    {{ my_post }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ShowMyPost",
  components: {},
  data() {
    return {
      my_post: []
    }
  },
  async created() {
    this.getData()
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
  }
}
</script>

<style scoped>

</style>
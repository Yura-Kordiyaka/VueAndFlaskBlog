<template>
  <div class="hello">
    <div class="container">
      <h1>Search</h1>
      <form class="Form">
        <input type="text" v-model="query">
      </form>
      <div>
        <ul v-for="(item,index) in items" :key="index">
          <li>{{ item }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data() {
    return {
      query: "",
      items: [],
    }
  },
  methods: {
    getData() {
      setTimeout(() => axios.get(`https://api.github.com/search/topics?q=${this.query}`)
          .then(response => {
            this.items = response.data.items
          })
          .catch(err => {
            console.log(err)
          }), 1000)
    }
  },
  watch: {
    query(value) {
      if (value.length === 0) {
        this.items = []
        console.log(value.length)
      } else {
        console.log(value)
        console.log(value.length)
        this.getData()
      }
    }
  }
}

</script>

<style scoped>
.container {
  text-align: center;

}

input {
  padding: 10px;
  border-radius: 4px;
  width: 50%;
  background: lightseagreen;
}

li {
  list-style: none;
}


</style>
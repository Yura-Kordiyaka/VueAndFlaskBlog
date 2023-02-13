<template>
  <div class="hello">
    <div class="container">
      <h1>Search</h1>
      <form class="Form">
        <input type="text" v-model="query">
      </form>
      <div class="select2-container">
        <p><strong>Знайдено всього збігів :</strong> {{ items.length }}</p>
        <ul v-for="(item,index) in items" :key="index">
          <li>
            <strong class="count">{{index +1}}</strong><br><br>
            <strong v-if="!item.name">name : -</strong>
            <strong v-else>name : </strong>{{ item.name }}<br>
            <strong v-if="!item.display_name">display_name : -</strong>
            <strong v-else>display_name : </strong>{{ item.display_name }}<br>
            <strong v-if="!item.short_description">short_description : -</strong>
            <strong v-else>short_description : </strong>{{ item.short_description }}<br>
            <strong v-if="!item.description">description : -</strong>
            <strong v-else>description : </strong>{{ item.description }}<br>
            <strong v-if="!item.created_by">created_by : -</strong>
            <strong v-else>created_by : </strong>{{ item.created_by }}<br>
            <strong v-if="item.released">released : -</strong>
            <strong v-else>released : </strong>{{ item.released }}<br>
            <strong>created_at : </strong>{{ item.created_at }}<br>
            <strong>updated_at : </strong>{{ item.updated_at }}<br>
            <strong>featured : </strong>{{ item.featured }}<br>
            <strong>curated : </strong>{{ item.curated }}<br>
            <strong>score : </strong>{{ item.score }}
          </li>
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

.count{
  font-size: 30px;
}


.container {
  text-align: center;

}

strong {
  text-align: end;
}

.select2-container {
  margin-top: 40px;
}

input {
  padding: 10px;
  border-radius: 4px;
  width: 50%;
  background: lightseagreen;
}

li {
  padding: 10px;
  list-style: none;
  text-align: start;
}

ul {
  margin-left: auto;
  margin-right: auto;
  border-radius: 10px;
  width: 40%;
  border: 3px solid lightseagreen;
}


</style>
<template>
  <div>
    <h1>It's user page Hello </h1>
    <router-link to="/CreatePost">Create Post</router-link>
    <div class="window" v-show="this.previousPath==='/Login'">
      <h1>Hello User</h1>
      <button @click="Close"></button>
    </div>
    <br>
    <router-link to="/ShowAllPost">Show all post</router-link>
    <br>
    <router-link to="/ShowMyPost">Show my post</router-link>
    <!--    {{ previousPage }}-->
    <br>
  </div>
  <router-view></router-view>
</template>

<script>
// import axios from "axios";


export default {
  name: "UserPage",
  components: {},
  data() {
    return {
      previousPath: this.$route.meta.previousPath,
      token: localStorage.getItem('token')
    }
  },
  methods: {
    Close() {
      this.previousPath = ' '
    }
  },
}
</script>

<style scoped>
.window {
  height: auto;
  width: auto;
  background: black;
}
</style>
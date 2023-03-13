<template>
  <div class="app">
    <ul>
      <li>
          <button @click="goAuthorization">Authorization</button>
      </li>
      <li>
          <button @click="goLogin">Login</button>
      </li>

    </ul>
    <br>
  </div>
  <router-view></router-view>
</template>

<script>
export default {
  name: "Main-page",
  data() {
    return {
      name: 'yura'
    }
  },
  methods: {
    goAuthorization() {
      this.$router.push('/Authorization')
    },
    goLogin() {
      this.$router.push('/Login')
    },
  }
}
</script>

<style scoped>
.app {margin:0;}
ul {
  list-style-type: none;
  margin: 0 0 0 -8px;
  padding: 10px;
  overflow: hidden;
  background-color: black;
  position: fixed;
  top: 0;
  width: 100%;
}

li {
  float: left;
}

li button {
  display: block;
  color: black;
  background:white;
  text-align: center;
  padding: 14px 16px;
  border-radius: 30px;
  margin-left: 10px;
}

button:hover{
  background: lightblue;
}



</style>
<template>
  <div class="navbar">
    <div class="container">
      <h1 class="navbar-brand">Blog</h1>
      <div class="navbar-wrap">
        <div class="navbar-menu">
          <ul>
            <li>
              <button @click.prevent="goAuthorization">Authorization</button>
            </li>
            <li>
              <button @click.prevent="goLogin">Login</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <router-view></router-view>
</template>

<script>
import '@/assets/main.page.css'
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


/*.container_main {*/
/*  margin: -10px;*/
/*}*/

/*ul {*/
/*  list-style-type: none;*/
/*  background: darkgreen;*/

/*}*/

/*li {*/
/*  display: inline-block;*/
/*}*/

/*li button {*/
/*  padding: 14px 16px;*/
/*  color: white;*/
/*  background: darkgreen;*/
/*  font-size: 40px;*/
/*}*/

/*li button:hover {*/
/*  background: black;*/
/*}*/


</style>
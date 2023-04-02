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
* {
  padding: 0;
  margin: 0;
  border: 0;
}

*, *:before, *:after {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

:focus, :active {
  outline: none;
}

a:focus, a:active {
  outline: none;
}

nav, footer, header, aside {
  display: block;
}

html, body {
  height: 100%;
  width: 100%;
  font-size: 100%;
  line-height: 1;
  font-size: 14px;
  -ms-text-size-adjust: 100%;
  -moz-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}

input, button, textarea {
  font-family: inherit;
}

input::-ms-clear {
  display: none;
}

button {
  cursor: pointer;
}

button::-moz-focus-inner {
  padding: 0;
  border: 0;
}

a, a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: none;
}

ul li {
  list-style: none;
}

img {
  vertical-align: top;
}

h1, h2, h3, h4, h5, h6 {
  font-size: inherit;
  font-weight: 400;
}

.navbar {
  width: 100%;
  height: 70px;
  box-shadow: 0 4px 10px rgb(0, 0, 0, .1);
}

.navbar .container {
  height: inherit;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-menu li {
  display: inline-block;
}

.navbar-menu li button {
  display: inline-block;
  color: black;
  opacity: 0.5;
  padding: 0 30px;
  background-color: white;
  transition: all .07s ease-in-out;
  font-size: 20px;

}

.navbar-wrap {
  display: flex;
  flex-flow: row nowrap;
}

.navbar-brand {
  margin-left: 30px;
  font-weight: 700;
  font-size: 26px;
  color: black;
}

.navbar-menu li button:hover {
  opacity: 1;
}

.navbar-brand:hover {
  color: coral;
  transition: all .07s ease-in-out;

}

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
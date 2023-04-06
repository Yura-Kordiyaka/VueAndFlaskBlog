<template>
  <div class="main">
    <form class="form_authorization">
      <h1 class="from_tittle">Authorization</h1>
      <div class="form_group">
        <input class="form_input" v-model=name type="text" name="name" id="name" required>
        <label class="form_label" for="name">Enter your name</label>
      </div>
      <div class="error">
        <span class="error_name" v-if="NameError">{{ NameError }}</span>
      </div>
      <div class="form_group">
        <input class="form_input" v-model=email type="email" name="email" id="email" required>
        <label class="form_label" for="email">email</label>
      </div>
       <div class="error">
         <span class="error_email" v-if="EmailError">{{ EmailError }}</span>
      </div>
      <div>
        <input class="form_input" v-model=password type="password" name="password" id="password" required>
        <label class="form_label" for="password">Enter your password</label>
      </div>
       <div class="div_error_password">
       <span class="error_password" v-if="PasswordError">{{ PasswordError }}</span>
      </div>
      <button class="form_button" @click.prevent="CreateUser">Authorization</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "АuthorizationUser",
  data() {
    return {
      name: '',
      password: '',
      email: '',
      status: '',
      NameError: '',
      PasswordError: '',
      EmailError: '',
    }
  },
  methods: {
    async CreateUser() {
      if (this.CheckEmail() && this.CheckName() && this.CheckPassword()) {
        const response = await axios.post(`/Authorization`, null, {
          params: {
            name: this.name,
            password: this.password,
            email: this.email
          }
        })
        this.status = response.data.status
        if (this.status === 'successfully') {
          this.$router.push(`/Login`)
        }
      } else {
        alert('incorrect data')
      }
    },
    CheckPassword() {
      if (this.password.length < 5) {
        this.PasswordError = 'password must have length more then 6 '
        return false
      } else {
        this.PasswordError = ''
        return true
      }
    },
    CheckEmail() {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!regex.test(this.email) || this.email.length < 6) {
        this.EmailError = 'email is incorrect'
        return false
      } else {
        this.EmailError = ''
        return true
      }

    },
    CheckName() {
      if (this.name.length < 4) {
        this.NameError = 'name must have length more then 4 '
        return false
      } else {
        this.NameError = ''
        return true
      }
    }
  },
  watch: {
    name(value) {
      console.log(value)
      this.CheckName()
    },
    password(value) {
      console.log(value)
      this.CheckPassword()
    },
    email(value) {
      console.log(value)
      this.CheckEmail()
    }
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

.main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
}

.form_authorization {
  width: 500px;
  height: 500px;
  padding: 32px;
  border-radius: 10px;
  box-shadow: 0 4px 16px #ccc;
  font-family: sans-serif;
  letter-spacing: 1px;
}

.form_input,
.form_button {
  font-family: sans-serif;
  letter-spacing: 1px;
  font-size: 16px;
}

.from_tittle {
  text-align: center;
  margin: 0 0 32px 0;
  font-weight: normal;
  font-size: 20px;
}

.form_group {
  position: relative;
  margin-bottom: 32px;
}

.form_label {
  /*position: absolute;*/
  top: 0;
  left: 0;
  z-index: -1;
  color: #9e9e9e;
  transition: 0.3s;
}

.form_input {
  width: 100%;
  padding: 0 0 10px 0;
  border-bottom: 1px solid #e0e0e0;
  background-color: transparent;
  outline: none;
  transition: 0.3s;
}

.form_input:focus {
  border-bottom: 1px solid #1a73a8;
}

.form_button {
  padding: 10px 20px;
  border-radius: 5px;
  color: #fff;
  background-color: #0071f0;
  cursor: pointer;
  transition: 0.3s;
}
.form_button:hover {
  opacity: 0.8;
}

.error {
  margin-bottom: 20px;
}

.error .error_email,.error_name {
  color: red;
  opacity: 0.5;
}
.div_error_password{
  margin-top: 20px;
  margin-bottom: 20px;
}
.div_error_password .error_password{
   color: red;
  opacity: 0.5;
}

/*template {*/
/*  border: black solid 20px;*/
/*}*/

/*.main {*/
/*  border: #3A7734 solid 10px;*/
/*  border-radius: 30px;*/
/*  width: 600px;*/
/*  margin: 0 auto;*/
/*  height: 600px;*/
/*  box-shadow: 10px 10px 30px 10px darkgreen;*/
/*}*/

/*.container_main {*/
/*  position: relative;*/
/*}*/

/*.container_main h1 {*/
/*  display: block;*/
/*  margin: 10px 0;*/
/*  text-align: center;*/
/*  font-size: 60px;*/
/*}*/

/*.container_main label {*/
/*  display: block;*/
/*  margin: 10px 0 20px 0;*/
/*  font-size: 30px;*/
/*  text-align: center;*/
/*}*/

/*.container_main input {*/
/*  background: white;*/
/*  font-size: 30px;*/
/*  display: block;*/
/*  margin: 0 auto 30px;*/
/*  border: black solid 3px;*/
/*  border-radius: 20px;*/
/*  padding: 5px 20px;*/
/*  width: 90%;*/
/*}*/

/*.container_main input:focus {*/
/*  color: black;*/
/*  border: darkgreen solid 1px;*/
/*  box-shadow: 5px 5px 5px 5px black;*/
/*}*/

/*.container_main button {*/
/*  font-size: 31px;*/
/*  display: block;*/
/*  margin: 0 auto;*/
/*  border: black solid 3px;*/
/*  width: 91%;*/
/*  border-radius: 20px;*/
/*}*/

/*.container_main button:hover {*/
/*  color: white;*/
/*  background: black;*/
/*}*/

/*.container_main .error {*/
/*  display: block;*/
/*  color: #9C1A1C;*/
/*  margin-left: 40px;*/
/*  font-size: 20px;*/
/*  margin-bottom: 30px;*/
/*}*/


</style>
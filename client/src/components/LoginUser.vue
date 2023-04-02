<template>
  <div class="global">
    <div class="container_for_form">
      <form class="form">
        <h1 class="from_tittle">Login in</h1>
        <div class="form_group">
          <input class="form_input" v-model=email type="email" name="email" id="email" required>
          <label class="form_label" for="email">email</label>
        </div>
        <div class="error">
          <span class="error_email" v-if="emailError">{{ emailError }}</span>
        </div>
        <div class="form_group">
          <input class="form_input" v-model=password type="password" name="password" id="password" required>
          <label class="form_label" for="password">password</label>
        </div>
        <div class="error">
          <span class="error_password" v-if="passwordError">{{ passwordError }}</span>
        </div>
        <button class="form_button" @click.prevent="getData">Login in</button>
      </form>

      <div class="window" v-show="this.path==='/Authorization'">
        <h3>User was authorization successfully please login in</h3>
        <button @click="Close">Close this Window</button>
      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";
import {required, minLength} from 'vuelidate/lib/validators'
import "@/assets/login.css"

export default {

  name: "LoginUser",
  data() {
    return {
      password: '',
      email: '',
      status: [],
      user: [],
      path: this.$route.meta.previousPath,
      passwordError: '',
      emailError: ''
    }
  },
  methods: {
    async getData() {
      if (this.CheckPassword() && this.CheckEmail()) {
        const response = await axios.get(`/Login`, {
          params: {
            password: this.password,
            email: this.email
          },
        })
        this.status = response.data.status
        if (this.status === 'successfully') {
          localStorage.setItem('token', response.data.token)
          this.$router.push(`/UserPage`)
        } else {
          alert('incorrect data')
          this.password = ''
          this.email = ''
        }
      } else {
        alert('incorrect data')
      }
    },
    CheckPassword() {
      if (this.password.length < 5) {
        this.passwordError = 'Password must have length more then 6 '
        return false
      } else {
        this.passwordError = ''
        return true
      }
    },
    CheckEmail() {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!regex.test(this.email) || this.email.length < 6) {
        this.emailError = 'email is incorrect'
        return false
      } else {
        this.emailError = ''
        return true
      }

    },
    Close() {
      this.path = ' '
    }
  },
  validations: {
    password: {
      required,
      minLength: minLength(4)
    }
  },
  watch: {
    password(value) {
      this.CheckPassword()
      console.log(value)
    },
    email(value) {
      console.log(value)
      this.CheckEmail()
    }
  }
}
</script>

<style scoped>


/*.main {*/
/*  border: #3A7734 solid 10px;*/
/*  width: 600px;*/
/*  height: 600px;*/
/*  box-shadow: 10px 10px 30px 10px darkgreen;*/

/*}*/

/*.container {*/
/*  margin-top: 10px;*/
/*}*/


/*.container h1 {*/
/*  margin: 10px 0;*/
/*  text-align: center;*/
/*  font-size: 60px;*/
/*}*/

/*.container label {*/
/*  display: block;*/
/*  margin: 10px 0 20px 0;*/
/*  font-size: 30px;*/
/*  text-align: center;*/
/*}*/

/*.container input {*/
/*  background: white;*/
/*  font-size: 30px;*/
/*  display: block;*/
/*  margin: 0 auto 30px;*/
/*  border: black solid 3px;*/
/*  border-radius: 20px;*/
/*  padding: 5px 20px;*/
/*  width: 90%;*/
/*}*/

/*.container input:focus {*/
/*  color: black;*/
/*  border: darkgreen solid 1px;*/
/*  box-shadow: 5px 5px 5px 5px black;*/
/*}*/

/*.container button {*/
/*  font-size: 31px;*/
/*  display: block;*/
/*  margin: 0 auto;*/
/*  border: black solid 3px;*/
/*  width: 91%;*/
/*  border-radius: 20px;*/
/*}*/

/*.container button:hover {*/
/*  color: white;*/
/*  background: black;*/
/*}*/

/*.container .error {*/
/*  display: block;*/
/*  color: #9C1A1C;*/
/*  margin-left: 40px;*/
/*  font-size: 20px;*/
/*  margin-bottom: 30px;*/
/*}*/


</style>

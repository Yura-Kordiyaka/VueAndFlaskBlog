<template>
  <div>
    <div class="container">
      <h1>Login</h1>
      <form class="form">
        <label for="email">Enter your email: </label>
        <input v-model=email type="email" name="email" id="email" required>
        <span v-if="emailError">{{ emailError }}</span>
        <label for="password">Enter your password: </label>
        <input v-model=password type="password" name="password" id="password" required>
        <span v-if="passwordError">{{ passwordError }}</span>
        <button class="btn" @click.prevent="getData">Submit</button>
      </form>
    </div>
    <div class="window" v-show="this.path==='/Authorization'">
      <h3>User was authorization successfully please login in</h3>
      <button @click="Close">Close this Window</button>
    </div>
  </div>

</template>

<script>
import axios from "axios";
import {required, minLength} from 'vuelidate/lib/validators'

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
.window {
  height: auto;
  width: auto;
  background: black;
}

.window button {
  padding: 10px 10px 10px 10px;
}


label {
  margin-top: 550px;
  color: white;
}

input[type=password], input[type=email] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
  border-radius: 40px;
}

.btn {
  width: 50%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
  border-radius: 40px;

}

.container h1 {
  color: white;
  margin-left: auto;
  margin-right: auto;
}

.container {
  width: 50%;
  vertical-align: center;
  border: 1px solid;
  border-radius: 30px;
  padding: 30px;
  background: black;
}

body {
  background: black;
}
</style>
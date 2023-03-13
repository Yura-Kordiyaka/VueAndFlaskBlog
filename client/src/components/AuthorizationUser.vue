<template>
  <div class="form">
    <form>
      <label for="name">Enter your name: </label>
      <input v-model=name type="text" name="name" id="name" required>
      <span v-if="NameError">{{ NameError }}</span>
      <br>
      <br>
      <label for="email">Enter your email: </label>
      <input v-model=email type="email" name="email" id="email" required>
      <span v-if="EmailError">{{ EmailError }}</span>
      <br>
      <br>
      <label for="password">Enter your password: </label>
      <input v-model=password type="password" name="password" id="password" required>
      <span v-if="PasswordError">{{ PasswordError }}</span>
      <button @click.prevent="CreateUser">Submit</button>
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
        this.PasswordError = 'Password must have length more then 6 '
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
        this.NameError = 'Password must have length more then 4 '
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
input {
  width: 100%;
  margin-top: 10px;
}

label {
  margin-top: 550px;
}


</style>
<template>
    <v-container class="fill-height">
        <v-responsive class="align-center text-center fill-height">

            <v-img height="300" src="@/assets/logo.svg" />

            <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
            <h1 class="text-h2 font-weight-bold">Grade Hero</h1>
            <v-card class="mx-auto px-6 py-8" max-width="344">
            <v-form v-model="form" @submit.prevent="onSubmit">

                <v-text-field
                v-model="username"
                :readonly="loading"
                :rules="[required]"
                class="mb-2"
                clearable
                label="Username"
                ></v-text-field>

                <v-text-field
                v-model="password"
                :readonly="loading"
                :rules="[required]"
                :type="'password'"
                clearable
                label="Password"
                placeholder="Enter your password"
                ></v-text-field>

                <div v-if="error" class="error">{{ error }}</div>

                <v-btn
                :disabled="!form"
                :loading="loading"
                block
                color="success"
                size="large"
                type="submit"
                variant="elevated"
                >
                Sign In
                </v-btn>
            </v-form>
            <div class="text-center">
                <router-link to="/register">
                  <v-btn
                      prepend-icon="mdi-check-circle"
                      append-icon="mdi-account-circle"
                      >
                      <template v-slot:prepend>
                          <v-icon color="success"></v-icon>
                      </template>
 
                      Register

                      <template v-slot:append>
                          <v-icon color="warning"></v-icon>
                      </template>
                  </v-btn>
                </router-link>
            </div>
            </v-card>
        </v-responsive>
    </v-container>
</template>

<script lang="ts">
import axios from 'axios'
  export default {
    data: () => ({
      form: false,
      email: null,
      password: null,
      loading: false,
      username: '',
      error: ''
    }),

    methods: {
      onSubmit() {
        if (!this.form) return
        const path = "http://localhost:5000/login"
        const data = {
          username: this.username,
          password: this.password
        }
        this.loading = true

        setTimeout(() => (
            axios.post(path, data)
            .then(res => {
              console.log(res.data)
              sessionStorage.setItem('username', this.username)
              this.loading = false
              this.$router.push('/home')
            }).catch(error => {
              this.loading = false
              this.error = 'Invalid username or password'
              console.log(error)
            })), 2000)
      },
      required(v: any) {
        return !!v || 'Field is required'
      },
    },
  }
</script>

<style>
  .error {
    color: #D50000;
  }
</style>
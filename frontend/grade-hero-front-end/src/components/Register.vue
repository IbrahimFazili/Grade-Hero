<template>
    <v-container class="fill-height">
        <v-responsive class="align-center text-center fill-height">

            <v-img height="300" src="@/assets/logo.svg" />

            <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
            <h1 class="text-h2 font-weight-bold">Grade Hero</h1>
            <v-card class="mx-auto px-6 py-8" max-width="344">
            <v-form v-model="form" @submit.prevent="onSubmit">
                <v-text-field
                v-model="email"
                :readonly="loading"
                :rules="[required]"
                class="mb-2"
                clearable
                label="Email"
                ></v-text-field>

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
                clearable
                label="Password"
                placeholder="Enter your password"
                ></v-text-field>

                <br />

                <v-btn
                :disabled="!form"
                :loading="loading"
                block
                color="success"
                size="large"
                type="submit"
                variant="elevated"
                >
                Register
                </v-btn>
            </v-form>
            </v-card>
        </v-responsive>
    </v-container>
</template>

<script lang="ts">
  export default {
    data: () => ({
      form: false,
      email: null,
      password: null,
      loading: false,
      username: null
    }),

    methods: {
      onSubmit() {
        if (!this.form) return

        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
      required(v: any) {
        return !!v || 'Field is required'
      },
      onRegister() {
        console.log('taking to register page')
      }
    },
  }
</script>
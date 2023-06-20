<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">

      <div v-if="loading">
      <!-- Show loading screen or spinner -->
        <p>Loading...</p>
      </div>
      <div v-else>
        <v-row class="align-end justify-end pt-6 pe-6">
        <v-btn
            min-width="164"
            rel="noopener noreferrer"
            target="_blank"
            variant="text"
            @click="handleSignOut"
            >
          <v-icon 
            icon="mdi-account-circle"
            size="large"
          />
          Sign Out
        </v-btn>
      </v-row>

      <v-img height="100" src="@/assets/logo.svg" />

      <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>

        <h1 class="text-h2 font-weight-bold">Grade Hero, {{ getUserName() }}!</h1>

        <div class="py-14" />

        <v-container>
          <v-row
            align="start"
            no-gutters
          >
            <v-col class="v-col-2">
              <div v-if="coursesExist">
                <CardList :courses="courses"/>
              </div>
              <div v-else class="pb-2">
                <p>Upload a syllabus to get started!</p>
              </div>
              <v-btn class="btn btn-info" @click="$refs.file.click()">upload</v-btn>
              <input ref="file" type="file" class="d-none" v-on:change="handleFileUpload()">
              <div>{{file.name}}</div>
            </v-col>
            <v-col>
              this will be main vueing
            </v-col>
          </v-row>
        </v-container>
        
        <div class="py-3" />
      </div>
    
    </v-responsive>
  </v-container>
</template>

<script lang="ts">
import CardList from './CardList.vue'

import axios from 'axios'

  export default {
    data: () => ({
      courses: [],
      coursesExist: true,
      file: "",
      selectedCourse: [],
      loading: true
    }),
    components: {
      CardList
    },
    mounted() {
      this.getCourses()
    }
    ,
    methods: {
      getUserName() {
        return sessionStorage.getItem('username')
      },

      getCourses() {
        const path = "http://localhost:5000/getCourse"
        const data = {
          username: this.getUserName(),
        }
        setTimeout(() => {
          axios.get(path, {
            params: data
          })
          .then((res) => {
            // @TODO: add logic if there is no courses for user so upload div should render
            this.courses = res.data
            this.loading = false
            this.coursesExist = true
            console.log('COURSES', this.coursesExist)
          }).catch((error) => {
            this.coursesExist = false
            console.log(error)
          })
        }, 2000);
      },

      handleSignOut() {
        sessionStorage.removeItem('username')
        this.$router.back()
      },

      handleFileUpload: function () {
        this.file = this.$refs.file.files[0];
      },
    }
  }
</script>

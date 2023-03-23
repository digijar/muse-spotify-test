<!-- <template>
  <div style="background-image: url('/assets/muse_background.jpg'); height: 100vh; background-size: cover;">
    <br><br><br>
    
    <div class="m-4">
      <h1>müse</h1>
      <h4 style="color: grey">Discover your music taste & blend them with your friends.</h4>
    </div>

    <div class="m-4">
      <RouterLink to="/loginauth">
        <button class="btn btn-outline-secondary login-btn" style="font-size: 1.2em; padding: 10px 20px;">
          log in
        </button>
      </RouterLink>
    </div>

    <div>
    <button @click="login">Log in to Spotify</button>
  </div>
  </div>
</template>


<script>
import VueSpotify from 'vue-spotify'

export default {
  methods: {
    login() {
      this.$spotify.login().then(response => {
        const accessToken = response.access_token
        // Store the access token in your application's state or in a cookie
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
 -->


<template>
  <br><br><br>

  <div class="m-4">
    <h1>müse</h1>
    <h4 style="color: grey">Discover your music taste & blend them with your friends.</h4>
  </div>

  <div>
    <button v-if="!isLoggedIn" @click="login">Log in to Spotify</button>
    <div v-else>
      <h3>Welcome, {{ user.display_name }}!</h3>
      <button @click="logout">Log out</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoggedIn: false,
      user: null
    }
  },
  methods: {
    login() {
      window.location.href = 'http://127.0.0.1:2504/api/login'
    },
    logout() {
      fetch('http://127.0.0.1:2504/api/logout')
        .then(response => response.json())
        .then(data => {
          this.isLoggedIn = false
          this.user = null
        })
        .catch(error => {
          console.log(error)
        })
    },
    getUserProfile() {
      fetch('http://127.0.0.1:2504/api/me')
        .then(response => response.json())
        .then(data => {
          this.isLoggedIn = true
          this.user = data
        })
        .catch(error => {
          console.log(error)
        })
    },
    check() {
      fetch('http://127.0.0.1:2504/api/check')
        .then(response => response.json())
        .then(data => {
          if (data.logged_in) {
            this.getUserProfile()
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created() {
    this.check()
  }
}
</script>





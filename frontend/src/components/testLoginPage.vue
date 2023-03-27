<template>
    <div>
        <button @click="login">Log in to Spotify</button>
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
  
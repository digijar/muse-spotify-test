<template>
  <br><br>

  <div class="m-4">
    <div>
      <h2 class="pt-4">{{ typingText }}</h2>
      <h3 id="typingeffect" style="color:grey">{{ typingSubtitle }}</h3>
    </div>
  </div>

  <div class="pt-2">
    <TopTracksCard v-if="showCards"></TopTracksCard>
  </div>

  <div class="pt-2">
    <TopArtistsCard v-if="showCards"></TopArtistsCard>
  </div>

  <div class="pt-2">
    <button class="btn btn-outline-secondary" @click="replay"
      style="font-size: 1.2em; padding: 10px 20px; font-weight: 800; display: flex; justify-content: center; align-items: center; text-align: center;">
      Reload top artists and songs!
      </button>
  </div>


  <br><br><br>
</template>

<script>
import TopTracksCard from './TopTracksCard.vue';
import TopArtistsCard from './TopArtistsCard.vue'
import { setTransitionHooks } from 'vue';
import axios from 'axios';
const email = localStorage.getItem('email')

export default {
  components: {
    TopTracksCard, TopArtistsCard
  },
  data() {
    return {
      typingText: '',
      typingSubtitle: '',
      typingComplete: false,
      showCardsAfterDelay: false,
      refreshIntervalId: null,
    }
  },
  mounted() {
    this.startRefresh()
    this.typeText()
  },
  computed: {
    showCards() {
      return this.typingComplete && this.showCardsAfterDelay
    }
  },
  methods: {

    // call Replay microservice to reload database information
    replay() {
      var auth_token = localStorage.getItem('spotifyAuthToken')
      axios.get('http://localhost:8000/api/v1/reload_top_items', {
        headers: {
          'Authorization': `Bearer ${auth_token}`,
          'Email':  `${email}`
        }
      }) 
        .then((response) => {
          this.result = response.data;
          console.log(response.data);
          location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // visual shit
    typeText() {
      const text = 'Explore your listening'
      let index = 0
      const typingInterval = setInterval(() => {
        this.typingText += text[index]
        index++
        if (index === text.length) {
          clearInterval(typingInterval)
          this.typeSubtitle()
        }
      }, 50)
    },
    typeSubtitle() {
      const text = 'for this month.'
      let index = 0
      const typingInterval = setInterval(() => {
        this.typingSubtitle += text[index]
        index++
        if (index === text.length) {
          clearInterval(typingInterval)
          setTimeout(() => {
            this.typingComplete = true
            setTimeout(() => {
              this.showCardsAfterDelay = true
            }, 1000)
          }, 0)
        }
      }, 50)
    },
    startRefresh() {
      this.refreshIntervalId = setInterval(() => {
        this.refreshData()
      }, 30000)
    },
    refreshData() {
      // code to refresh data goes here
    },
    stopRefresh() {
      clearInterval(this.refreshIntervalId)
    }
  },
  beforeDestroy() {
    this.stopRefresh()
  }
}
</script>

<style>
#typingeffect::after {
  content: '|';
  animation: blink 0.7s infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>

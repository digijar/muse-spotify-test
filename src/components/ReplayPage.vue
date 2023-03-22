<template>
  <br><br>

  <div class="m-4">
    <div>
      <h2>{{ typingText }}</h2>
      <h4 id="typingeffect" style="color:grey">{{ typingSubtitle }}</h4>
    </div>
  </div>

    <TopSongsCard></TopSongsCard>

    <TopArtistsCard></TopArtistsCard>


    <TopAlbumsCard></TopAlbumsCard>

  <br><br><br>
</template>

<script>
import TopSongsCard from '../components/TopSongsCard.vue';
import TopArtistsCard from '../components/TopArtistsCard.vue';
import TopAlbumsCard from '../components/TopAlbumsCard.vue';
import HistoryCard from '../components/HistoryCard.vue'

export default {
  components: {
    TopSongsCard, TopArtistsCard, TopAlbumsCard, HistoryCard
  },
  data() {
    return {
      typingText: '',
      typingSubtitle: '',
      showCards: {
        songs: false,
        artists: false,
        albums: false
      },
      refreshIntervalId: null
    }
  },
  mounted() {
    this.startRefresh()
    this.typeText()
  },
  methods: {
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
      const text = 'as of this week.'
      let index = 0
      const typingInterval = setInterval(() => {
        this.typingSubtitle += text[index]
        index++
        if (index === text.length) {
          clearInterval(typingInterval)
          this.showCards.songs = true
          setTimeout(() => {
            this.showCards.artists = true
          }, 1000)
          setTimeout(() => {
            this.showCards.albums = true
          }, 2000)
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

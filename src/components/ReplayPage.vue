<template>
  <br><br>

  <div class="m-4">
    <div>
      <h2>{{ typingText }}</h2>
      <h4 id="typingeffect" style="color:grey">{{ typingSubtitle }}</h4>
    </div>
  </div>

  <TopSongsCard v-if="showCards"></TopSongsCard>
  <TopArtistsCard v-if="showCards"></TopArtistsCard>
  <TopAlbumsCard v-if="showCards"></TopAlbumsCard>

  <br><br><br>
</template>

<script>
import TopSongsCard from '../components/TopSongsCard.vue';
import TopArtistsCard from '../components/TopArtistsCard.vue';
import TopAlbumsCard from '../components/TopAlbumsCard.vue';

export default {
  components: {
    TopSongsCard, TopArtistsCard, TopAlbumsCard
  },
  data() {
    return {
      typingText: '',
      typingSubtitle: '',
      typingComplete: false,
      showCardsAfterDelay: false,
      refreshIntervalId: null
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
          setTimeout(() => {
            this.typingComplete = true
            setTimeout(() => {
              this.showCardsAfterDelay = true
            }, 1500)
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

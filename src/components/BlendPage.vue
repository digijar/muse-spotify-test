<template>
  <TopNav></TopNav>

  <br><br>
  <div class="m-4">
    <div>
      <h2>{{ typingText }}</h2>
      <h4 id="typingeffect" style="color: grey">{{ subtitle }}</h4>
    </div>
  </div>

  <PlaylistsCard v-if="showCard"></PlaylistsCard>

</template>

<script>
import TopNav from '../components/TopNav.vue';
import PlaylistsCard from './PlaylistsCard.vue';

export default {

  data() {
    return {
      dummy_groups: [
        "group1", "group2", "group3"
      ],
      typingText: '',
      subtitle: '',
      showCard: false,
    }
  },
  components: {
    TopNav, PlaylistsCard
  },
  mounted() {
    this.typeText()
  },
  methods: {
    typeText() {
      const text = 'Craft the ultimate playlist'
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
      const text = ' with your friends.'
      let index = 0
      const typingInterval = setInterval(() => {
        this.subtitle += text[index]
        index++
        if (index === text.length) {
          clearInterval(typingInterval)
          setTimeout(() => {
            this.showCard = true
          }, 1500)
        }
      }, 50)
    }
  },
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

<script>
import TopSongsCard from '../components/TopSongsCard.vue';
import TopArtistsCard from '../components/TopArtistsCard.vue';
import TopAlbumsCard from '../components/TopAlbumsCard.vue';
import HistoryCard from '../components/HistoryCard.vue'



export default {
  components: {
    TopSongsCard, TopArtistsCard, TopAlbumsCard, HistoryCard
  }
}
</script>

<template>
  <div class="m-4">
    <h0>Explore your listening</h0>
    <h2 style="color: grey">as of this week.</h2>
  </div>


  <br />
  <br />

  <TopSongsCard></TopSongsCard>
  <TopArtistsCard></TopArtistsCard>
  <TopAlbumsCard></TopAlbumsCard>
  <HistoryCard></HistoryCard>

  <br>
  <br>


  <button class="empty-btn">
    populate songs, artists, and albums (empty button)
  </button>
  <p>note: maybe we should keep it to maximum 4 or 5 ish</p>
</template>
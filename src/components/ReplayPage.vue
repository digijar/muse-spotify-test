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

    <div>
        <h1>Explore your listening</h1>
        <h5 style="color: grey">As of this week.</h5>
    </div>


    <br/>
    <br/>

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
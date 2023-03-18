<script>
import TopSongsCard from '../components/TopSongsCard.vue';
import TopArtistsCard from '../components/TopArtistsCard.vue';
import TopAlbumsCard from '../components/TopAlbumsCard.vue';



export default {
  components: {
    TopSongsCard, TopArtistsCard, TopAlbumsCard
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
    

<button class="empty-btn">
    populate songs, artists, and albums (empty button)
</button>
</template>
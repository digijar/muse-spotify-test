<script>
export default {
  data() {
    return {
      dummy_songs: [
        ["Kill Bill", "SZA", "69 plays"],
        ["Flowers", "Miley Cyrus", "57 plays"],
        ["The Most Beautiful Thing", "Bruno Major", "49 Plays"],
        ["As It Was", "Harry Styles", "35 plays"],
        ["fifth song", "idk who", "50 plays"],
      ],
      top_tracks: {

      }
    }
  }
}
</script>


<template>
  <div>
    <div class="m-4">
      <h4 style="color: black">Top Songs</h4>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for='list in dummy_songs' class="col">
          <div class="card-1 card-block"></div>
          <div>
            <h5 class="title mt-3">{{ list[0] }}</h5>
            <h5 class="sub-title-1 mt-1">{{ list[1] }}</h5>
            <h6 class="sub-title-2 mt-2">{{ list[2] }}</h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
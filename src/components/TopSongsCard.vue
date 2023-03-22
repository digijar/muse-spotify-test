<script>
export default {
  data() {
    return {
      test: ["hello", "2"],
      dummy_songs: [
        ["Kill Bill", "SZA", "69 plays"],
        ["Flowers", "Miley Cyrus", "57 plays"],
        ["The Most Beautif...", "Bruno Major", "49 Plays"],
        ["As It Was", "Harry Styles", "35 plays"],
        ["fifth song", "idk who", "50 plays"],
      ]
    }
  }
}

</script>


<template>
  <div>
    <h5 style="color: black">Top Songs</h5>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
        <div v-for='list in dummy_songs' class="col">
          <div class="card-1 card-block"></div>
          <div>
            <h6>{{ list[0] }}</h6>
            <h6 style="font-weight:400">{{ list[1] }}</h6>
            <h6 style="color: grey; font-weight:400; font-size: 14px;">{{ list[2] }}</h6>
          </div>
        </div>
      </div>
    </div>
  </div>
  <br />
  <br />
</template>
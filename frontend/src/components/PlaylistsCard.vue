<template>
  <div>
    <div class="m-4">
      <h4 style="color: black">Your Shared Playlists</h4>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for='playlist in dummy_playlists' class="col">
          <RouterLink to="/blend">
            <div class="card-1 card-block"></div>
          </RouterLink>
          <div>
            <h5 class="title mt-3">{{ playlist.playlistName }}</h5>
            <h6 class="sub-title-2 mt-1">{{ playlist.contributors.join(', ') }} and You </h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      dummy_playlists: [
        {
          "playlistID": "1f2f507e-03c2-4b7d-94e6-3819477c35f6",
          "playlistName": "Playlist 1",
          "contributors": [
            "Person A",
            "Person B",
            "Person C"
          ]
        },
        {
          "playlistID": "39aa5ebf-5d5c-4425-a5af-8e534563a3d7",
          "playlistName": "Playlist 2",
          "contributors": [
            "Person D",
            "Person E"
          ]
        },
        {
          "playlistID": "ad39127a-4b4d-4f4d-a70f-1e2f0dd7f520",
          "playlistName": "Playlist 3",
          "contributors": [
            "Person F",
            "Person G",
            "Person H"
          ]
        },
        {
          "playlistID": "d08cf84a-f3a7-4447-8b29-83c436ff70d2",
          "playlistName": "Playlist 4",
          "contributors": [
            "Person I"
          ]
        },
        {
          "playlistID": "e8710d62-d121-475e-a10d-9e1fa45a6162",
          "playlistName": "Playlist 5",
          "contributors": [
            "Person J",
            "Person K",
            "Person L",
            "Person M",
            "Person N"
          ]
        }
      ]
    }
  }
}
</script>

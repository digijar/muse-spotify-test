<script>
export default {
  data() {
    return {
      test: ["hello", "2"],
      dummy_albums: [
        ["Easy On Me", "Stephen Sanchez", '53 Plays'],
        ["A Moment or Two", "Troye Sivan", "29 Plays"],
        ["Ultraviolence", "Lana Del Rey", "17 Plays"],
        ["Awaken, My Lov...", "Childish Gambino", "12 Plays"],
        ["Awaken, My Lov...", "Childish Gambino", "12 Plays"]
      ]
    }
  }
}
</script>

<template>
  <div>
    <div class="m-4">
      <h4 style="color: black">Top Albums</h4>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for='list in dummy_albums' class="col">
          <div class="card-3 card-block"></div>
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
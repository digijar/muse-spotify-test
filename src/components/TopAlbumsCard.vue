<script>
export default {
  data() {
    return {
      test: ["hello", "2"],
      dummy_albums: [
        ["Easy On Me", "Stephen Sanchez", '53 Plays'],
        ["A Moment or Two", "Troye Sivan", "29 Plays"],
        ["Ultraviolence", "Lana Del Rey", "17 Plays"],
        ["Awaken, My Lov...", "Childish Gambino", "12 Plays"]
      ]
    }
  }
}
</script>

<template>
  <div>
    <h5 style="color: black">Top Albums</h5>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
        <div v-for='list in dummy_albums' class="col-3">
          <div class="card-3 card-block"></div>
          <div>
            <h6>{{ list[0] }}</h6>
            <h6 style="font-weight:400">{{ list[1] }}</h6>
            <h6 style="font-weight:400; color: grey">{{ list[2] }}</h6>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>
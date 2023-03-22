<script>
export default {
  data() {
    return {
      test: ["hello", "2"],
      dummy_artists: [
        ["Le Sserafim", "352 minutes"],
        ["Beyoncé", "230 minutes"],
        ["NewJeans", "182 minutes"],
        ["Billie Eilish", "175 minutes"],
        ["artist", "minjutes"]
      ]
    }
  }
}

</script>

<template>
 <div>
    <div class="m-4">
      <h4 style="color: black">Top Artists</h4>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for='list in dummy_artists' class="col">
          <div class="card-block-round card-2 text-center"></div>
          <div class="text-center">
            <h5 class="title mt-3">{{ list[0] }}</h5>
            <h6 class="sub-title-2 mt-2">{{ list[1] }}</h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
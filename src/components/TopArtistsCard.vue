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
        ["someone", "10 minutes"],
        ["someone", "10 minutes"],
        ["someone", "10 minutes"],
        ["someone", "10 minutes"],

      ]
    }
  }
}

</script>

<template>
  <div>
    <h5 style="color: black">Top Artists</h5>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
        <div v-for='list in dummy_artists' class="col-3">
          <div class="card-block-round card-2 text-center"></div>
          <div class="text-center">
            <h6>{{ list[0] }}</h6>
            <h6 style="font-weight:400; color: grey">{{ list[1] }}</h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
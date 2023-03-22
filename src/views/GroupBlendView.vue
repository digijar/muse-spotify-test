<script>
import TopNav from '../components/TopNav.vue';

export default {

  data() {
    return {
      dummy_groups: [
        "group1", "group2", "group3"
      ]
    }
  },
  components: {
    TopNav
  }
}
</script>

<template>
  <TopNav></TopNav>

  <div class="m-4">
    <div>
      <h2>Craft the ultimate playlist</h2>
      <h4 style="color: grey">with your friends.</h4>
    </div>
  </div>

  <div>
    <div class="m-4">
      <h4 style="color: black">Your Shared Playlists</h4>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
        <div v-for='item in dummy_groups' class="col-2">
          <RouterLink to="/blend">
            <div class="card-block card-2 text-center"></div>
          </RouterLink>
          <div class="text-center">
            <h6>{{ item }}</h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>




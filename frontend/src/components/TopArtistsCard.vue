<template>
  <div>
    <div class="m-4">
      <h3 style="color: black">Top Artists</h3>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for="(artist, index) in itemsToShow" class="col">
          <div class="card-block-round text-center">
            <a :href="artist.external_urls.spotify" target="_blank">
              <img class="card-img-top" :src="artist.images[0].url" :alt="artist.name"
                style="height: 280px; width: 280px; object-fit: cover; border-radius: 50%;">
            </a>
          </div>
          <div class="text-center">
            <h4 class="title mt-3">{{ artist.name.length > 16 ? artist.name.substr(0, 16) + '...' : artist.name }}</h4>
          </div>
        </div>
        <!-- <div class="col d-flex align-items-center" v-if="itemsToShow.length < result.items.length"> -->
          <div class="card-block text-center justify-content-center">
            <button class="btn btn-outline-secondary" @click="showMore"
              style="font-size: 1.2em; padding: 10px 20px; font-weight: 800; display: flex; justify-content: center; align-items: center;">
              View More
            </button>
          </div>
        <!-- </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  data() {
    return {
      result: {},
      itemsToShow: [],
    };
  },
  beforeMount() {
    this.getTopArtists();
  },
  methods: {
    getTopArtists() {
      axios.get('http://127.0.0.1:5001/api/v1/get_top_artists')
        .then((response) => {
          this.result = response.data;
          console.log(response.data)
          this.showMore();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showMore() {
      if (this.result && this.result.items) {
        const startIndex = this.itemsToShow.length
        const endIndex = Math.min(startIndex + 5, this.result.items.length)
        this.itemsToShow.push(...this.result.items.slice(startIndex, endIndex))
      }
    }
  },
};


// export default {
//   data() {
//     return {
//       result: {},
//       itemsToShow: []
//     }
//   },
//   mounted() {
//     this.showMore()
//     this.mongoTopArtists()
//   },
//   methods: {

//     mongoTopArtists() {
      
//     },


//     showMore() {
//       const startIndex = this.itemsToShow.length
//       const endIndex = Math.min(startIndex + 5, this.result.items.length)
//       this.itemsToShow.push(...this.result.items.slice(startIndex, endIndex))
//     }
//   }
// }
</script>
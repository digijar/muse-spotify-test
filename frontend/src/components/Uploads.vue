<template>
  <div>

    <br>
    <br>
    <br>


    <div>
      <div v-if="personalUpload">
        <div class="container mt-4">
          <div class="text-center">
            <h5>Your uploaded playlist</h5>
          </div>
          <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2 justify-content-center">
              <div class="col-3 mr-2">
                <div class="card bg-light mb-3">
                  <div class="card-body text-center">
                    <div class="square shadow-4-strong" :style="{ 'background-image': 'url(' + personalAlbumCover + ')', 'background-size': 'cover', 'background-position': 'center', 'background-color': 'transparent' }"></div>
                    <h6 class="card-title mb-3">{{personalAlbumName}}</h6>
                    <h6 class="card-subtitle text-muted mb-2"> <a :href="personalAlbumLink" target="_blank">Album Link</a></h6>
                  </div>

                  <div v-if="personalUpload && recommendedStatus == false">
                    <button class="text center" data-bs-toggle="modal" data-bs-target="#changeBtnModal">change your
                      playlist?</button>
                  </div>
                </div>
              </div>
              <!-- add more card elements here as needed -->
            </div>
          </div>
        </div>
      </div>


      <div v-else>
        <div class="container mt-4">
          <div class="text-center">
            <h5>Upload your playlist!</h5>
            <h5>Your friends are waiting for you</h5>
            <button class="" data-bs-toggle="modal" data-bs-target="#changeBtnModal">Upload your playlist!</button>
          </div>
          <!-- <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2 justify-content-center">
              <div class="col-3 mr-2">
                <div class="card bg-light mb-3">
                  <div class="card-body text-center">
                    <div class="square rounded-circle"></div>
                    <h6 class="card-title mb-0">album name</h6>
                    <h6 class="card-subtitle text-muted mb-2">album link</h6>
                  </div>
                  <div>
                    <button class="" data-bs-toggle="modal" data-bs-target="#changeBtnModal">Upload your playlist!</button>
                  </div>
                </div>
              </div>
            </div>
          </div> -->
        </div>
      </div>
    </div>

    <div>
      <div v-if="groupStatus == 'waiting'">
        <div class="container mt-4">
          <div class="text-center">
            <h5>Waiting for groupmates to upload...</h5>
          </div>
        </div>
      </div>

      <div v-else>

        <div v-if="recommendedStatus == true" class="container mt-4">
          <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2 justify-content-center">
              <div class="col-3 mr-2">
                <div class="card bg-light mb-3">
                  <div class="card-body text-center">
                    <div class="square shadow-4-strong" :style="{ 'background-image': 'url(' + recommendedAlbumCover + ')', 'background-size': 'cover', 'background-position': 'center', 'background-color': 'transparent' }"></div>
                    <h6 class="card-title mb-3">{{recommendedAlbumName}}</h6>
                    <h6 class="card-subtitle text-muted mb-2"> <a :href="recommendedAlbumLink" target="_blank">Recommended Album Link</a></h6>
                    <button @click="deleteRecommendedPlaylist">Remove Playlist?</button>
                  </div>
                </div>
              </div>
              <!-- add more card elements here as needed -->
            </div>
          </div>
        </div>

        <div v-else class="container mt-4">
          <div class="text-center">
            <h5>All your friends have uploaded their playlists!</h5>
            <h5>But no one has generated a new playlist yet!</h5>
            <button @click="generateRecommendations">Generate Playlist Recommendation?</button>
          </div>
        </div>
      </div>
    </div>


    <!-- modal -->
    <div class="modal fade" id="changeBtnModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="btn1ModalLabel">New playlist</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Playlist URL: {{ this.inputPlaylistLink }}</label>
                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="inputPlaylistLink">
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button @click="savePlaylist" type="button" class="btn btn-primary" data-bs-dismiss="modal">Save Changes</button>
          </div>
        </div>
      </div>
    </div>




  </div>
</template>

<script>
import axios from 'axios'
const email = localStorage.getItem('email')
const auth_token = localStorage.getItem('spotifyAuthToken')

export default {
  props: ["group_name"],

  data() {
    return {
      personalUpload: false,
      personalAlbumName: "",
      personalAlbumLink: "",
      personalAlbumCover: "",

      inputPlaylistLink: "",

      groupStatus: "waiting",
      // waiting, successful

      recommendedStatus: false,
      recommendedAlbumCover: "",
      recommendedAlbumName: "",
      recommendedAlbumLink: "",

    playlist_ids: [],
    }
  },

  created() {
    // this.checkPersonalUpload()
    this.checkGroupStatus()
    this.checkRecommendedStatus()
  },

  beforeMount() {
    this.checkPersonalUpload()
  },

  methods: {
    checkPersonalUpload() {
      axios.get('http://127.0.0.1:5004/api/v1/check_personalUpload', {
        headers: {
          'Authorization': `Bearer ${auth_token}`,
          'Email': `${email}`,
          "group_name": this.group_name
        }
      })
        .then((response) => {
          console.log('personal upload: ' + response.data.bool)
          this.personalUpload = response.data.bool;
          if (this.personalUpload == true) {
            this.personalAlbumName = response.data.name
            this.personalAlbumLink = response.data.link
            this.personalAlbumCover = response.data.cover
          }
        })
        .catch((error) => {
          console.log(error);
      });
    },

    checkGroupStatus() {
      axios.get('http://127.0.0.1:5004/api/v1/check_groupStatus', {
        headers: {
          "group_name": this.group_name
        }
      })
        .then((response) => {
          console.log(response.data)
          if (response.data.bool == true) {
            this.groupStatus = "successful"
          }
          this.playlist_ids = response.data.playlist_arr
        })
        .catch((error) => {
          console.log(error);
      });
    },

    // for Recommendations
    checkRecommendedStatus() {
      axios.get('http://127.0.0.1:5004/api/v1/check_recommendedStatus', {
        headers: {
          "group_name": this.group_name
        }
      })
        .then((response) => {
          console.log('recommended status: ' + response.data.bool)
          this.recommendedStatus = response.data.bool
          if (this.recommendedStatus == true) {
            this.recommendedAlbumCover = response.data.cover
            this.recommendedAlbumName = response.data.name
            this.recommendedAlbumLink = response.data.link
          }
        })
        .catch((error) => {
          console.log(error);
      });
    },

    savePlaylist() {
      axios.post('http://127.0.0.1:5004/api/v1/save_playlist', 
      {
        'playlist_link': this.inputPlaylistLink,
        'email': `${email}`,
        "group_name": this.group_name
      })
        .then((response) => {
          console.log('playlist saved?' + response.data)
        })
        .catch((error) => {
          console.log(error);
      });

      this.inputPlaylistLink = ""
      setTimeout(function(){
        window.location.reload();
      }, 3000);
    },

    generateRecommendations() {
      axios.get('http://127.0.0.1:5004/api/v1/get_recommendations', {
        headers: {
          'Authorization': `Bearer ${auth_token}`,
          'Email': `${email}`,
          "group_name": this.group_name,
          'playlist_ids': this.playlist_ids.join(',')
        }
      })
        .then((response) => {
          console.log(response.data)
          setTimeout(function(){
            window.location.reload();
          }, 5000);
      })
        .catch((error) => {
          console.log(error);
      });
    },

    deleteRecommendedPlaylist() {
      axios.post('http://127.0.0.1:5004/api/v1/remove_playlist', 
      {
        "group_name": this.group_name
      })
        .then((response) => {
          console.log('recommended playlist deleted?' + response.data)
          setTimeout(function(){
            window.location.reload();
          }, 3000);
      })
        .catch((error) => {
          console.log(error);
      });
    }
  }
}
</script>
<template>
  <div>

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
                    <div class="square rounded-circle"></div>
                    <h6 class="card-title mb-0">album name</h6>
                    <h6 class="card-subtitle text-muted mb-2">artist name</h6>
                  </div>

                  <div v-if="personalUpload && groupStatus == 'waiting'">
                    <button class="">change your playlist?</button>
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
          </div>
          <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2 justify-content-center">
              <div class="col-3 mr-2">
                <div class="card bg-light mb-3">
                  <div class="card-body text-center">
                    <div class="square rounded-circle"></div>
                    <h6 class="card-title mb-0">album name</h6>
                    <h6 class="card-subtitle text-muted mb-2">artist name</h6>
                  </div>
                </div>
              </div>
              <!-- add more card elements here as needed -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <div>
      <div v-if="groupStatus == 'waiting'">
        <div class="container mt-4">
          <div class="text-center">
            <h5>Waiting for groupmates to upload...</h5>
          </div>
          <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2 justify-content-center">
              <div class="col-3 mr-2">
                <div class="card bg-light mb-3">
                  <div class="card-body text-center">
                    <div class="square rounded-circle"></div>
                    <h6 class="card-title mb-0">album name</h6>
                    <h6 class="card-subtitle text-muted mb-2">artist name</h6>
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
            <h5>Your group's playlist upload was successful!</h5>
          </div>
          <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2 justify-content-center">
              <div class="col-3 mr-2">
                <div class="card bg-light mb-3">
                  <div class="card-body text-center">
                    <div class="square rounded-circle"></div>
                    <h6 class="card-title mb-0">album name</h6>
                    <h6 class="card-subtitle text-muted mb-2">artist name</h6>
                  </div>
                </div>
              </div>
              <!-- add more card elements here as needed -->
            </div>
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
      personalUpload: true,
      groupStatus: "waiting",
      // waiting, successful
    }
  }
}
</script>
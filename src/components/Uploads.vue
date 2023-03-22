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
                    <button class="" data-bs-toggle="modal" data-bs-target="#changeBtnModal">change your
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
                <label for="exampleInputEmail1" class="form-label">Playlist URL</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Save Changes</button>
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
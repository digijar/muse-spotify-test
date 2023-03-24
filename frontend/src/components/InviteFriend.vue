<template>
  <br>
  <br>

  
  <div class="container">
    <div class="row">
      <div class="col-md-2 text-center">
        <div class="rounded-circle bg-primary d-flex align-items-center justify-content-center"
          style="height: 150px; width: 150px;">
          <span class="text-white" style="font-size: 3em;">you</span>
        </div>
      </div>

      <div class="col-md-2 text-center" v-for="i in 4" data-bs-toggle="modal" data-bs-target="#btn1Modal">
        <div class="rounded-circle bg-primary d-flex align-items-center justify-content-center"
          style="height: 150px; width: 150px;">
          <span class="text-white font-weight-bold" style="font-size: 3em;">+</span>
        </div>
      </div>

    </div>
  </div>

  <div class="modal fade" id="btn1Modal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="btn1ModalLabel">Invite!</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Email address</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Send!</button>
        </div>
      </div>
    </div>
  </div>

  <!-- <div v-if="UserDetails" @click="toggleUserView(UserDetails.name, UserDetails.id)">

  </div> -->
</template>

<script>

// export default{
//   props:['UserDetails'],

//   methods:{
//     toggleUserView = router.push(UserDetails)
//   }
// }

</script>
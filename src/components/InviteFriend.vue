<template>
  <div class="container">
    <div class="row align-items-start">

      <div class="col" style="position: relative">
        <span class="big-icon"></span>
      </div>




      <div class="col" style="position: relative">
        <span class="small-icon1 text-center">
          <button type="button" class="add-btn btn" data-bs-toggle="modal" data-bs-target="#btn1Modal"
            id="btn1">+</button>
        </span>

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
      </div>

      <div class="col" style="position: relative">
        <span class="small-icon1 text-center">
          <button class="add-btn" id="btn2">+</button>
        </span>
      </div>

      <div class="col" style="position: relative">
        <span class="small-icon1 text-center">
          <button class="add-btn" id="btn3">+</button>
        </span>
      </div>

      <div class="col" style="position: relative">
        <span class="small-icon1 text-center">
          <button class="add-btn" id="btn4">+</button>
        </span>
      </div>
    </div>
  </div>
</template>
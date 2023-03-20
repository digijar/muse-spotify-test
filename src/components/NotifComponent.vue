<template>
    <div class="d-flex flex-row bd-highlight mb-3">
        <h6>You've been invited!</h6>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Click to join!
        </button>
    </div>

    <div class="d-flex flex-row bd-highlight mb-3">
        <h6>You've just sent an invitation!</h6>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Click to join!
        </button>
    </div>



    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Success!</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <h5>You've successfully joined the group!</h5>
                    <h5>Go to blend to upload your playlist</h5>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Ok! Blend later</button>
                    <RouterLink to="/blend"><button type="button" class="btn btn-primary" data-bs-dismiss="modal">Start blending</button></RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>


 


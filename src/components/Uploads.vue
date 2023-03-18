<template>
    <!-- personal upload playlist -->
    <h3>note: uploaded personal playlist:</h3>
    <div>
        <h5 style="color: black">
            <h5>Your uploaded playlist</h5>
        </h5>
        <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                <div class="col-3">
                    <div class="card-1 card-block"></div>
                    <div>
                        <h6>hello</h6>
                        <h6 style="font-weight:400">ok</h6>
                        <h6 style="color: grey; font-weight:400; font-size: 14px;">yes</h6>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- if you have not uploaded the playlist -->
    <h3>note: if you have not uploaded the playlist:</h3>
    <div>
        <h5 style="color: black">
            <h5>Upload your playlist</h5>
            <h6>Your friends are waiting!</h6>
        </h5>
        <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                <div class="col-3">
                    <div class="card-1 card-block align-middle">+</div>
                    <!-- CENTRALISE THE PLUS SIGN, MAKE THIS A BUTTON -->
                </div>
            </div>
        </div>
    </div>

    <!-- generated playlist from friends upload -->
    <h3>note: when your group successfully created playlist:</h3>
    <div>
        <div>
            <h5 style="color: black">
                <h5>Your group's playlist</h5>
                <h6>exclusively generated for you and your friends</h6>
            </h5>
            <div class="container-fluid">
                <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                    <div class="col-3">
                        <div class="card-1 card-block"></div>
                        <div>
                            <h6>hello</h6>
                            <h6 style="font-weight:400">ok</h6>
                            <h6 style="color: grey; font-weight:400; font-size: 14px;">yes</h6>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- if not all members have created the playlist -->
    <h3>note: if not all members have created the playlist:</h3>
    <div>
        <div>
        <h5 style="color: black">
            <h5>Upload your playlist</h5>
            <h6>Your friends are waiting!</h6>
        </h5>
        <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                <div class="col-3">
                    <div class="card-1 card-block align-middle">waiting...</div>
                    <!-- CENTRALISE THIS -->
                </div>
            </div>
        </div>
    </div>
    </div>

    <h3>note: when you want to change the playlist while waiting for the group to generate</h3>
    <div>
        <div>
            <h5 style="color: black">
                <h5>Your playlist</h5>
            </h5>
            <div class="container-fluid">
                <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                    <div class="col-3">
                        <div class="card-1 card-block"></div>
                        <div>
                            <h6>hello</h6>
                            <h6 style="font-weight:400">ok</h6>
                            <h6 style="color: grey; font-weight:400; font-size: 14px;">yes</h6>
                            <button>Change your mind? click to replace this playlist with a new one!</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <h5>note: the page should look like theres 2 squares, one for personal playlist and one for group's generated playlist, top and bottom centralised.</h5>
</template>
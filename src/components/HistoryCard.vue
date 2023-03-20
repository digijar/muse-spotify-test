<template>
    <div>
        <h5 style="color: black">History</h5>

    </div>

    <br>

    <div>
        <div v-if='history' style="font-weight: 400">
            <div>
                <h5 style="color: black">Your Albums</h5>
                <div class="container-fluid">
                    <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                        <div v-for='list in dummy_history' class="col-3">
                            <div class="card-3 card-block"></div>
                            <div>
                                <h6>{{ list[0] }}</h6>
                                <h6 style="font-weight:400">{{ list[1] }}</h6>
                                <h6 style="font-weight:400; color: grey">{{ list[2] }}</h6>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <h6 style="color: grey">It's empty now! Check out
                <RouterLink to="/blend">
                    <a style="color: black">blend</a>
                </RouterLink>
                to create playlists with your friend!
            </h6>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            history: true,
            dummy_history: [
                ["Easy On Me", "Stephen Sanchez", '53 Plays'],
                ["A Moment or Two", "Troye Sivan", "29 Plays"],
                ["Ultraviolence", "Lana Del Rey", "17 Plays"],
                ["Awaken, My Lov...", "Childish Gambino", "12 Plays"]
            ]
        }
    },
}
</script>
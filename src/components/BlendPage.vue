
<template>
    <h1>Craft the ultimate playlist</h1>
    <h5>With your friends.</h5>

        <div>
            <h5>Choose Your Group</h5>
            <div class="container-fluid">
                <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                    <div v-for='item in dummy_groups' class="col-3">
                        <div class="card-block-round card-2 text-center"></div>
                        <div class="text-center">
                            <h6>{{ item }}</h6>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div>
            the things below should be on a separate page that takes in data dynamically
        </div>
</template>

<script>

export default {
    data() {
        return {
            dummy_groups: [
                "group1", "group2", "group3"
            ]
        }
    },
}
</script>


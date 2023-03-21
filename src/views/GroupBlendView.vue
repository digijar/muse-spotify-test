<script>
import TopNav from '../components/TopNav.vue';

export default {

    data() {
        return {
            dummy_groups: [
                "group1", "group2", "group3"
            ]
        }
    },
    components: {
        TopNav
    }
}
</script>

<template>
    <TopNav></TopNav>

    <h1>Craft the ultimate playlist</h1>
    <h5>With your friends.</h5>

    <div>
        <h5>Choose Your Group</h5>
        <div class="container-fluid">
            <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
                <div v-for='item in dummy_groups' class="col-3">
                    <RouterLink to="/blend">
                        <div class="card-block-round card-2 text-center"></div>
                    </RouterLink>
                    <div class="text-center">
                        <h6>{{ item }}</h6>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>




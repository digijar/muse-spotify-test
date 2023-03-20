<script>
import TopNav from '../components/TopNav.vue';
import BlendPage from '../components/BlendPage.vue';
import Upload from '../components/Uploads.vue';
import InviteFriend from '../components/InviteFriend.vue'

export default {
  components: {
    TopNav, BlendPage, Upload, InviteFriend
  }
}


</script>

<template>
    <TopNav></TopNav>
    <BlendPage></BlendPage>
    <Upload></Upload>
    <InviteFriend></InviteFriend>
</template>
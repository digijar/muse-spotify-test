<script>
import TopNav from '../components/TopNav.vue';
import BlendPage from '../components/BlendPage.vue';
import Uploads from '../components/Uploads.vue';
import InviteFriend from '../components/InviteFriend.vue'

export default {
  components: {
    TopNav, BlendPage, Uploads, InviteFriend
  }
}


</script>

<template>
    <TopNav></TopNav>
    <BlendPage></BlendPage>
    <Uploads></Uploads>
    <InviteFriend></InviteFriend>
</template>
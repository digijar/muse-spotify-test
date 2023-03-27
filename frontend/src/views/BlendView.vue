<script>
import TopNav from '../components/TopNav.vue';
import Uploads from '../components/Uploads.vue';
import InviteFriend from '../components/InviteFriend.vue'

export default {
  components: {
    TopNav, Uploads, InviteFriend
  },
  // methods:{
  //   toggleUserView = ()
  // }
}
</script>

<template>
  <div>
    <TopNav></TopNav>
    <Uploads></Uploads>
    <InviteFriend></InviteFriend>
  </div>
</template>

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
  </div>
  <div>
    <br><br><br><br><br>
    <h4 style="text-align: center;">Group: {{ $route.params.group_name }}</h4>
    <Uploads></Uploads>
    <InviteFriend></InviteFriend>
    <br><br><br><br>
  </div>
</template>

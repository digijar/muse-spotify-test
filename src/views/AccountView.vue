<script>
import TopNav from '../components/TopNav.vue';
import AccountPage from '../components/AccountPage.vue'
import NotifComponent from '../components/NotifComponent.vue'

export default {
  components: {
    TopNav, AccountPage, NotifComponent
  }
}
</script>

<template>
  <TopNav></TopNav>
  <AccountPage></AccountPage>
  <NotifComponent></NotifComponent>
</template>
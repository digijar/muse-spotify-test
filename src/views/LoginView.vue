<script>
import LoginPage from '../components/LoginPage.vue';
import TopNav from '../components/TopNav.vue'

export default {
  components: {
    TopNav, LoginPage
  }
}
</script>

<template>
  <div>
    <TopNav></TopNav>
    <LoginPage></LoginPage>
  </div>
</template>

<template>
  <nav class="navbar bg-body-tertiary fixed-top">
    <div class="container d-flex justify-content-between">
      <div>
        <router-link to="/" class="nav-item">
          <p class="nav-link text-dark" style="font-size: 25.89px; font-weight: 800;">müse</p>
        </router-link>
      </div>
      <div>
        <router-link to="/groupblend">
          <span class="nav_item active" style="font-size: 25.89px; font-weight: 800;">blend</span>
        </router-link>
        <router-link to="/replay">
          <span class="nav_item" style="font-size: 25.89px; font-weight: 800;">replay</span>
        </router-link>

      </div>

    </div>
  </nav>
  <hr class="solid" style="height: 2px; border-top: 2px solid black; margin: 0px; padding: 0px">
</template>

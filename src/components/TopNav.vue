<template>
  <nav class="navbar bg-body-tertiary d-flex">
    <div class="container d-flex justify-content-between">
      <div>
        <router-link to="/" class="nav-item">
          <p class="nav-link text-dark">müse</p>
        </router-link>
      </div>
      <div>
        <router-link to="/groupblend">
          <span class="nav_item active">blend</span>
        </router-link>
        <router-link to="/replay">
          <span class="nav_item">replay</span>
        </router-link>
        <router-link to="/account">
          <span><i class="bi bi-person-circle">icon</i></span>
        </router-link>
      </div>

    </div>

  </nav>
  <hr class="solid" style="border-top: 2px solid black; margin: 0px; padding: 0px">
</template>
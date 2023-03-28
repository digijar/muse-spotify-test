<template>
  <div>
    <div class="m-4">
      <h4 style="color: black">Your Shared Groups</h4>
    </div>
    <div class="container-fluid">
      <div v-if="actual" class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for='group in actual_groups' class="col">
          <RouterLink :to="{name: 'blend', params: {group_name: group}}">
            <div class="card-1 card-block"></div>
          </RouterLink>
          <div>
            <h5 class="title mt-3">{{ group }}</h5>
            <!-- <h6 class="sub-title-2 mt-1">{{ group.contributors.join(', ') }} and You </h6> -->
          </div>
        </div>
      </div>

      <div v-else class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for='group in dummy_groups' class="col">
          <RouterLink :to="{name: 'blend', params: {group_name: group}}">
            <div class="card-1 card-block"></div>
          </RouterLink>
          <div>
            <h5 class="title mt-3">{{ group }}</h5>
            <!-- <h6 class="sub-title-2 mt-1">{{ group.contributors.join(', ') }} and You </h6> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { createDOMCompilerError } from '@vue/compiler-dom';
import axios from 'axios'
const email = localStorage.getItem('email')

export default {
  data() {
    return {
      actual: false,
      actual_groups: [],
      dummy_groups: ["group microservice not working", "Best Group", "Decent ESD Group", "Hello Spotify", "what is this?"]
    }
  },

  created() {
    this.loadGroups()
  },

  methods: {
    loadGroups() {
      axios.get('http://127.0.0.1:4998/api/v1/get_groups', {
        headers: {
          'Email': `${email}`
        }
      })
        .then((response) => {
          console.log(response.data)

          var group_names = response.data;

          if (group_names.length > 0) {
            this.actual = true
            this.actual_groups = group_names
          }
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }
}
</script>

<template>
  <div>
    <div class="m-4">
      <h4 style="color: black">Your Shared Groups</h4>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div class="col">
          <div class="card-1 card-block ">
            <button class="text-center" data-bs-toggle="modal" data-bs-target="#createGroupModal">create group</button>
          </div>
        </div>
      </div>


      <div v-if="actual" class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for='group in actual_groups' class="col">
          <RouterLink :to="{ name: 'blend', params: { group_name: group } }">
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
          <RouterLink :to="{ name: 'blend', params: { group_name: group } }">
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



  <!-- modal -->
  <div class="modal fade" id="createGroupModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="btn1ModalLabel">New playlist</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label>Group Name</label>
              <input type="text" class="form-control" id="group_name_input" v-model="group_name">
              {{ group_name }}
            </div>

            <!-- <div v-for="i in 5" :key="i" class="mb-3">
              <label>Email input {{ i }}:</label>
              <input type="text" class="form-control" id="email_input" v-model="emails[i - 1]">
            </div> -->

          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button @click="createGroup" type="button" class="btn btn-primary" data-bs-dismiss="modal">Create Group</button>
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
      dummy_groups: ["group microservice not working", "Best Group", "Decent ESD Group", "Hello Spotify", "what is this?"],
      emails: [],
      group_name: ''
    }
  },

  created() {
    this.loadGroups()
  },

  methods: {
    loadGroups() {
      axios.get('http://localhost:8000/api/v1/get_groups', {
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
    },
    createGroup() {
      axios.post('http://localhost:8000/api/v1/create_group', {
        "group_name": this.group_name,
        "email": email
      })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      });

      this.group_name = ''
      setTimeout(function(){
        window.location.reload();
      }, 2000);
    }
  }
}
</script>

<template>
  <div class="vh-100 d-flex justify-content-center align-items-center">
    <div class="container">
      <div class="row d-flex justify-content-center">
        <div class="col-12 col-md-8 col-lg-6">
          <div class="card bg-white" style="background-color: white;">
            <div class="card-body p-5">
              <form class="mb-3 mt-md-4">
                <h2 class="fw-bold mb-2 ">müse</h2>
                <p class=" mb-5">Please enter your email and password</p>
                <div class="mb-3">
                  <label for="email" class="form-label ">Email address</label>
                  <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="email">
                </div>
                <div class="mb-3">
                  <label for="password" class="form-label ">Password</label>
                  <input type="password" class="form-control" id="password" placeholder="*******" v-model="password">
                </div>
                <div class="d-grid">
                  <RouterLink to="/groupblend">
                    <button @click.prevent="createUserCredentials" class="btn btn-outline-dark" type="submit">Sign Up</button>
                  </RouterLink>
                </div>
              </form>
              <div>
                <p class="mb-0  text-center">Have an account?
                  <RouterLink to=/loginauth><a href="signup.html" class="text-primary fw-bold">Login</a></RouterLink>
                </p>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignUpPage',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    async createUserCredentials() {
      try {
        console.log(this.email, this.password);

        // Send request to Flask API to authenticate user and retrieve JWT
        const response = await axios.post('http://127.0.0.1:5003/api/createUser', {
          email: this.email,
          password: this.password,
        });

        const { access_token } = response.data;
        console.log('SignUp successful');

        
        // Redirect to login page
        this.$router.push('/loginauth');
      } catch (error) {
        console.error(error);
        console.log('SignUp failed');
      }
    },
  },
};
</script>
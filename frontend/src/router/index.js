import { createRouter, createWebHistory } from 'vue-router'
import ReplayView from '../views/ReplayView.vue'
import BlendView from '../views/BlendView.vue'
import LoginView from '../views/LoginView.vue'
// import AccountView from '../views/AccountView.vue'
import LoginAuthView from '../views/LoginAuthView.vue'
import SignUpView from '../views/SignUpView.vue'
import Test from '../views/Test.vue'
import GroupBlend from '../views/GroupBlendView.vue'
import axios from 'axios'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/replay',
      name: 'replay',
      component: ReplayView,
      meta: {
        needsAuth: true
      }
    },
    {
      path: '/blend/:group_name',
      name: 'blend',
      component: BlendView,
      meta: {
        needsAuth: true
      }
    },
    {
      path: '/loginauth',
      name: 'loginauth',
      component: LoginAuthView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/groupblend',
      name: "groupblend",
      component: GroupBlend,
      meta: {
        needsAuth: true
      }
    },

    {
      path: '/test/:id',
      name: "Test",
      component: Test
    }
  ]
})

const SPOTIFY_AUTH_ENDPOINT = 'https://accounts.spotify.com/authorize'
const REFRESH_TIME_LIMIT = 3599 // 1 hour in seconds

router.beforeEach((to, from, next) => { // this is to check if user logged in
  if (to.meta.needsAuth && sessionStorage.getItem("access_token") == null) {
    next("/loginauth");
  } else {
    next();
  }
})

router.beforeEach((to, from, next) => {
  const auth_token = localStorage.getItem('spotifyAuthToken')
  const urlParams = new URLSearchParams(window.location.search)
  const code = urlParams.get('code')

  if (!auth_token && !code) {
    // Authorization token does not exist, redirect to Spotify auth page
    redirectToSpotifyAuth()
  } else if (code) {
    // Code is present, get the auth token from the Python backend
    getAuthTokenFromPython(code)
    location.reload();
  } else {
    // Authorization token exists, check if it needs to be refreshed
    const refresh_token = localStorage.getItem('spotifyRefreshToken')
    const expiry_time = localStorage.getItem('spotifyExpiryTime')

    const now = new Date().getTime()
    if (expiry_time && now > parseInt(expiry_time)) {
      // Authorization token has expired, refresh it with the refresh code
      refreshAuthTokenWithPython()
    } else {
      // Authorization token is still valid, set a timer to refresh it when it expires
      const time_until_expiry = parseInt(expiry_time) - now
      setTimeout(refreshAuthTokenWithPython, time_until_expiry)
    }
  }
  getUserEmail(auth_token)
  next()
})

function getUserEmail(auth_token) {
  axios.get('http://127.0.0.1:5002/api/v1/email', {
    headers: {
      'Authorization': `Bearer ${auth_token}`
    }
  })
    .then((response) => {
      const email = response.data.email

      // Store email in localStorage
      localStorage.setItem('email', email)
    })
    .catch((error) => {
      console.log(error);
    });
}

function redirectToSpotifyAuth() {
  const redirect_uri = window.location.href
  window.location = `${SPOTIFY_AUTH_ENDPOINT}?client_id=a3b760e2b44741e1aefab722fe0af956&response_type=code&redirect_uri=http://localhost:5173/`
}

function getAuthTokenFromPython(code) {
  // Make an Axios API request to the Python microservice to get the authorization token and refresh code
  axios.get('http://127.0.0.1:5002/api/v1/login', { params: { code } })
    .then((response) => {
      const auth_token = response.data.auth_token
      const refresh_token = response.data.refresh_token

      // Store the authorization token and refresh code in localStorage
      localStorage.setItem('spotifyAuthToken', auth_token)
      localStorage.setItem('spotifyRefreshToken', refresh_token)

      // Set a timer to automatically refresh the authorization token using the refresh code
      setTimeout(refreshAuthTokenWithPython, REFRESH_TIME_LIMIT * 1000)
    })
    .catch((error) => {
      console.error(error)
    })
}

function refreshAuthTokenWithPython() {
  // Get the refresh code from localStorage
  const refresh_token = localStorage.getItem('spotifyRefreshToken')

  // Make an Axios API request to the Python microservice to refresh the authorization token
  axios.post('http://127.0.0.1:5002/api/v1/refresh', { refresh_token })
    .then((response) => {
      const auth_token = response.data.auth_token

      // Store the new authorization token in localStorage
      localStorage.setItem('spotifyAuthToken', auth_token)

      // Set a timer to automatically refresh the authorization token again
      setTimeout(refreshAuthTokenWithPython, REFRESH_TIME_LIMIT * 1000)
    })
    .catch((error) => {
      console.error(error)
    })
}

export default router

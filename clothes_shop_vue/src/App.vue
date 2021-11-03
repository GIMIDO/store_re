<template>
  <div id="app">
<!--  -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div class="container px-4 px-lg-5">
        <router-link to="/" class="navbar-brand fw-bold fst-italic fs-4">leMode</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="dropdown me-auto ms-lg-4">

          <button class="btn btn-outline-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
            Categories menu
          </button>

          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
            <router-link to="/shoes" class="dropdown-item" href="#">Shoes</router-link>
            <router-link to="/pants" class="dropdown-item" href="#">Pants</router-link>
            <router-link to="/hoodies" class="dropdown-item" href="#">Hoodies</router-link>
          </ul>
        </div>

          <!-- <form class="d-flex my-1 me-2">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form> -->

          <form class="d-flex">
            <template v-if="$store.state.isAuthenticated">
              <router-link to="/account" class="btn btn-primary me-2">Account</router-link>
            </template>
            <template v-else>
              <router-link to="/log-in" class="btn btn-primary me-2">Log In</router-link>
            </template>
              <router-link to="/cart" class="btn btn-success">Cart
                <span class="badge bg-dark ms-1">{{ cartTotalLength }}</span>
              </router-link>
          </form>
        </div>
      </div>
    </nav>
<!--  -->
      <router-view/>
<!--  -->
    <footer class="py-5">
      <p class="m-0 text-center">Copyright &copy; <span class="fst-italic">leMode</span> 2021</p>
    </footer>
<!--  -->
  </div>
</template>

<style lang="scss">

</style>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      cart: {
        items: []
      }
    }
  },

  beforeCreate() {
    this.$store.commit('initializeStore')
  },

  mounted() {
    this.cart = this.$store.state.cart
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    }
    else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },

  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].qty
      }
      return totalLength
    }
  },

}
</script>


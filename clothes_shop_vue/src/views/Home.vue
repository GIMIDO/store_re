<template>
  <div class="home">
    <header class="bg-transparent mt-5">
      <div class="container px-4 px-lg-5">
        <div class="text-center">
          <h1 class="display-4 fw-bolder fst-italic">leMode</h1>
          <p class="lead fw-normal">Subtitle</p>
        </div>
      </div>
    </header>

    <div class="container px-4 px-lg-5 mt-5">
      <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">
        <div class="col mb-5" v-for="clothes in latestClothes" v-bind:key="clothes.id">
          <div class="card h-100">
            <img class="card-img-top" :src="clothes.get_image" alt="..." />
            <div class="card-body p-4">
              <div class="text-center">
                <h5 class="fw-bolder">{{ clothes.name }}</h5>
                {{ clothes.price }} BYN
              </div>
            </div>
            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
              <div class="text-center">
                <router-link v-bind:to="clothes.get_absolute_url" class="btn btn-outline-dark mt-auto">View details</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Home',
  
  data() {
    return {
      latestClothes: []
    }
  },

  mounted() {
    this.getLatestClothes()
    document.title = 'Home | leMode'
  },

  methods: {
    getLatestClothes() {
      axios
        .get('/api/v1/latest-clothes')
        .then(response => {
          this.latestClothes = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

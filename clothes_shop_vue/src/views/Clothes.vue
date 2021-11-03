<template>
    <div class="container px-4 my-5">
		<div class="row gx-4 gx-lg-5 align-items-top">
			<div class="col-md-6"><img class="card-img-top mb-0 mb-md-0" v-bind:src='clothes.get_image'></div>
			<div class="col-md-6">
				<h1 class="display-6 fw-bolder">{{ clothes.name }}</h1>
				<p class="lead my-3">{{ clothes.price }} BYN</p>
				<p class="lead my-3">{{ clothes.description }}</p>
				<div class="fs-6 input-group">
                    <span class="input-group-text">Quantity:</span>
                    <input type="number" min="1" class="form-control" v-model="qty">
					<a class="btn btn-success" @click="addToCart">Add to Cart</a>
				</div>
        <div class="mt-3" v-if="errors.length">
            <div class="alert alert-primary alert-dismissible fade show mb-1" v-for="error in errors" v-bind:key="error" role="alert">
                <strong>{{ error }}</strong>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        </div>
			</div>
		</div>

	</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Clothes',

    data() {
        return {
            message: '',
            clothes: {},
            qty: 1,
            errors: []
        }
    },

    mounted() {
        this.getClothes()
    },

    methods: {
        getClothes() {

            const category_slug = this.$route.params.category_slug
            const clothes_slug = this.$route.params.clothes_slug

            axios
                .get(`/api/v1/clothes/${category_slug}/${clothes_slug}`)
                .then(response => {
                    this.clothes = response.data
                    document.title = this.clothes.name + ' | leMode'
                })
                .catch(error => {
                    console.log(error)
                })
        },

        addToCart() {
            this.errors = []
            if (isNaN(this.qty) || this.qty < 1) {
                this.qty = 1
            }
            const item = {
                clothes: this.clothes,
                qty: this.qty
            }
            this.$store.commit('addToCart', item)
            this.errors.push('added')
        }
    }
}
</script>
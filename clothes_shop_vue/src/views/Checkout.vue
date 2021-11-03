<template>
    <div class="checkout">
        <header class="bg-transparent mt-5">
            <div class="container px-4 px-lg-5">
                <div class="text-center">
                    <h1 class="display-4 fw-bolder fst-italic">Checkout</h1>
                </div>
            </div>
        </header>

        <div class="container px-4 px-lg-5">
            <table class="table mt-5 text-center">
                <thead>
                <tr>
                    <th scope="col">Clothes</th>
                    <th scope="col">Price</th>
                    <th scope="col">qty</th>
                    <th scope="col">Total</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in cart.items" v-bind:key="item.clothes.id">
                    <td>{{ item.clothes.name }}</td>
                    <td>{{ item.clothes.price }} BYN</td>
                    <td>{{ item.qty }}</td>
                    <td>{{ getItemTotal(item).toFixed(2) }} BYN</td>
                </tr>
                </tbody>
                <tfoot>
                <tr>
                    <td colspan="4" class="text-end fw-bold fs-4">Total:&nbsp;{{ cartTotalPrice.toFixed(2) }} BYN</td>
                    
                </tr>
                </tfoot>
            </table>

            <div class="input-group mb-3">
                <input type="text" aria-label="First name" placeholder="First name" class="form-control" v-model="first_name">
                <input type="text" aria-label="Last name" placeholder="Last name" class="form-control" v-model="last_name">
                <input type="text" aria-label="Phone" placeholder="Phone" class="form-control" v-model="phone">
            </div>
            <div class="input-group mb-3">
                <input type="email" aria-label="E-mail" placeholder="E-mail" class="form-control" v-model="email">
            </div>
            <div class="input-group mb-3">
                <input type="text" aria-label="Address" placeholder="Address" class="form-control" v-model="address">
            </div>
            <div class="mb-3" v-if="errors.length">
                <div class="alert alert-danger alert-dismissible fade show mb-1" v-for="error in errors" v-bind:key="error" role="alert">
                    <strong>{{ error }}</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            </div>
            <template v-if="cartTotalLength">
                <hr>
                <button @click="submitForm" class="btn btn-danger">Pay</button>
            </template>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | leMode'
        this.cart = this.$store.state.cart
    },

    methods: {
        getItemTotal(item) {
            return item.qty * item.clothes.price
        },

        submitForm() {
            this.errors = []
            if (this.first_name === '') {
                this.errors.push('The First Name field is missing!')
            }
            if (this.last_name === '') {
                this.errors.push('The Last Name field is missing!')
            }
            if (this.phone === '') {
                this.errors.push('The Phone field is missing!')
            }
            if (this.email === '') {
                this.errors.push('The E-mail field is missing!')
            }
            if (this.address === '') {
                this.errors.push('The Address field is missing!')
            }

            
            if (!this.errors.length) {
                const items = []

                for (let i = 0; i < this.cart.items.length; i++) {
                    const item = this.cart.items[i]
                    const obj = {
                        clothes: item.clothes.id,
                        qty: item.qty,
                        price: item.clothes.price * item.qty
                    }
                    items.push(obj)
                }
                const data = {
                    'first_name': this.first_name,
                    'last_name': this.last_name,
                    'email': this.email,
                    'address': this.address,
                    'phone': this.phone,
                    'items': items
                }
                console.log(data.items)
                axios
                    .post('/api/v1/checkout/', data)
                    .then(response => {
                        this.$store.commit('clearCart')
                        this.$router.push('/cart/success')
                    })
                    .catch(error => {
                        this.errors.push('Something went wrong. Please try again!')
                        console.log(error)
                    })
            }
        }
    },


    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.clothes.price * curVal.qty
            }, 0)
        },

        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.qty
            }, 0)
        }
    }
    
}
</script>
<template>
    <div id="cart">
        <header class="bg-transparent mt-5">
            <div class="container px-4 px-lg-5">
                <div class="text-center">
                <h1 class="display-4 fw-bolder fst-italic">Cart</h1>
                </div>
            </div>
        </header>

        <div class="container px-4 px-lg-5">
        <table class="table mt-5 text-center" v-if="cartTotalLength">
            <thead>
            <tr>
                <th scope="col">Clothes</th>
                <th scope="col">Price</th>
                <th scope="col">qty</th>
                <th scope="col">Total</th>
                <th scope="col"></th>
            </tr>
            </thead>
            <tbody>
                <CartItem
                    v-for="item in cart.items"
                    v-bind:key="item.clothes.id"
                    v-bind:initialItem="item"
                    v-on:removeFromCart="removeFromCart" />
            </tbody>
        </table>
        <h2 v-else>Empty!</h2>
        <div class="input-group mt-5">
            <span class="input-group-text">Summary:&nbsp;<strong>{{ cartTotalPrice.toFixed(2) }} BYN</strong></span>
            <router-link to="/cart/checkout" class="btn btn-primary w-auto">Proceed to checkout</router-link>
        </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
export default {
    name: 'Cart',

    components: {
        CartItem
    },

    mounted() {
        this.cart = this.$store.state.cart
    },

    data() {
        return {
            cart: {
                items: []
            }
        }
    },

    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.clothes.id !== item.clothes.id)
        }
    },

    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.qty
            }, 0)
        },

        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.clothes.price * curVal.qty
            }, 0)
        }
    },

}
</script>
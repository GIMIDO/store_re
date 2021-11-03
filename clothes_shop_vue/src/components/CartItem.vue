<template>
    <tr>
        <td scope="row"><router-link :to="item.clothes.get_absolute_url" class="btn btn-outline-primary">{{ item.clothes.name }}</router-link></td>
        <td><i>{{ item.clothes.price }} BYN</i></td>
        <td>
            <a class="btn btn-danger btn-sm py-0" @click="decrementQty(item)"> - </a>
            <span class="fw-bold mx-2">{{ item.qty }}</span>
            <a class="btn btn-success btn-sm py-0" @click="incrementQty(item)"> + </a>
            
        </td>
        <td class="fw-bold">{{ getItemTotal(item).toFixed(2) }} BYN</td>
        <td><button class="btn btn-outline-danger btn-sm" @click="removeFromCart(item)">Delete</button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',

    props: {
        initialItem: Object
    },

    data() {
        return {
            item: this.initialItem
        }
    },

    methods: {
        getItemTotal(item) {
            return item.qty * item.clothes.price
        },

        decrementQty(item) {
            item.qty -= 1
            if (item.qty === 0) {
                this.$emit('removeFromCart', item)
            }
            this.updateCart()
        },

        incrementQty(item) {
            item.qty += 1
            this.updateCart()
        },

        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },

        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        }
    }
}
</script>
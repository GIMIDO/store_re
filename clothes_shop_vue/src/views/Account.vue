<template>
    <div class="account">
        <header class="bg-transparent mt-5">
            <div class="container px-4 px-lg-5">
                <div class="text-center">
                    <h1 class="display-4 fw-bolder fst-italic">My account page</h1>
                </div>
            </div>
        </header>

        <div class="container px-4 px-lg-5">
            <button @click="logout()" class="btn btn-danger">Log out</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Account',
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')
            this.$router.push('/')
        }
    }
}
</script>
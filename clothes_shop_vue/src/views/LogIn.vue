<template>
    <div class="signUp">
        <header class="bg-transparent mt-5">
            <div class="container px-4 px-lg-5">
                <div class="text-center">
                <h1 class="display-4 fw-bolder fst-italic">Log In</h1>
                </div>
            </div>
        </header>

        <div class="container px-4 px-lg-5 my-5 col-6">
            <form @submit.prevent="submitForm">
                <input type="text" class="form-control mb-3" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model='username'>
                <input type="password" class="form-control mb-3" placeholder="Password" aria-label="Username" aria-describedby="basic-addon1" v-model='password'>
                <div class="mb-3" v-if="errors.length">
                    <div class="alert alert-info alert-dismissible fade show mb-5" v-for="error in errors" v-bind:key="error" role="alert">
                        <strong>{{ error }}</strong>
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                </div>
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                    <button type="submit" class="btn btn-outline-success" >Log In</button>
                </div>
            </form>

            <hr>

            Or <router-link to="/sign-up" class="text-decoration-none"><strong>sign up</strong></router-link> here!
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },

    mounted() {
        document.title = 'Log In | leMode'
    },

    methods: {
        submitForm() {
            axios.defaults.headers.common['Authorization'] = ""
            localStorage.removeItem('token')
            const formData = {
                username: this.username,
                password: this.password
            }

            axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = 'Token ' + token
                    localStorage.setItem('token', token)
                    const toPath = this.$route.query.to || '/cart'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    }
                    else {
                        this.errors.push('Something went wrong. Please try again!')
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>
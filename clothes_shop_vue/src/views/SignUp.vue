<template>
    <div class="signUp">
        <header class="bg-transparent mt-5">
            <div class="container px-4 px-lg-5">
                <div class="text-center">
                <h1 class="display-4 fw-bolder fst-italic">Sign Up</h1>
                </div>
            </div>
        </header>

        <div class="container px-4 px-lg-5 my-5 col-6">
            <form @submit.prevent="submitForm">
                <input type="text" class="form-control mb-3" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model='username'>
                <input type="password" class="form-control mb-3" placeholder="Password" aria-label="Username" aria-describedby="basic-addon1" v-model='password'>
                <input type="password" class="form-control mb-3" placeholder="Confirm password" aria-label="Username" aria-describedby="basic-addon1" v-model='conf_password'>
                <div class="mb-3" v-if="errors.length">
                    <div class="alert alert-info alert-dismissible fade show mb-5" v-for="error in errors" v-bind:key="error" role="alert">
                        <strong>{{ error }}</strong>
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                </div>
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                    <button type="submit" class="btn btn-outline-success" >Sign up</button>
                </div>
            </form>

            <hr>

            Or <router-link to="/log-in" class="text-decoration-none"><strong>login</strong></router-link> here!
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            conf_password: '',
            errors: []
        }
    },

    methods: {
        submitForm() {
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing!')
            }
            if (this.password === '') {
                this.errors.push('The password is too short')
            }
            if (this.password !== this.conf_password) {
                this.errors.push('The password doesn\'t match')
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

            axios
                .post("/api/v1/users/", formData)
                .then(response => {
                    console.log('success')
                    this.$router.push('/log-in')
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data))
                    }
                    else if (error.message) {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(JSON.stringify(error))
                    }
                })

            }
        }
    }
}
</script>
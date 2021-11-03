<template>
    <div id="success">
        <header class="bg-transparent mt-5">
            <div class="container px-4 px-lg-5">
                <div class="text-center">
                    <h1 class="display-4 fw-bolder fst-italic">Thank you for buying</h1>
                    <p class="lead fw-normal">Subtitle</p>
                </div>
            </div>
        </header>
    </div>
</template>

<script>
export default {
    name: 'Success',

    mounted() {
        document.title = 'Success | leMode'
    }
}
</script>
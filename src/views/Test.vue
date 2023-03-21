<template>
    <h1>hello world {{ $route.params.id }}</h1>
    <!-- {{ test.text }} -->
</template>

<!-- <script>
import testData from '../components/test.json'
import { useRoute } from 'vue-router';
import { ref, onMounted } from "vue"

const test = ref(null)
const route = useRoute()
const { id } = route.params

onMounted(async() => {
    const result = await fetch("http://localhost:5173/test/${id}")
    const response = result.json();
    queryMovie.value = response;
    isLoading.value = false;
}

)


</script>
 -->

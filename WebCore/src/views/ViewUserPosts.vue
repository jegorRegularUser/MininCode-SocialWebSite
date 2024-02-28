<template>
<body>
    <navigation :isAuthorized="isAuthorized" :username="username"/>
    <div class="home">
        <post :posts="user_posts"></post>
    </div>
</body>
</template>

<script setup>
// @ is an alias to /src
import navigation from '../components/oftenUsesComponents/navigation.vue';
import axios from 'axios';
import { ref } from 'vue';
import { useRoute } from 'vue-router'
import post from '../components/mainpage/main/post.vue';

const route = useRoute();
const username = route.params.username;
const user_posts = ref([]);
axios
  .post("/api", {method: "get_posts", username: username})
  .then(response => {
        console.log(response)
      if (response["data"]["ok"]) {
        console.log(response)
        user_posts.value.push(response["data"]["posts"])
      }
  })
  .catch(error => (console.log(error)));
  
</script>


<style scoped>
body{
    background-color: #AFAFAF;
    background-image: url("/src/assets/lake1.jpeg");
    background-repeat: no-repeat;
    background-size: cover;

    width: 100%;
    height: 100vh;
}

.home {
    padding-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>

<template>
  <body>
    <navigation :isAuthorized="isAuthorized" :username="username"></navigation>
    <main>
    <section class="posts">
    <post :posts="user_posts"></post>
    </section>
    <section class="features">
      <router-link to="/userpage/newPost" class="aside-item"><span>создать новый пост</span></router-link>
    </section>
    </main>
</body>

</template>
    
<script setup>
import {ref} from 'vue';
import axios from 'axios';
import navigation from "../components/oftenUsesComponents/navigation.vue";
import post from '../components/mainpage/main/post.vue';

const isAuthorized = ref(false)
const username = ref('');
const errors = ref([]);
const user_posts = ref([]);

axios
  .post("/auth/check_auth")
  .then(response => {
      if (response["data"]["ok"]) {username.value = response["data"]["user"]["username"]; isAuthorized.value=true}
  })
  .catch(error => (console.log(error)));

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
    background-image: url("/src/assets/desert1.jpg");
    width: 100%;
    height: 100vh;
}
.user-post{
  background: rgba(0, 0, 0, 0.25);
  border-radius: 5px;
}
main {
  max-width: 1200px;
  display: flex;
  margin: 0 auto;
  margin-top: 5%;
}
.posts{
  margin-right: 170px;
}
.features{
background: rgba(0, 0, 0, 0.25);
border-radius: 5px;
padding: 5px;
max-height: 150px;
}
.aside-item {
  position: relative;
  font-family: "OpenSans-Bold";
  text-transform: uppercase;
  padding-bottom: 15px;
}
.aside-item::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 35%;
  width: 30%;
  border-bottom: 4px #b59f5b solid;
}
.aside-item span:hover{
  color: #b59f5b;
}
</style>
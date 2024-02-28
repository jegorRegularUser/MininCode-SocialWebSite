<template>
  <div class="home">
    <header class="head" id="head">
      <navigation :isAuthorized="isAuthorized" :username="username"/>
      <h1>блог о творчестве, спорте и образе жизни</h1>
      </header>

      <div class="main" id="main">
        <post :posts="user_posts"></post>
      </div>

    <Vfooter/>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import navigation from '@/components/oftenUsesComponents/navigation.vue';
import Vfooter from '@/components/mainpage/vfooter.vue';
import post from '@/components/mainpage/main/post.vue';
const isAuthorized = ref(false)
const username = ref('');
const user_posts = ref([]);

axios
  .post("/auth/check_auth")
  .then(response => {
      if (response["data"]["ok"]) {username.value = response["data"]["user"]["username"]; isAuthorized.value=true}
  })
  .catch(error => (console.log(error)));

axios
  .post("/api", {method: "get_my_posts"})
  .then(response => {
      console.log(response)
      if (response["data"]["ok"]) {console.log(response)}
  })
  .catch(error => (console.log(error)));

axios
  .post("/api", {method: "get_last_posts"})
  .then(response => {
      console.log(response)
      if (response["data"]["ok"]) {
        user_posts.value.push(response["data"]["posts"])
      }
  })
  .catch(error => (console.log(error)));
</script>


<style scoped>

.main {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.head {
 position: relative;
 z-index: 1;

 background-color: black;
 background-image: url(https://netology-code.github.io/html-2-diploma/sources/images/banner-bg.jpg);
 background-repeat: no-repeat;
 background-size: cover;
 text-align: center;
 margin-bottom: 65px;
}
.head::after {
 content: '';
 background-color: #000000;
 opacity: 0.5;

 position: absolute;
 top: 0;
 right: 0;
 left: 0;
 bottom: 0;
 z-index: -1;
}
h1 {
 font-family: 'OpenSans-Bold';
 font-size: 45px;
 width: 680px;
 display: inline-block;
 color: white;
 text-transform: uppercase;
 margin-bottom: 150px;
}



@media only screen and (max-width: 767px) {
  h1 {
    font-size: 20px;
    width: 100%;
    display: block;
    margin-top: 85px;
    margin-bottom: 150px;
  }
  .head {
    background-size: 100% auto; 
    position: relative;
  }
}

</style>


<template>
 <nav>
   <a href="/"><img src="https://netology-code.github.io/html-2-diploma/sources/images/noemi-logo.svg"
     class="logo" alt="logo" /></a>
   <ul class="nav-ul">
    <li class="nav-li"><router-link to="/"><a class="nav-link" href="#main">Главная</a></router-link></li>
    <li v-if="props.isAuthorized" class="nav-li"><router-link to="/newPost"><a class="nav-link">Создать статью</a></router-link></li>
    <li v-if="!props.isAuthorized" class="nav-li"><router-link to="/loginform"><a class="nav-link">войти / зарегистрироваться</a></router-link></li>
    <li v-if="props.isAuthorized" class="nav-li">{{props.username}}</li>
    <li v-if="props.isAuthorized" class="nav-li" @click="logout()"><box-icon name='log-out' color='#ffffff'></box-icon></li>
   </ul>
  </nav>
</template>

<script setup>
import boxicons from 'boxicons'
import axios from 'axios'

const props = defineProps({
 isAuthorized: Boolean,
 username: String
});

function logout() {
  axios.post("/auth/logout").then(response => (document.location.href="/"))
}
</script>

<style scoped>
nav {
 max-width: 1200px;
 margin: 0 auto;
 padding-top: 30px;
 display: flex;
 justify-content: space-between;
 align-items: center;
}
.logo {
 width: 180px;
}
.nav-ul {
 margin: 0;
 padding: 0;
 display: flex;
 list-style: none;
}
.nav-li {
 margin: 0 10px;
 color: white;
 cursor: pointer;
}
a {
 color: black;
 text-decoration: none;
}
.nav-link {
 font-size: 13px;
 color: white;
 text-transform: uppercase;
}
.nav-link:hover {
 text-decoration: underline;
}
</style>
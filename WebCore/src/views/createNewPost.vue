<template>
    <body>
    <navigation :isAuthorized="isAuthorized" :username="username"></navigation>

    <div class="container">
        <form action="submit" @submit.prevent="createPost">
            <h1 class="title">Создать блог</h1>
            <input class="form-input" v-model="title" type="text" name="title" placeholder="Название блога">
            <textarea v-model="description" class="form-textarea" placeholder="Расскажите о ваших приключениях" name="description"></textarea>

            <div style="display: flex; gap: 10px; width: 90%;"> 
              <input class="form-input"  v-model="tag_value" type="text" name="tags" placeholder="Введите теги">
              <button class="button--submit" @click.prevent="add_tag()" style="width: 50px">+</button>
            </div>

            <div class="tags">
                <p v-for="(item, index) in tags"><div class="tag" >{{ item }} <button @click.prevent="close_tag(index)" class="close-tag-button"><box-icon name='x-circle' type='solid' ></box-icon></button></div></p>
            </div>

            <p v-for="(err) in errors" style="color: red;">{{err}}</p>
            <input type="submit" class="button--submit" value="Опубликовать">
        </form>
    </div>
  </body>
  </template>
      
<script setup>
import {ref} from 'vue';
import axios from 'axios';
import navigation from "@/components/oftenUsesComponents/navigation.vue";
import Boxicons from 'boxicons';

const title = ref('')
const description = ref('')
const tags = ref([]);
const errors = ref([]);

const tag_value = ref('');
const isAuthorized = ref(false)
const username = ref('');

axios
  .post("/auth/check_auth")
  .then(response => {
      if (response["data"]["ok"]) {username.value = response["data"]["user"]["username"]; isAuthorized.value=true}
  })
  .catch(error => (console.log(error)));
  

async function createPost(event){
    let formData = new FormData(event.target);
    console.log(formData)
    try {
        let response = await axios.post(
          "/api", 
          {method: "create_post", "title": title.value, "description": description.value, "tags": tags.value}
        );

        let data = response.data;
        if (data.ok===false) {
          errors.value.splice(0, errors.value.length);
          errors.value.push(data.err)
        } else {
          window.location.href = `/users/${username.value}`
        }
    } catch (error) {
        alert("Произошла ошибка: " + error.message);
    }
}

function close_tag(index){
  tags.value.splice(index, 1)
}

function add_tag(e) {
  tags.value.push(tag_value.value);
  tag_value.value = ""
}
    
</script>
<style scoped>
body{
  background-image:url(https://sportishka.com/uploads/posts/2022-11/1667490691_51-sportishka-com-p-gora-pabaku-pinterest-51.jpg);
  background-repeat: no-repeat;
  background-color: #AFAFAF;
  background-size: cover;
  width: 100%;
  height: 100vh;
}

.container{
    margin: 10% auto;
    width: 50%;
    max-width: 400px;
    background: rgba(0, 0, 0, 0.25);
    border-radius: 10px;
    padding: 0 10px 20px;
}

form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
}

.title {
    margin-top: 20px;
    margin-bottom: 10px;
    color: #FFFFFF;
}

.form-input {
    background: none;
    width: 90%;
    height: 50px;
    border-radius: 10px;
    border: 1px solid #b59f5b;
    padding-left: 10px;
    box-sizing: border-box;
}

.form-input::placeholder {
    color: #FFFFFF;
}

.form-textarea {
    height: 80px;
    width: 90%;
    color: #ffffff;
    padding-left: 5px;
    padding-top: 5px;
    font-size: 15px;
    border: 1px solid #b59f5b;
    border-radius: 6px;
    background-color: transparent;
    box-sizing: border-box;
}

.form-textarea::placeholder {
    color: #FFFFFF;
}

.button--submit {
    width: 90%;
  min-height: 50px;
  padding: .5em 1em;
  border: none;
  border-radius:  6px ;
  background-color: #b59f5b;
  color: #fff;
  font-size: 15px;
  cursor: pointer;
}

.button--submit:hover {
	background-color: #F1DC9A;
}

.tags{
    display: flex;
    flex-wrap: wrap;
}
.tag{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-left: 5px;
    background: rgba(181, 159, 91, 0.4);
    border: none;
    color: white;
    border-radius: 5px;
    width: auto;
    font-size: 10px;
    margin: 0 5px 5px 15px;
    box-sizing: border-box;
}

.close-tag-button{
    background: none;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    width: 60%;
}

.input-file {
	position: relative;
	display: inline-block;
}

.input-file span {
	position: relative;
	display: inline-block;
	cursor: pointer;
	outline: none;
	text-decoration: none;
	font-size: 14px;
	vertical-align: middle;
	color: rgb(255 255 255);
	text-align: center;
	border-radius: 4px;
	background: #b59f5b;
	line-height: 22px;
	height: 40px;
	padding: 10px 20px;
	box-sizing: border-box;
	border: none;
	margin: 0;
	transition: background-color 0.2s;
}
.input-file input[type=file] {
	position: absolute;
	z-index: -1;
	opacity: 0;
	display: block;
	width: 0;
	height: 0;
}
 
.input-file:hover span {
	background-color: #F1DC9A;
}

</style>
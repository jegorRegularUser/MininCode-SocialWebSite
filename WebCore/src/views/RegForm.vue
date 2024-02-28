<template>
<body>
  	<navigation/> 
  	<div class="form-block">
		<p id="heading">Регистрация</p>
		<form @submit.prevent="register" class="form">  
			<div class="inputs">
				<input autocomplete="off" placeholder="Почта" class="input-field" type="email" name="email" required/>
				<input autocomplete="off" placeholder="Логин" class="input-field" type="text" name="username" required/>
				<input placeholder="Пароль" class="input-field" type="password" name="password"/>
			</div>
			<p v-for="(err) in errors" style="color: red;">{{err}}</p>
			<div class="union">
				<button class="button1">Зарегестрироваться</button>
				<a href="/loginform">Уже есть аккаунт?</a>
			</div>
		</form>
  	</div>
</body>
</template>

<script setup>
import navigation from "@/components/oftenUsesComponents/navigation.vue"
import axios from "axios";
import {ref} from 'vue';

const errors = ref([])

async function register(event) {
    let formData = new FormData(event.target);
    try {
        let response = await axios.post("/auth/registration", formData, {
            headers: {"Content-Type": "application/x-www-form-urlencoded"}
        });

		console.log(response)
        let data = response.data;
        if (data.ok===false) {
			errors.value.splice(0, errors.value.length);
			data.errors.forEach(err => {errors.value.push(err)})	
		} else {
			let url = new URL("/", window.location.href);
        	window.location.href = url.href;
		}

		

    } catch (error) {
        alert("Произошла ошибка при регистрации: " + error.message);
    }
}
</script>

<style scoped>
body{
    background-color: #AFAFAF;
    background-image: url("/src/assets/bg.jpeg");
    width: 100%;
    height: 100vh;
}

#heading {
  color: #FFFFFF;
  font-size: 25px;
  margin-top: 50px;
}

.form-block {
  margin: 0 auto;
  margin-top: 9%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #00000095;
  width: 500px;
  height: 500px;
  border-radius: 15px; 
}

.form {
	width: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	height: 100%;
	padding-bottom: 30px;
}

.inputs {
	width: 100%;
	display: flex;
	flex-direction: column;
	gap: 10px;
	margin-top: 40px;
	align-items: center;
}

.inputs input {
  background: #19204885;
  width: 80%;
  height: 60px; 
  border: none;
  border-radius: 10px;
  padding-left: 15px; 
  color: #FFFFFF;
  font-size: 18px;
}

.inputs input::placeholder {
  color: #FFFFFF;
}

.union {
    display: flex;
	flex-direction: column;
    gap: 5px;
    justify-content: center;
	align-items: center;
}

.union button {
	background: #31318699;
	border: none;
	width: 70%;
	height: 50px;
	color: #FFFFFF;
	margin: auto 0;
	border-radius: 15px;
	font-size: 18px;
	cursor: pointer;
}

.union a {
	color: #FFFFFF;	
	font-size: 15px;
	cursor: pointer;
}
</style>
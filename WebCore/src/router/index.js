import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginForm from '../views/LoginForm.vue'
import RegForm from '../views/RegForm.vue'

import userpage from '../views/userpage.vue'
import createNewPost from '../views/createNewPost.vue'
import ViewUserPosts from '../views/ViewUserPosts.vue'


const routes = [
  {path: '/users/:username', component: ViewUserPosts},
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/loginform',
    name: 'loginform',
    component: LoginForm
  },
  {
    path: '/regform',
    name: 'regform',
    component: RegForm
  },
  {
    path: '/newPost',
    name: 'newPost',
    component: createNewPost
    
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router

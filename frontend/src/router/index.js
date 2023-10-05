import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/HomeView.vue";
import HistoryView from "@/views/HistoryView.vue";

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path:'/history',
    component: HistoryView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
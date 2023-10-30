// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import DashBoard from '@/views/DashBoard.vue';

const routes = [
  {
    path: '/',
    name: 'DashBoard',
    component: DashBoard
  },
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;

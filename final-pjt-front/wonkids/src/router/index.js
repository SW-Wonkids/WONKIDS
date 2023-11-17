import { createRouter, createWebHistory } from 'vue-router'

import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleListView from '@/views/ArticleListView.vue'
import ArticleView from '@/views/ArticleView.vue'
import BankListView from '@/views/BankListView.vue'
import BankMapView from '@/views/BankMapView.vue'
import BankView from '@/views/BankView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import HomeView from '@/views/HomeView.vue'
import LogInView from '@/views/LogInView.vue'
import PollView from '@/views/PollView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/banklist',
      name: 'banklist',
      component: BankListView
    },
    {
      path: '/bank',
      name: 'bank',
      component: BankView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/bankmap',
      name: 'bankmap',
      component: BankMapView
    },
    {
      path: '/article-create',
      name: 'article-create',
      component: ArticleCreateView
    },
    {
      path: '/article-list',
      name: 'article-list',
      component: ArticleListView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/exchange-rate',
      name: 'exchange-rate',
      component: ExchangeRateView
    },
    {
      path: '/poll',
      name: 'poll',
      component: PollView
    },
  ]
})

export default router

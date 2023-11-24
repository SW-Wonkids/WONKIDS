import { createRouter, createWebHistory } from 'vue-router'

// 게시판(CRUD) 출력 관련 페이지
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleListView from '@/views/ArticleListView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'

// 은행 지도 출력 관련 페이지
import BankMapView from '@/views/BankMapView.vue'

// 환율 계산기 출력 관련 페이지
import ExchangeRateView from '@/views/ExchangeRateView.vue'

// 회원 관리 기능 관련 페이지
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import LogOutView from '@/views/LogOutView.vue'
import ProfileView from '@/views/ProfileView.vue'

// 유형검사(포켓몬) 관련 페이지
import PollView from '@/views/PollView.vue'
import PollQuestionsView from '@/views/PollQuestionsView.vue'

// 정기예금 , 적금 데이터 출력 관련 페이지 
import BankTotalView from '@/views/BankTotalView.vue' 
import BankListDepositView from '@/views/BankListDepositView.vue'
import BankListSavingsView from '@/views/BankListSavingsView.vue'
import BankDepositDetailView from '@/views/BankDepositDetailView.vue'
import BankSavingsDetailView from '@/views/BankSavingsDetailView.vue'

// 접근 불가능한 경로로 왔을 때 출력되는 페이지
import NotFoundView from '@/views/NotFoundView.vue'


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
      path: '/logout',
      name: 'logout',
      component: LogOutView
    },
    {
      path: '/banklist_deposit',
      name: 'banklist_deposit',
      component: BankListDepositView
    },
    // {
    //   path: '/bank/:id',
    //   name: 'bank',
    //   component: BankView
    // },
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
      path: '/article/:pk',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/article-update',
      name: 'article-update',
      component: ArticleUpdateView
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
    {
      path: '/poll/questions',
      name: 'poll-questions',
      component: PollQuestionsView
    },
    {
      path: '/notfound',
      name: 'notfound',
      component: NotFoundView
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/notfound'
    },
    {
      path: '/banktotal',
      name: 'banktotal',
      component: BankTotalView
    },
    {
      path: '/banklist_savings',
      name: 'banklist_savings',
      component: BankListSavingsView
    },
    {
      path: '/BankDepositDetail/:id',
      name: 'BankDepositDetail',
      component: BankDepositDetailView
    },
    {
      path: '/BankSavingsDetail/:id',
      name: 'BankSavingsDetail',
      component: BankSavingsDetailView
    },

  ]
})

export default router

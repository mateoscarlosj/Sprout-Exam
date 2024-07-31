import { createRouter, createWebHistory } from 'vue-router';
import store from '../store';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import Login from '../pages/AppLogin.vue';
import EmployeePage from '../pages/EmployeePage.vue';

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/',
    component: DefaultLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '/employees',
        name: 'EmployeePage',
        component: EmployeePage,
      }
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  const isAuthenticated = store.getters['auth/isAuthenticated'];

  if (requiresAuth && !isAuthenticated) {
    next({ name: 'Login' });
  } else if (!requiresAuth && isAuthenticated) {
    next({ name: 'EmployeeList' });
  } else {
    next();
  }
});

export default router;

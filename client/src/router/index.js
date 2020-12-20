import Vue from 'vue';
import Router from 'vue-router';
import References from '../components/References.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'References',
      component: References,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});

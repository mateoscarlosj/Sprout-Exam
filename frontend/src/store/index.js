import { createStore } from 'vuex';
import auth from './modules/auth';
import employees from './modules/employees';

const store = createStore({
  modules: {
    auth,
    employees
  },
});

export default store;

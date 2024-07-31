import { createStore } from 'vuex';
import auth from './modules/auth'; // Import your auth module
import employees from './modules/employees';

const store = createStore({
  modules: {
    auth,
    employees
  },
});

export default store;

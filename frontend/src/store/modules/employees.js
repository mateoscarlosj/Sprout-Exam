import { getApi} from '../../api/employee';

const state = {
  employees: [],
  employee: null,
  loading: false,
  error: null
};

const getters = {
  allEmployees: (state) => state.employees,
  loading: (state) => state.loading,
  error: (state) => state.error,
};

const actions = {
  async fetchEmployees({ commit }) {
    commit('setLoading', true);
    try {
      const employees = await getApi('employees');
      commit('setEmployees', employees);
    } catch (error) {
      commit('setError', 'Failed to fetch employees');
    } finally {
      commit('setLoading', false);
    }
  },
  async fetchEmployeeById({ commit }, id) {
    commit('setLoading', true);
    try {
      const data = await getApi(`employees/employees/${id}`);
      commit('setEmployees', data);
    } catch (err) {
      commit('setError', 'Failed to fetch employee');
    } finally {
      commit('setLoading', false);
    }
  },
};

const mutations = {
  setEmployees(state, employees) {
    state.employees = employees;
  },
  setLoading(state, loading) {
    state.loading = loading;
  },
  setError(state, error) {
    state.error = error;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};

import { getApi, postApi, putApi, deleteApi } from '../../api/employee'; // Adjust the import path as necessary

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
  async addEmployee({ dispatch }, employee) {
    try {
      await postApi('employees', employee);
      dispatch('fetchEmployees');
    } catch (error) {
      console.error('Failed to add employee:', error.message);
    }
  },
  async updateEmployee({ dispatch }, { id, employee }) {
    try {
      await putApi(`employees/${id}`, employee);
      dispatch('fetchEmployees');
    } catch (error) {
      console.error('Failed to update employee:', error.message);
    }
  },
  async deleteEmployee({ dispatch }, id) {
    try {
      await deleteApi(`employees/${id}`);
      dispatch('fetchEmployees');
    } catch (error) {
      console.error('Failed to delete employee:', error.message);
    }
  }
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

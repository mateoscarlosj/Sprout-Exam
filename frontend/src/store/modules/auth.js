import axios from 'axios';

export const API_URL = "http://0.0.0.0:8000"

const state = {
    user: null,
    token: localStorage.getItem('token') || null,
};

const mutations = {
    SET_USER(state, user) {
        state.user = user;
    },
    SET_TOKEN(state, token) {
        state.token = token;
    },
    CLEAR_USER(state) {
        state.user = null;
        state.token = null;
        localStorage.removeItem('token');
    },
};


const actions = {
  async login({ commit }, { username, password }) {
    console.log(username)
    try {

        const response = await axios.post(`${API_URL}/users/token`, { username, password }, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })

        const { access_token, user_type } = response.data;
        commit('SET_USER', user_type);
        commit('SET_TOKEN', access_token);
        localStorage.setItem('token', access_token);
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  },
  logout({ commit }) {
    commit('CLEAR_USER');
  },
};

const getters = {
    isAuthenticated: (state) => !!state.token,
    currentUser: (state) => state.user,
  };

export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters,
};

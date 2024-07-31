import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/';

export const login = async (credentials) => {
  return axios.post(`${API_BASE_URL}auth/login`, credentials);
};

export const getProfile = async () => {
  return axios.get(`${API_BASE_URL}auth/profile`);
};

import axios from 'axios';

export const API_BASE_URL = 'http://0.0.0.0:8000/employees'; // Replace with your API base URL

const AUTH_TOKEN = localStorage.getItem('token') ;

export const getApi = async (endpoint) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${endpoint}`, {
      headers: {
        Authorization: `Bearer ${AUTH_TOKEN}`
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const postApi = async (endpoint, body) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/${endpoint}`, body, {
      headers: {
        Authorization: `Bearer ${AUTH_TOKEN}`,
        'Content-Type': 'application/json'
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error posting data:', error);
    throw error;
  }
};

export const putApi = async (endpoint, body) => {
  try {
    const response = await axios.put(`${API_BASE_URL}/${endpoint}`, body, {
      headers: {
        Authorization: `Bearer ${AUTH_TOKEN}`,
        'Content-Type': 'application/json'
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error updating data:', error);
    throw error;
  }
};

export const deleteApi = async (endpoint) => {
  try {
    const response = await axios.delete(`${API_BASE_URL}/${endpoint}`, {
      headers: {
        Authorization: `Bearer ${AUTH_TOKEN}`
      }
    });
    return response.status === 200;
  } catch (error) {
    console.error('Error deleting data:', error);
    throw error;
  }
};

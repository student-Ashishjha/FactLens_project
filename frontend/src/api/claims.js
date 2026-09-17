import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export async function getClaims() {
  const response = await axios.get(`${API_BASE_URL}/claims`);
  return response.data;
}

export async function createClaim(text) {
  const response = await axios.post(`${API_BASE_URL}/claims`, { text });
  return response.data;
}
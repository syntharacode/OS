import axios from "axios";

export async function createUser(username) {
  const res = await axios.post("/api/user/create", { username });
  return res.data;
}
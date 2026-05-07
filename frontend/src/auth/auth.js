const API_URL = "http://127.0.0.1:9000";

export async function login(email, password) {
  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  const response = await fetch(`${API_URL}/users/login`, {
    method: "POST",
    body: formData,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });

  const data = await response.json();

  console.log("STATUS:", response.status);
  console.log("DATA:", data);

  if (!response.ok) {
    // 👇 CLAVE: mostrar error real
    throw new Error(data.detail || "Error en login");
  }

  localStorage.setItem("token", data.access_token);

  return data;
}
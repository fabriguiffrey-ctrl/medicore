import { useEffect, useState } from "react";
import { apiFetch } from "../api/client";

export default function Profile() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    apiFetch("/users/me")
      .then(setUser)
      .catch(() => alert("No autorizado"));
  }, []);

  if (!user) return <p>Cargando...</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Perfil</h2>
      <p>Email: {user.email}</p>
      <p>Role: {user.role}</p>
    </div>
  );
}
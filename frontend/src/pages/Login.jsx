import { useState } from "react";
import { login } from "../auth/auth";

export default function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {  // 👈 CLAVE
    e.preventDefault();

    try {
      await login(email, password);
      onLogin();
    } catch (err) {
      console.error(err);
      alert("Login incorrecto");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Login</h2>

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <br /><br />

        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <br /><br />

        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
}
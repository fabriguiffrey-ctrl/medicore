import { useState } from "react";
import Login from "./pages/Login";
import Profile from "./pages/Profile";

function App() {
  const [logged, setLogged] = useState(!!localStorage.getItem("token"));

  return (
    <>
      {!logged ? (
        <Login onLogin={() => setLogged(true)} />
      ) : (
        <Profile />
      )}
    </>
  );
}

export default App;
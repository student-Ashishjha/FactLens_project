import { useState } from "react";
import ClaimForm from "./components/ClaimForm";
import ClaimList from "./components/ClaimList";

function App() {
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  function handleClaimCreated() {
    setRefreshTrigger((prev) => prev + 1);
  }

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>FactLens</h1>
      <ClaimForm onClaimCreated={handleClaimCreated} />
      <ClaimList refreshTrigger={refreshTrigger} />
    </div>
  );
}

export default App;
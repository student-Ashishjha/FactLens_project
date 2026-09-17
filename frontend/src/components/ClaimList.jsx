import { useState, useEffect } from "react";
import { getClaims } from "../api/claims";

function ClaimList({ refreshTrigger }) {
  const [claims, setClaims] = useState([]);

  useEffect(() => {
    async function fetchClaims() {
      const data = await getClaims();
      setClaims(data);
    }
    fetchClaims();
  }, [refreshTrigger]);

  return (
    <div>
      <h2>All Claims</h2>
      {claims.length === 0 && <p>No claims yet.</p>}
      <ul>
        {claims.map((claim) => (
          <li key={claim.id}>
            {claim.text} — <strong>{claim.status}</strong>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ClaimList;
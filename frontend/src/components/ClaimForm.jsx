import { useState } from "react";
import { createClaim } from "../api/claims";

function ClaimForm({ onClaimCreated }) {
  const [text, setText] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    if (!text.trim()) return;

    await createClaim(text);
    setText("");
    onClaimCreated();
  }

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter a claim to investigate..."
      />
      <button type="submit">Investigate</button>
    </form>
  );
}

export default ClaimForm;
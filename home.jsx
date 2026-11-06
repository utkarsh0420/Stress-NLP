import { useState } from "react";

export default function StressChecker() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function check() {
    setLoading(true);
    const res = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    setResult(await res.json());
    setLoading(false);
  }

  return (
    <div>
      <textarea value={text} onChange={(e) => setText(e.target.value)}
        placeholder="Write a few sentences about how you feel..." rows={5} />
      <button onClick={check} disabled={loading}>{loading ? "Checking..." : "Check"}</button>

      {result?.error && <p>{result.error}</p>}
      {result && !result.error && (
        <p>
          {result.stressed ? "This text shows signs of stress" : "This text does not show signs of stress"}
          {" "}({Math.round(result.confidence * 100)}% confident)
        </p>
      )}
      <small>Research demo only. This is not a medical or mental health diagnosis.</small>
    </div>
  );
}
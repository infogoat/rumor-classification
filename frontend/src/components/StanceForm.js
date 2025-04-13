import React, { useState } from "react";

function StanceForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [probability, setProbability] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await response.json();
    setResult(data.result);
    setProbability(data.probability);
  };

  return (
    <div className="max-w-xl mx-auto p-4 shadow-lg rounded bg-white mt-10">
      <h1 className="text-2xl font-bold mb-4">Rumor Stance Prediction</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full p-2 border rounded mb-4"
          rows="5"
          placeholder="Enter the text to analyze"
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
        ></textarea>
        <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Predict
        </button>
      </form>
      {result && (
        <div className="mt-4">
          <p>
            <strong>Result:</strong> {result}
          </p>
          <p>
            <strong>Probability:</strong> {(probability * 100).toFixed(2)}%
          </p>
        </div>
      )}
    </div>
  );
}

export default StanceForm;

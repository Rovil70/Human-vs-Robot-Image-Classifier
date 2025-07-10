import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:8000/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });
      setResult(res.data);
    } catch (err) {
      console.error("Error uploading image", err);
    }
  };

  return (
    <div>
      <h1>Human vs Robot Classifier</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept="image/*" />
        <button type="submit">Predict</button>
      </form>

      {result && (
        <div>
          <h2>Prediction: {result.prediction}</h2>
          <h3>Confidence: {(result.confidence * 100).toFixed(2)}%</h3>
        </div>
      )}
    </div>
  );
}

export default App;

import { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  const handleSearch = async () => {
    const response = await axios.post("http://127.0.0.1:8000/recommend", {
      query: query,
    });
    setResult(response.data);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Procurement Agent</h1>

      <input
        type="text"
        placeholder="Enter procurement request..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ width: "300px", padding: "10px" }}
      />

      <button
        onClick={handleSearch}
        style={{ marginLeft: "10px", padding: "10px" }}
      >
        Find Supplier
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Recommended Supplier</h2>
          <p><strong>Name:</strong> {result.name}</p>
          <p><strong>Price:</strong> ₹{result.price}</p>
          <p><strong>Rating:</strong> {result.rating}</p>
        </div>
      )}
    </div>
  );
}

export default App;

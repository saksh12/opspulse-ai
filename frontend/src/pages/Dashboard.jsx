import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchEvents();
  }, []);

  const fetchEvents = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/events");
      setEvents(res.data);
    } catch (err) {
      console.log("API error:", err);
    }
  };

  return (
    <div style={{
      background: "#0b0b0b",
      color: "white",
      minHeight: "100vh",
      padding: "20px"
    }}>
      <h1>📊 OpsPulse AI Dashboard</h1>

      {events.length === 0 ? (
        <p>No events yet...</p>
      ) : (
        events.map((e, i) => (
          <div key={i} style={{
            border: "1px solid gray",
            margin: "10px",
            padding: "10px",
            borderRadius: "8px"
          }}>
            <p>Type: {e.type}</p>
            <p>User: {e.user}</p>
            <p>Value: {e.value}</p>
            <p>Region: {e.region}</p>
            <p>Time: {e.time}</p>
          </div>
        ))
      )}
    </div>
  );
}
import React, { useState } from "react";
import axios from "axios";

export default function UserProfile({ userId }) {
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState("");

  const handleFetchProfile = async () => {
    try {
      setError("");
      const response = await axios.get(
        `https://api.example.com/users/${userId}`,
      );
      setProfile(response.data);
    } catch (err) {
      setError("Failed to fetch user data");
    }
  };

  return (
    <div className="profile-card">
      <h2>User Profile Portal</h2>
      <button onClick={handleFetchProfile}>Load Profile Info</button>

      {error && <p className="error-msg">{error}</p>}

      {profile && (
        <div data-testid="profile-display">
          <p>Name: {profile.name}</p>
          <p>Role: {profile.role}</p>
        </div>
      )}
    </div>
  );
}

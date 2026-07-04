import React from "react";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import "@testing-library/jest-dom";
import axios from "axios";
import UserProfile from "../src/UserProfile";

jest.mock("axios");

describe("UserProfile React Component UI & Network Isolation Suite", () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should successfully render profile data upon a user clicking the load button", async () => {
    axios.get.mockResolvedValue({
      data: { name: "Cypher King", role: "Cloud Engineer" },
    });

    render(<UserProfile userId="999" />);

    const loadButton = screen.getByRole("button", {
      name: /Load Profile Info/i,
    });
    fireEvent.click(loadButton);

    await waitFor(() => {
      expect(screen.getByTestId("profile-display")).toBeInTheDocument();
    });

    expect(screen.getByText("Name: Cypher King")).toBeInTheDocument();
    expect(screen.getByText("Role: Cloud Engineer")).toBeInTheDocument();
    expect(axios.get).toHaveBeenCalledWith("https://api.example.com/users/999");
    expect(axios.get).toHaveBeenCalledTimes(1);
  });

  it("should present a visual error block when the network backend request drops", async () => {
    axios.get.mockRejectedValue(new Error("Network Crash"));

    render(<UserProfile userId="999" />);

    const loadButton = screen.getByRole("button", {
      name: /Load Profile Info/i,
    });
    fireEvent.click(loadButton);

    await waitFor(() => {
      expect(
        screen.getByText(/failed to fetch user data/i),
      ).toBeInTheDocument();
    });
  });
});

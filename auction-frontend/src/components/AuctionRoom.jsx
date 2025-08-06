import React, { useState } from "react";
import { useWebSocket } from "../hooks/useWebSocket";

const AuctionRoom = ({ itemId }) => {
  const [user, setUser] = useState("Bidder_" + Math.floor(Math.random() * 1000));
  const [amount, setAmount] = useState("");
  const { messages, sendBid } = useWebSocket(itemId);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (amount) sendBid(user, amount);
    setAmount("");
  };

  return (
    <div className="max-w-xl mx-auto p-6 bg-white rounded-2xl shadow-md mt-10 space-y-4">
      <h2 className="text-2xl font-bold text-center">Live Auction</h2>
      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="number"
          placeholder="Your bid"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          className="border p-2 rounded w-full"
        />
        <button className="bg-blue-600 text-white px-4 py-2 rounded">Bid</button>
      </form>

      <div className="mt-6">
        <h3 className="text-lg font-semibold mb-2">Bid History</h3>
        <ul className="max-h-64 overflow-y-auto space-y-1">
          {messages.map((msg, i) => (
            <li key={i} className="text-sm bg-gray-100 p-2 rounded">
              💰 {msg.user} bid ₹{msg.amount}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AuctionRoom;

import { useEffect, useRef, useState } from "react";

export const useWebSocket = (itemId) => {
  const [messages, setMessages] = useState([]);
  const socket = useRef(null);

  useEffect(() => {
    socket.current = new WebSocket(`ws://localhost:8000/ws/auction/${itemId}`);

    socket.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data]);
    };

    return () => {
      socket.current.close();
    };
  }, [itemId]);

  const sendBid = (user, amount) => {
    const message = { user, amount: parseFloat(amount) };
    socket.current.send(JSON.stringify(message));
  };

  return { messages, sendBid };
};

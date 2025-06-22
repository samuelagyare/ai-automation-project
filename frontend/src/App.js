import React, { useState } from 'react';
import './App.css';

function App() {
  // State to hold the list of messages
  const [messages, setMessages] = useState([]);
  // State to hold the content of the input box
  const [input, setInput] = useState('');
  // State to track if the AI is thinking
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    // Prevents the page from refreshing on form submission
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage = { text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      // Send the user's message to YOUR LIVE backend API
      const response = await fetch('https://ai-automation-backend-685273303639.europe-west1.run.app/api/agent', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: input }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      
      // Add the AI's response to the chat
      const aiMessage = { text: data.response, sender: 'ai' };
      setMessages(prev => [...prev, userMessage, aiMessage]);

    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
      // Add an error message to the chat
      const errorMessage = { text: 'Sorry, I ran into an error. Please try again.', sender: 'ai' };
      setMessages(prev => [...prev, userMessage, errorMessage]);
    } finally {
      // AI has finished thinking
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Automation Agent</h1>
      </header>
      <main className="chat-container">
        <div className="message-list">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
          {isLoading && (
            <div className="message ai">
              <span className="typing-indicator">...</span>
            </div>
          )}
        </div>
        <form onSubmit={handleSubmit} className="message-form">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask the AI anything..."
            disabled={isLoading}
          />
          <button type="submit" disabled={isLoading}>Send</button>
        </form>
      </main>
    </div>
  );
}

export default App;
import React, { useState } from 'react';
import './App.css';
import MultiStepForm from './MultiStepForm';

const hardcodedCredentials = {
  email: 'user@example.com',
  password: 'password123'
};

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (email === hardcodedCredentials.email && password === hardcodedCredentials.password) {
      setIsAuthenticated(true);
      setError('');
    } else {
      setError('Incorrect email or password!');
    }
  };

  // If authenticated, show the multi-step form
  if (isAuthenticated) {
    return (
      <div className="App">
        <MultiStepForm />
      </div>
    );
  }

  return (
    <div className="App">
      <div className="login-page">
        <div className="title-section">
          <div className="title-text">
            Welcome to
          </div>
          <div className="title-text">
            MediMate
          </div>
        </div>
        <div className="credentials-section">
          <div className="login-container">
            <form onSubmit={handleSubmit} className="login-form">
              <input
                className="login-form-input"
                type="email"
                placeholder="Email*"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
              <input
                className="login-form-input"
                type="password"
                placeholder="Password*"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
              <button type="submit">Login</button>
              {error && <div className="login-error">{error}</div>}
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

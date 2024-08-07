// components/common/LoginForm.js
import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGoogle, faMicrosoft, faFacebook } from '@fortawesome/free-brands-svg-icons';
import Input from '../common/Input';
import Button from '../common/Button';
import styles from '../../styles/LoginForm.module.css';
import Navbar from '../common/navbar'
import axios from 'axios';

function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      // Make POST request to login endpoint
      const response = await axios.post('http://127.0.0.1:5000/login', {
        username,
        password
      });

      // Check if login was successful (you may need to adjust this based on your API response)
      if (response.status === 200) {
        // Redirect to dashboard page if login successful
        window.location.href = '/dashboard';
      } else {
        // Handle other response statuses
        setError('Failed to log in. Please try again later.');
      }
    } catch (error) {
      // Handle network error or other errors
      if (error.response && error.response.status === 404) {
        setError('Invalid username or password.');
      } else {
        setError('Failed to log in. Please try again later.');
      }
    }
  };

  return (
    <div>
      <Navbar/>
      <div className={styles.formContainer}>
        <div className="fw-bold stylish-font">XAI Login</div>
        <div className={styles.card}>
          <Input type="text" placeholder="Username or Phone" value={username} onChange={(e) => setUsername(e.target.value)} />
          <Input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
          <Button onClick={handleLogin}>Login</Button>
          <div className={styles.socialLogin}>
            <div className={styles.divider}>
              <div className={styles.line}></div>
              <div className={styles.text}>OR</div>
              <div className={styles.line}></div>
            </div>
            <div>
              <FontAwesomeIcon icon={faGoogle} className={styles.icon} size="2x" style={{ color: '#DB4437' }} />
              <FontAwesomeIcon icon={faMicrosoft} className={styles.icon} size="2x" style={{ color: '#0078D7' }} />
              <FontAwesomeIcon icon={faFacebook} className={styles.icon} size="2x" style={{ color: '#1877F2' }} />
            </div>
          </div>
          {error && <p className={styles.error}>{error}</p>}
          <p className={styles.forgotPasswordLink}><a href="/forgotpassword">Forgot password?</a></p>
        </div>
      </div>
      <div className={styles.formContainer2}>
        <p className={styles.signUpLink}>Don't have an account? <a href="/signup">Sign up here</a></p>
      </div>
      {/* <Footer/> */}
    </div>
  );
}

export default LoginForm;

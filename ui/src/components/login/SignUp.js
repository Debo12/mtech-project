import React, { useState } from 'react';
import Input from '../common/Input';
import Button from '../common/Button';
import styles from '../../styles/SignUp.module.css';
import Navbar from '../common/navbar';
import Footer from '../common/Footer';
import axios from 'axios';

function SignUp() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [phone, setPhone] = useState('');
  const [error, setError] = useState('');
  const [isSignUpSuccess, setIsSignUpSuccess] = useState(false);

  const handleSignUp = async () => {
    try {
      // Validate inputs
      if (!username.trim()) {
        setError('Please enter a username.');
        return;
      }
      if (!/^[a-zA-Z0-9!@#$%^&*]+$/g.test(username)) {
        setError('Username must be alphanumeric with special characters.');
        return;
      }
      if (!isValidEmail(email)) {
        setError('Please enter a valid email address.');
        return;
      }
      if (!isValidPassword(password)) {
        setError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.');
        return;
      }
      if (password !== confirmPassword) {
        setError('Password and Confirm Password do not match.');
        return;
      }
      if (!isValidPhoneNumber(phone)) {
        setError('Please enter a valid phone number.');
        return;
      }
    
      // Make API request to submit form data
      const response = await axios.post('http://127.0.0.1:5000/user', {
        username,
        email,
        password,
        phone
      });

      // Check response status code
      if (response.status === 201) {
        setIsSignUpSuccess(true);
        setTimeout(() => {
          window.location.href = '/login'; // Redirect to login page after successful sign-up
        }, 3000); // Redirect after 3 seconds (adjust as needed)
      } else {
        setError('Failed to sign up. Please try again later.');
      }
    } catch (error) {
      // Handle error
      setError(error.message);
    }
  };

  const isValidEmail = (email) => {
    // Regular expression for email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
  };

  const isValidPassword = (password) => {
    // Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordPattern.test(password);
  };

  const isValidPhoneNumber = (phone) => {
    // Regular expression for phone number validation
    const phonePattern = /^\+\d{12}$/;
    return phonePattern.test(phone);
  };

  return (
    <div>
      <Navbar />
      <div className={styles.formContainer}>
        <div className={`text-center mb-4 ${styles.stylishFont}`}>
          <h2 className="fw-bold">Sign Up</h2>
        </div>
        <div className={styles.card}>
          <Input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
          <Input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
          <Input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
          <Input type="password" placeholder="Confirm Password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
          <Input type="tel" placeholder="Phone Number" value={phone} onChange={(e) => setPhone(e.target.value)} />
          <Button onClick={handleSignUp}>Sign Up</Button>
          {error && <p className={styles.error}>{error}</p>}
        </div>
        <div className={`text-center`}>
          <p className={styles.signInLink}><a href="/login">Return to Login</a></p>
        </div>
        {isSignUpSuccess && <p>Sign up successful! Redirecting to login page...</p>}
      </div>    
      <Footer />
    </div>
  );
}

export default SignUp;

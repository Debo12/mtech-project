// components/common/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import styles from '../../styles/Navbar.module.css';

function Navbar() {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>
        <Link to="/">XAI Insurance</Link>
      </div>
      <ul className={styles.navLinks}>
        <li><Link to="/dashboard">Dashboard</Link></li>
        <li><Link to="/upload">Upload Data</Link></li>
        <li><Link to="/train">Train Model</Link></li>
        <li><Link to="/prediction">Prediction</Link></li>
        <li><Link to="/settings">Settings</Link></li>
        <li><Link to="/admin">Admin Panel</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;

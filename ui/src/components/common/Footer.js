// components/common/Footer.js
import React from 'react';
import styles from '../../styles/Footer.module.css';

function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.footerContent}>
        <div className={styles.footerSection}>
          <h3>Contact Us</h3>
          <p>Email: contact@example.com</p>
          <p>Phone: +1234567890</p>
        </div>
        <div className={styles.footerSection}>
          <h3>Address</h3>
          <p>123 Main Street</p>
          <p>City, Country</p>
        </div>
        <div className={styles.footerSection}>
          <h3>Follow Us</h3>
          <p>Facebook</p>
          <p>Twitter</p>
          <p>LinkedIn</p>
        </div>
      </div>
      <div className={styles.copyRight}>© 2024 XAI Insurance. All rights reserved.</div>
    </footer>
  );
}

export default Footer;

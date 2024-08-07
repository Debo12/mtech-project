// components/common/Input.js
import React from 'react';
import styles from '../../styles/Input.module.css';

function Input({ type, placeholder, value, onChange }) {
  return <input type={type} className={styles.input} placeholder={placeholder} value={value} onChange={onChange} />;
}

export default Input;

import React from 'react';
import LoginForm from '../login/LoginForm'
import insuranceImage from '../../public/images/insurance.jpg';
import dataAnalyticsImage from '../../public/images/data-analytics.jpg';
import ExlpainableAI from '../../public/images/exlpainable-ai-2.jpg'
import styles from '../../styles/HomePage.module.css';
import Navbar from '../common/navbar';
import Footer from '../common/Footer';

function HomePage() {
  return (
    <div>
      <Navbar/>
      <section className={styles.hero}>
        <div className={styles.heroContent} img={ExlpainableAI}>
          <h1>Welcome to XAI Insurance Data Portal</h1>
          <p>Unlock the power of explainable artificial intelligence for insurance data analysis.</p>
        </div>
      </section>
      <section className={styles.features}>
        <div className={styles.feature}>
          <img src={insuranceImage} alt="Insurance" />
          <h2>Insurance Insights</h2>
          <p>Gain valuable insights into insurance data to make informed decisions.</p>
        </div>
        <div className={styles.feature}>
          <img src={dataAnalyticsImage} alt="Data Analytics" />
          <h2>Advanced Analytics</h2>
          <p>Utilize state-of-the-art data analytics techniques for predictive modeling.</p>
        </div>
      </section>
      <section className={styles.footer}>
        <Footer />
      </section>
    </div>
  );
}

export default HomePage;

// DetailsPage.js
import React, { useEffect, useState } from 'react';
import { Container, Card, Spinner } from 'react-bootstrap';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import styles from '../../styles/DetailsPage.module.css'; // Import the CSS module
import Navbar from '../common/navbar';

function DetailsPage() {
  const { id } = useParams();
  const [companyDetails, setCompanyDetails] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (id) {
      fetchCompanyDetails(id);
    }
  }, [id]);

  const fetchCompanyDetails = async (companyId) => {
    try {
      const companyResponse = await axios.get(`http://127.0.0.1:5000/companies?_id=${companyId}`);
      if (companyResponse.data && companyResponse.data.companies && companyResponse.data.companies.length > 0) {
        const companyData = companyResponse.data.companies[0];
        const { NAIC } = companyData;
        const complaintsResponse = await axios.get(`http://127.0.0.1:5000/complaints?NAIC=${NAIC}`);
        const complaintsData = complaintsResponse.data.complaint[0];

        // Combine company data and complaints data
        const mergedData = { ...companyData, ...complaintsData };
        setCompanyDetails(mergedData);
      } else {
        setError('No company details found for the specified ID.');
      }
    } catch (error) {
      setError('Error fetching company details.');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className={styles.spinnercontainer}>
        <Spinner animation="border" role="status">
          <span className="sr-only">Loading...</span>
        </Spinner>
      </div>
    );
  }

  if (error) {
    return (
      <Container className={styles.errorcontainer}>
        <Card className="mt-4">
          <Card.Body>
            <Card.Title>Error</Card.Title>
            <Card.Text>{error}</Card.Text>
          </Card.Body>
        </Card>
      </Container>
    );
  }

  return (
    <div>
      <Navbar />
      <Container className={styles.container}>
        <div className={styles.table}>
          <h1 className={styles.companyName}>{companyDetails.Company_Name}</h1>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Name:</strong></div>
            <div className={styles.tableCell}>{companyDetails.Company_Name}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>NAIC:</strong></div>
            <div className={styles.tableCell}>{companyDetails.NAIC}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Filing Year:</strong></div>
            <div className={styles.tableCell}>{companyDetails.Filing_Year}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Rank:</strong></div>
            <div className={styles.tableCell}>{companyDetails.Rank}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Premiums Written (in Millions):</strong></div>
            <div className={styles.tableCell}>{companyDetails.Premiums_Written_in_Millions}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Not Upheld Complaints:</strong></div>
            <div className={styles.tableCell}>{companyDetails['Not Upheld Complaints']}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Question of Fact Complaints:</strong></div>
            <div className={styles.tableCell}>{companyDetails['Question of Fact Complaints']}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Total Complaints:</strong></div>
            <div className={styles.tableCell}>{companyDetails['Total Complaints']}</div>
          </div>
          <div className={styles.tableRow}>
            <div className={styles.tableCell}><strong>Upheld Complaints:</strong></div>
            <div className={styles.tableCell}>{companyDetails['Upheld Complaints']}</div>
          </div>
        </div>
        <div className={styles.graph}>
          {/* Placeholder for the graph */}
          <img src="/path/to/your/graph.png" alt="Graph" />
        </div>
      </Container>
    </div>
  );
}

export default DetailsPage;

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Container, Table, Button } from 'react-bootstrap';
import axios from 'axios';
import Navbar from '../common/navbar';
import Footer from '../common/Footer';

function Dashboard() {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/companies');
        setCompanies(response.data.companies);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []);

  return (
    <div>
      <Navbar />
      <Container className="mt-4">
        <h2>Dashboard</h2>
        <Table striped bordered hover className="mt-4">
          <thead>
            <tr>
              <th>Name</th>
              <th>NAIC</th>
              <th>Filing Year</th>
              <th>Rank</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {companies.map((company) => (
              <tr key={company._id}>
                <td>{company.Company_Name}</td>
                <td>{company.NAIC}</td>
                <td>{company.Filing_Year}</td>
                <td>{company.Rank}</td>
                <td>
                  <Link to={`/details/${company._id}`}>
                    <Button variant="primary">View Details</Button>
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Container>
      <Footer />
    </div>
  );
}

export default Dashboard;

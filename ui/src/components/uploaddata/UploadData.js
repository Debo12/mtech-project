// components/pages/DataEntryPage.js
import React, { useState } from 'react';
import Navbar from '../common/navbar';
import Footer from '../common/Footer';
import Input from '../common/Input';
import Button from '../common/Button';
import styles from '../../styles/UploadData.module.css';

function UploadData() {
    const [formData, setFormData] = useState({
        naic: '',
        companyName: '',
        ratio: '',
        upheldComplaints: '',
        questionOfFactComplaints: '',
        notUpheldComplaints: '',
        totalComplaints: '',
        premiumsWritten: '',
        rank: '',
        filingYear: ''
      });
    
      const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
      };
    
      const handleSubmit = async (e) => {
        e.preventDefault();
        // Simulate API call
        try {
          const response = await submitFormData(formData); // Call your API function here
          console.log('Data submitted successfully:', response);
          // Optionally, show a success message or redirect to another page
        } catch (error) {
          console.error('Error submitting data:', error);
          // Handle error, show error message, etc.
        }
      };
    
      const submitFormData = async (formData) => {
        // Simulate API call delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        // Mock response
        return { success: true };
      };
    
      return (
        <div>
          <Navbar />
          <div className={styles.container}>
            <h2>Data Entry</h2>
            <form onSubmit={handleSubmit}>
              <Input type="text" name="naic" placeholder="NAIC" value={formData.naic} onChange={handleChange} />
              <Input type="text" name="companyName" placeholder="Company Name" value={formData.companyName} onChange={handleChange} />
              <Input type="text" name="ratio" placeholder="Ratio" value={formData.ratio} onChange={handleChange} />
              <Input type="text" name="upheldComplaints" placeholder="Upheld Complaints" value={formData.upheldComplaints} onChange={handleChange} />
              <Input type="text" name="questionOfFactComplaints" placeholder="Question of Fact Complaints" value={formData.questionOfFactComplaints} onChange={handleChange} />
              <Input type="text" name="notUpheldComplaints" placeholder="Not Upheld Complaints" value={formData.notUpheldComplaints} onChange={handleChange} />
              <Input type="text" name="totalComplaints" placeholder="Total Complaints" value={formData.totalComplaints} onChange={handleChange} />
              <Input type="text" name="premiumsWritten" placeholder="Premiums Written (in Millions)" value={formData.premiumsWritten} onChange={handleChange} />
              <Input type="text" name="rank" placeholder="Rank" value={formData.rank} onChange={handleChange} />
              <Input type="text" name="filingYear" placeholder="Filing Year" value={formData.filingYear} onChange={handleChange} />
              <Button type="submit">Submit</Button>
            </form>
          </div>
          <Footer />
        </div>
      );
    }
    

export default UploadData;

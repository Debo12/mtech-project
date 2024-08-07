import './App.css';
import HomePage from './components/homepage/HomePage';
import UploadData from './components/uploaddata/UploadData';
import TrainModel from './components/trainmodel/TrainModel';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from './components/dashboard/Dashboard';
import DetailsPage from './components/dashboard/DetailsPage';
import Prediction from './components/prediction/Prediction';
import Settings from './components/settings/Settings';
import AdminPanel from './components/adminpanel/AdminPanel';
import LoginForm from './components/login/LoginForm';
import SignUp from './components/login/SignUp';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/upload" element={<UploadData />} />
        <Route path="/train" element={<TrainModel />} />
        <Route path="/prediction" element={<Prediction />} />
        <Route path="/details/:id" element={<DetailsPage />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/admin" element={<AdminPanel />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/signup" element={<SignUp />} />
      </Routes>
    </Router>
  );
}




export default App;

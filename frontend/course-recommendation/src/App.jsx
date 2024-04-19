import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {
  BrowserRouter,
  Routes, // instead of "Switch"
  Route,
} from "react-router-dom";


import { Navigate } from 'react-router-dom'
import { Outlet } from 'react-router-dom';
import Home from './pages/home/Home'
import Login from './pages/auth/Login'
import SignUp from './pages/auth/SignUp'

import FeedbackForm from './pages/feedback/FeedBackForm';
// import Feedback from './pages/feedback/Feedback';
import Recommendation from './pages/rcmd/RecommendForm';

function App() {

  return (

    <BrowserRouter>
    <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />


        {/* <PrivateRoute path="/feedback" component={FeedbackForm} />
        <PrivateRoute path="/recommendation" component={Recommendation} /> */}

        <Route path="/feedback" element={<PrivateRoute component={FeedbackForm} />} />
        <Route path="/recommendation" element={<PrivateRoute component={Recommendation} />} />
        
      </Routes>

    </BrowserRouter>
  )
}

function PrivateRoute({ component: Component, ...rest }) {
  const loggedIn = localStorage.getItem('token');

  return loggedIn ? ( <Component {...rest} /> ) : ( <Navigate to="/login" /> );
 
}


export default App

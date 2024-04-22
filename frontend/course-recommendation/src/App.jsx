import { useEffect, useState } from 'react'
import { React } from 'react'
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

import { RecoilRoot, useRecoilValue } from 'recoil';
import { loginState } from './atoms/LoginState';
import NavBar from './pages/home/NavBar'


function App() {

  return (
    <>

      <NavBar />
      <RecoilRoot>
        <BrowserRouter>
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/feedback" element={<PrivateRoute component={FeedbackForm} />} />
            <Route path="/recommendation" element={<PrivateRoute component={Recommendation} />} />
          </Routes>
        </BrowserRouter>
      </RecoilRoot>
    </>


  )
}

function PrivateRoute({ component: Component, ...rest }) {
  // const loggedIn = localStorage.getItem('token');

  // const [login, setLogin] = useState(useRecoilValue(loginState));

  // const token = localStorage.getItem('token');
  // const email = localStorage.getItem('email');
  // if (token != null) {
  //   setLogin({ loggedIn: true, token: token, email: email });
  // }

  return (localStorage.getItem('token')) ? (<Component {...rest} />) : (<Navigate to="/login" />);

}


export default App;

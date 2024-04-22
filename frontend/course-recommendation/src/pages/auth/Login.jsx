import React  from "react";
import { RecoilRoot, useRecoilState,useRecoilValue,useSetRecoilState } from "recoil";

import { useState } from "react";

import { loginState } from "../../atoms/LoginState";

import axios from 'axios';
import { BaseUrl, login_api } from "../../Helper";
import { Navigate } from "react-router-dom";

function Login(){

    return(
        <div>
            <RecoilRoot>
                <LoginForm />
            </RecoilRoot>
        </div>
    )
}


function LoginForm(){

    // const [login,setLogin] = useRecoilState(loginState)
    const setLogin = useSetRecoilState(loginState);

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {

        // axios request take care of cors error
        const response = await axios.post( login_api,
            JSON.stringify( {email: email, password: password}),
            {
                headers: {
                    'Content-Type': 'application/json',
                    'allow-origin': BaseUrl
                }
            })

        if (response.data.success){

            setLogin((prevLogin) => ({
                ...prevLogin,
                token: response.data.user.token,
                email: response.data.user.email,
                loggedIn: true,
              }));

            localStorage.setItem('token', response.data.user.token);
            localStorage.setItem('email', response.data.user.email);


              // on alert ok button, redirect to home page
            // alert('Logged in successfully', Navigate('/feedback'));
            alert('Logged in successfully');
            window.location.href = '/feedback';
        }
    }
    
    return(
        <div>
            <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleLogin}>Login</button>
        </div>
    )
}


export default Login;

import React  from "react";
import { RecoilRoot, useRecoilState,useRecoilValue,useSetRecoilState } from "recoil";

import { useState } from "react";

import { loginState } from "./LoginState";

// import {axios} from 'axios';

import axios from 'axios';

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

    const [login, setLoggedIn] = useRecoilState(loginState);

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    
    const handleLogin = async () => {

        // axios request take care of cors error
        const response = await axios.post('http://localhost:5000/login/',
        JSON.stringify( {email: email, password: password}),

        {headers: {
            'Content-Type': 'application/json',
            'allow-origin': 'http://localhost:5000',

        }});


        console.log(response.data);
        if (response.data.success){
            setLoggedIn({token: response.data.token, username: response.data.username, loggedIn: true});
            alert('Logged in successfully');
        }

        // console.log(login);
        // if (login.loggedIn){
        //     // setLoggedIn({token: login.token, username: login.username, loggedIn: true});
        //     alert('Logged in successfully');
        // }
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

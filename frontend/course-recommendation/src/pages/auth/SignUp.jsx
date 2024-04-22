import React  from "react";
import { RecoilRoot, useRecoilState,useRecoilValue,useSetRecoilState } from "recoil";

import { signupState } from "../../atoms/SignupState";

import { signup_api } from "../../Helper";

// import {axios} from 'axios';

import axios from 'axios';
import { BaseUrl, login_api } from "../../Helper";
import { Navigate } from "react-router-dom";

function SignUp(){

    return(
        <div>
            <RecoilRoot>
                <SignupForm />
            </RecoilRoot>
        </div>
    )
}


function SignupForm(){

    const [signup,setSignup] = useRecoilState(signupState)

    
    const handleSignup = async () => {

        // axios request take care of cors error
        const response = await axios.post( signup_api,
            JSON.stringify( {role: signup.role, email: signup.email, password: signup.password}),
            {
                headers: {
                    'Content-Type': 'application/json',
                    'allow-origin': BaseUrl
                }
            })

        if (response.data.success){
            alert('Signup successful');
        }
    }

    return(
        <div>
            <h1>Signup</h1>

            <select value={signup.role} onChange={(e) => setSignup({...signup, role: e.target.value})}>
                <option value="student">Student</option>
                <option value="teacher">Teacher</option>
            </select>
            <br />
            <input type="email" value={signup.email} onChange={(e) => setSignup({...signup, email: e.target.value})} placeholder="Email" />
            <br />
            <input type="password" value={signup.password} onChange={(e) => setSignup({...signup, password: e.target.value})} placeholder="Password" />
            <br />
            <button onClick={handleSignup}>Signup</button>


        </div>
    )
}



export default SignUp;
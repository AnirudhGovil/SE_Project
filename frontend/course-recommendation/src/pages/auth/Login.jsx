import React, { useState } from "react";
import { RecoilRoot, useSetRecoilState } from "recoil";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
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

    const setLogin = useSetRecoilState(loginState);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post(login_api,
                JSON.stringify({ email: email, password: password }),
                {
                    headers: {
                        'Content-Type': 'application/json',
                        'allow-origin': BaseUrl
                    }
                });

            if (response.data.success) {
                setLogin(prevLogin => ({
                    ...prevLogin,
                    token: response.data.user.token,
                    email: response.data.user.email,
                    loggedIn: true,
                }));

                localStorage.setItem('token', response.data.user.token);
                localStorage.setItem('email', response.data.user.email);

                alert('Logged in successfully');
                window.location.href = '/feedback';
            }
        } catch (error) {
            console.error('Error logging in:', error);
            // Handle error (display error message, etc.)
        }
    }

    return (
        <Container>
            <Row className="justify-content-md-center mt-5">
                <Col md={6}>
                    <div className="p-4 border rounded">
                        <h2 className="mb-4">Login</h2>
                        <Form>
                            <Form.Group controlId="formBasicEmail">
                                <Form.Label>Email address</Form.Label>
                                <Form.Control type="email" placeholder="Enter email" value={email} onChange={(e) => setEmail(e.target.value)} />
                            </Form.Group>

                            <Form.Group controlId="formBasicPassword">
                                <Form.Label>Password</Form.Label>
                                <Form.Control type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                            </Form.Group>

                            <Button variant="primary" type="button" onClick={handleLogin} block>
                                Login
                            </Button>
                        </Form>
                    </div>
                </Col>
            </Row>
        </Container>
    )
}

export default Login;

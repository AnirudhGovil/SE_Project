import React, { useState } from "react";
import { RecoilRoot, useRecoilState } from "recoil";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import { signupState } from "../../atoms/SignupState";
import axios from 'axios';
import { BaseUrl, signup_api } from "../../Helper";

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

    const [signup, setSignup] = useRecoilState(signupState);

    const handleSignup = async () => {
        try {
            const response = await axios.post(signup_api,
                JSON.stringify({ role: signup.role, email: signup.email, password: signup.password }),
                {
                    headers: {
                        'Content-Type': 'application/json',
                        'allow-origin': BaseUrl
                    }
                });

            if (response.data.success) {
                alert('Signup successful');
            }
        } catch (error) {
            console.error('Error signing up:', error);
            // Handle error (display error message, etc.)
        }
    }

    return(
        <Container>
            <Row className="justify-content-md-center mt-5">
                <Col md={6}>
                    <div className="p-4 border rounded">
                        <h2>Signup</h2>
                        <Form>
                            <Form.Group controlId="formRole">
                                <Form.Label>Role</Form.Label>
                                <Form.Control as="select" value={signup.role} onChange={(e) => setSignup({...signup, role: e.target.value})}>
                                    <option value="student">Student</option>
                                    <option value="teacher">Teacher</option>
                                </Form.Control>
                            </Form.Group>

                            <Form.Group controlId="formEmail">
                                <Form.Label>Email address</Form.Label>
                                <Form.Control type="email" value={signup.email} onChange={(e) => setSignup({...signup, email: e.target.value})} placeholder="Enter email" />
                            </Form.Group>

                            <Form.Group controlId="formPassword">
                                <Form.Label>Password</Form.Label>
                                <Form.Control type="password" value={signup.password} onChange={(e) => setSignup({...signup, password: e.target.value})} placeholder="Password" />
                            </Form.Group>

                            <Button variant="primary" type="button" onClick={handleSignup} block>
                                Signup
                            </Button>
                        </Form>
                    </div>
                </Col>
            </Row>
        </Container>
    )
}

export default SignUp;

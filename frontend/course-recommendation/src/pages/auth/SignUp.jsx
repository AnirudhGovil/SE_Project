import React, { useState } from "react";
import { RecoilRoot, useRecoilState } from "recoil";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import { signupState } from "../../atoms/SignupState";
import axios from 'axios';
import { signup_student_api, signup_instructor_api } from "../../Helper";
import { Navigate } from "react-router-dom";

function SignUp() {

    return (
        <div>
            <RecoilRoot>
                <SignupForm />
            </RecoilRoot>
        </div>
    )
}

function SignupForm() {

    const [signup, setSignup] = useRecoilState(signupState);

    const handleSignup = async () => {
        try {

            /*
             student_data = {
            'student_id': 12022,
            'name': 'John Doe',
            'email': 'john1@example.com',
            'roll_number': '122345'
            }
            */

            if (signup.role === 'student') {
                const response = await axios.post(signup_student_api, {
                    student_id: signup.id,
                    name: signup.name,
                    email: signup.email,
                    password: signup.password,
                    roll_number: signup.id
                },
                    {
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    });

                console.log(response.data);

                if (response.data.success) {
                    alert('Signup successful');
                    Navigate('/home')
                }
            } else {
                const response = await axios.post(signup_instructor_api,
                    {
                        instructor_id: signup.id,
                        name: signup.name,
                        email: signup.email,
                        password: signup.password
                    },
                    {
                        headers: {
                            'Content-Type': 'application/json',
                            
                        }
                    });

                if (response.data.success) {
                    alert('Signup successful');
                    Navigate('/home')
                }
            }

        } catch (error) {

            console.error('Error signing up:', error);
            // Handle error (display error message, etc.)
        }

    }





    return (
        <Container>
            <Row className="justify-content-md-center mt-5">
                <Col md={6}>
                    <div className="p-4 border rounded">
                        <h2>Signup</h2>
                        <Form>
                            <Form.Group controlId="formRole">
                                <Form.Label>Role</Form.Label>
                                <Form.Control as="select" value={signup.role} onChange={(e) => setSignup({ ...signup, role: e.target.value })}>
                                    <option value="">Select role</option>
                                    <option value="student">Student</option>
                                    <option value="teacher">Instructor</option>
                                </Form.Control>
                            </Form.Group>

                            {/*  based on role select instructor id or student roll number */}

                            <Form.Group controlId="formId">
                                <Form.Label>{signup.role === 'student' ? 'Roll Number' : 'Instructor Id'}</Form.Label>
                                <Form.Control type="text" value={signup.id} onChange={(e) => setSignup({ ...signup, id: e.target.value })} placeholder={signup.role === 'student' ? 'Enter roll number' : 'Enter instructor id'} />
                            </Form.Group>


                            <Form.Group controlId="formName">
                                <Form.Label>Name</Form.Label>
                                <Form.Control type="text" value={signup.name} onChange={(e) => setSignup({ ...signup, name: e.target.value })} placeholder="Enter name" />
                            </Form.Group>



                            <Form.Group controlId="formEmail">
                                <Form.Label>Email address</Form.Label>
                                <Form.Control type="email" value={signup.email} onChange={(e) => setSignup({ ...signup, email: e.target.value })} placeholder="Enter email" />
                            </Form.Group>

                            <Form.Group controlId="formPassword">
                                <Form.Label>Password</Form.Label>
                                <Form.Control type="password" value={signup.password} onChange={(e) => setSignup({ ...signup, password: e.target.value })} placeholder="Password" />
                            </Form.Group>




                            <Button variant="primary" type="button" onClick={handleSignup} block="true">
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

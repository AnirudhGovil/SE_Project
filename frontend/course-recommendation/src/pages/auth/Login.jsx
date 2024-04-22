import React, { useState } from "react";
import { RecoilRoot, useSetRecoilState } from "recoil";
import { useRecoilValue } from "recoil";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import { loginState } from "../../atoms/LoginState";
import axios from 'axios';
import { login_student_api } from "../../Helper";
import { login_instructor_api } from "../../Helper";
import { Navigate } from "react-router-dom";

function Login() {

    return (
        <div>
            <RecoilRoot>
                <LoginForm />
            </RecoilRoot>
        </div>
    )
}

function LoginForm() {

    const setLogin = useSetRecoilState(loginState);
    const login = useRecoilValue(loginState);

    const handleLogin = async () => {


        // data in json format

        if (login.role === 'student') {
            const response = await axios.post(login_student_api, {
                student_id: login.id,
                password: login.password
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            console.log(response.data);

            if (response.data.student) {
                // setLogin({ token: response.data.token, email: response.data.email, loggedIn: true });

                localStorage.setItem('name', response.data.student.name);
                localStorage.setItem('student_id', response.data.student.student_id);
                localStorage.setItem('email', response.data.student.email);
                localStorage.setItem('token', "student");

                alert('Login successful');

                Navigate('/home');
            }

        } else {

            const response = await axios.post(login_instructor_api, {
                instructor_id: login.id,
                password: login.password
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            console.log(response.data);

            if (response.data.instructor) {

                // setLogin({ token: response.data.token, email: response.data.email, loggedIn: true });
                localStorage.setItem('token', "instructor");
                localStorage.setItem('name', response.data.instructor.name);
                localStorage.setItem('instructor_id', response.data.instructor.instructor_id);
                localStorage.setItem('email', response.data.instructor.email);

                alert('Login successful');
                Navigate('/home');

            }

        }
    }


        return (
            <Container>
                <Row className="justify-content-md-center mt-5">
                    <Col md={6}>
                        <div className="p-4 border rounded">
                            <h2 className="mb-4">Login</h2>
                            <Form>

                                <Form.Group controlId="formRole">
                                    <Form.Label>Role</Form.Label>
                                    <Form.Control as="select" value={login.role === 'student' ? 'student' : 'teacher'} onChange={(e) => setLogin({ ...login, role: e.target.value })}>
                                        <option value="">Select role</option>
                                        <option value="student">Student</option>
                                        <option value="teacher">Instructor</option>
                                    </Form.Control>
                                </Form.Group>

                                <Form.Group controlId="formId" onChange={(e) => setLogin({ ...login, id: e.target.value })}>
                                    <Form.Label>{login.role === 'student' ? 'Roll Number' : 'Instructor Id'}</Form.Label>
                                    <Form.Control type="text" placeholder={login.role === 'student' ? 'Enter roll number' : 'Enter instructor id'} />
                                </Form.Group>

                                <Form.Group controlId="formBasicPassword" onChange={(e) => setLogin({ ...login, password: e.target.value })}>
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control type="password" placeholder="Password" />
                                </Form.Group>

                                <Button variant="primary" type="button" onClick={handleLogin} block="true">
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

import React, { useState } from 'react';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';

import axios from 'axios';
import { Navigate, redirect } from 'react-router-dom';

const RecommendationForm = () => {
  const [formData, setFormData] = useState({
    courseType: '',
    rollNumber: '',
    difficulty: '',
    timeCommitment: '',
    learningImportance: '',
    courseStructureImportance: '',
    courseMaterialQuality: '',
    assignmentQuality: '',
    examQuality: '',
    expectationsAlignment: '',
    instructorQuality: '',
    recommendationsImportance: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8080/recommend_courses', {
      roll_number: formData['question-1'],
      course_type: formData['question-0'],
      user_preferences: [
        (-1 / formData['question-2']),
        parseInt(formData['question-3']), // Parse time commitment as integer
        parseInt(formData['question-4']), // Parse new learning as integer
        parseInt(formData['question-5']), // Parse structure quality as integer
        parseInt(formData['question-6']), // Parse material quality as integer
        parseInt(formData['question-7']), // Parse assignment quality as integer
        parseInt(formData['question-8']), // Parse exam quality as integer
        parseInt(formData['question-9']), // Parse expectation alignment as integer
        parseInt(formData['question-10']), // Parse instructor quality as integer
        parseInt(formData['question-11']), // Parse recommendation likelihood as integer
      ],
      feature_labels: [
        'Difficulty', 'Time commitment', 'New learning', 'Structure quality',
        'Material quality', 'Assignment quality', 'Exam quality', 'Expectation alignment',
        'Instructor quality', 'Recommendation Likelihood'
      ],
      feature_keys: [
        "How would you rate the difficulty of the course?",
        "How would you rate the extent of time commitment required for the course?",
        "How much would you say you learned from the course?",
        "How well do you think the course was structured?",
        "How would you rate the quality of the course material?",
        "How would you rate the quality of the assignments?",
        "How would you rate the quality of the exams?",
        "How well did the course align with your expectations?",
        "How would you rate the quality of your instructor?",
        "How likely are you to recommend this course to your juniors?"
      ]
    }, {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    })
    .then((response) => {

      localStorage.setItem('recommendationData', JSON.stringify(response.data));

      console.log(response.data);
      window.location.href = '/recommendations';
    })
    .catch((error) => {
      console.error('There was an error!', error);
    });
  };

  const questions = [
    "What type of course are you looking for?",
    "Enter your roll number:",
    "What difficulty are you willing to tolerate?",
    "How much time can you commit to the course?",
    "How important is it to you to learn something new from the course?",
    "How important is it to you that the course is well structured?",
    "How much do you value the quality of the course material?",
    "How much do you value the quality of the assignments?",
    "How much do you value the quality of the exams?",
    "How important is it to you that the course aligns with your expectations?",
    "How much do you value the quality of the instructor?",
    "How important are other students' recommendations to you?"
  ];

  return (
    <Container>
      <Row>
        <Col>
          <h2>Course Recommendation Form</h2>
          <Form onSubmit={handleSubmit}>
            {questions.map((question, index) => (
              <Row key={index} className="align-items-start">
                <Col xs={12}>
                  <Form.Label>{question}</Form.Label>
                </Col>
                <Col xs={12}>
                  {(index === 0) ?
                    <Form.Control
                      as="select"
                      name={`question-${index}`}
                      onChange={handleChange}
                      value={formData[`question-${index}`]}
                    >
                      <option value="">Select</option>
                      <option value="SC">Science</option>
                      <option value="MA">Mathematics</option>
                      <option value="EE">Electrical Engineering</option>
                      <option value="HU">Humanities</option>
                      <option value="CS">Computer Science</option>
                    </Form.Control>
                  :
                  (index === 1) ?
                    <Form.Control
                      type="text"
                      name={`question-${index}`}
                      onChange={handleChange}
                      value={formData[`question-${index}`]}
                    />
                  :
                    <div>
                      {[...Array(10)].map((_, optionIndex) => (
                        <Form.Check
                          key={optionIndex}
                          inline
                          type="radio"
                          label={optionIndex + 1}
                          name={`question-${index}`}
                          value={optionIndex + 1}
                          checked={parseInt(formData[`question-${index}`]) === optionIndex + 1}
                          onChange={handleChange}
                        />
                      ))}
                    </div>
                  }
                </Col>
              </Row>
            ))}
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default RecommendationForm;

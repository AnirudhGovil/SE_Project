import React, { useState, useEffect } from "react";
import axios from "axios";
import { Card, Button, Container, Row, Col } from "react-bootstrap";

const Courses = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await axios.get('http://localhost:8080/generatedCourses');
        setCourses(response.data); // Assuming response.data is an array of courses
        localStorage.setItem('courses', JSON.stringify(response.data));
      } catch (error) {
        console.error("Error fetching courses:", error);
      }
    };

    fetchCourses();
  }, []);

  return (
    <Container>
      <h1 className="my-4">Courses</h1>
      <Row>
        {courses.map((course, index) => (
          <Col md={4} key={index}>
            <CourseCard course={course} />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

const CourseCard = ({ course }) => {
  const handleFeedbackClick = () => {
    // Store the selected course ID in local storage
    localStorage.setItem('selectedCourse', JSON.stringify(course));
    // Redirect to the feedback form
    window.location.href = '/feedback';
  };

  return (
    <Card className="mb-4">
      <Card.Body>
        <Card.Title>{course.Name}</Card.Title>
        <Card.Text>
          <strong>ID:</strong> {course.ID}<br />
          <strong>Category:</strong> {course.Category}<br />
          <strong>Credits Worth:</strong> {course['Credits Worth']}<br />
          <strong>Year:</strong> {course.Year}
        </Card.Text>
        <Button variant="primary" onClick={handleFeedbackClick}>Give Feedback</Button>
      </Card.Body>
    </Card>
  );
};

export default Courses;

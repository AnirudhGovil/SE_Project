// CoursesPage.js

import React from "react";
import { useRecoilValue } from "recoil";
import { Link } from "react-router-dom";
import { courseState } from "../../atoms/CourseState";
import { Card, Button, Container, Row, Col } from "react-bootstrap";

const Courses = () => {
  const courses = useRecoilValue(courseState);

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
        <Link to={`/feedback/${course.ID}`}>
          <Button variant="primary">Give Feedback</Button>
        </Link>
      </Card.Body>
    </Card>
  );
}


export default Courses;

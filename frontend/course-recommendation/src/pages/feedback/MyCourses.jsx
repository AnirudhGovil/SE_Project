import axios from "axios";
import { my_courses_instructor_api } from "../../Helper";

import { useState, useEffect } from "react";

import { Card, Button, Container } from "react-bootstrap";
import { Link } from "react-router-dom";




function MyCourses(){

    const [courses, setCourses] = useState([]);

    useEffect(() => {
        axios.get(`${my_courses_instructor_api}${localStorage.getItem('instructor_id')}`) 
            .then(response => {
                console.log(response.data);
                setCourses(response.data);
            })


    }, []);

    return (

        <Container>
            <h1>My Courses</h1>
            {courses.map(course => <CourseCard course={course} />)}
        </Container>

    );

    
}

const CourseCard = ({ course }) => {
    return (
      <Card className="mb-4">
        <Card.Body>
          <Card.Title>{course.name}</Card.Title>
          <Card.Text>
            <strong>ID:</strong> {course.course_id}<br />
            <strong>Category:</strong> {course.instructor_id}<br />
            <strong>Credits Worth:</strong> {}<br />
            <strong>Year:</strong> {course.session}
          </Card.Text>
          <Link to={`/feedback/${course.ID}`}>
            <Button variant="primary">Give Feedback</Button>
          </Link>
        </Card.Body>

      </Card>
    );
  }
  
  
export default MyCourses;
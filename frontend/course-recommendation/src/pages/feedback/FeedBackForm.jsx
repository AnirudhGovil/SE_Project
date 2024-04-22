import React, { useState, useEffect } from 'react';
import { Form, Button, Container } from 'react-bootstrap';

const FeedBackForm = () => {
  const [course, setCourse] = useState(null);
  const [ratings, setRatings] = useState({
    difficulty: null,
    timeCommitment: null,
    learningExtent: null,
    courseStructure: null,
    courseMaterialQuality: null,
    assignmentQuality: null,
    examQuality: null,
    expectationsAlignment: null,
    instructorQuality: null,
    likelihoodToRecommend: null,
  });
  const [additionalFeedback, setAdditionalFeedback] = useState('');

  useEffect(() => {
    // Fetch course details from local storage
    const storedCourse = JSON.parse(localStorage.getItem('selectedCourse'));
    if (storedCourse) {
      setCourse(storedCourse);
    }
  }, []);

  const handleRatingChange = (question, value) => {
    setRatings({ ...ratings, [question]: value });
  };

  const handleAdditionalFeedbackChange = (e) => {
    setAdditionalFeedback(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Survey ratings:', ratings);
    console.log('Additional feedback:', additionalFeedback);
    // Submit ratings to the server or perform other actions
  };

  if (!course) {
    return <div>Loading...</div>;
  }

  return (
    <Container>
      <h2 className="mb-4">{course.Name}</h2>
      <Form onSubmit={handleSubmit}>
        {/* Existing course-specific questions */}
        {course.Questions.map((question, index) => (
          <Form.Group controlId={`rating-${index}`} key={index}>
            <Form.Label>{question}</Form.Label>
            <div>
              {[...Array(10).keys()].map((num) => (
                <Form.Check
                  key={num + 1}
                  inline
                  type="radio"
                  id={`rating-${index}-${num + 1}`}
                  label={num + 1}
                  name={`rating-${index}`}
                  value={num + 1}
                  checked={ratings[question] === num + 1}
                  onChange={() => handleRatingChange(question, num + 1)}
                />
              ))}
            </div>
          </Form.Group>
        ))}
        {/* Additional generic questions */}
        {genericFeedbackQuestions.map((question, index) => (
          <Form.Group controlId={`generic-rating-${index}`} key={index + course.Questions.length}>
            <Form.Label>{question}</Form.Label>
            <div>
              {[...Array(10).keys()].map((num) => (
                <Form.Check
                  key={num + 1}
                  inline
                  type="radio"
                  id={`generic-rating-${index}-${num + 1}`}
                  label={num + 1}
                  name={`generic-rating-${index}`}
                  value={num + 1}
                  checked={ratings[question] === num + 1}
                  onChange={() => handleRatingChange(question, num + 1)}
                />
              ))}
            </div>
          </Form.Group>
        ))}
        {/* Text area for additional feedback */}
        <Form.Group controlId="additionalFeedback">
          <Form.Label>Additional Feedback</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            value={additionalFeedback}
            onChange={handleAdditionalFeedbackChange}
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </Container>
  );
};

export default FeedBackForm;

// Additional generic feedback questions
const genericFeedbackQuestions = [
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
];

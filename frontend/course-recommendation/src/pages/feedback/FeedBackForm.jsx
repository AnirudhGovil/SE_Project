// FeedbackForm.js

import React, { useState } from "react";
import { useParams } from "react-router-dom";
import PropTypes from "prop-types";

const questions = [
    "How well did the course cover fundamental concepts of linear algebra such as vectors, matrices, and systems of equations?",
    "To what extent did the course provide insights into linear transformations, eigenvalues, and eigenvectors?",
    "How useful were the assignments and applications in understanding linear algebra in various fields?"

];

function FeedbackForm() {
  const { courseId } = useParams();
  const [feedback, setFeedback] = useState({});
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFeedback({
      ...feedback,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you can send the feedback data to your backend or handle it as needed
    console.log("Feedback submitted:", feedback);
  };

  return (
    <div>
      <h1>Feedback Form for Course {courseId}</h1>
      <form onSubmit={handleSubmit}>
        {questions.map((question, index) => (
          <div className="form-group" key={index}>
            <label htmlFor={`question${index + 1}`}>{question}</label>
            <input
              type="number"
              className="form-control"
              id={`question${index + 1}`}
              name={`question${index + 1}`}
              value={feedback[`question${index + 1}`] || ''}
              onChange={handleInputChange}
              min="1"
              max="10"
              required
            />
          </div>
        ))}
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
};

export default FeedbackForm;

import React, { useState } from "react";
import { Form, Button, Card } from "react-bootstrap";

const RecommendationForm = () => {
  const categories = ['Science', 'Mathematics', 'Electrical Engineering', 'Humanities', 'Computer Science'];

  const [formData, setFormData] = useState({
    courseType: '',
    rollNumber: '',
    difficulty: '',
    timeCommitment: '',
    newLearning: '',
    structureQuality: '',
    materialQuality: '',
    assignmentQuality: '',
    examQuality: '',
    expectationAlignment: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted:", formData);
    // Here you can handle form submission (e.g., send data to backend)
  };

  return (
    <div className="container mt-4">
      <Card>
        <Card.Body>
          <Card.Title>Course Recommendation Form</Card.Title>
          <Form onSubmit={handleSubmit}>
            <Form.Group>
              <Form.Label>Course Type:</Form.Label>
              <Form.Control as="select" name="courseType" value={formData.courseType} onChange={handleChange} required>
                <option value="">Select Course Type</option>
                {categories.map((category, index) => (
                  <option key={index} value={category}>{category}</option>
                ))}
              </Form.Control>
            </Form.Group>
            <Form.Group>
              <Form.Label>Roll Number:</Form.Label>
              <Form.Control type="text" name="rollNumber" value={formData.rollNumber} onChange={handleChange} required />
            </Form.Group>
            <Form.Group>
              <Form.Label>Difficulty:</Form.Label>
              <Form.Control type="number" name="difficulty" value={formData.difficulty} onChange={handleChange} required />
            </Form.Group>
            {/* Add other form fields similarly */}
            <Button type="submit" variant="primary">Submit</Button>
          </Form>
        </Card.Body>
      </Card>
    </div>
  );
};

export default RecommendationForm;

import React, { useEffect, useState } from 'react';
import { Container, Col, Card } from 'react-bootstrap';
import { RadialChart } from 'react-vis';

const Recommendations = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch data from local storage
    const savedData = localStorage.getItem('recommendationData');
    if (savedData) {
      setData(JSON.parse(savedData));
    }
  }, []);

  if (!data) {
    return <div>Loading...</div>;
  }

  // Define distinctive colors for each feature
  const featureColors = {
    'Assignment quality': '#FF6F61',
    'Difficulty': '#6B5B95',
    'Exam quality': '#88B04B',
    'Expectation alignment': '#F7CAC9',
    'Instructor quality': '#92A8D1',
    'Material quality': '#F7CAC9',
    'New learning': '#955251',
    'Recommendation Likelihood': '#B565A7',
    'Structure quality': '#B5B35C',
    'Time commitment': '#F4C724'
  };

  const renderRadialChart = (courses, title) => {
    const renderLegend = (features) => {
      return (
        <div style={{ marginBottom: '20px' }}>
          <h5>Legend</h5>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            {features.map((feature, index) => (
              <li key={index} style={{ marginBottom: '5px', display: 'flex', alignItems: 'center' }}>
                <span style={{
                  display: 'inline-block',
                  width: '20px',
                  height: '10px',
                  marginRight: '10px',
                  backgroundColor: featureColors[feature],
                }}></span>
                <span>{feature}</span>
              </li>
            ))}
          </ul>
        </div>
      );
    };

    return (
      <div>
        <h3>{title}</h3>
        <Container>
          <Col>
            {courses.map((course, index) => (
              <Card key={index} style={{ marginBottom: '20px' }}>
                <Card.Body>
                  <Card.Title>{course.name}</Card.Title>
                  <p>{course.summary}</p> {/* Course summary */}
                  <div style={{ height: '200px', width: '200px' }}>
                    <RadialChart
                      data={Object.entries(course.features).map(([feature, value]) => ({
                        angle: 360 / Object.keys(course.features).length,
                        radius: value,
                        color: featureColors[feature], // Assigning color from featureColors
                        subLabel: value.toFixed(2), // Displaying values on hover
                      }))}
                      width={200}
                      height={200}
                      showLabels
                      labelsRadiusMultiplier={1.1}
                      labelsStyle={{ fontSize: 10, fill: '#333' }}
                    />
                  </div>
                </Card.Body>
              </Card>
            ))}
            {renderLegend(Object.keys(courses[0].features))} {/* Assuming features are same for all courses */}
          </Col>
        </Container>
      </div>
    );
  };

  return (
    <Container className="mt-5">
      <Card>
        <Card.Body>
          {renderRadialChart(data.recommended_courses, 'Recommended Courses')}
          {renderRadialChart(data.similar_courses, 'Similar Courses')}
        </Card.Body>
      </Card>
    </Container>
  );
};

export default Recommendations;

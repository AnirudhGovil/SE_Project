import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';


function Profile() {
    const userName = localStorage.getItem('name');
    const email = localStorage.getItem('email');
    const userId = localStorage.getItem('student_id');

    return (
        <ProfileView userName={userName} email={email} userId={userId} />
    );
}


const ProfileView = ({ userName, email, userId }) => {
  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        <Col md={6}>
          <Card>
            <Card.Body>
              <Card.Title>Profile Information</Card.Title>
              <Card.Text>
                <strong>User Name:</strong> {userName}
              </Card.Text>
              <Card.Text>
                <strong>Email:</strong> {email}
              </Card.Text>
              <Card.Text>
                <strong>User ID:</strong> {userId}
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};


export default Profile;

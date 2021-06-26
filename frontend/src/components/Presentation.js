import React, { useState } from 'react';
import Button from 'react-bootstrap/esm/Button';
import Card from 'react-bootstrap/Card'
import Accordion from 'react-bootstrap/Accordion';
import TeamMembers from './TeamMembers';
import '../App.css'
import '../styles/buttons.css'

const Presentation = () => {

    return (
        <div className="presentation-container">
            <div className='imgContainer'></div>
            <Accordion className='displayer' defaultActiveKey="0">
                <Card className='header'>
                    <Card.Header className='card-header'>
                    <Accordion.Toggle as={Button} variant="primary" eventKey="0">
                        Know our team
                    </Accordion.Toggle>
                    <Accordion.Toggle as={Button} variant="primary" eventKey="1">
                        Know challenge goal
                    </Accordion.Toggle>
                    </Card.Header>
                    <Accordion.Collapse eventKey="0">
                        <TeamMembers />
                    </Accordion.Collapse>
                    <Accordion.Collapse eventKey="1">
                    <Card.Body>Create a solution that evaluates code according to metrics that indicate sustainable principles</Card.Body>
                    </Accordion.Collapse>
                </Card>
            </Accordion>
        </div>
    );
}




export default Presentation;
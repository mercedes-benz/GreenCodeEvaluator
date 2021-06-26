import React from 'react';
import Nav from 'react-bootstrap/Nav';
import '../styles/navBar.css'

const Header = () => (
  <>
  <header>                
                <h2>Welcome to our Mercedes Benz challenge for the HerHackethon event!</h2>
                <h3>Green Code Evaluator</h3>
            </header>
  <Nav fill variant="tabs" className="nav" defaultActiveKey="/home">
  <Nav.Item>
    <Nav.Link href="/" className="nav-item">Presentation</Nav.Link>
  </Nav.Item>
  <Nav.Item>
    <Nav.Link className="nav-item" eventKey="link-1" href='/green-code-about'>Green code</Nav.Link>
  </Nav.Item>
  <Nav.Item>
    <Nav.Link className="nav-item" eventKey="link-2">Best practices</Nav.Link>
  </Nav.Item>
  <Nav.Item>
    <Nav.Link className="nav-item" href="/total-time">Total time mesure</Nav.Link>
  </Nav.Item>
  <Nav.Item>
    <Nav.Link className="nav-item" href="/cpu">CPU mesure</Nav.Link>
  </Nav.Item>
  <Nav.Item>
    <Nav.Link className="nav-item" href="/unused">Unused imports</Nav.Link>
  </Nav.Item>
  <Nav.Item>
    <Nav.Link className="nav-item" href="/memory">Memory</Nav.Link>
  </Nav.Item>
</Nav>
</>
);

export default Header;
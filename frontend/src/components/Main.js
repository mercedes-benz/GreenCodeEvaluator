import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import '../App.css'

const Main = () => {
    const [file, setFile] = useState(null)

    const handleSubmit = (ev) => {
        ev.preventDefault();
    
        const data = new FormData();
        data.append('file', file.files[0]);
    
        const options = {
            headers: {
              'Content-type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Referrer-Policy': 'origin-when-cross-origin'
            },
            method: 'POST',
            mode: 'no-cors',
            body: data,
        }
        fetch('http://localhost:5000/uploader', options)
        .then((response) => {
          console.log(response)
        });
      }
    return (
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <div>
            <input ref={(ref) => { setFile(ref) }} type="file" />
          </div>
          <br />
          <div>
            <Button>Upload</Button>
          </div>
        </form>
        </div>
      );
    
}




export default Main;
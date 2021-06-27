import React, { useEffect, useState } from 'react';
import ListGroup from 'react-bootstrap/ListGroup';
import ProgressBar from 'react-bootstrap/ProgressBar';
import SysInfo from './SysInfo.js'

const ChartCPU = () => {
    const [data, setData] = useState([]);

    useEffect(()=>{
        getData();
      },[])

    const getData=()=>{
        fetch('cpu.json'
        ,{
          headers : {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        }
        )
          .then(function(response){
            return response.json();
          }).then (function(result) {
              console.log(result)
                setData(result);
          })
      }
      console.log(data)
      const title = 'CPU measurement'
    return (
        (data && data.length === 0 ? <div>Loading...</div> :
          <>
                  <h2>Your System</h2>
          <SysInfo/>
          <h2 className='result-title'>{title}</h2>
          <div className='result-container'>
          <ListGroup className='result-container'>
            {(data.map((item) => 
                (<ListGroup.Item>
                    <p>{item.detail}</p>
              <ProgressBar now={item.value} label={`${item.value} %`}/>
                </ListGroup.Item>)
              ) )}
          </ListGroup>
        </div>
        </>
            )
        
    );

}

export default ChartCPU;

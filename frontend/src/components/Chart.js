import React, { useEffect, useState } from 'react';
import ListGroup from 'react-bootstrap/ListGroup';
import ProgressBar from 'react-bootstrap/ProgressBar';


const Chart = () => {
    const [data, setData] = useState([]);
    
    useEffect(()=>{
        getData();
        
      },[])

    const getData=()=>{
        fetch('cprotxt.json'
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
              const dataPoints = [];
              for (let index = 0; index < result.length; index++) {
                  dataPoints.push({x:result[index].filenamelinenofunction , y:result[index].tottime});
              }
                setData(dataPoints);
          })
      }
      console.log(data)
      const title = 'total time measurement'
    return (
        (data && data.length === 0 ? <div>Loading...</div> :
            <>
            <h2 className='result-title'>{title}</h2>
            <div className='result-container'>
            <ListGroup className='result-container'>
            {(data.map((item) => 
                (<ListGroup.Item>
                    <p>{item.x}</p>
                   <ProgressBar now={item.y * 10} label={`${item.y}ms`} />
                </ListGroup.Item>)
              ) )}
          </ListGroup>
        </div>
        </>
            )
        
    );

}

export default Chart;
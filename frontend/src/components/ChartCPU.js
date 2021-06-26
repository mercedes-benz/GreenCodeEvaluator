import { useEffect, useState } from 'react';
import CanvasJSReact from '../assets/canvasjs.react';
import ProgressBar from 'react-bootstrap/ProgressBar';

var React = require('react');
var Component = React.Component;

//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

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
      const title = 'CPU mesure'
    return (
        (data && data.length === 0 ? <div>Loading...</div> :
          <>
          <h2 className='result-title'>{title}</h2>
          <div className='result-container'>
            {(data.map((item) => 
              (<>
              <p>{item.detail}</p>
              <ProgressBar now={item.value} />
              </>)
            ) )}
        </div>
        </>
            )
        
    );

}

export default ChartCPU;
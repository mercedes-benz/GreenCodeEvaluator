import { useEffect, useState } from 'react';
import CanvasJSReact from '../assets/canvasjs.react';
import ProgressBar from 'react-bootstrap/ProgressBar';

var React = require('react');
var Component = React.Component;

//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

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
              console.log(result)
              const dataPoints = [];
              for (let index = 0; index <= 10; index++) {
                  dataPoints.push({x: `func`, y:result[index].tottime});
              }
                setData(dataPoints);
          })
      }
      console.log(data)
      const title = 'total time mesure'
    return (
        (data && data.length === 0 ? <div>Loading...</div> :
            <>
            <h2 className='result-title'>{title}</h2>
            <div className='result-container'>
            {(data.map((item) => 
              (<>
              <p>{item.x}</p>
              <ProgressBar now={item.y * 10} label={`${item.y}ms`} />
              </>)
            ) )}
        </div>
        </>
            )
        
    );

}

export default Chart;
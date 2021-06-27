import React, { useEffect, useState } from 'react';
import ReactDOM from "react-dom";
import "../assets/static/css/SysinfoStyle.css";


const SysInfo = () => {
  const [data, setData] = useState([]);

  useEffect(()=>{
      getData();
    },[])

  const getData=()=>{
      fetch('sysinfo.json'
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
    console.log("sys info",data)
    const title = 'Your System'
  return (
      (data && data.length === 0 ? <div>Loading...</div> :
        <>
        <h2 className='result-title'>{title}</h2>
        <div className='result-container'>
        <table 
          style={{
            border: "1px solid black",
            marginLeft: "auto",
            marginRight: "auto"
          }}
        >
          <tbody style={{ color: "blue" }}>
            <tr>
              <td>Platform</td>
              <td>{data.platform}</td>
            </tr>
            <tr>
              <td>Platform Release</td>
              <td>{data.platform_release}</td>
            </tr>
            <tr>
              <td>Platform Version</td>
              <td>{data.platform_version}</td>
            </tr>
            <tr>
              <td>Processor</td>
              <td>{data.processor}</td>
            </tr>
            <tr>
              <td>RAM</td>
              <td>{data.ram}</td>
            </tr>
            {/* {this.state.dSys.map((data, i) => {
                            return (
                                <tr key={i}>
                                    <td>{data.platform}</td>
                                    <td>{data.lastname}</td>
                                </tr>
                            )
                        })} */}
          </tbody>
        </table>
      
      </div>
      </>
          )
      
  );

}

export default SysInfo;

import { useEffect, useState } from 'react';

var React = require('react');

const UnusedImport = () => {
    const [data, setData] = useState([]);
    
    useEffect(()=>{
        getData();
        
      },[])

    const getData=()=>{
        fetch('unused.json'
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
              console.log(result.unused_import)
                setData(result.unused_import);
          })
      }
      console.log(data)
      const title = 'Unused imports'
    return (
        (data && data.length === 0 ? <div>Loading...</div> :
          <>
          <h2 className='result-title'>{title}</h2>
            <div>
            {(data.map((item) => 
              (<p> {item}
              </p>)
            ) )}
        </div>
        </>
            )
        
    );

}

export default UnusedImport;
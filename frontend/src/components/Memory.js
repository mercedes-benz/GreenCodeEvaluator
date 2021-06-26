import React from 'react';
import memoryImg from '../img/memory_usage.png'

const Memory = () => {
    
  
      const title = 'Memory'
    return (
        <>
        <h2 className='result-title'>{title}</h2>
            <div>
            <img src={memoryImg} alt='img graph'/>
        </div>
        </>
    );

}

export default Memory;
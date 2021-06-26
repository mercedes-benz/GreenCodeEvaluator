import React from 'react';
import memoryImg from '../../public/memory_usage.png'

const Memory = () => {
    const title = 'Memory';
    return (
        <>
        <h2 className='result-title'>{title}</h2>
            <div className='result-container'>
            <img src={memoryImg} alt='img graph'/>
        </div>
        </>
    );

}

export default Memory;
import React from 'react';

const Memory = () => {
    const title = 'Memory usage';
    return (
        <>
        <h2 className='result-title'>{title}</h2>
            <div className='result-container'>
            <img src={window.location.origin + '/memory_usage.png'} alt='img graph'/>
        </div>
        </>
    );

}

export default Memory;
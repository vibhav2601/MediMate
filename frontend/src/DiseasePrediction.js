// src/DiseasePredictions.js

import React, { useState, useEffect } from 'react';

const DiseasePredictions = ({ endpoint }) => {
    const [topDiseases, setTopDiseases] = useState([]);

    useEffect(() => {
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                // Replace 'prediction' with the actual key in the response that contains the prediction data
                setTopDiseases(data.prediction.slice(0, 5));
            })
            .catch(error => {
                console.error('Error fetching disease predictions:', error);
            });
    }, [endpoint]);

    return (
        <div>
            {topDiseases.length > 0 && (
                <ul>
                    {topDiseases.map((disease, index) => (
                        <li key={index}>{disease[0]} - Probability: {disease[1]}</li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default DiseasePredictions;

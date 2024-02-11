import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import 'chart.js/auto';

const DonutChart = ({ data }) => {
  const chartData = {
    labels: data.map(item => item[0]),
    datasets: [
      {
        label: 'Disease Probability',
        data: data.map(item => item[1]),
        backgroundColor: [
          // Define a set of colors for your slices here
          '#FF6384',
          '#36A2EB',
          '#FFCE56',
          '#4BC0C0',
          '#9966FF',
        ],
        hoverOffset: 4,
        cutout: '80%',
      },
    ],
  };

  return <Doughnut data={chartData} />;
};

export default DonutChart;

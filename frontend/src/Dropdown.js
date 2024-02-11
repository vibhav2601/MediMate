import React, { useState } from 'react';

function Dropdown({ title, details }) {
    const [isOpen, setIsOpen] = useState(false);
  
    const toggleDropdown = () => setIsOpen(!isOpen);
  
    // Inline style for centering table content
    const tableStyle = {
      width: '80%', // Ensure the table stretches to the container width
      textAlign: 'center', // Center text within cells
      margin: 'auto', // Center the table within its container if necessary
      marginRight: 'calc(50% - 500px)'
    };
  
    return (
      <div>
        <button onClick={toggleDropdown} class="backNextButtons">{title}</button>
        {isOpen && (
          <table style={tableStyle} className="dropdown-table">
            <thead>
              <tr>
                <th>Assessment Criteria</th>
                <th>Diseases Covered</th>
                <th>Coverage</th>
              </tr>
            </thead>
            <tbody>
              {details.map((row, idx) => (
                <tr key={idx}>
                  <td>{row.criteria}</td>
                  <td>{row.diseases}</td>
                  <td>{row.coverage}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    );
  }
  

export default Dropdown;

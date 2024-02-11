import React, { useState } from 'react';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import CloseIcon from '@mui/icons-material/Close';
import { FormControl, InputLabel, Select, TextField, MenuItem, Slider, Box, IconButton } from '@mui/material';
import { red } from '@mui/material/colors';
import logo from './medimate.png';
import DonutChart from './DonutChart';
import Dropdown from './Dropdown'; // Adjust the path as necessary



const initialFormData = {
  name: '',
  age: '',
  currentLocation: '',
  gender: '',
  familyHistory: [],
  symptoms: [],
  symptomIntensity: {}
};

const familyHistoryOptions = [
  "Diabetes",
  "Bronchial Asthma",
  "Hypertension",
  "Migraine",
  "Cervical spondylosis",
  "Hypothyroidism",
  "Hyperthyroidism",
  "Osteoarthritis",
  "Arthritis"
];

const symptomOptions = ['abdominal pain',
'abnormal menstruation',
'acidity',
'acute liver failure',
'altered sensorium',
'anxiety',
'back pain',
'belly pain',
'blackheads',
'bladder discomfort',
'blister',
'blood in sputum',
'bloody stool',
'blurred and distorted vision',
'breathlessness',
'brittle nails',
'bruising',
'burning micturition',
'chest pain',
'chills',
'cold hands and feets',
'coma',
'congestion',
'constipation',
'continuous feel of urine',
'continuous sneezing',
'cough',
'cramps',
'dark urine',
'dehydration',
'depression',
'diarrhoea',
'dischromic patches',
'distention of abdomen',
'dizziness',
'drying and tingling lips',
'enlarged thyroid',
'excessive hunger',
'extra marital contacts',
'family history',
'fast heart rate',
'fatigue',
'fluid overload',
'fluid overload',
'foul smell of urine',
'headache',
'high fever',
'hip joint pain',
'history of alcohol consumption',
'increased appetite',
'indigestion',
'inflammatory nails',
'internal itching',
'irregular sugar level',
'irritability',
'irritation in anus',
'itching',
'joint pain',
'knee pain',
'lack of concentration',
'lethargy',
'loss of appetite',
'loss of balance',
'loss of smell',
'malaise',
'mild fever',
'mood swings',
'movement stiffness',
'mucoid sputum',
'muscle pain',
'muscle wasting',
'muscle weakness',
'nausea',
'neck pain',
'nodal skin eruptions',
'obesity',
'pain behind the eyes',
'pain during bowel movements',
'pain in anal region',
'painful walking',
'palpitations',
'passage of gases',
'patches in throat',
'phlegm',
'polyuria',
'prominent veins on calf',
'puffy face and eyes',
'pus filled pimples',
'receiving blood transfusion',
'receiving unsterile injections',
'red sore around nose',
'red spots over body',
'redness of eyes',
'restlessness',
'runny nose',
'rusty sputum',
'scurrying',
'shivering',
'silver like dusting',
'sinus pressure',
'skin peeling',
'skin rash',
'slurred speech',
'small dents in nails',
'spinning movements',
'spotting urination',
'stiff neck',
'stomach bleeding',
'stomach pain',
'sunken eyes',
'sweating',
'swelled lymph nodes',
'swelling joints',
'swelling of stomach',
'swollen blood vessels',
'swollen extremeties',
'swollen legs',
'throat irritation',
'toxic look (typhos)',
'ulcers on tongue',
'unsteadiness',
'visual disturbances',
'vomiting',
'watering from eyes',
'weakness in limbs',
'weakness of one body side',
'weight gain',
'weight loss',
'yellow crust ooze',
'yellow urine',
'yellowing of eyes',
'yellowish skin'];

function MultiStepForm() {
  const [activeOption, setActiveOption] = useState(null);

  const [showInsurance, setShowInsurance] = useState(false);

  // Example of converting and mapping over disease prediction

// Now you can map over diseasePredictionsArray


  const [predictionResults, setPredictionResults] = useState([]); // Initialize as an empty array
  const [insuranceResults, setInsuranceResults] = useState([]);

    const [error, setError] = useState('');
    
    const [isSubmitted, setIsSubmitted] = useState(false);

  const [formData, setFormData] = useState(initialFormData);
  const [currentStep, setCurrentStep] = useState(1);
  const [seeWhy, setSeeWhy] = useState({});


  const handleShowInsurance = () => {
    setShowInsurance(true);
  };
  

  const handleFamilyHistoryChange = (event) => {
    const { value } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      familyHistory: prevFormData.familyHistory.includes(value)
        ? prevFormData.familyHistory.filter((history) => history !== value)
        : [...prevFormData.familyHistory, value],
    }));
  };

  const renderExplanations = () => {
    return Object.entries(seeWhy).map(([insuranceName, criteriaDetails], index) => {
      const tableData = Object.entries(criteriaDetails).map(([criteria, [diseases, coverage]]) => {
        // Remove "DXX:" pattern from the criteria names
        const formattedCriteria = criteria.replace(/D\d+:\s*/, '');
  
        // Adjust coverage value based on its size
        let adjustedCoverage;
        if (coverage < 1) {
          // If coverage is less than 1, multiply by 100 to convert to a percentage
          adjustedCoverage = (coverage * 100).toFixed() + '%';
        } else {
          // If coverage is 100 (or potentially greater), just append a '%' sign without multiplying
          adjustedCoverage = coverage + '%';
        }
  
        return {
          criteria: formattedCriteria, // Use the formatted criteria
          diseases: diseases.join(', '), // Convert diseases array to a string
          coverage: adjustedCoverage // Use the adjusted coverage value
        };
      });
  
      return (
        <Dropdown
          key={index}
          title={insuranceName}
          details={tableData} // Pass the transformed table data
        />
      );
    });
  };
  
  
  

  const handleOptionClick = (optionName) => {
    // If the option is already active, clicking again will collapse it
    setActiveOption(activeOption === optionName ? null : optionName);
  };
  

  const handleSymptomChange = (event) => {
    if (!formData.symptoms.includes(event.target.value)) {
      setFormData({
        ...formData,
        symptoms: [...formData.symptoms, event.target.value],
        symptomIntensity: { ...formData.symptomIntensity, [event.target.value]: 1 }
      });
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleIntensityChange = (symptom, intensity) => {
    setFormData({
      ...formData,
      symptomIntensity: { ...formData.symptomIntensity, [symptom]: intensity }
    });
  };

  const renderInsuranceDetails = () => {
    if (!activeOption) return null; // If no option is active, don't render anything
  
    // Find the details for the active option
    const details = insuranceResults.find((result) => result.name === activeOption);
  
    // Render the details in a table
    return (
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>Diseases</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {details.features.map((feature, index) => (
            <tr key={index}>
              <td>{feature.name}</td>
              <td>{feature.diseases.join(', ')}</td>
              <td>{feature.score.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  };

  const renderErrorMessage = () => {
    return error ? <div style={{ color: 'red' }}>{error}</div> : null;
  };

  const handleSymptomSelection = (event) => {
    const symptom = event.target.value;
    if (!formData.symptoms.includes(symptom)) {
      setFormData({
        ...formData,
        symptoms: [...formData.symptoms, symptom],
        symptomIntensity: { ...formData.symptomIntensity, [symptom]: 1 }
      });
    }
  };

  const removeSymptom = (symptomToRemove) => {
    setFormData({
      ...formData,
      symptoms: formData.symptoms.filter(symptom => symptom !== symptomToRemove),
      symptomIntensity: { ...formData.symptomIntensity, [symptomToRemove]: undefined }
    });
  };

  const [showExplanations, setShowExplanations] = useState(false);


  const handleSubmit = (e) => {
    e.preventDefault();
    if (currentStep === 3) {
      if (validateCurrentStep()) {
        console.log("Form Data Submitted:", JSON.stringify(formData, null, 2));
        
        // Send the form data to the Flask backend
        fetch('http://127.0.0.1:5000/predict', { // Replace with the URL where your Flask app is running
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
          console.log('Success:', data);
          setIsSubmitted(true);
          setShowInsurance(false);
  
          const predictions = data['disease predictions'];
          const sortedPredictions = Object.entries(predictions)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5);
          setPredictionResults(sortedPredictions);
  
          console.log('Insurance Predictions:', data['insurance predictions']);
          const insurancePredictions = data['insurance predictions'];
          const insurancePredictionsArray = Object.values(insurancePredictions);
          setInsuranceResults(insurancePredictionsArray.slice(0, 5));
  
          // Update the seeWhy state with the data received from the backend
          // Make sure the key 'see why' matches exactly what your backend sends
          setSeeWhy(data['see why']); // This line updates the seeWhy state
        })
        .catch((error) => {
          console.error('Error:', error);
        });
      }
    } else {
      nextStep();
    }
  };
  
  
  

  
  const validateCurrentStep = () => {
    let isValid = true; // Assume the step is valid initially

    // Clear any existing errors
    setError('');

    switch (currentStep) {
        case 1:
            // Validate all personal information fields in the first step
            if (!formData.name.trim()) {
                setError('Name is required');
                isValid = false;
            } else if (!formData.age.trim()) {
                setError('Age is required');
                isValid = false;
            } else if (!formData.currentLocation.trim()) {
                setError('Current location is required');
                isValid = false;
            } else if (!formData.gender) {
                setError('Gender is required');
                isValid = false;
            }
            break;
            case 2:
              break;
          case 3:
              // Assuming case 3 is for symptoms validation (if necessary)
              // Example: Ensure at least one symptom is selected
              if (formData.symptoms.length === 0) {
                  setError('Please select at least one symptom');
                  isValid = false;
              }
              break;
        // No need for cases 4, 5, 6, etc., since we've consolidated steps
    }

    return isValid; // Return the validation status of the current step
};


  const nextStep = () => {
    if (validateCurrentStep()) {
      setCurrentStep((prevStep) => prevStep + 1);
    }
  };

  const prevStep = () => {
    setCurrentStep((prevStep) => prevStep - 1);
  };

  const renderSelectedSymptoms = () => {
    return formData.symptoms.map((symptom, index) => (
      <Box key={index} sx={{ display: 'flex', alignItems: 'center', mb: 2, pl: 3, pr: 20 }}>
        <Box sx={{flexGrow: 1, mr: 2, pr:10, fontWeight: 'bold' }}>{symptom}</Box>
        <Slider
          sx={{ mr: 1, width: '300px', color: red[600] }}
          value={formData.symptomIntensity[symptom] || 1}
          onChange={(e, value) => handleIntensityChange(symptom, value)}
          aria-labelledby="symptom-slider"
          valueLabelDisplay="auto"
          step={1}
          marks
          min={1}
          max={5}
        />
        <IconButton onClick={() => removeSymptom(symptom)} size="small">
          <CloseIcon />
        </IconButton>
      </Box>
    ));
  };
  

  // Helper function to render the current step
  const renderStep = () => {

    const heading = currentStep === 1 ? (
      <h1 className="form-heading">First some general information!</h1>
    ) : null;
    
    switch (currentStep) {
      case 1:
        // Combine the fields into one step
        return (
          <Box sx={{ padding: '0 40px' }}>
            {heading}
            <TextField
              fullWidth
              margin="normal"
              label="Name"
              name="name"
              value={formData.name}
              onChange={handleInputChange}
            />
            <TextField
              fullWidth
              margin="normal"
              label="Age"
              name="age"
              type="number"
              value={formData.age}
              onChange={handleInputChange}
            />
            <TextField
              fullWidth
              margin="normal"
              label="Current Location"
              name="currentLocation"
              value={formData.currentLocation}
              onChange={handleInputChange}
            />
<FormControl fullWidth margin="normal" sx={{ textAlign: 'left' }}>
  <InputLabel id="gender-label">Gender</InputLabel>
  <Select
    labelId="gender-label"
    id="gender-select"
    name="gender"
    value={formData.gender}
    onChange={handleInputChange}
  >
    <MenuItem value="male">Male</MenuItem>
    <MenuItem value="female">Female</MenuItem>
    <MenuItem value="other">Other</MenuItem>
  </Select>
</FormControl>
          </Box>
        );
            case 2:
              return (
                <div>
                  <p className="familyHistoryHeading">Family history</p>
                  <p className="description">Check all the incidents that have taken place within immediate family members.</p>
                  <FormGroup row sx={{ justifyContent: 'center', m: 3 }}>
  {familyHistoryOptions.map((condition, index) => (
    <FormControlLabel
    control={
      <Checkbox
        sx={{
          color: red[800],
          '&.Mui-checked': {
            color: red[600],
          },
        }}
        value={condition}
        onChange={handleFamilyHistoryChange}
        checked={formData.familyHistory.includes(condition)}
      />
    }
    label={condition}
    sx={{ margin: 2 }} // This ensures each FormControlLabel has the same margin
  />  
  ))}
</FormGroup>

                  <div className="selectedConditions">
                    <p>Selected Conditions:</p>
                    <ul className="selectedConditionsList">
                      {formData.familyHistory.map((condition, index) => (
                        <li key={index}>{condition}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              );
            
              case 3:
                const symptomProgress = (formData.symptoms.length / symptomOptions.length) * 100;
                return (
                  <Box sx={{ p: 3 }}> {/* Padding added here */}
                    <FormControl fullWidth>
                      <InputLabel id="symptom-select-label">Symptom</InputLabel>
                      <Select
                        labelId="symptom-select-label"
                        id="symptom-select"
                        value=""
                        label="Symptom"
                        onChange={handleSymptomSelection}
                        sx={{
                          mb: 2,
                          '.MuiSvgIcon-root': {
                            color: red[600],
                          },
                        }}
                      >
                        {symptomOptions.map((symptom, index) => (
                          <MenuItem key={index} value={symptom}>{symptom}</MenuItem>
                        ))}
                      </Select>
                    </FormControl>
            
                    {renderSelectedSymptoms()}
                    
                    <div className="progress-container" style={{marginTop: "20px"}}>
                      <div className="progress-bar" style={{width: `${symptomProgress}%`, backgroundColor: 'lightblue', height: '20px'}}></div>
                    </div>

                  </Box>
                );           
        // ... handle the final step
        default:
            return null;
        }
    };

    return (
      <div className="multi-step-form-container">
        <div className="logo-container">
          <img src={logo} alt="Medimate Logo" className="logo" />
          <span className="logo-text">Medimate</span>
        </div>
        
        <div>
          {isSubmitted ? (
            <>
              {showInsurance ? (
                // Display the insurance list if showInsurance is true
                <div className="insurance-list-container">
                  <h3>Top Insurance Plans:</h3>
                  <ul className="insurance-list">
                    {insuranceResults.map((result, index) => (
                      <li key={index}>{result[0]} </li>
                    ))}
                  </ul>
                  {/* Add a button or mechanism to toggle showing explanations */}
                  <button onClick={() => setShowExplanations(!showExplanations)} className="backNextButtons">
                    {showExplanations ? "Hide Explanations" : "Show Explanations"}
                  </button>
                </div>
              ) : (
                // Display the disease predictions if showInsurance is false
                <div className="results-container">
                  <div className="chart-container">
                    <DonutChart data={predictionResults} />
                  </div>
                  <div className="predictions-list-container">
                    <h3>Top Disease Predictions:</h3>
                    <ul className="predictions-list">
                      {predictionResults.map((result, index) => (
                        <li key={index}>{result[0]} : {(result[1] * 100).toFixed()}%</li>
                      ))}
                    </ul>
                  </div>
                  <button onClick={() => setShowInsurance(true)} className="backNextButtons">Next</button>
                </div>
              )}
              {/* Conditionally render explanations if showExplanations is true */}
              {showExplanations && (
                <div className="explanations-container">
                  <h3>Why These Insurance Plans?</h3>
                  {renderExplanations()} {/* Call the function to render explanations */}
                </div>
              )}
            </>
          ) : (
            // The form and its steps are displayed only if isSubmitted is false
            <form onSubmit={handleSubmit}>
              {renderStep()}
              {renderErrorMessage()}
              <div>
                {currentStep > 1 && <button type="button" onClick={prevStep} className="backNextButtons">Back</button>}
                {currentStep < 3 && <button type="button" onClick={nextStep} className="backNextButtons">Next</button>}
                {currentStep === 3 && <button type="submit" className="backNextButtons">Submit</button>}
              </div>
            </form>
          )}
        </div>
      </div>
    );
  } 

export default MultiStepForm;

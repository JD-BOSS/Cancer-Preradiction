import React, { Component } from "react";
import axios from "axios";
import './App.css';

class App extends Component {
  state = {
    values: {
      Gender: "",
      Age: "",
      Smoking: "",
      Fatigue: "",
      Allergy: "",
    },
    prediction: null,
    error: null,
    loading: false,
    formSubmitted: false,
  };

  handleChange = (e) => {
    const { name, value } = e.target;
    this.setState(prevState => ({
      values: {
        ...prevState.values,
        [name]: value,
      },
    }));
  };

  handleSubmit = (e) => {
    e.preventDefault();
    this.setState({ loading: true });
    axios
      .post("http://127.0.0.1:8000/api/predict/", this.state.values)
      .then((response) => {
        this.setState({
          prediction: response.data.prediction,
          error: null,
          loading: false,
          formSubmitted: true,
        });
      })
      .catch((error) => {
        console.error("An error occurred:", error);
        this.setState({
          error: "An error occurred. Please try again later.",
          loading: false,
        });
      });
  };

  clearForm = () => {
    this.setState({
      values: {
        Gender: "",
        Age: "",
        Smoking: "",
        Fatigue: "",
        Allergy: "",
      },
      formSubmitted: false,
    });
  };

  render() {
    const { values, prediction, error, loading, formSubmitted } = this.state;

    return (
      <div className="cancer-form-container">
        {!formSubmitted ? (
          <div className="form">
            <h1 className="form-title">Cancer Prediction</h1>
            <form className="cancer-form" onSubmit={this.handleSubmit}>
              {Object.entries(values).map(([fieldName, fieldValue]) => (
                <div className="form-field" key={fieldName}>
                  <label className="field-label">{fieldName}:</label>
                  <input
                    className="field-input"
                    type='number'
                    name={fieldName}
                    value={fieldValue}
                    onChange={this.handleChange}
                  />
                </div>
              ))}
              <button className="submit-button" type="submit" disabled={loading}>
                {loading ? 'Loading...' : 'Submit'}
              </button>
            </form>
            {error && <div className="error-message">Error: {error}</div>}
          </div>
        ) : (
          <div className="result-container">
            <h2 className="result-title">Prediction:</h2>
            <p className="result">{prediction}</p>
            <button className="recheck-button" onClick={this.clearForm}>Recheck</button>
          </div>
        )}
      </div>
    );
  }
}

export default App;

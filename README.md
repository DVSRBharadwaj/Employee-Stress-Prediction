# Employee Stress Prediction

This repository contains a machine learning-powered application for detecting employee stress levels. The project consists of:

- A **Power BI dashboard** for visualizing employee stress insights.
- A **Streamlit-based web application** for predicting employee stress using an ML model.

## Features
- **Employee Stress Prediction:** Uses machine learning to assess stress levels based on various workplace and personal factors.
- **Interactive Dashboard:** Power BI dashboard provides visual insights into employee stress data.
- **User-Friendly Interface:** Built with Streamlit, allowing easy input and prediction.

## Installation
### Prerequisites
- Python 3.7+
- Streamlit
- NumPy
- Pickle (for loading the ML model)
- Power BI (for viewing the dashboard)

### Steps to Run the Application
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/employee-stress-prediction.git
   cd employee-stress-prediction
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run final_app.py
   ```

## Usage
- Open the web application.
- Navigate between **Home**, **About**, and **Predictions** sections.
- Enter employee details and get a stress prediction.
- View the Power BI dashboard to analyze trends.

## Model Details
- A **Random Forest Classifier** (`rf_model.pkl`) is used for prediction.
- Features include department, education, gender, workload, income, and more.
- Prediction probability determines if an employee is under stress.

## Dashboard
- The Power BI dashboard (`Employee Dashboard.pbix`) visualizes:
  - Stress distribution across departments.
  - Work-life balance and satisfaction trends.
  - Employee performance vs. stress levels.


## Contributing
Contributions are welcome! Feel free to submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


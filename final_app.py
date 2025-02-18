import streamlit as st
import pickle
import numpy as np

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Employee Stress Prediction", layout="wide")

# Load the model from the pickle file
with open("rf_model.pkl", "rb") as file:
    model = pickle.load(file)


# CSS for custom background and sidebar toggle
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: white;
            color: black;
            font-size: 16px;
            border: 1px solid black;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #e0e0e0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for page control
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar
with st.sidebar:
    st.title("Navigation")
    if st.button("Home"):
        st.session_state.page = "Home"
    if st.button("About"):
        st.session_state.page = "About"
    if st.button("Predictions"):
        st.session_state.page = "Predictions"


# Home Page
def home_page():
    st.title("Welcome to Employee Stress Prediction")
    st.image("background.jpg", use_column_width=True)
    st.markdown("""
        ### Explore Insights into Workplace Stress
        Workplace stress affects employee productivity, well-being, and overall job satisfaction. This application uses advanced machine learning models to predict stress levels based on various workplace and personal factors.

        #### Why Stress Prediction Matters:
        - **Increased Productivity**: Understanding stress helps organizations create better work environments.
        - **Improved Well-being**: Identifying stressors allows for timely interventions.
        - **Reduced Turnover**: A healthy work environment reduces employee churn and absenteeism.

        #### Features:
        - **Data-Driven Insights**: Leverage data to predict stress levels.
        - **Simple and Intuitive**: Easy-to-use interface for everyone.
        - **Actionable Results**: Helps managers make informed decisions to reduce workplace stress.
    """)


# About Page
def about_page():
    st.title("About Employee Stress Prediction")
    st.image("background.jpg", use_column_width=True)
    st.markdown("""
        ### Understanding Employee Stress
        Employee stress is a growing concern in modern workplaces. This application aims to help organizations identify stress levels among their employees and take corrective actions.

        #### Factors Influencing Stress:
        - **Work-Life Balance**: Employees with a poor work-life balance are more prone to stress.
        - **Workload**: High workloads often lead to burnout.
        - **Physical Activity**: Lack of physical activity negatively impacts mental health.
        - **Sleep Patterns**: Insufficient sleep contributes to heightened stress levels.

        #### How This Application Helps:
        - **Improved Employee Engagement**: By identifying stress, organizations can boost employee morale.
        - **Custom Insights**: Predict stress based on unique inputs like workload, sleep hours, and job satisfaction.
        - **Data Visualization**: Gain actionable insights through visualized results.
    """)


# Predictions Page
def prediction_page():
    st.title("Predict Employee Stress")
    st.markdown("### Enter the following details to predict stress:")

    # Input fields (in the correct order)
    department = st.selectbox(
        "Department",
        [
            "Sales & Marketing",
            "Operations",
            "Technology",
            "Procurement",
            "Analytics",
            "Finance",
            "HR",
            "Legal",
            "R&D",
        ],
    )

    education = st.selectbox(
        "Education", ["Bachelor's", "Master's & above", "Below secondary"]
    )

    gender = st.selectbox("Gender", ["male", "female"])

    recruitment_channel = st.selectbox(
        "Recruitment Channel", ["other", "sourcing", "referred"]
    )

    training_time = st.number_input("Training Time", min_value=1, max_value=10, step=1)
    age = st.number_input("Age", min_value=20, max_value=60, step=1)
    performance_rating = st.number_input(
        "Performance Rating", min_value=1, max_value=6, step=1
    )
    years_at_company = st.number_input(
        "Years at Company", min_value=1, max_value=34, step=1
    )
    working_hours = st.number_input(
        "Working Hours per Week", min_value=4, max_value=10, step=1
    )
    flexible_timings = st.selectbox("Flexible Timings", ["yes", "no"])
    workload_level = st.selectbox("Workload Level", ["low", "high"])
    monthly_income = st.number_input(
        "Monthly Income", min_value=18000, max_value=89000, step=100
    )
    work_satisfaction = st.selectbox("Work Satisfaction", ["yes", "no"])
    percent_salary_hike = st.number_input(
        "Percent Salary Hike", min_value=8, max_value=525, step=1
    )
    companies_worked = st.number_input(
        "Companies Worked", min_value=1, max_value=8, step=1
    )
    marital_status = st.selectbox("Marital Status", ["yes", "no"])

    # Mappings for categorical variables
    department_mapping = {
        "Sales & Marketing": 7,
        "Operations": 4,
        "Technology": 8,
        "Procurement": 5,
        "Analytics": 0,
        "Finance": 1,
        "HR": 2,
        "Legal": 3,
        "R&D": 6,
    }

    education_mapping = {"Bachelor's": 0, "Master's & above": 2, "Below secondary": 1}
    gender_mapping = {"male": 1, "female": 0}
    recruitment_channel_mapping = {"other": 0, "sourcing": 2, "referred": 1}
    flexible_timings_mapping = {"yes": 1, "no": 0}
    workload_level_mapping = {"low": 1, "high": 0}
    work_satisfaction_mapping = {"yes": 1, "no": 0}
    marital_status_mapping = {"yes": 1, "no": 0}

    # Encoding the inputs (in the correct order)
    department_encoded = department_mapping[department]
    education_encoded = education_mapping[education]
    gender_encoded = gender_mapping[gender]
    recruitment_channel_encoded = recruitment_channel_mapping[recruitment_channel]
    flexible_timings_encoded = flexible_timings_mapping[flexible_timings]
    workload_level_encoded = workload_level_mapping[workload_level]
    work_satisfaction_encoded = work_satisfaction_mapping[work_satisfaction]
    marital_status_encoded = marital_status_mapping[marital_status]

    # Create input array for prediction (correct order)
    input_data = np.array(
        [
            [
                department_encoded,  # department
                education_encoded,  # education
                gender_encoded,  # gender
                recruitment_channel_encoded,  # recruitment_channel
                training_time,  # Training_Time
                age,  # age
                performance_rating,  # Prformance_Rating
                years_at_company,  # Years_at_company
                working_hours,  # Working_Hours
                flexible_timings_encoded,  # Flexible_Timings
                workload_level_encoded,  # Workload_level
                monthly_income,  # Monthly_Income
                work_satisfaction_encoded,  # Work_Satisfaction
                percent_salary_hike,  # Percent_salary_hike
                companies_worked,  # companies_worked
                marital_status_encoded,  # Marital_Status
            ]
        ]
    )

    if st.button("Predict Stress Status"):
        # Make prediction and calculate probabilities
        prediction = model.predict(input_data)
        pred = int(prediction)
        prediction_proba = model.predict_proba(input_data)[0]

        st.write("Prediction:", pred)
        st.write(prediction_proba)
        # Show debug info (optional)

        # Classify based on probability threshold
        if prediction_proba[1] >= 0.5:
            stress_status = "Yes"
        else:
            stress_status = "No"

        # Display result
        st.markdown(f"### Predicted Stress Status: **{stress_status}**")

        # Optionally show prediction probabilities
        st.markdown(
            f"Prediction Probabilities: [No: {prediction_proba[0]:.4f}, Yes: {prediction_proba[1]:.4f}]"
        )


# Display the appropriate page
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "About":
    about_page()
elif st.session_state.page == "Predictions":
    prediction_page()

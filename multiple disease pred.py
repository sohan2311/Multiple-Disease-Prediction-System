import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


diabetes_model_path = "/Users/sohanmaity/Desktop/ML - Projects/Project/Multiple Disease Prediction System/saved models/diabetes_model.sav"
heart_disease_model_path = "/Users/sohanmaity/Desktop/ML - Projects/Project/Multiple Disease Prediction System/saved models/heart_disease_model.sav"
parkinsons_model_path = "/Users/sohanmaity/Desktop/ML - Projects/Project/Multiple Disease Prediction System/saved models/parkinsons_model.sav"


with open(diabetes_model_path, 'rb') as f:
    diabetes_model = pickle.load(f)

with open(heart_disease_model_path, 'rb') as f:
    heart_disease_model = pickle.load(f)

with open(parkinsons_model_path, 'rb') as f:
    parkinsons_model = pickle.load(f)


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0)

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0)

    with col3:
        BMI = st.number_input('BMI value', min_value=0.0, format="%.2f")

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.3f")

    with col2:
        Age = st.number_input('Age of the Person', min_value=0, step=1)

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness,
                          Insulin, BMI, DiabetesPedigreeFunction, Age]
            diab_prediction = diabetes_model.predict([user_input])

            diab_diagnosis = '🩸 The person **is diabetic**' if diab_prediction[0] == 1 else '✅ The person **is not diabetic**'

        except Exception as e:
            diab_diagnosis = f'❌ Error occurred: {e}'

    st.success(diab_diagnosis)



if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex_input = st.selectbox('Sex', options=['Male', 'Female'])

    with col3:
        cp_input = st.selectbox('Chest Pain types', options=[
            'Typical Angina (0)', 'Atypical Angina (1)', 'Non-anginal Pain (2)', 'Asymptomatic (3)'
        ])

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')

    with col3:
        fbs_input = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['Yes', 'No'])

    with col1:
        restecg_input = st.selectbox('Resting Electrocardiographic results', options=[
            'Normal (0)', 'Having ST-T wave abnormality (1)', 'Left ventricular hypertrophy (2)'
        ])

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang_input = st.selectbox('Exercise Induced Angina', options=['Yes', 'No'])

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope_input = st.selectbox('Slope of peak exercise ST segment', options=[
            'Upsloping (0)', 'Flat (1)', 'Downsloping (2)'
        ])

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0–3)')

    with col1:
        thal_input = st.selectbox('Thalassemia', options=[
            'Normal (0)', 'Fixed Defect (1)', 'Reversable Defect (2)'
        ])

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            # Map inputs
            sex = 1 if sex_input == 'Male' else 0
            cp = ['Typical Angina (0)', 'Atypical Angina (1)', 'Non-anginal Pain (2)', 'Asymptomatic (3)'].index(cp_input)
            fbs = 1 if fbs_input == 'Yes' else 0
            restecg = ['Normal (0)', 'Having ST-T wave abnormality (1)', 'Left ventricular hypertrophy (2)'].index(restecg_input)
            exang = 1 if exang_input == 'Yes' else 0
            slope = ['Upsloping (0)', 'Flat (1)', 'Downsloping (2)'].index(slope_input)
            thal = ['Normal (0)', 'Fixed Defect (1)', 'Reversable Defect (2)'].index(thal_input)

            user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg,
                                             thalach, exang, oldpeak, slope, ca, thal]]
            heart_prediction = heart_disease_model.predict([user_input])

            heart_diagnosis = 'The person **has** heart disease 💔' if heart_prediction[0] == 1 else 'The person **does NOT have** heart disease ❤️'

        except ValueError:
            heart_diagnosis = '❌ Please enter valid numeric values for all fields.'

    st.success(heart_diagnosis)


if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    inputs = {}
    input_labels = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]


    for i, label in enumerate(input_labels):
        col = [col1, col2, col3, col4, col5][i % 5]
        with col:
            inputs[label] = st.number_input(label, format="%.6f")

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        try:
            user_input = [float(inputs[label]) for label in input_labels]
            parkinsons_prediction = parkinsons_model.predict([user_input])

            parkinsons_diagnosis = (
                "🧠 The person **has** Parkinson's disease" if parkinsons_prediction[0] == 1 
                else "✅ The person **does NOT have** Parkinson's disease"
            )

        except ValueError:
            parkinsons_diagnosis = '❌ Please enter valid numeric values for all fields.'

    st.success(parkinsons_diagnosis)


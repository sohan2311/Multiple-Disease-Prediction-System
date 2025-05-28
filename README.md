
# Multiple Disease Prediction System

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/4333/4333609.png" alt="Doctor Icon" width="150" />
</p>

A **Streamlit** web app for predicting **Diabetes**, **Heart Disease**, and **Parkinson's Disease** using machine learning models.  
This tool allows users to input medical parameters and receive disease prediction results instantly.

---

## Features

- Predict Diabetes based on clinical features like glucose, BMI, age, etc.
- Predict Heart Disease using standard cardiovascular health metrics.
- Predict Parkinson's Disease from vocal and speech signal features.
- Interactive and user-friendly UI built with Streamlit.
- Uses pre-trained models saved with pickle.

---

## Demo (Localhost)

To run the app locally and access the web interface, use this URL in your browser after starting the Streamlit app:

[http://localhost:8501](http://localhost:8501)

---

## Dataset Links

Here are the datasets used for training the models (publicly available):

| Disease         | Dataset Name & Source                             | Link                                                |
|-----------------|-------------------------------------------------|-----------------------------------------------------|
| Diabetes        | Pima Indians Diabetes Dataset (Kaggle)           | [Diabetes Dataset](https://drive.google.com/file/d/1DQa_LDAzedAfVGEaKoPSlug0dbwzXmsC/view?usp=sharing) |
| Heart Disease   | Cleveland Heart Disease Dataset (UCI Machine Learning Repository) | [Heart Disease Dataset](https://drive.google.com/file/d/1b4YKL6ra3LQdRfc0FP9AS_fD8OpGqkD1/view?usp=sharing)          |
| Parkinson's     | Parkinson's Disease Dataset (UCI Machine Learning Repository)    | [Parkinson's Dataset](https://drive.google.com/file/d/1OB8YsOUK9UlYCSFa3RggNEAFtUtzDIQc/view?usp=sharing)               |

---

## Project Structure

```

.
├── multiple\_disease\_pred.py        # Main Streamlit app script
├── saved models/
│   ├── diabetes\_model.sav          # Pickled diabetes prediction model
│   ├── heart\_disease\_model.sav     # Pickled heart disease prediction model
│   └── parkinsons\_model.sav        # Pickled Parkinson's disease prediction model
├── README.md                       # This documentation file
└── requirements.txt                # Python dependencies file

````

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/multiple-disease-prediction.git
cd multiple-disease-prediction
````

2. **Create a virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**

```bash
streamlit run multiple_disease_pred.py
```

5. Open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## Dependencies

* Python 3.7+
* streamlit
* streamlit-option-menu
* scikit-learn
* numpy
* pandas (if required by models)

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## Usage

* Select the disease prediction type from the sidebar menu.
* Enter the required health parameters in the input fields.
* Click the respective prediction button to get the result.
* Input validation checks ensure numeric data entry.

---

## Contributing

Contributions and suggestions are welcome! Feel free to open issues or pull requests.

---

## License

This project is licensed under the MIT License.

---

## Contact

Created by [Sohan Maity](https://github.com/sohan2311) – feel free to reach out for questions or collaborations!

---

## Acknowledgements

* [Streamlit](https://streamlit.io/)
* Datasets from [Kaggle](https://www.kaggle.com/) and [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
* Icons from [Icons8](https://icons8.com)

---

**Enjoy predicting health outcomes with ease! 🩺**



---




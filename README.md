# Traffic Volume Prediction Using Decision Tree

A Machine Learning web application that predicts traffic volume as **Low, Medium, or High** based on historical traffic observations.

The project uses a **Decision Tree Classifier** with an interactive **Streamlit** interface. Users can upload a CSV dataset, train the model, and enter a new traffic observation to obtain a prediction.

## Project Overview

Traffic conditions can vary depending on factors such as time, day, weather, and the number of vehicles on the road.

This project applies a basic Machine Learning learning process to historical traffic data:

```text
Historical Data
      |
      v
Training
      |
      v
Decision Tree Model
      |
      v
New Observation
      |
      v
Prediction
```

The system learns traffic patterns from the uploaded dataset and predicts the traffic level for a new observation.

## Objective

* Predict traffic volume as Low, Medium, or High.
* Apply the basic stages of a Machine Learning learning algorithm.
* Use historical traffic observations for model training.
* Provide an interactive web interface using Streamlit.
* Demonstrate prediction using a new traffic observation.

## Machine Learning Algorithm

### Decision Tree Classifier

A Decision Tree is a supervised Machine Learning algorithm used for classification.

In this project, the model learns decision rules from:

* Hour
* Day
* Weather
* Vehicles

The target variable is:

* Traffic: Low, Medium, or High

Example decision process:

```text
             Vehicles > 60?
              /          \
            YES           NO
             |             |
             v             v
          Weather?        LOW
          /      \
         /        \
      Rainy      Clear
        |           |
        v           v
       HIGH       MEDIUM
```

## Dataset

The dataset contains historical traffic observations.

### Input Features

| Feature  | Description        |
| -------- | ------------------ |
| Hour     | Hour of the day    |
| Day      | Day of the week    |
| Weather  | Weather condition  |
| Vehicles | Number of vehicles |

### Target

| Target  | Description                         |
| ------- | ----------------------------------- |
| Traffic | Traffic level: Low, Medium, or High |

### Sample Data

```csv
Hour,Day,Weather,Vehicles,Traffic
7,Monday,Clear,35,Low
8,Monday,Clear,55,Medium
9,Monday,Rainy,75,High
10,Tuesday,Clear,30,Low
11,Tuesday,Cloudy,45,Medium
17,Friday,Clear,80,High
18,Friday,Clear,95,High
```

## How the System Works

### 1. Upload Dataset

The user uploads a CSV file through the Streamlit interface.

### 2. Data Preprocessing

Categorical values such as `Day`, `Weather`, and `Traffic` are converted into numerical values using Label Encoding.

### 3. Model Training

The Decision Tree Classifier learns patterns from the historical dataset.

```python
model.fit(X, y)
```

### 4. Enter New Observation

The user provides:

```text
Hour
Day
Weather
Number of Vehicles
```

### 5. Prediction

The trained Decision Tree processes the new observation and predicts one of the following:

```text
LOW
MEDIUM
HIGH
```

## Application

The project uses Streamlit to provide an interactive web interface.

The application allows users to:

* Upload a traffic CSV dataset.
* View the uploaded dataset.
* Train the Decision Tree model.
* Enter a new traffic observation.
* Predict the traffic level.
* Display the prediction result.

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Decision Tree Classifier
* Label Encoding

## Project Structure

```text
traffic-volume-prediction/
|
├── Main.py
├── traffic_data.csv
├── requirements.txt
├── README.md
|
└── PPT/
    └── Traffic_Volume_Prediction.pptx
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/traffic-volume-prediction.git
```

### 2. Open the Project Folder

```bash
cd traffic-volume-prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the required libraries manually:

```bash
pip install streamlit pandas scikit-learn
```

## Run the Application

Run the following command:

```bash
streamlit run Main.py
```

Alternatively:

```bash
python -m streamlit run Main.py
```

The Streamlit application will open in the web browser.

## Example Prediction

### New Observation

```text
Hour      = 18
Day       = Friday
Weather   = Clear
Vehicles  = 90
```

### Output

```text
Traffic Volume: HIGH
```

## Learning Process

```text
Historical Traffic Dataset
          |
          v
Data Preprocessing
          |
          v
Input Features
          |
          v
Decision Tree Training
          |
          v
Trained Model
          |
          v
New Traffic Observation
          |
          v
Prediction
          |
          v
Low / Medium / High
```

## Advantages

* Simple and easy to understand.
* Suitable for classification problems.
* Requires no hardware components.
* Provides an interactive web interface.
* Easy to train using a CSV dataset.
* Provides quick traffic predictions.

## Limitations

* Prediction quality depends on the available historical data.
* Sudden traffic changes may not be predicted accurately.
* Unexpected events such as accidents or road closures are not included.
* A larger and more diverse dataset can improve the learning process.

## Future Enhancements

Possible future improvements include:

* Real-time traffic data integration.
* Larger traffic datasets.
* Weather API integration.
* Traffic visualization and analytics.
* Comparison with other Machine Learning algorithms.
* Traffic prediction for multiple future time periods.

## Academic Information

**Project:** Traffic Volume Prediction Using Machine Learning
**Algorithm:** Decision Tree Classifier
**Interface:** Streamlit
**Domain:** Artificial Intelligence and Machine Learning

## License

This project is developed for educational and academic purposes.

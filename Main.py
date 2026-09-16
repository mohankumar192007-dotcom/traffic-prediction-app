import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

st.title("🚦 Traffic Volume Prediction")
st.write("Learning Model using Decision Tree")

# Upload dataset
file = st.file_uploader("Upload Traffic Dataset (CSV)", type=["csv"])

if file is not None:

    # Read dataset
    data = pd.read_csv(file)

    st.subheader("Uploaded Dataset")
    st.dataframe(data)

    # Check required columns
    required = ["Hour", "Day", "Weather", "Vehicles", "Traffic"]

    if all(col in data.columns for col in required):

        # Copy data
        df = data.copy()

        # Encode categorical columns
        day_encoder = LabelEncoder()
        weather_encoder = LabelEncoder()
        traffic_encoder = LabelEncoder()

        df["Day"] = day_encoder.fit_transform(df["Day"])
        df["Weather"] = weather_encoder.fit_transform(df["Weather"])
        df["Traffic"] = traffic_encoder.fit_transform(df["Traffic"])

        # Input and Target
        X = df[["Hour", "Day", "Weather", "Vehicles"]]
        y = df["Traffic"]

        # Train model
        model = DecisionTreeClassifier(random_state=42)
        model.fit(X, y)

        st.success("Model trained successfully!")

        # User input
        st.subheader("Enter New Traffic Observation")

        hour = st.number_input(
            "Hour",
            min_value=0,
            max_value=23,
            value=8
        )

        day = st.selectbox(
            "Day",
            day_encoder.classes_
        )

        weather = st.selectbox(
            "Weather",
            weather_encoder.classes_
        )

        vehicles = st.number_input(
            "Number of Vehicles",
            min_value=0,
            value=50
        )

        # Prediction
        if st.button("Predict Traffic"):

            day_value = day_encoder.transform([day])[0]
            weather_value = weather_encoder.transform([weather])[0]

            new_data = [[
                hour,
                day_value,
                weather_value,
                vehicles
            ]]

            prediction = model.predict(new_data)

            result = traffic_encoder.inverse_transform(prediction)[0]

            st.subheader("Prediction Result")

            if result.lower() == "high":
                st.error("🚨 Traffic Volume: HIGH")

            elif result.lower() == "medium":
                st.warning("⚠️ Traffic Volume: MEDIUM")

            else:
                st.success("✅ Traffic Volume: LOW")

    else:
        st.error(
            "Dataset must contain: "
            "Hour, Day, Weather, Vehicles, Traffic"
        )
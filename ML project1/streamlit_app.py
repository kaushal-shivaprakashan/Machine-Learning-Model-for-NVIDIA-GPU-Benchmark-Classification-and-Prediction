import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('/Users/kaushalshivaprakash/Desktop/ML project1/best_model.joblib')

# Load the GPU data from the CSV file
gpu_data = pd.read_csv('/Users/kaushalshivaprakash/Desktop/ML project1/GPU_benchmarks1.csv')

# Define the mapping of prediction output to category names
category_mapping = {
    0: "Desktop",
    1: "Mobile",
    2: "Workstation"
}

# Title and description for the app
st.title("GPU Classification App")
st.write("Predict the category of a GPU based on its specifications.")

# Input fields for user to enter GPU specifications
G3Dmark = st.number_input("G3Dmark", min_value=0)
G2Dmark = st.number_input("G2Dmark", min_value=0)
gpuValue = st.number_input("GPU Value", min_value=0.0)
TDP = st.number_input("TDP (Watts)", min_value=0)
powerPerformance = st.number_input("Power Performance", min_value=0.0)

# Calculating additional features
performance_per_dollar = G3Dmark / gpuValue if gpuValue else 0
performance_per_watt = G3Dmark / TDP if TDP else 0

# Prediction button
if st.button("Predict"):
    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame({
        'G3Dmark': [G3Dmark],
        'G2Dmark': [G2Dmark],
        'gpuValue': [gpuValue],
        'TDP': [TDP],
        'powerPerformance': [powerPerformance],
        'performance_per_dollar': [performance_per_dollar],
        'performance_per_watt': [performance_per_watt],
        # Adding missing columns with placeholder values
        'price': [0.0],  # Replace with an estimated or default price if available
        'category_name': ['Unknown']  # Replace with an appropriate category if available
    })

    try:
        # Make a prediction using the pre-trained model
        prediction = model.predict(input_data)
        # Map prediction to category name
        predicted_category = category_mapping.get(prediction[0], "Unknown")
        st.write(f"Predicted Category: {predicted_category}")
    except ValueError as e:
        st.error(f"Prediction failed: {e}")
        st.stop()

    # Find the closest matching GPU based on G3Dmark
    closest_gpu = gpu_data.iloc[(gpu_data['G3Dmark'] - G3Dmark).abs().argsort()[:1]]

    # Display the closest matching GPU details
    if not closest_gpu.empty:
        st.write(f"Closest matching GPU: {closest_gpu.iloc[0]['gpuName']}")
        st.write(f"Price: ${closest_gpu.iloc[0]['price']:.2f}")
    else:
        st.write("No matching GPU found in the dataset.")

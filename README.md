# GPU Performance Analysis and Model Deployment

## Project Overview
This project showcases a comprehensive workflow to analyze GPU performance and deploy machine learning models for real-time predictions. The dataset used contains specifications for over 2,300 GPUs, spanning categories like Desktop, Mobile, and Workstation.

## Workflow Steps

### 1. Data Selection
- Selected a relevant GPU dataset from Kaggle containing performance metrics and specifications for GPUs.

### 2. Data Preprocessing
- Conducted thorough data cleaning and preprocessing to ensure quality and consistency of the dataset.

### 3. ML Pipeline for Classification
- Built a machine learning pipeline for classification tasks.
- Logged results in DagsHub MLflow for tracking and reproducibility.

### 4. ML Pipeline for Prediction
- Developed a separate ML pipeline for prediction tasks.
- Stored logs in DagsHub MLflow to ensure detailed tracking.

### 5. Feature Engineering
- Performed feature engineering to enhance model performance and uncover meaningful relationships within the data.

### 6. FastAPI Application
- Created a FastAPI application to serve the trained models, enabling real-time predictions.

### 7. Containerization
- Containerized the FastAPI application using Docker.
- Pushed the container image to Docker Hub for seamless deployment.

### 8. Cloud Deployment
- Deployed the containerized API to a cloud platform, ensuring scalability and global accessibility.

### 9. Streamlit Application
- Developed a Streamlit app to provide an interactive interface for users to:
  - Interact with the deployed model.
  - Perform real-time classification and predictions.

## Dataset Overview

### Attributes
- **gpuName:**
  - The name or model of the GPU, e.g., 'GeForce RTX 3090 Ti' (high-end) to entry-level models.

- **G3Dmark:**
  - A benchmark score for 3D graphics performance.
  - Ranges from ~29,000 (high-end GPUs) to ~2,000 (older models).

- **G2Dmark:**
  - A score for 2D graphics performance.
  - Typically ranges from 400-900.

- **Price:**
  - GPU cost in USD at the time of testing.
  - Ranges from ~$200 (budget GPUs) to over $4,000 (enterprise-grade GPUs).

- **gpuValue:**
  - Performance per dollar metric.
  - Calculated as: G3Dmark / Price.
  - Highlights price-performance efficiency.

- **TDP (Thermal Design Power):**
  - Represents power consumption and heat dissipation.
  - Ranges from 35W (mobile GPUs) to 450W (high-end desktop GPUs).

- **powerPerformance:**
  - Performance per watt metric.
  - Calculated as: G3Dmark / TDP.
  - Mobile GPUs often excel in this metric due to power optimizations.

- **testDate:**
  - The year the GPU was benchmarked.
  - Covers the years 2010 to 2022, showing performance trends over time.

- **Category:**
  - Market segment or intended use of the GPU.
  - Categories include Desktop, Mobile, Workstation, or combinations like 'Mobile, Workstation.'

## Project Highlights

- Comprehensive ML pipelines for classification and prediction.
- Reproducible workflows with DagsHub MLflow logging.
- Real-time model serving with FastAPI.
- Docker-based containerization for easy deployment.
- Scalable and globally accessible cloud deployment.
- User-friendly interface via Streamlit for real-time interactions.

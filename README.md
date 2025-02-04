# Image Classification with AWS SageMaker for Scones Unlimited

This repository contains the solution for the AWS AI/ML Scholarship Program Nanodegree project, "AWS Machine Learning Fundamentals". In this project, an image classification model was built to identify vehicle types (bicycles and motorcycles) for a scone-delivery-focused logistics company, Scones Unlimited. The project demonstrates designing, training, deploying, and monitoring an ML model using AWS SageMaker along with AWS Lambda functions and AWS Step Functions to compose a full ML-enabled workflow.

--------------------------------------------------

## Table of Contents

- [Project Introduction](#project-introduction)
- [Project Overview](#project-overview)
- [Architecture and Workflow](#architecture-and-workflow)
- [Project Steps](#project-steps)
- [Review Highlights](#review-highlights)
- [License & Acknowledgments](#license--acknowledgments)

--------------------------------------------------

## Project Introduction
### Background
Image classification is a critical computer vision task with applications spanning autonomous vehicles, augmented reality, eCommerce, and even diagnostic medicine. For this project, Scones Unlimited, a scone-delivery-focused logistics company, leverages image classification to optimize its operations by routing delivery drivers based on their vehicle type.  
 
By building an image classification model capable of distinguishing between bicycles and motorcycles, the company can efficiently allocate orders: nearby orders for bicycle couriers and farther routes for motorcyclists. This not only improves operational efficiency but also reduces the chance of misrouting and delays.

### Project Goals
- Develop an end-to-end machine learning workflow.
- Train and deploy a scalable image classification model using AWS SageMaker.
- Integrate AWS Lambda functions and AWS Step Functions to create an event-driven application.
- Enable continuous monitoring using SageMaker Model Monitor with DataCaptureConfig.
- Provide a robust, production-ready demo that showcases the integration of ML and AWS services.

--------------------------------------------------

## Project Overview
The repository includes code and scripts for:
- Data extraction and transformation (ETL) along with staging data to Amazon S3.
- Training an image classification model on SageMaker.
- Deploying the trained model on a SageMaker endpoint and configuring DataCapture for ongoing monitoring.
- Creating three individual AWS Lambda functions to:
  1. Prepare and return image data.
  2. Invoke the image classification endpoint.
  3. Filter out low-confidence predictions.
- Orchestrating the Lambda functions using AWS Step Functions to build a full machine learning workflow.
- Testing and evaluating the model’s performance and visualizing output from the Model Monitor.

### File Structure
#### Key Files:
- `images/`: Contains workflow visualization and execution result screenshots
- `workflows/`: Step Function state machine definition (ASL JSON)
- `lambda.py`: Contains three Lambda handlers:
  1. **Data Generation**: Fetches images from S3
  2. **Image Classification**: Invokes SageMaker endpoint
  3. **Confidence Filter**: Validates prediction confidence
- `starter.ipynb`: Main notebook for data prep, model training, and monitoring

--------------------------------------------------

## Architecture and Workflow
1. **Data Staging:**  
   - Load images and metadata from a specified URL.
   - Transform and upload images to Amazon S3 for further processing.

2. **Model Training & Deployment:**  
   - Configure and initialize the "image-classification" estimator with parameters such as the ml.p3.2xlarge instance type.
   - Train the model and achieve a validation accuracy of 0.81 over 30 epochs.
   - Deploy the model on AWS SageMaker and configure model capture settings for ongoing monitoring.

3. **Lambda Functions & Step Functions:**  
   - Three Lambda functions are crafted to handle:
     - Data preparation.
     - Model inference.
     - Filtering of results based on a confidence threshold.
   - AWS Step Functions are used to orchestrate the execution of these functions, ensuring a modular and decoupled architecture.

4. **Monitoring & Evaluation:**  
   - Continuous monitoring of model performance via SageMaker Model Monitor.
   - Custom visualization of the captured data outputs for further analysis.

--------------------------------------------------

## Project Steps

### Step 1: Data Staging

- Retrieve the dataset from the provided URL.
- Transform the images as per model requirements.
- Upload the processed images to an S3 bucket for training.

### Step 2: Model Training and Deployment

- Create an image classification estimator with proper configuration using SageMaker.
- Train the model on the provided dataset and validate its performance.
- Deploy the trained model to a SageMaker endpoint.
- Configure DataCaptureConfig for continuous monitoring via SageMaker Model Monitor.

### Step 3: Lambda Functions and Step Function Workflow

- Develop three Python lambda functions to:
  1. Preprocess and return image data.
  2. Invoke the deployed SageMaker endpoint to get predictions.
  3. Filter low-confidence predictions to ensure high-quality inferences.
- Integrate these Lambda functions using AWS Step Functions into a coherent workflow, ensuring modularity and ease of debugging.

### Step 4: Testing and Evaluation

- Test the entire workflow by running sample images through the system.
- Validate the output from the SageMaker endpoint.
- Use custom visualizations to analyze captured data from the Model Monitor.

### Step 5: Cleanup Cloud Resources

- Follow the cleanup procedures to remove any AWS resources created during the project to avoid unwanted charges.

--------------------------------------------------

## Review Highlights

The project received positive feedback from the reviewer, highlighting key achievements:

- Successfully executed API calls to SageMaker, ensuring correct permissions and secure operations.
- Deployed the trained image classification model and demonstrated its inference capabilities on sample images.
- Configured DataCaptureConfig, enabling continuous monitoring with SageMaker Model Monitor.
- Constructed the "image-classification" estimator with optimal parameters and selected the appropriate ml.p3.2xlarge instance type.
- Implemented modular AWS Lambda functions combined with AWS Step Functions for an efficient, decoupled architecture.
- Demonstrated attention to detail by correctly identifying class labels for bicycles and motorcycles and successfully staging data on S3.
- Delivered custom visualizations for monitoring model performance, ensuring ongoing insights into production quality.

--------------------------------------------------

## License & Acknowledgments

**Educational Context**  
This project was completed as part of the [AWS AI/ML Scholarship Program](https://www.udacity.com/scholarships/aws-ai-ml-scholarship-program) Nanodegree through Udacity. The project requirements, starter code, and learning framework were provided by Udacity and AWS.

**Code Licensing**  
Original project infrastructure and specifications are Udacity/AWS intellectual property.  
Code written by the student contributor (implementation details in `lambda.py`, workflow configurations, and monitoring logic) is made available under the **[Apache License 2.0](LICENSE)** to align with AWS sample code practices.

**Gratitude**  
Special thanks to:
- 🚀 **AWS AI/ML Scholarship Program** for providing platform access and cloud resources
- 🧑💻 **Udacity Reviewers** for detailed feedback and guidance
- 🌐 **AWS Community** for documentation, forums, and technical support

--------------------------------------------------
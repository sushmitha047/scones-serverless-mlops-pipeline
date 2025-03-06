# Image Classification with AWS SageMaker for Vehicle Type Identification

An end-to-end machine learning workflow that identifies bicycles and motorcycles for Scones Unlimited's delivery operations using AWS SageMaker, Lambda functions, and Step Functions.

## Project Overview

This project demonstrates how to build, deploy, and monitor an image classification model that distinguishes between bicycles and motorcycles to optimize delivery routing. By correctly identifying vehicle types, Scones Unlimited can efficiently allocate orders: nearby deliveries to bicycle couriers and farther routes to motorcyclists.

### Key Technologies
- AWS SageMaker
- AWS Lambda
- AWS Step Functions
- SageMaker Model Monitor

## Key Components

### Model Training and Deployment
- CNN-based image classification using SageMaker's built-in algorithm
- Trained on bicycle and motorcycle images from CIFAR-100 dataset
- 81% validation accuracy over 30 epochs
- Deployed to SageMaker endpoint with monitoring enabled
- Training: `ml.p3.2xlarge`, Deployment: `ml.m5.xlarge`

### Data Preparation
- Extracted relevant images from CIFAR-100
- Transformed 3073 unsigned integers per image into 32x32x3 RGB arrays
- Saved as PNG files with TSV metadata
- Uploaded to S3 for training

### Serverless Workflow
Three Lambda functions in a Step Functions workflow:
1. **Data Generation**: S3 image retrieval and preparation
2. **Image Classification**: SageMaker endpoint invocation
3. **Confidence Filter**: 75% threshold validation

## Implementation Details

### Model Configuration
SageMaker estimator configured with SageMaker's built-in algorithm image URI, instance type, and output path. Proper IAM role and SageMaker session specified.

### Monitoring Setup
DataCaptureConfig set to capture 100% of requests/responses, storing data in S3 for analysis.

## Results and Evaluation

The model successfully:
- Distinguishes vehicles with high confidence
- Routes low-confidence predictions for review
- Provides ongoing performance insights
- Maintains 75% production confidence threshold

## Repository Structure

- `starter.ipynb`: Main notebook for data preparation, model training, and monitoring
- `lambda.py`: Lambda function handlers
- `images/`: Contains workflow visualization and execution result screenshots
- `workflows/`: Step Function state machine definition (ASL JSON)

## Review Highlights

The project received positive feedback from the reviewer, highlighting key achievements:

- Successfully executed API calls to SageMaker, ensuring correct permissions and secure operations.
- Deployed the trained image classification model and demonstrated its inference capabilities on sample images.
- Configured DataCaptureConfig, enabling continuous monitoring with SageMaker Model Monitor.
- Constructed the "image-classification" estimator with optimal parameters and selected the appropriate ml.p3.2xlarge instance type.
- Implemented modular AWS Lambda functions combined with AWS Step Functions for an efficient, decoupled architecture.
- Demonstrated attention to detail by correctly identifying class labels for bicycles and motorcycles and successfully staging data on S3.
- Delivered custom visualizations for monitoring model performance, ensuring ongoing insights into production quality.

## License & Acknowledgments

**Educational Context**  
This project was completed as part of the [AWS AI/ML Scholarship Program](https://www.udacity.com/scholarships/aws-ai-ml-scholarship-program) Nanodegree through Udacity. The project requirements, starter code, and learning framework were provided by Udacity and AWS.

**Intellectual Property**  
- Project specifications and requirements are **Udacity/AWS intellectual property**.  
- Student implementations in [`starter.ipynb`](/starter.ipynb), [`lambda.py`](/lambda.py), and workflow configurations are shared for **portfolio demonstration purposes only**. 

**Usage Rights**  
As per scholarship guidelines:
- You may showcase this work in portfolios/job applications
- Commercial use requires written permission from Udacity/AWS
- Udacity/AWS retain all rights to project structure and evaluation criteria

**Gratitude**  
Special thanks to:
- 🚀 **AWS AI/ML Scholarship Program** for providing platform access and cloud resources
- 🧑💻 **Udacity Reviewers** for detailed feedback and guidance
- 🌐 **AWS Community** for documentation, forums, and technical support
# data-generation-lambda
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    print("Received event:", json.dumps(event, indent=2))
    
    key = event.get('s3_key')  
    bucket = event.get('s3_bucket')  
    
    # Check if key and bucket are present
    if not key or not bucket:
        print(f"Key: {key}, Bucket: {bucket}")  
        raise ValueError("Missing 's3_key' or 's3_bucket' in event")

    try:
        s3.download_file(bucket, key, '/tmp/image.png')  
    except Exception as e:
        raise RuntimeError(f"Failed to download file from S3: {str(e)}")

    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')  

    return {
        'statusCode': 200,
        'body': {
            "s3_bucket": bucket,
            "s3_key": key,
            "image_data": image_data,
            "inferences": []
        }
    }



# image-classification-lambda
import json
import base64
import boto3

# Fill this in with the name of the deployed model endpoint
ENDPOINT = "image-classification-2024-10-15-07-04-31-716"

runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data from the event
    image = base64.b64decode(event["body"]["image_data"])
    
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="image/png",  
        Body=image
    )
    
    inferences = json.loads(response['Body'].read().decode())
        
    event["body"]["inferences"] = inferences
    
    return {
        'statusCode': 200,
        'body': event["body"]
    }



# filter-low-confidence-lambda
import json

# Define a threshold for confidence
THRESHOLD = 0.75

def lambda_handler(event, context):
    
    # Ensure 'body' exists and is already a dictionary
    if isinstance(event.get("body"), str):
        body = json.loads(event["body"])  # Convert to dict if it's a string
    else:
        body = event.get("body", {})
    
    # Extract 'inferences' from body
    inferences = body.get("inferences", None)
    
    # Raise an error if 'inferences' is missing
    if inferences is None:
        raise KeyError("The 'inferences' key is missing from the event object.")
    
    # Check if any values in our inferences are above the THRESHOLD
    meets_threshold = any(float(inference) >= THRESHOLD for inference in inferences)
    
    # If our threshold is met, pass the data back out of the Step Function
    if meets_threshold:
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
    else:
        # If no inference meets the threshold, raise an error
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")


import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='555',
    aws_secret_access_key='555',
    region_name='us-east-1'  # Replace with your desired region
)

# Create an S3 client
s3 = session.client('s3')

# Specify the bucket and folder (prefix) path
bucket_name = 'ediscovery-dataset'
folder_path = 'dev_customer/dev_space/documents/'

# List all objects in the specified folder
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)

# Clear the existing content of the text file
with open('uploadScripts\\b_CheckFilesPresentinS3\\document_names.txt', 'w') as file:
    file.write('')

# Extract and print the document names
with open('uploadScripts\\b_CheckFilesPresentinS3\\document_names.txt', 'a') as file:
    for obj in response['Contents']:
        # Extract the document name from the full object key
        doc_name = obj['Key'].split('/')[-1]
        file.write(doc_name + '\n')
        print(doc_name)

import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
    region_name='us-east-1'  # Replace with your desired region
)

# Create an S3 client
s3 = session.client('s3')


def read_names_from_file(file_path):
    names = []
    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip()
            names.append(name)
    return names


def copy_file(source_bucket, source_path, destination_bucket, destination_path, file_name):
    source_key = source_path + file_name
    destination_key = destination_path + file_name

    try:
        # Copy the file to the destination path
        s3.copy_object(
            Bucket=destination_bucket,
            CopySource={'Bucket': source_bucket, 'Key': source_key},
            Key=destination_key
        )
        print(f"Copied: {source_key} -> {destination_key}")

        # Start execution and wait for completion
        execution_arn = start_state_machine_execution(
            state_machine_arn, {'documentKey': destination_key})
        print(f"Started execution with ARN: {execution_arn}")

        while True:
            status = check_execution_status(execution_arn)
            if status == 'SUCCEEDED':
                print(f"Ingested: {destination_key}")
                break
            elif status == 'FAILED':
                print(f"Execution failed for document: {destination_key}")
                break
            elif status == 'RUNNING':
                print(
                    f"Execution is still running for document: {destination_key}")
                time.sleep(10)  # Wait for 10 seconds before checking again
            else:
                print("Execution status:", status)
                break

    except Exception as e:
        print(f"Error occurred for document: {destination_key}")
        print(e)


def copy_files_in_pairs(filelist, source_bucket, source_path, destination_bucket, destination_path):
    num_files = len(filelist)
    if num_files % 2 != 0:
        print("Error: Number of files should be even for copying in pairs.")
        return

    for i in range(0, num_files, 2):
        file1 = filelist[i]
        file2 = filelist[i+1]

        copy_file(source_bucket, source_path,
                  destination_bucket, destination_path, file1)
        copy_file(source_bucket, source_path,
                  destination_bucket, destination_path, file2)


# Specify the source and destination details
source_bucket_name = 'ediscovery-dataset'
source_path = 'dev_customer/dev_space/documents/'

destination_bucket_name = 'ediscovery-dataset'
destination_path = 'dev_customer/esw_space/documents/'

state_machine_arn = 'arn:aws:states:us-east-1:123456789012:stateMachine:MyStateMachine'

filelist_path = 'uploadScripts/d_MoveFilesToSpace/intersection.txt'
filelist = read_names_from_file(filelist_path)

# Copy files in pairs and ingest them
copy_files_in_pairs(filelist, source_bucket_name, source_path,
                    destination_bucket_name, destination_path)

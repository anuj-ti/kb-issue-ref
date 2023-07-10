import boto3


def read_names_from_file(file_path):
    names = []
    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip()
            names.append(name)
    return names


filelist_path = 'uploadScripts\d_MoveFilesToSpace\intersection.txt'
filelist = read_names_from_file(filelist_path)


# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='555',
    aws_secret_access_key='555',
    region_name='us-east-1'  # Replace with your desired region
)

# Create an S3 client
s3 = session.client('s3')


def copy_files_in_range(start_idx, end_idx, filelist, source_bucket, source_path, destination_bucket, destination_path):
    if start_idx < 0 or end_idx >= len(filelist):
        print("Error: Index out of bounds.")
        return

    for i in range(start_idx, end_idx + 1):
        file_name = filelist[i]
        copy_file(source_bucket, source_path, destination_bucket,
                  destination_path, file_name)


def copy_file(source_bucket, source_path, destination_bucket, destination_path, file_name):
    source_key = source_path + file_name
    destination_key = destination_path + file_name

    # Copy the file to the destination path
    s3.copy_object(
        Bucket=destination_bucket,
        CopySource={'Bucket': source_bucket, 'Key': source_key},
        Key=destination_key
    )

    print(f"Copied: {source_key} -> {destination_key}")


# Specify the source and destination details
source_bucket_name = 'ediscovery-dataset'
source_path = 'dev_customer/dev_space/documents/'

destination_bucket_name = 'ediscovery-dataset'
destination_path = 'dev_customer/esw_space/documents/'


def copy_files(start_idx, end_idx):
    copy_files_in_range(start_idx, end_idx, filelist, source_bucket_name,
                        source_path, destination_bucket_name, destination_path)


# 66 done
copy_files(61, 66)

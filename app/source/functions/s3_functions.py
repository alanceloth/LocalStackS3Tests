import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_files_in_bucket(s3, bucket_name):
    """
    List all files in the specified S3 bucket.

    Args:
        s3: Boto3 S3 client object.
        bucket_name (str): Name of the S3 bucket.

    Returns:
        list: List of file names in the bucket.

    Raises:
        Exception: If there is an error listing files in the bucket.
    """
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        files = [obj['Key'] for obj in response.get('Contents', [])]
        return files
    except Exception as e:
        print(f"Error listing files in bucket: {e}")
        return []

def upload_file_to_bucket(s3, file_name, bucket_name, object_name=None):
    """
    Upload a file to the specified S3 bucket.

    Args:
        s3: Boto3 S3 client object.
        file_name (str): Path to the file to upload.
        bucket_name (str): Name of the S3 bucket.
        object_name (str, optional): S3 object name. If not specified, file_name is used.

    Returns:
        bool: True if file was uploaded, else False.

    Raises:
        FileNotFoundError: If the file is not found.
        NoCredentialsError: If credentials are not available.
        PartialCredentialsError: If incomplete credentials are provided.
        Exception: If there is an error uploading the file.
    """
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return False
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False

def download_file_from_bucket(s3, bucket_name, object_name, file_name):
    """
    Download a file from the specified S3 bucket.

    Args:
        s3: Boto3 S3 client object.
        bucket_name (str): Name of the S3 bucket.
        object_name (str): S3 object name.
        file_name (str): Path to the file to download.

    Returns:
        bool: True if file was downloaded, else False.

    Raises:
        FileNotFoundError: If the file is not found.
        NoCredentialsError: If credentials are not available.
        PartialCredentialsError: If incomplete credentials are provided.
        Exception: If there is an error downloading the file.
    """
    try:
        s3.download_file(bucket_name, object_name, file_name)
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return False
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False

def delete_file_from_bucket(s3, bucket_name, object_name):
    """
    Delete a file from the specified S3 bucket.

    Args:
        s3: Boto3 S3 client object.
        bucket_name (str): Name of the S3 bucket.
        object_name (str): S3 object name.

    Returns:
        bool: True if file was deleted, else False.

    Raises:
        NoCredentialsError: If credentials are not available.
        PartialCredentialsError: If incomplete credentials are provided.
        Exception: If there is an error deleting the file.
    """
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False

def create_folder_in_bucket(s3, bucket_name, folder_name):
    """
    Create a folder in the specified S3 bucket.

    Args:
        s3: Boto3 S3 client object.
        bucket_name (str): Name of the S3 bucket.
        folder_name (str): Name of the folder to create.

    Returns:
        bool: True if folder was created, else False.

    Raises:
        Exception: If there is an error creating the folder.
    """
    try:
        s3.put_object(Bucket=bucket_name, Key=(folder_name + '/'))
        return True
    except Exception as e:
        print(f"Error creating folder: {e}")
        return False

def delete_folder_from_bucket(s3, bucket_name, folder_name):
    """
    Delete a folder from the specified S3 bucket.

    Args:
        s3: Boto3 S3 client object.
        bucket_name (str): Name of the S3 bucket.
        folder_name (str): Name of the folder to delete.

    Returns:
        bool: True if folder was deleted, else False.

    Raises:
        Exception: If there is an error deleting the folder.
    """
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        return True
    except Exception as e:
        print(f"Error deleting folder: {e}")
        return False

def move_file_in_bucket(s3, bucket_name, source_key, destination_key):
    """
    Move a file within the specified S3 bucket.

    Args:
        s3: Boto3 S3 client object.
        bucket_name (str): Name of the S3 bucket.
        source_key (str): Source S3 object key.
        destination_key (str): Destination S3 object key.

    Returns:
        bool: True if file was moved, else False.

    Raises:
        Exception: If there is an error moving the file.
    """
    try:
        copy_source = {'Bucket': bucket_name, 'Key': source_key}
        s3.copy_object(CopySource=copy_source, Bucket=bucket_name, Key=destination_key)
        s3.delete_object(Bucket=bucket_name, Key=source_key)
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False
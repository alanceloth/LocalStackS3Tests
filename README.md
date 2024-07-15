
# LocalStack S3 File Management

This project is an example of how to upload and manage files in an S3 bucket using LocalStack. The project includes functions to list, upload, download, delete, create folders, and move files within the simulated S3 bucket. Additionally, it contains code to generate test data.

## Project Structure

```
app/
├── source/
│   ├── functions/
│   │   ├── s3_functions.py
│   ├── create_data.py
│   └── main.py
├── .env
```

## Features

### S3 File Management

The following functions are available to manage files in an S3 bucket:

- `list_files_in_bucket`: Lists all files in an S3 bucket.
- `upload_file_to_bucket`: Uploads a file to an S3 bucket.
- `download_file_from_bucket`: Downloads a file from an S3 bucket.
- `delete_file_from_bucket`: Deletes a file from an S3 bucket.
- `create_folder_in_bucket`: Creates a folder in an S3 bucket.
- `delete_folder_from_bucket`: Deletes a folder from an S3 bucket.
- `move_file_in_bucket`: Moves a file within an S3 bucket.

### Test Data Generation

Scripts to generate test data using Pandas and Polars. The data is then uploaded to the S3 bucket.

## Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/)
- LocalStack
- Docker

## Installation

1. Clone the repository:
    ```bash
    git clone <REPOSITORY_URL>
    cd <REPOSITORY_NAME>
    ```

2. Install the dependencies using Poetry:
    ```bash
    poetry install
    ```

3. Create a `.env` file in the root directory of the project with the following variables:
    ```env
    ENDPOINT_URL=https://localhost.localstack.cloud:4566
    AWS_ACCESS_KEY_ID=test
    AWS_SECRET_ACCESS_KEY=test
    REGION_NAME=sa-east-1
    ```

## Usage

### 1. Start LocalStack

Make sure LocalStack is running. You can start LocalStack using Docker:

```bash
docker run --rm -it -p 4566:4566 -p 4571:4571 localstack/localstack
```

### 2. Run the Main Script

The main script (`main.py`) demonstrates the use of the S3 functions:

```bash
poetry run python app/source/main.py
```

### 3. Test Data Generation

The data generation scripts (`create_data.py`) can be run to generate test data and upload it to the S3 bucket:

```bash
poetry run python app/source/create_data.py
```

## Contact

If you have questions feel free to ask me.
- [LinkedIn](https://www.linkedin.com/in/alanlanceloth/)
- [GitHub](https://github.com/alanceloth/)
- [alan.lanceloth@gmail.com](mailto:alan.lanceloth@gmail.com)
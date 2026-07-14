# Manipulating AWS S3 Storage Using the AWS CLI

## Table of Contents

- [Manipulating AWS S3 Storage Using the AWS CLI](#manipulating-aws-s3-storage-using-the-aws-cli)
  - [Table of Contents](#table-of-contents)
  - [What is Amazon S3?](#what-is-amazon-s3)
    - [S3 terminology](#s3-terminology)
  - [Prerequisites](#prerequisites)
  - [Connect to the EC2 Instance](#connect-to-the-ec2-instance)
  - [Update the EC2 Instance](#update-the-ec2-instance)
  - [Install AWS CLI Version 2](#install-aws-cli-version-2)
    - [1. Install the required dependencies](#1-install-the-required-dependencies)
    - [2. Download the AWS CLI installer](#2-download-the-aws-cli-installer)
    - [3. Extract the installer](#3-extract-the-installer)
    - [4. Check the installed version](#4-check-the-installed-version)
  - [Authenticate the AWS CLI](#authenticate-the-aws-cli)
  - [Useful AWS CLI Help Commands](#useful-aws-cli-help-commands)
  - [List S3 Buckets](#list-s3-buckets)
  - [Create an S3 Bucket](#create-an-s3-bucket)
  - [List Files in a Bucket](#list-files-in-a-bucket)
  - [Create and Upload a File](#create-and-upload-a-file)
  - [Download Files from S3](#download-files-from-s3)
  - [Synchronise Files](#synchronise-files)
    - [Upload a local directory to S3](#upload-a-local-directory-to-s3)
    - [Download a bucket to a local directory](#download-a-bucket-to-a-local-directory)
  - [Delete a Single Object](#delete-a-single-object)
  - [Delete All Objects in a Bucket](#delete-all-objects-in-a-bucket)
  - [Delete an Empty Bucket](#delete-an-empty-bucket)
  - [Delete a Bucket and Its Contents](#delete-a-bucket-and-its-contents)
  - [Useful Terminal Commands](#useful-terminal-commands)
  - [Command Summary](#command-summary)

---

## What is Amazon S3?

Amazon S3 stands for **Amazon Simple Storage Service**.

It is an AWS service used to store and retrieve data from the cloud.

S3 can be used for:

- Images and videos
- Log files
- Backups
- Application files
- Website resources
- Static website hosting
- Data storage and archiving

Important S3 features include:

- Data can be accessed at any time from anywhere, depending on permissions.
- S3 provides built-in redundancy across multiple Availability Zones within an AWS Region.
- S3 can be managed through:
  - The AWS Management Console
  - The AWS Command Line Interface
  - AWS SDKs such as Python Boto3
- Objects uploaded to S3 are private by default.
- Permissions must be configured before objects can be accessed publicly.

### S3 terminology

| Term | Meaning |
|---|---|
| Bucket | A container used to store objects |
| Object | A file stored inside a bucket |
| Key | The full name or path of an object |
| Region | The AWS Region where the bucket is created |
| URI | The S3 address, such as `s3://bucket-name/file.txt` |

---

## Prerequisites

Before starting, we need:

- A running EC2 instance
- SSH access to the EC2 instance
- An AWS account
- AWS credentials with permission to use S3
- A globally unique S3 bucket name

> S3 bucket names must be globally unique across all AWS accounts.

---

## Connect to the EC2 Instance

Connect to the EC2 instance using SSH:

```bash
ssh -i ~/.ssh/your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

Example:

```bash
ssh -i ~/.ssh/tech610-key.pem ubuntu@12.34.56.78
```

---

## Update the EC2 Instance

Update the package list:

```bash
sudo apt update -y
```

Upgrade installed packages:

```bash
sudo apt upgrade -y
```
---

## Install AWS CLI Version 2

### 1. Install the required dependencies

Install `curl` and `unzip`:

```bash
sudo apt install curl unzip -y
```

### 2. Download the AWS CLI installer

For an x86-64 EC2 instance:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

### 3. Extract the installer

```bash
unzip awscliv2.zip
```

### 4. Check the installed version

```bash
aws --version
```

Example output:

```text
aws-cli/2.x.x Python/3.x Linux/x.x exe/x86_64.ubuntu
```
---

## Authenticate the AWS CLI

Run:

```bash
aws configure
```

Enter the requested values:

```text
AWS Access Key ID: YOUR_ACCESS_KEY_ID
AWS Secret Access Key: YOUR_SECRET_ACCESS_KEY
Default region name: eu-west-1
Default output format: json
```

---

## Useful AWS CLI Help Commands

Display general AWS CLI help:

```bash
aws help
```

Display help for S3 commands:

```bash
aws s3 help
```

Display help for a particular command:

```bash
aws s3 rm help
```

Press `q` to exit the help screen.

---

## List S3 Buckets

List all S3 buckets accessible using the configured AWS credentials:

```bash
aws s3 ls
```
---

## Create an S3 Bucket

Create a bucket:

```bash
aws s3 mb s3://tech610-montezer-first-bucket
```

Because the bucket name must be globally unique, use a naming format such as:

```text
tech610-firstname-first-bucket
```
Confirm that the bucket was created:

```bash
aws s3 ls
```

---

## List Files in a Bucket

List the objects inside a bucket:

```bash
aws s3 ls s3://tech610-montezer-first-bucket
```
---

## Create and Upload a File

Create a test file:

```bash
echo "This is the first line in a test file" > test.txt
```

Check the contents:

```bash
cat test.txt
```

Upload the file to the bucket:

```bash
aws s3 cp test.txt s3://tech610-montezer-first-bucket/
```

Upload it using a different S3 object name:

```bash
aws s3 cp test.txt s3://tech610-montezer-first-bucket/test1.txt
```

Confirm the upload:

```bash
aws s3 ls s3://tech610-montezer-first-bucket
```

> `aws s3 cp` copies or uploads data. It does **not** delete the local file or the S3 bucket.

---

## Download Files from S3

Download one object:

```bash
aws s3 cp s3://tech610-montezer-first-bucket/test.txt .
```

Download an object to a specific path:

```bash
aws s3 cp s3://tech610-montezer-first-bucket/test.txt ~/downloads/test.txt
```

Download all objects recursively:

```bash
aws s3 cp s3://tech610-montezer-first-bucket/ ./downloaded-files --recursive
```

---

## Synchronise Files

### Upload a local directory to S3

```bash
aws s3 sync ./local-folder s3://tech610-montezer-first-bucket/
```

### Download a bucket to a local directory

```bash
aws s3 sync s3://tech610-montezer-first-bucket/ ./downloaded-files
```

Only new or changed files are normally transferred.

> Be careful when using the `--delete` option with `sync`. It deletes files from the destination when they do not exist in the source.

Example:

```bash
aws s3 sync ./local-folder s3://tech610-montezer-first-bucket/ --delete
```

---

## Delete a Single Object

Delete one file from the bucket:

```bash
aws s3 rm s3://tech610-montezer-first-bucket/test.txt
```

Example output:

```text
delete: s3://tech610-montezer-first-bucket/test.txt
```

> This deletes the object without asking for confirmation.

---

## Delete All Objects in a Bucket

Delete every object inside a bucket:

```bash
aws s3 rm s3://tech610-montezer-first-bucket --recursive
```

This removes the files but leaves the empty bucket in place.

> **Warning:** This operation does not request confirmation and can delete many objects.

---

## Delete an Empty Bucket

Once the bucket is empty, delete it using:

```bash
aws s3 rb s3://tech610-montezer-first-bucket
```

The `rb` command means **remove bucket**.

If the bucket still contains objects, the command will fail unless `--force` is used.

---

## Delete a Bucket and Its Contents

Delete all objects and then delete the bucket itself:

```bash
aws s3 rb s3://tech610-montezer-first-bucket --force
```

> **Danger:** This command deletes the bucket and its contents without asking for confirmation.

Therefore, the correct command to completely remove a non-empty bucket is:

```bash
aws s3 rb s3://tech610-montezer-first-bucket --force
```

By comparison:

```bash
aws s3 rm s3://tech610-montezer-first-bucket --recursive
```

only deletes the objects and does **not** delete the bucket.

---

## Useful Terminal Commands

Clear the terminal:

```bash
clear
```

Display command history:

```bash
history
```

Run a previous history command by its number:

```bash
!COMMAND_NUMBER
```

Example:

```bash
!25
```

Search previous commands interactively:

```text
Ctrl + R
```

Check the current directory:

```bash
pwd
```

List files:

```bash
ls -la
```

---

## Command Summary

| Task | Command |
|---|---|
| Check AWS CLI version | `aws --version` |
| Configure credentials | `aws configure` |
| Verify identity | `aws sts get-caller-identity` |
| List buckets | `aws s3 ls` |
| Create a bucket | `aws s3 mb s3://BUCKET-NAME` |
| List bucket contents | `aws s3 ls s3://BUCKET-NAME` |
| Upload a file | `aws s3 cp FILE s3://BUCKET-NAME/` |
| Download a file | `aws s3 cp s3://BUCKET-NAME/FILE .` |
| Upload a directory | `aws s3 sync LOCAL-DIRECTORY s3://BUCKET-NAME/` |
| Download a bucket | `aws s3 sync s3://BUCKET-NAME/ LOCAL-DIRECTORY` |
| Delete one object | `aws s3 rm s3://BUCKET-NAME/FILE` |
| Delete all objects | `aws s3 rm s3://BUCKET-NAME --recursive` |
| Delete an empty bucket | `aws s3 rb s3://BUCKET-NAME` |
| Delete bucket and contents | `aws s3 rb s3://BUCKET-NAME --force` |

---



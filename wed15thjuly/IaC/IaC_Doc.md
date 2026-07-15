# Infrastructure as Code

## Project overview

This folder contains my Infrastructure as Code learning and documentation.

The main tools covered will be:

* Terraform
* Ansible

Terraform will be used to define and provision infrastructure through configuration files.

Ansible will be used for configuration management and application provisioning.

## Folder structure

```text
infrastructure-as-code/
├── IaC.md
├── terraform/
└── ansible/
```

## Installing Terraform on macOS

### Prerequisites

Terraform was installed using Homebrew.

I first confirmed that Homebrew was installed:

```bash
brew --version
```

### Adding the official HashiCorp repository

I added the official HashiCorp Homebrew repository:

```bash
brew tap hashicorp/tap
```

### Installing Terraform

I installed Terraform using:

```bash
brew install hashicorp/tap/terraform
```

Homebrew installs Terraform into a command-line location that is already included in the macOS `PATH`.

Therefore, unlike a manual Windows installation, I did not need to move a Terraform executable or manually add its folder to the PATH environment variable.

## Testing the installation

I tested the Terraform installation using:

```bash
terraform --version
```

My output was:

```text
Terraform v1.15.8
on darwin_arm64
```

The operating-system value should normally be:

* `darwin_arm64` for an Apple Silicon Mac
* `darwin_amd64` for an Intel Mac

## Checking the Terraform installation location

I checked the location of the Terraform executable using:

```bash
which terraform
```

My output was:

```text
/opt/homebrew/bin/terraform
```

## Verifying Terraform works from anywhere

I closed the original Terminal window and opened a new one.

I then changed to my home directory:

```bash
cd ~
```

From there, I ran:

```bash
terraform --version
```

Terraform returned the version successfully, confirming that the command was available globally through the macOS PATH.

## Installing the Terraform VS Code extension

I opened the Extensions section in VS Code using:

```text
Command + Shift + X
```

I searched for and installed:

```text
HashiCorp Terraform
```

The extension was published by HashiCorp.

The extension provides features including:

* Terraform syntax highlighting
* Code completion
* Code formatting
* IntelliSense
* Code navigation
* Terraform language-server support

The extension can also be installed through the command line:

```bash
code --install-extension HashiCorp.terraform
```

# Configuring AWS Credentials for Terraform on macOS

## Overview

Terraform needs permission to connect to AWS and create or manage AWS resources.

On macOS, the recommended approach is to install the AWS CLI and save the AWS credentials in an AWS profile using:

```bash
aws configure
```

## Installing the AWS CLI

I first checked whether the AWS CLI was already installed:

```bash
aws --version
```

If the AWS CLI was not installed, I installed it using Homebrew:

```bash
brew install awscli
```

I then confirmed the installation:

```bash
aws --version
```

The command returned the installed AWS CLI version successfully.

## Configuring the AWS credentials

I ran the following command:

```bash
aws configure
```

I was prompted to enter:

```text
AWS Access Key ID:
AWS Secret Access Key:
Default region name:
Default output format:
```

I entered the access key ID and secret access key from the CSV file provided by the trainer.

I configured the default region as:

```text
eu-west-1
```

I configured the default output format as:

```text
json
```

## Checking the AWS configuration

I checked the active AWS CLI configuration using:

```bash
aws configure list
```

This showed that the access key, secret key and region were being loaded from the AWS profile.

The secret access key was masked in the output.

## Testing access to AWS

I tested the credentials using:

```bash
aws sts get-caller-identity
```

The command returned information including:

* The AWS user ID
* The AWS account ID
* The AWS identity ARN

This confirmed that the AWS CLI could authenticate successfully with AWS.

Terraform will also be able to use the same default AWS profile.

## Security considerations

The CSV file containing the credentials should also be stored outside the Git repository.

I did not include any AWS access keys or secret access keys in this documentation.

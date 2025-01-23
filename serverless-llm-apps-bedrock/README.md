# Serverless LLM Applications with Amazon Bedrock

This repository contains the code and resources for building serverless applications powered by large language models (LLMs) using Amazon Bedrock. The project showcases a practical example of deploying an event-driven architecture to handle customer service calls, automatically process transcripts, and generate summaries—all without managing infrastructure.

## Overview

The course and this project focus on creating a serverless pipeline for processing customer service call recordings. The workflow includes:

1. **Event-driven triggers**: Detecting new audio uploads.
2. **Automatic Speech Recognition (ASR)**: Converting audio to text.
3. **LLM Summarization**: Generating call summaries.
4. **Serverless architecture**: Implementing the pipeline using Amazon Bedrock and other AWS serverless services.

### Why Serverless?
- No need for infrastructure management (e.g., servers or containers).
- Scalability to handle millions of users.
- Faster deployment with production-grade reliability.

## Architecture
The workflow is built using an event-driven serverless architecture:

1. **Trigger Event**: Upload of a new customer service call recording.
2. **ASR Step**: Transcribe the audio into text using ASR services.
3. **LLM Processing**: Summarize the transcript using an LLM accessed via Amazon Bedrock.
4. **Storage**: Save the summary for future use.

### Key AWS Services
- **Amazon Bedrock**: Provides access to various LLMs.
- **AWS Lambda**: Executes computational steps in response to events.
- **Amazon S3**: Stores customer call recordings and outputs.
- **Amazon EventBridge**: Manages event-driven triggers.

## Setup Instructions

### Prerequisites
1. AWS account with permissions for Lambda, S3, EventBridge, and Bedrock.
2. Node.js and npm installed locally for deploying serverless functions.
3. AWS CLI configured for your account.

### Deployment Steps
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd serverless-llm-app
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Set up AWS resources**:
   - Create an S3 bucket for storing call recordings.
   - Configure Amazon Bedrock access.

4. **Deploy the serverless application**:
   ```bash
   npm run deploy
   ```

5. **Test the workflow**:
   - Upload an audio file to the S3 bucket.
   - Monitor the pipeline and verify the summary output.

## Usage
1. Upload an audio file to the designated S3 bucket.
2. The system will automatically transcribe the file, summarize it, and store the output.
3. Access the summary from the output storage or monitor logs for real-time updates.

## Course Instructor
- **Mike Chambers**: Developer Advocate at AWS specializing in generative AI, with extensive experience in building scalable AI applications.

## Key Takeaways
- Learn to build production-grade serverless AI workflows.
- Understand the advantages of event-driven architectures.
- Gain hands-on experience with Amazon Bedrock and serverless technologies.

## Resources
- [Amazon Bedrock Documentation](https://aws.amazon.com/bedrock/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [EventBridge Documentation](https://docs.aws.amazon.com/eventbridge/)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
Enjoy building scalable, serverless LLM applications with Amazon Bedrock!
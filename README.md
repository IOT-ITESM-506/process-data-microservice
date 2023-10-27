# AWS SNS -> SQS -> Lambda -> PostgreSQL Microservice

This repository contains a microservice that utilizes various AWS services to process data from AWS SNS and store it in a PostgreSQL database on AWS RDS.

## Architecture

The architecture of the microservice is composed of the following elements:

1. **AWS SNS (Simple Notification Service):**
   - Used to send messages to subscribers about specific events.

2. **AWS SQS (Simple Queue Service):**
   - Acts as an intermediary to store messages from AWS SNS before being processed by the Lambda.

3. **AWS Lambda:**
   - The Lambda is configured to listen on the SQS queue and automatically process messages when they arrive.
   - The Lambda code extracts data from the message and stores it in the PostgreSQL database.

4. **AWS RDS (Relational Database Service):**
   - Used to host the PostgreSQL database that stores the data processed by the Lambda.

## Configuration

To run this microservice in your environment, follow these steps:

1. **AWS Configuration:**
   - Ensure you have AWS credentials configured.
   - Set up an SNS, SQS, Lambda, and RDS in your AWS account.

2. **Repository Setup:**
   - Clone this repository to your local machine.

3. **Environment Variable Configuration:**
   - Set up the necessary environment variables for the Lambda, such as database credentials.

4. **Deployment:**
   - Deploy the Lambda and configure triggers for the SQS queue.

## Project Structure

Brief explanation of the project structure, highlighting key directories and files.

## Contribution

Feel free to contribute to this project by opening issues or sending pull requests.

## License

This project is licensed under [license name]. Refer to the LICENSE.md file for more details.

<img width="573" alt="Screenshot 2023-10-23 at 12 58 25 a m" src="https://github.com/IOT-ITESM-506/process-data-microservice/assets/119972872/ee0fa1b5-86a4-41fd-a17a-aff53e4d5716">

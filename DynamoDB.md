# DynamoDB:
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
- **Serverless** NoSQL database
- SQL database can have performance  and scaling issue and rigid schema makes difficult to store variation in data
- DynamoDB continues to help you move away from relational databases while reducing cost and improving performance at scale.
- DynamoDB is purpose-built and optimized for operational workloads that require consistent performance at any scale
- Customers across all sizes, industries, and geographies use DynamoDB to build modern, serverless applications that can start small and **scale globally.**
- Sales to support tables of virtually any size

## Characteristics of DynamoDB:
- Serverless
    - you don't need to provision any servers, or patch, manage, install, maintain, or operate any software
    - it has no versions and there are no maintenance windows

- NoSQL
    - As a NoSQL databse, it is built to deliver improved performance, scalability, manageability and flexibility compared to traditional relational databases
    - it support both key-value and document data modules
    - doesn't support JOIN operator
    - denormalize your data model to reduce database round trips and processing power needed to answer queries
- Fully managed
    -  It handles setup, configurations, maintenance, high availability, hardware provisioning, security, backups, monitoring, and more.
- Single-digit millisecond performance at any scale
    - It omits features that are inefficient and non-performing at scale, such as JOIN operations


## DynamoDB use cases:
DynamoDB is ideal for use cases that require consistent performance at any scale with little to zero operational overhead.
- Financial service applications: pplications, such as live trading and routing, loan management, token generation, and transaction ledgers
- Gaming applications: 
- Streaming applications: 


## Change data capture with DynamoDB:
 ### Streaming options for change data capture:
    - It offers two streaming models for change data capture:
    - You can enable both streaming models on the same table
        i. Kinesis Data Streams for DynamoDb
        ii. DynamoDB Streams


| Kinesis Data Streams for Dynamodb | DynamoDB Streams |
| --------- | ------ |
| Kinesis Data Streams integrates with DynamoDB for real-time analytics or complex event processing | A native feature of DynamoDB that captures data changes in a table and provides a near-real-time ordered stream of changes (with a 24-hour retention period) |
| Suitable for applications that require real-time, custom analytics, or external stream processing (e.g., using Apache Flink, custom consumers, or AWS Lambda). | Best for simple, serverless, real-time data processing tasks such as event-driven architectures. Commonly used with AWS Lambda to automatically trigger actions based on DynamoDB changes. |
| more powerful, flexible suitable for advanced real-time analytics and complex event processing | lightweight, simple, and ideal for basic event-driven architectures with Lambda |


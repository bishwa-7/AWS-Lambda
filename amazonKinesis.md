# Amazon Kinesis Data Streams:

- https://docs.aws.amazon.com/streams/latest/dev/introduction.html
- it is messaging service for collecting and transferring data between different application similar to SQS and SNS
- to collect and process large streams of data records in real time
- You can use Kinesis Data Streams for rapid and continuous data intake and aggregation
- Kinesis is able to handle large stream of incoming data and also be able to connect to other services to do real time reporting on these large data streams
- SQS is used for simpler usecase hence its name Simple
- The type of data used can include IT infrastructure log data, application logs, social media, market data feeds, and web clickstream data

## Usecase:
- Accelerated log and data feed intake & processing
- Real-time metrics & reporting
- Real-time data analytics
- Complex stream processing


## Architecture of Kinesis Data Streams:
- https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html

i. Producers
- Producers continually push data to Kinesis Data Streams

ii. Amazon Kinesis Stream
- Data stream is a set of shards
- Each shard has a sequence of data records
- Each record has a sequence number that is assigned by Data Streams

iii. Consumers
- Consumers process the data in real time
- Consumers(an application running on EC2 or Firehose) can store their results using AWS services like DynanoDB, Redshift or S3


## Terminology:

### Data Record:
- Unit of data stored in data stream
- Data record are composed of a sequence number, a partition key, and a data blob

### Capacity Mode:
- It determines how capacity is managed and how you are charged for the usage of your data stream
- you can switch between modes and the status of stream is **Updating**
- Types of data streams:
    - On-Demand:
        - Kinesis Data Streams automatically manages the shards in order to provide the necessary throughput
        - no capacity planning required
        - Use case:
            - ideal for addressing the needs of **highly variable and unpredictable application traffic**
        - you **pay per GB of data written and read from your data streams**
    - Provisioned:
        - you must specify the number of shards for the data stream
        - The total capacity of a data stream is the sum of the capacities of its shards
        - Usecase:
            -  suited for predictable traffic with capacity requirements that are easy to forecast
            - use the provisioned mode if you want fine-grained control over how data is distributed across shards


### Retention Period:
- length of time data are accessible after they are added to the stream
- default: 24 hours
- Can increase upto 365 days, additional charge is applied

### Shard:
- uniquely identified **sequence of data** records in a stream
- A stream is composed of one or more shards, each of which provides a **fixed unit of capacity**.
- Each shard can support up to 5 transactions per seconds for reads, & 1000 records/sec for writes
- If data rate increases or decreases, you can increase or decrease number of shards called reshard
- **To achieve optimum performance, you should have one KCL worker assigned to each shard**
    - each EC2 instance runs one KCL

## Kinesis Resharding:
- https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html
- enables you to increase or decrease the number of shards in a stream in order to adapt to change in the rate of data flowing through the stream
- Resharding is always pairwise meaning you can not split into more than two shards in a single operations
- 2 types of resharding:
    - Shard Split:
        - combine two shards into a single shard
        - splitting increases the number of shards in the stream and therefore increases the data capacity of the stream
        - it also increases the cost
    - Shard Merge:
        - combine two shards into a single shard
        - reduces the number of shards in the stream and thus ruduces the data capacity and cost
- The Kinesis Client Library (KCL) tracks the shards in the stream using an Amazon DynamoDB table, and adapts to changes in the number of shards that result from resharding
- The workers automatically discover the new shards and create processors to handle the data from them.
- **When you use the KCL, you should ensure that the number of instances does not exceed the number of shards (except for failure standby purposes).** 
    - Each shard is processed by exactly one KCL worker and has exactly one corresponding record processor. However, one worker can process any number of shards, so it's fine if the number of shards exceeds the number of instances.
    - Because each shard can not be processed by multiple workers at a same time, there is no point to use EC2 instance > number of shards.

## Kinesis Client Library (KCL):
- https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html
- KCL helps you consume and process data from a Kinesis data stream by taking care of many of the complex tasks associated with distributed computing

### KCL concepts:
- **KCL consumer application**: an application that is custom-built using KCL and designed to read and process records from data streams.
- **Consumer application instance**: KCL consumer applications are typically distributed, with one or more application instances running simultaneously in order to coordinate on failures and dynamically load balance data record processing.
- **Worker**: a high level class that a KCL consumer application instance uses to start processing data.
- The worker initializes and oversees various tasks, including syncing shard and lease information, tracking shard assignments, and processing data from the shards

**Lease**:
- By default, a worker can hold one or more leases at the same time
- One worker holds the lease to a particular shard until it is ready to stop processing this shard’s data records or until it fails.
- 2 workers can not hold the same shard at the same time
- 

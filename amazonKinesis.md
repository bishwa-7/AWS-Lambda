# Amazon Kinesis Data Streams:

- https://docs.aws.amazon.com/streams/latest/dev/introduction.html
- to collect and process large streams of data records in real time
- You can use Kinesis Data Streams for rapid and continuous data intake and aggregation
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
- A stream is composed of one or more shards, each of which provides a fixed unit of capacity.
- 
# Lambda

## Lambda execution environment lifecycle:

- https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html
- By default, each AWS account has a concurrency limit of 1,000 concurrent executions across all Lambda functions in a given region, This limit can be raised by requesting for AWS to increase the limit of the concurrent executions of your account.
- Lambda invokes function in execution environment which manages the resources required for the function
- When you create lambda, you specify memory, maximum execution time, etc and lambda uses this information to set up the execution environment
- The execution environment provides lifecycle support for the function's runtime and any external extensions
    - meaning the execution environment is responsible for:
        - Running the runtime for lambda function (such as python, node.js, etc)
        - Handling invocation of the function
        - Managing the function's lifecycle, including cold starts and warm invocations

        Cold Start:
            - When a lamnda function is invoked for the first time and new execution environment is created
        Warm Invocations:
            - Lambda attempts to reuse execution environments for subsequent invocations to reduce cold start latency as it skips initialization steps

        - Supporting external extensions that enhance or customize the behavior of the Lambda functions



## Lambda execution environment lifecycle:

INIT -> INVOKE -> INVOKE -> SHUTDOWN

## Concurrency in Lambda:
- concurrent executions = (invocations per second) x (average execution duration in seconds)
- AWS Lambda dynamically scales function execution in response to increased traffic, up to your concurrency limit.


## Invocation type:
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html
- Trigger based invocation:
    - some services(s3) can invoke a lambda function with each new event 
    - we have no control over the invocation type
- Event source mapping: 
    - for stream and queue-based services and invoke in batches of records
    - using Invoke API
- In Invoke API, Invocation type:
    - RequestResponse - synchronously
    - Event - acynchronously
    - DryRun 

### Synchronous invocation
- you wait for the function to process the event and return the response
- the connection is open until the function returns a response or time out

### Asynchronous invocation
- Lambda queues the event for processing and returns a response immediately
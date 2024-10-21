# AWS Elastic Beanstalk:
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
- Beanstalk is great if you have a single code base for the project
- it can b~e challenging to figure out which services to use and how to provision them in AWS which provides variety of services
- You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.
- Allows you to quickly deploy and manage applications in the AWS Cloud without worrying about the infrastructure that runs those applications.
- You can interact with Elastic Beanstalk by using the Elastic Beanstalk console, the AWS Command Line Interface (AWS CLI), or eb
- There is no additional charge for Elastic Beanstalk. You pay only for the underlying AWS resources that your application consumes.


## Beanstalk vs Lambda:

| Beanstalk | Lambda |
| --------- | ------ |
| Platform as Service (PaaS) | Servrless Computing |
| Deploys and manages long-running applications on servers | Runs short-lived functions in response to events (event-driven) |
| Uses EC2 instances | Functions run on demand, automatically scaling as needed |
| Applications can be stateful (you manage the state) | Stateless (no state is preserved between invocations) |

## AWS Elastic Beanstalk Concepts:
- Application: a logical collection of Elastic Beanstalk components, including environments, versions, and environment configurations. It is conceptually similar to a folder.

- Application Version: refers to a specific, labeled iteration of deployable code for a web application. An application version points to an Amazon S3 object that contains the deployable code. Applications can have many versions and each application version is unique.

- Environment: a version that is deployed on to AWS resources. Each environment runs only a single application version at a time, however, you can run the same version or different versions in many environments at the same time.

- Environment Configuration:  identifies a collection of parameters and settings that define how an environment and its associated resources behave.

- Platform: a combination of OS, language runtime, web/application server, and Elastic Beanstalk components.

## Managing Elastic Beanstalk environments:
- Environments can be long-running or temporary
- When you terminate an environment, you can save its configuration to recreate it later
- Beanstalk lets you configure deployment process
    -  You can deploy to all of the instances in your environment **simultaneously, or split a deployment into batches** with rolling deployments.

- Configuration changes are processed separately from deployments, and have their own scope
- Modify the resources in your environment only by using Elastic Beanstalk. If you use other to monitor, Beanstalk won't be able to accurately monitor it


## Environment types:
- The type of environment depends on the application to deploy. Example, test application is deployed in single-instance environment to save cost.

i. load-balanced, scalable environment:
- Uses Elastic Load Balancing & EC2 Auto Scaling
- If your application requires **scalability** with the option of running in multiple Availability Zones, use a load-balanced, scalable environment.


ii. single-instance environment:
- contains one EC2 instance
- doesn't have load balancer and EC2 Auto Scaling
- Use a single-instance environment if you expect your production application to have low traffic or if you are doing remote development.

## Elastic Beanstalk worker environments:
- If Beanstalk application takes long time to complete, you can offload those tasks to a dedicated **worker environment**
- For long running task, you can send request to SQS and run the process that performs them on a separate set of instances
- Elastic Beanstalk worker environments simplify this process by managing the Amazon SQS queue and running a daemon process on each instance that reads from the queue for you.


## Deployment policies:

- **All at once**: deploys the new version to all instances simultaneously and will be out of service for a short time.

- **Rolling**: deploys the new version in batches.

- **Rolling with additional batch**: deploys the new version in batches, but first launch a new batch of instances.

- **Immutable**: deploys the new version to a new set of instances.

- **Traffic splitting**: deploys the new version to a new set of instances and temporarily splits incoming client traffic.

## Security:
- When you create an environment, Elastic Beanstalk prompts you to provide two AWS IAM roles:
    - Service role:
        - assumed by Elastic Beanstalk to use other AWS services on your behalf
    - Instance profile:
        - applied to the instances in your environment and allows them to retrieve application versions from S3, upload logs to S3, and perform other tasks that vary depending on the environment type and platform.
        - AWS EB CLI can not create the instance profile for your BeanStalk environment
- User Policies: allow users to create and manage Elastic Beanstalk applications and environments.

## Logs:

- Server log files can be stored in either s3 or CloudWatch Logs

- AWS Elastic Beanstalk stores your application files and optionally, server log files in Amazon S3
- With CloudWatch Logs, you can monitor and archive your Elastic Beanstalk application, system, and custom log files from Amazon EC2 instances of your environments. 

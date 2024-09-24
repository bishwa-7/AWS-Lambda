# AWS Elastic Beanstalk:
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
- it can be challenging to figure out which services to use and how to provision them in AWS which provides variety of services
- You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.
- You can interact with Elastic Beanstalk by using the Elastic Beanstalk console, the AWS Command Line Interface (AWS CLI), or eb
- There is no additional charge for Elastic Beanstalk. You pay only for the underlying AWS resources that your application consumes.


## Beanstalk vs Lambda:

| Beanstalk | Lambda |
| --------- | ------ |
| Platform as Service (PaaS) | Servrless Computing |
| Deploys and manages long-running applications on servers | Runs short-lived functions in response to events (event-driven) |
| Uses EC2 instances | Functions run on demand, automatically scaling as needed |
| Applications can be stateful (you manage the state) | Stateless (no state is preserved between invocations) |




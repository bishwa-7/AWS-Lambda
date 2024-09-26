# Amazon Relational Database Service (RDS):
- RDS is a service that enables to run relational databases (MySQL, PostgresSQL, Oracle, Microsoft SQL server) in the AWS cloud
- Amazon RDS is a managed service that **automates database management tasks** such as hardware provisioning, database setup, patching, and backups.
- RDS can be integrated with other AWS services like Lambda etc
- RDS provides a number of different security options
- RDS offer encryption at rest (protecting data while it is stored) and encryption in transit (protecting data while it is being sent and received)

- Amazon recommends using RDS as default choice for most relational database deployment.
- RDS is responsible for hosting the software components and infrastructure and you are responsible for query tuning

### Disadvantage of alternatives:
- On-premise deployment:
    - Need to maintain server, OS, database software, etc
- Amazon EC2:
    - Unlike on-premise server, CPU, memory, storage and IOPS are separated in EC2 and can be scaled independently
    - EC2 is that you're more prone to user errors
        - When updating OS or database software manually, you might accidently cause application downtime

- **DB instance** are the basic building block of RDS

### DB instance classes:
- DB instance class determines the computation and memory capacity of a DB instance
- It consists of both the DB instance class type and the size and each class offer different compute, memory and storage capabilities.
    - General purpose – db.m*
    - Memory optimized – db.z*, db.x*, db.r*
    - Compute optimized – db.c*

### DB instance storage:
- General Purpose (SSD)
    - cost-effective storage
    - best suited for development and testing environment
- Provisioned IOPS (PIOPS)
    - designed to meet the needs of I/O-intensive workloads, particularly database workloads, that require low I/O latency and consistent I/O throughput
    - best suited for production environments
- Magnetic
    - We recommend that you use General Purpose SSD or Provisioned IOPS SSD for any new storage needs.

## Amazon Aurora:
- It is enterprise-class relational database
- It is compatible with MySQL and PostgreSQL relational databases
- up to five times faster than standard MySQL databases and up to three times faster than standard PostgreSQL datab
- 

## DB instance billing for Amazon RDS:
Amazon RDS instances are billed based on the following components:
- DB instance hours (per hour)
- Storage (per GiB per month)
- Input/output (I/O) requests (per 1 million requests)
- Provisioned IOPS (per IOPS per month)
- Backup storage (per GiB per month)
- Data transfer (per GB)

## Amazon RDS Proxy:
- RDS Proxy makes applications more resilient to database failures by automatically connecting to a standby DB instance while preserving application connections
- Using RDS Proxy, you can handle unpredictable surges in database traffic.
- RDS Proxy queues or throttles application connections that can't be served immediately from the connection pool. Although latencies might increase, your application can continue to scale without abruptly failing or overwhelming the database
- Each AWS account ID is limited to 20 proxies. If application requires more proxies, request an increase

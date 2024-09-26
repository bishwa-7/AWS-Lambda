# Amazon VPC

- VPC is private network to deploy resources
- is a regional resource
- if you have 2 regions, you will have 2 VPC
- you can add subnets, specify IP addresses, add gateways, security groups

## Subnets
- Subnets is a section of a VPC in which you can group resources based on security or operational needs
- Subnest is a range of IP addresses in the VPC
- It can be public or private
    - Public subnet has direct route to internet gateway and can access the public internet
    - Private subnet does not have direct route to internet gateway and require NAT to access public internet
- Each subnet must reside entirely within one Availability Zone and can not span zones

### Subnet Security:
- use private subnets to protect AWS resources and use NAT to provide internet access to resources in private subnet
- **Security groups** allow inbound and outbound traffic for associated resources, such as EC2 instances
- **Network ACLs** allow or deny inbound and outbound traffic at the subnet level
- Security groups can meet the needs but Network ACLs can be used for additional layer of security.

| Security Groups | Network ACLs |
| --------- | ------ |
| Operates at instance level | Operates at subnet level |
| Applies to an instance only if it is associated with the instance | Applies to all instances deployed in the associated subnet |
| Supports allow rules only | Supports allow and deny rules |
| Evaluates all rules before deciding whether to allow traffic | Evaluates rules in order, starting with the lowest numbered rule |
| Stateful: return traffic is allowed, regardless of the rules | Stateless: Return traffic must be explicitly allowed by the rules |
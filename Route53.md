# Route 53
- https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html
- highly available and scalable Domain Name System (DNS) web service.
- use Route 53 to perform three main functions and its combination:
    - Domain Registration
        - website needs name such as example.com
        - Route 53 lets us register a name for the website or web application
    - DNS routing:
        - When a user opens a web browser and enters your domain name (example.com) or subdomain name (acme.example.com) in the address bar, Route 53 helps connect the browser with your website or web application.
    - Health checking
        - Route 53 sends automated request to the resources to check its health status
- Route 53 and Route 53 Resolver resources can be configured using AWS CloudFormation service.

## Working of Domain registration with Route 53:
1. Choose a domain name that no one has used before
2. Register domain name with Route 53 providing names and contact information of the domain owner. 
    - The service automatically makes itself the DNS service for the domain.
3. At the end, they send our information to the registrar for the domain.
4. Registrar sends our informatino to the registry(sells domain registrations) for the domain
5. The registry stores the information

## How internet traffic is router to our website:
- Domain names are mapped to IP address by DNS
- After you register your domain name, Route 53 automatically creates a public hosted zone that has the same name as the domain
- To route traffic to your resources, you create records, also known as resource record sets, in your hosted zone. 
    - Each record includes information about how you want to route traffic for your domain
- User -> www.example.com -> DNS (managed by ISP) -> DNS root name server -> TLD name server (looks .com domains) and responds with the names of the four Route 53 name server. -> DNS serrver chooses Route 53 name server and Route 53 provides IP for web server. Now Web browser has IP of server to connect.


## Amazon Route 53 Resolver:
- it responds recursively to DNS queries from AWS resources for public records, Amazon VPC-specific DNS names, and Amazon Route 53 private hosted zones
- previously called Amazon DNS server


## Routing policy:
-https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html


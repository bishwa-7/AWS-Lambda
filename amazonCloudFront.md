# Amazon Cloud Front
- CF **speeds up distribution** of static and dynamic web content
- When users request your content, CloudFront delivers it through a worldwide network of **edge locations** that **provide low latency and high performance**.
- If content in edge location -> CloudFront delivers it immediately
- If content not in edge location, CF retrieves if from an origin that you have defined such as S3 bucket, HTTP server, etc
- CloudFront speeds up the distribution of your content by routing each user request through the AWS backbone network to the edge location that can best serve your content. Typically, this is a CloudFront edge server that provides the fastest delivery to the viewer. Using the AWS network dramatically reduces the number of networks that your users' requests must pass through, which improves performance.
- **CloudFront is not suitable for storing user session data. It is primarily used as a content delivery network.**

## Working of CloudFront:
- You specify origin servers, like an S3 bucket from which CloudFront gets your files which will then be distributed from CloudFront edge locations all over the world.
- Upload your files to your origin servers.
- Create a CloudFront distribution, which tells CloudFront which origin servers to get your files from when users request the files through your web site or application.
- CloudFront assigns a domain name to your new distribution that you can see in the CloudFront console.
- CloudFront sends your distribution’s configuration (but not your content) to all of its edge locations—collections of servers in geographically dispersed data centers where CloudFront caches copies of your objects.
- Objects are cached for 24 hours by default. You can invalidate files in CloudFront edge caches even before they expire.
- 

## LambdaEdge:
- https://aws.amazon.com/lambda/edge/
- Lambda@Edge is a compute service that lets you execute functions that customize the content that Amazon CloudFront delivers.
- This lets the code to run closer to users of the application.
- after creating function, we can add triggers in Lambda console or CloudFront console so that the functions to **run in AWS locations that are closer to the viewer**
- This gives high performance and low latency 
- No servers to manage
- You can use Lambda@Edge to help authenticate and authorize users for the premium pay-wall content on your website, filtering out unauthorized requests before they reach your origin infrastructure
- Use Lambda@Edge and Amazon Cognito to authenticate and authorize premium customers to download the firmware update.


## Performance and Availability:
- CloudFront also allows you to set up multiple origins to enable redundancy with Origin Failover. 
- 

## CloudFront Security:
- CloudFront, AWS Shield, AWS WAF, and Route 53 work seamlessly together to create a flexible, layered security perimeter against multiple types of attacks including network and application layer DDoS attacks.
- Through geo-restriction capability, you can prevent users in specific geographic locations from accessing content that you’re distributing through CloudFront.
- With Origin Access Control (OAC) feature, you can restrict access to an S3 bucket to only be accessible from CloudFront distributions.


## Configure secure access and restrict access to content:

CloudFront provides several options for securing content that it delivers. Following are the ways to use CloudFront to secure and restrict access to content:

### Configure HTTPs connections:
- Configure CloudFront to require that viewers use HTTPs so connections are encrypted when communicating with viewers
- Also configure to use HTTPs with origin for encrypted communication
- Communication when using HTTPs:
    - Viewer sends an HTTPs request to CloudFront. There's some SSL/TLS negotiations between viewer and CloudFront. Viewer submits encrypted request
    - If CloudFront edge location contains a cache response, CloudFront sends encrypted response to viewer which then decrypts it
    - If not, CloudFront performs SSL/TLS negotiation with origin, and sends encrypted request to origin
    - Origin decrypts the request, processes it and generates encrypted response to CloudFront
    - CloudFront decrypts the response, re-encrypts it and forwards it to viewer and decrypts it

### Prevent users in specific geographic locations from accessing content
- Use CloudFront geographic restrictions feature to restrict access to all of the files
- Geographic restrictions apply to an entire distribution. If you need to apply one restriction to part of your content, you must create separate CloudFront distributions or use a third-party service 
### Require users to access content using CloudFront signed URLs or signed cookies
You can control user access to your private content in two ways:
- Restrict access to files in CloudFront caches
- Restrict access to files in origin by doing one of the following:
    - Set up an origin access control (OAC) **for S3 bucket only**
    - CloudFront provides 2 ways to send authenticated requests to and S3 origin: Origin Access Control (OAC) **recommended** and Origin Access Identity (OAI)
    - Configure custom headers for a private HTTP server
### Set up field-level encryption for specific content fields
- With using HTTPs we can create encryption
- Additionally, Field-level encryption adds an additional layer of security to protect specific data throughout system processing.
- To use field-level encryption, when you configure your CloudFront distribution, specify the set of fields in POST requests that you want to be encrypted, and the public key to use to encrypt them. You can encrypt up to 10 data fields in a request. 
### Use AWS WAF to control access to your content
- AWS WAF is a web application firewall that helps secure your web applications and APIs by blocking requests before they reach the servers.
- To enable WAF protections, we can use One-Click protection and create WAF web access control list (web ACL), configures rules to protect the servers from common web threats.

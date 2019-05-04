# AWS Private API Gateway

This project presents a complete way to build and check a Private API Gateway in AWS


## Prerequisites
I am used to store common parameters in the AWS Parameter Store.

The CloudFormation templates of this project use the following parameters :
* /vpc/id
* /vpc/subnet/a
* /vpc/subnet/b
* /vpc/subnet/c

Feel free to create these parameters with your own configuration or replace them directly in the templates.


## 1 - Build VPC Endpoint
In order to your VPC to communicate directly with the AWS API Gateway's VPC, you have to set up a gateway between them.

This can be realize running the template *vpc-endpoint.yml* in CloudFormation

**WARNING** : This template enable private DNS. So, [you won't be able to use your public API Gateways anymore from your VPC](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-vpc-connections/?nc1=h_ls). In this case, you've got 2 workarounds :
* disable the private DNS (but your private API Gateways will be thougher to use).
* use [edge-optimized custom domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-edge-optimized-custom-domain-name.html) for your public API (my favorite workaround).


## 2 - Build a private API Gateway
The template *hello.yml* build a Private API Gateway which call a Lambda function to say "Hello" ;)

The tricky part of the template is the Lambda integration :

        Uri: !Sub
          - "arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${lambdaArn}/invocations"
          - lambdaArn: !GetAtt HelloFunction.Arn

The Lambda can be updated with the script *hello.bat*

## 3 - Check a private API Gateway
As the private API Gateway is *private*, it could be difficult to test it from your PC.

The template *check.yml* build a Lambda function running in your VPC and calling the API Gateway defined in the environment variables.

The Lambda can be updated with the script *check.bat*

**WARNING** : If you've disabled the private DNS, you'll have to specify the VPC Endpoint to execute your private API Gateway

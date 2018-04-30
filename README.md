# Calculator in Python training
This is a simple python calculator that works with POST API. The calculator runs on a cloud platform. In this case it is a lambda function on AWS.
The whole purpose of the project was to teach the (not yet a) developer (me) the basics of a general development process.

### The basics were:
* Writing the code
* understand process flow working with github
* learn how to use commits, pushes and branching on github
* deploy an API gateway on AWS
* writing a nice readme to my software :)

### The Python Calculator
To use the complete API calculator you have to POST to below URL

`https://0t5mt851o6.execute-api.eu-central-1.amazonaws.com/alfa_deployment/`

example event:

`{  "numbera": 1,  "numberb": 4,  "operation": "mult"}`
There are 4 operations allowed: `mult, div, sub, sum`.

### Special thanks

My thanks goes to David Kubec who is my mentor in this whole `Become a Developer` project.

### Authors:
* David Kubec
* Tomas Breburda

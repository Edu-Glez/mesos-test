# Mesos-test Project 

## Introduction

The test compares the performance of a mesos-cluster against a local computer, to do this a job is executed in each platform taking the time of execution for each to analyze. 

## Development

To run this project we used the following requirements:

 * Two nodes with this characteristics:

  * 4 GB of RAM
  * 75 GB of HDD
  * 4 CPUs

The configuration for the mesos-cluster is with two master nodes and two slave nodes.

A docker process should be up and running and the image edu-glez/mesos-test3 must be pulled from docker hub. The Dockerfile used to generate this image is located in the container folder and it only consists of pulling a Python3 instance, adding the necessary files for the job to run and the command to install some python packages.

The job deploys a docker container in the mesos cluster with the image previously mentioned and executes a python script which consists of the training of a neuronal network used to determine the sentiment inside a text. The algorithm is located in the "test_naive_bayes.py" script and also the files needed for the training, each files contains approximately 100000 tweets but for the test only 100 positives and 200 negatives are being used. Inside the application configuration file named "appedu.json", we stablish that the script will run every x seconds and this configuration file is being sent by a json file using the following command:

`curl -X POST http://10.141.141.10:8080/v2/apps -d @app.json -H "Content-type: application/json"`

The results are the following 



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

The results can be seen in the file stdout(19) obtained from the mesos cluster where several times of excecution are written with an average of 1.8 seconds:

Tomo 1.6909887790679932 segundos ejecutarse
Tomo 1.737644910812378 segundos ejecutarse
Tomo 1.7120234966278076 segundos ejecutarse
Tomo 1.7042474746704102 segundos ejecutarse
Tomo 1.714615821838379 segundos ejecutarse
Tomo 1.7018582820892334 segundos ejecutarse
Tomo 1.756645679473877 segundos ejecutarse
Tomo 1.7567250728607178 segundos ejecutarse
Tomo 1.7509968280792236 segundos ejecutarse
Tomo 1.7327919006347656 segundos ejecutarse
Tomo 1.705024003982544 segundos ejecutarse
Tomo 1.7102999687194824 segundos ejecutarse
Tomo 1.7610230445861816 segundos ejecutarse
Tomo 1.7125771045684814 segundos ejecutarse
Tomo 1.8029544353485107 segundos ejecutarse
Tomo 1.7476527690887451 segundos ejecutarse
Tomo 1.7452330589294434 segundos ejecutarse

Whereas in the local machine takes 3.3 seconds approx.

![alt text](https://github.com/Edu-Glez/mesos-test/blob/master/Time_local.png)



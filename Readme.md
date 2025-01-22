# Essential Files for LKS Wilayah 2025 Practice Module

credit belongs to [https://github.com/Cydnirn/lks-w2024-ess](Cydnirn)

## Lambda
Python function to be deployed to AWS, **it reads** data from AWS IoT Core and store it to AWS DynamoDB, if it receive an anomaly, it will send an email message to the SNS arn, 

## AWS-IOT

C++ file for ESP32 with Sensor

## AWS-IOT-Rand

C++ file for ESP32 without Sensor, generates random number to be sent to AWS IoT Core

## Wiring System

Ignore the Relay, connect the Soil Moisture sensor directly to ESP32
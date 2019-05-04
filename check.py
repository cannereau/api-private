import os
import json
import requests
import logging 
logger = logging.getLogger() 
logger.setLevel(logging.INFO) 

def handler(event, context): 

    # load parameters
    VPC_ENDPOINT = os.environ['VPC_ENDPOINT'].strip()
    API_ENDPOINT = os.environ['API_ENDPOINT'].strip()
    PATH = os.environ['PATH'].strip()
    METHOD = os.environ['METHOD'].strip().upper()

    # log parameters
    logger.info('VPC Endpoint : {}'.format(VPC_ENDPOINT))
    logger.info('API Endpoint : {}'.format(API_ENDPOINT))
    logger.info('Path : {}'.format(PATH))
    logger.info('Method : {}'.format(METHOD))

    # build request
    if VPC_ENDPOINT == '':
        url = 'https://' + API_ENDPOINT + PATH
        headers = {}
    else:
        url = 'https://' + VPC_ENDPOINT + PATH
        headers = {'Host': API_ENDPOINT}

    # make request
    logger.info('URL : {}'.format(url))
    if METHOD == 'POST':
        response = requests.post(url, headers=headers, json=event)
    elif METHOD == 'PUT':
        response = requests.put(url, headers=headers, json=event)
    else:
        response = requests.get(url, headers=headers, json=event)

    # results
    return response.text

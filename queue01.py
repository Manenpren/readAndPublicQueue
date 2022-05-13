import json
import boto3
import os
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class QueueService(ABC):

    @staticmethod
    def create():
        """
        Creates sqs-client
        :return: sqs-Client
        :rtype: sqsIdentityProvider.Client
        """
        return QueueServiceImplementation()

    @abstractmethod
    def createCommunity(self, req):
        """
        User signup in Cognito
        :type req: dict
        :return: Cognito signup user response
        :rtype: boto3.Response
        """
        raise NotImplementedError

class QueueServiceImplementation(QueueService):

    @classmethod
    def __init__(self):
        self.client = boto3.client('sqs', region_name='us-east-1')
        self.queue_url = 'redsocial-ws-taks-test'

    def createCommunity(self, req):
        try:
            logger.info(f'>>> MESSAGE BODY: {req}')
            response = self.client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(req)
            )
            return {
                'response': response,
            }
        
        except self.client.exceptions.InvalidMessageContents:
            raise NameError
        else:
            return response            


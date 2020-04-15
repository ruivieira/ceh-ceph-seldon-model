import joblib
import logging
import numpy as np
import pandas as pd
import boto3
import os
import io

logger = logging.getLogger('ceh-model')

class Model(object):

    def __init__(self):
        print("Initializing.")
        
        # Configure S3 reading
        self._S3_ENDPOINT_URL = os.environ['S3_ENDPOINT_URL']
        self._S3_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
        self._S3_SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

        self._S3_BUCKET="data"

        client = boto3.client(
            service_name='s3',
            aws_access_key_id=self._S3_ACCESS_KEY,
            aws_secret_access_key=self._S3_SECRET_KEY,
            endpoint_url=self._S3_ENDPOINT_URL)
        print(f"Loading model from {self._S3_ENDPOINT_URL}/{self._S3_BUCKET}/model.pkl.")
        obj = client.get_object(Bucket=self._S3_BUCKET, Key="uploaded/model.pkl")
        self.model = joblib.load(io.BytesIO(obj['Body'].read()))

    def predict(self, X, names, meta):
        logger.debug(X)
        _X = pd.DataFrame(X, columns=['income', 'response', 'events'])
        return self.model.predict_proba(_X)
import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

	transactionToUpload = {}
	transactionToUpload['transactionId'] = '3456789'
	transactionToUpload['type'] = 'SELL'
	transactionToUpload['amount'] = 20
	transactionToUpload['customerId'] = 'CID-34256'

	fileName = 'CID-34256' + '.json'

	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=BUCKET_NAME,Body=uploadByteStream)

	print('Put Complete')





# called_function = context.invoked_function_arn

lambda_client = boto3.client('lambda', region_name='us-east-1')
        lambda_client.invoke(
            FunctionName='',
            InvocationType='Event',
            Payload=bytes(json.dumps(event_to_send))
        )
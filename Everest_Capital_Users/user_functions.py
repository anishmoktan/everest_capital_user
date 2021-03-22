import boto3


# class AWS_Manager():


dynamodb = boto3.resource('dynamodb')
dynamoTable = dynamodb.Table('Table_Name')

dynamoTable.put_item(
    Item =
        {
            "username":"Ben",
         }
)


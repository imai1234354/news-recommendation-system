import json
import boto3

# AWS Personalizeの設定
personalize_runtime = boto3.client('personalize-runtime')
campaign_arn = 'arn:aws:personalize:region:account-id:campaign/campaign-name'

# DynamoDBの設定
dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('UserPreferences')
news_table = dynamodb.Table('NewsArticles')

def lambda_handler(event, context):
    # ユーザーIDを取得
    user_id = event['queryStringParameters']['userId']
    
    # AWS Personalizeにリクエストを送信
    response = personalize_runtime.get_recommendations(
        campaignArn=campaign_arn,
        userId=user_id
    )
    
    # 推薦されたニュース記事のIDを取得
    recommended_news_ids = [item['itemId'] for item in response['itemList']]
    
    # ニュース記事の詳細を取得
    recommended_news = []
    for news_id in recommended_news_ids:
        news_item = news_table.get_item(Key={'newsId': news_id})
        recommended_news.append(news_item['Item'])
    
    return {
        'statusCode': 200,
        'body': json.dumps(recommended_news)
    }

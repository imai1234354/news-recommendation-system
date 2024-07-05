# パーソナライズド・ニュースレコメンデーションシステム

このプロジェクトは、AWSサービスを使用してユーザーの興味に基づいてニュース記事を推薦するシステムです。

## 使用技術

- AWS Personalize
- AWS Lambda
- Amazon DynamoDB
- API Gateway


## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd news-recommendation-system
    ```

2. DynamoDBテーブルの作成:
    - AWSコンソールにログインし、以下のDynamoDBテーブルを作成します。
    - テーブル名: `UserPreferences`
      - プライマリキー: `userId`（文字列）
    - テーブル名: `NewsArticles`
      - プライマリキー: `newsId`（文字列）

3. AWS Personalizeの設定:
    - AWS Personalizeコンソールで新しいデータセットグループとデータセットを作成します。
    - データをインポートし、ソリューションとキャンペーンを作成します。
    - `lambda_function.py`のコード内の`campaign_arn`を設定します。

4. Lambda関数のデプロイ:
    - AWS Lambdaコンソールで新しい関数を作成します。
    - `lambda_function.py`のコードを関数にコピーします。
    - `boto3`ライブラリを含むLambdaレイヤーを作成して関数にアタッチします。

5. API Gatewayの設定:
    - API Gatewayで新しいAPIを作成し、Lambda関数をトリガーするエンドポイントを設定します。

## 使用方法

- ユーザーがAPIエンドポイントにリクエストを送信すると、Lambda関数がAWS Personalizeからニュース記事を推薦します。
- 推薦されたニュース記事の詳細がDynamoDBから取得され、レスポンスとして返されます。





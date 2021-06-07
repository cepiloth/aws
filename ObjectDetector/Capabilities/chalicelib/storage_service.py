import boto3
from botocore.retries import bucket

# 클래스 StorageService는 아마존 S3와 연동하는 기능을 캡슐화
class StorageService:
    def __init__(self, storage_location):
        self.client = boto3.client('s3')
        self.bucket_name = storage_location

    def get_storage_location(self):
        return self.bucket_name

    def list_files(self):
        response = self.client.list_objects_v2(Bucket = self.bucket_name)

        files = []
        for content in response['Contents']:
            files.append({
                'location': self.bucket_name,
                'file_name': content['Key'],
                'url': "http://" + self.bucket_name + ".s3.amazonaws.com/"
                       + content['Key']
            })
        return files
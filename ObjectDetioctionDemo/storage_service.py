import boto3

# 클래스 StorageService는 아마존 S3와 연동하는 기능을 캡슐화
class StorageService:
    def __init__(self):
        self.s3 = boto3.resource('s3')
    
    def get_all_files(self, storage_location):
        return self.s3.Bucket(storage_location).objects.all()

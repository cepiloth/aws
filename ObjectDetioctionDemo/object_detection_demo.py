from botocore.retries import bucket
from storage_service import StorageService
from recognition_service import RecognitionService

storage_service = StorageService()
recognition_service = RecognitionService()

#자신이 만든 S3 버킷 주소를 설정한다
bucket_name = ''

for file in storage_service.get_all_files(bucket_name):
    if file.key.endswith('.jpeg'):
        print(file.key + ' 이미지에서 탐지한 객체' + ':')
        labels = recognition_service.detect_object(file.bucket_name, file.key)

        for label in labels:
            print('-- ' + label['Name'] + ': ' + str(label['Confidence']))
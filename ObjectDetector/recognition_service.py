import boto3

class RecognitionService:
    def __init__(self):
        self.client = boto3.client('rekognition')
        self.bucket_name = storage_service
    
    def detect_object(self, storage_location, image_file):
        response = self.client.detect_labels(
            Image = {
                'S3Object' : {
                    'Bucket': storage_location,
                    'Name' : image_file
                }
            }
        )
        return response['Labels']
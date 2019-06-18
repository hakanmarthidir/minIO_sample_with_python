from minio import Minio
from minio.error import (ResponseError, BucketAlreadyExists)
import os

class MinioManager:

    __minioclient = None

    def __init__(self, url, accessKey, secretkey):
        self.__minioclient = Minio(
            endpoint=url, access_key=accessKey, secret_key=secretkey, secure=False)

    def createBucket(self, bucketname):
        if self.__minioclient.bucket_exists(bucketname) == False:
            try:
                self.__minioclient.make_bucket(bucketname)
            except ResponseError as ex:
                print(ex.message)
                raise

    def listBucket(self):
        return self.__minioclient.list_buckets()

    def saveFile(self, bucketname, filename, filepath, contenttype):
        with open(filepath, 'rb') as file:
            filestat = os.stat(filepath)
            self.__minioclient.put_object(bucketname, filename, file,
                        filestat.st_size, content_type=contenttype)

    

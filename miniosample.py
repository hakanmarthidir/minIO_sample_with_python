from miniomanager import MinioManager
from PIL import Image, ImageDraw
import io
import uuid
import os

#-----------------------------------------------
# Connect to Minio
minioManager = MinioManager('localhost:9000', 'minio', 'minio123')

#-----------------------------------------------
# Create a Folder
minioManager.createBucket("customerx")
minioManager.createBucket("customery")
minioManager.createBucket("customerz")
print("OK - Buckets Were Created")

#-----------------------------------------------
# Getting Buck List
bucketlist = minioManager.listBucket()
for buck in bucketlist:
    print(buck)

#-----------------------------------------------
# Create an Image and Put the Image In Buck List
img = Image.new('RGB', (100, 30), color=(73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello Minio", fill=(255, 255, 0))
# value = io.BytesIO(img.tobytes())
imgid = str(uuid.uuid4())
imgname = imgid+'.png'
imgpath = './temp/'+imgname
img.save(imgpath)
print('File Created and Trasferring to MinIO')
minioManager.saveFile('customerx', imgname, imgpath, 'image/jpeg')

#-----------------------------------------------
#Download Files 
minioManager.downloadFile('customerx', imgname, './downloads/'+imgname)
print('Download Completed...')


#-----------------------------------------------
#Permanent Urls 
print(minioManager.getPermanentUrl('customerx', imgname))
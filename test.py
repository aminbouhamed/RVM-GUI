import os
import cv2
from detect import object_detection, volume_brand_classification
os.environ['QT_QPA_PLATFORM'] = 'xcb'
import qrcode
from authentication import QRCodeAuthentication
import requests

"""
client_id = 2
token = "1e9c642076edad4f06474540ec2d4f03df19cd1"
data = f"{client_id}:{token}"
qrCode = qrcode.make(data)


qrCode = qrcode.make("wissemboujlida")
qrCode.save('qrcode.png')
"""

authentication = QRCodeAuthentication()

qrcode = authentication.scan_QRCode()

response = authentication.authenticate(qrcode)

print(qrcode)


"""
ressources.load_models()
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
cam.release()
cv2.imwrite("img.jpg", frame)
img = cv2.imread('img.jpg')
img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (512,512))
img = np.array(img)

object_detection(img)
volume_brand_classification(img)
"""

"""
url1 = "http://192.168.1.16/object_detection"
#url2 = "http://192.168.1.16/volume_brand_classification"

img_path = 'ressources/dataset/BOTTLE_0,5_COCA/coca_sbsm0.jpg'
img = cv2.imread(img_path)

_, img_encoded = cv2.imencode('.jpg', img)
img_file = {'img': ('img.jpg', img_encoded.tobytes(), 'img/jpeg')}

# Send the HTTP request
response1 = requests.post(url1, files=img_file)
#response2 = requests.post(url2, files=img_file)

print(response1.text)
#print(response2.text)
"""
"""
img_path = 'ressources/dataset/BOTTLE_0,5_COCA/coca_sbsm0.jpg'
img = cv2.imread(img_path)

_, img_encoded = cv2.imencode('.jpg', img)
img_file = {'img': ('img.jpg', img_encoded.tobytes(), 'img/jpeg')}

url2 = "http://192.168.1.16/volume_brand_classification"
response2 = requests.post(url2, files=img_file)
print(response2.json())
"""
"""
cam = cv2.VideoCapture(3) # check this
ret, frame = cam.read()
cv2.imwrite("img.jpg", frame)
cam.release()
"""
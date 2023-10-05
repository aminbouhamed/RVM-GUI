import cv2
import requests
import json
import time

class QRCodeAuthentication:
    def __init__(self):
        self.is_authenticated = False
        self.id = None
        self.token = None

    def scan_QRCode(self):
        capture_duration = 5
        cam = cv2.VideoCapture(0)
        QRCode_scanner = cv2.QRCodeDetector()
        start_time = time.time()
        while int(time.time() - start_time) < capture_duration:
            _,img = cam.read()
            data, one, _ = QRCode_scanner.detectAndDecode(img)
            if data:
                qrcode=data
                return qrcode 
        

    def authenticate(self, qrcode):
        URL_TO_QRCODE_AUTHENTICATION = "https://rvm-production.up.railway.app/rvm/api/qrcode-auth"
        id = qrcode.split(':')[0]
        token = qrcode.split(':')[1]
        request = {}
        request['id'] = id
        request['token'] = token

        json_request = json.dumps(request)
        headers = {
                "Content-Type": "application/json"
            }
            # Make the POST request
        response = requests.post(URL_TO_QRCODE_AUTHENTICATION, headers=headers, data=json_request)
        return response



        """
        URL_TO_QRCODE_AUTHENTICATION = "https://rvm-production.up.railway.app/rvm/api/qrcode-auth"
        try:
            id = qrcode.split(':')[0]
            token = qrcode.split(':')[1]
            request = {}
            request['id'] = id
            request['token'] = token
            # Convert the JSON data to a string
            json_request = json.dumps(request)
            headers = {
                "Content-Type": "application/json"
            }
            # Make the POST request
            response = requests.post(URL_TO_QRCODE_AUTHENTICATION, headers=headers, data=json_request)
            if (response.status_code == 200):
                self.is_authenticated=True
                self.id = id
                self.token = token
                return True
            else:
                return False
        except:
            return False
            """




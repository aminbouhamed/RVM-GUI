import requests
import json
from datetime import datetime
from authentication import QRCodeAuthentication


classes = [
 'BOTTLE_0,5_SAFIA',
 'BOTTLE_0,5_ROYALE',
 'BOTTLE_1,0_MIRA',
 'BOTTLE_1,5_MELLITI',
 'CAN_0,24_SPRITE',
 'BOTTLE_0,5_CRISTALINE',
 'BOTTLE_1,5_DELICE',
 'BOTTLE_1,5_BOGACIDRE',
 'BOTTLE_0,5_MARWA',
 'CAN_0,24_BOGACITRON',
 'BOTTLE_2,0_DIMA',
 'BOTTLE_1,5_SAFIA',
 'BOTTLE_1,5_MARWA',
 'BOTTLE_0,5_TIBA',
 'CAN_0,24_COCA',
 'BOTTLE_2,0_DENYA',
 'CAN_0,24_FANTA',
 'BOTTLE_1,5_TIJEN',
 'CAN_0,24_ORANGINA',
 'BOTTLE_0,5_TIJEN',
 'BOTTLE_0,5_COCA',
 'BOTTLE_0,5_BEYA',
 'BOTTLE_2,0_FOURAT',
 'BOTTLE_0,5_DELICE',
 'BOTTLE_0,5_AQUALINE',
 'CAN_0,24_APLA',
 'BOTTLE_1,5_SABRINE',
 'BOTTLE_1,5_BARGOU',
 'BOTTLE_0,5_MIRA',
 'BOTTLE_1,5_COCA',
 'BOTTLE_0,5_DIMA',
 'CAN_0,24_BOGACIDRE']

class RecyclingSession:
    def __init__(self):
        self.authentication = QRCodeAuthentication()
        self.recyclableItemList = {}
        self.bottleCount = 0
        self.canCount = 0
        self.total_recompense = 0.0

    def update_total_recompense(self):
        recompense_per_bottle = 0.3
        recompense_per_can = 0.2
        self.total_recompense = self.bottleCount*recompense_per_bottle + self.canCount*recompense_per_can
    
    def persistRecyclingSession(self):
        URL_TO_PERSIST_RECYCLING_TRASACTION = "https://rvm-production.up.railway.app/rvm/api/recyclingTransaction/add"
        request = {}
        request['rvm'] = 1
        request['transactionDate'] = datetime.now().isoformat()
        request['totalRecompense'] = self.total_recompense
        # Convert the JSON data to a string
        if (self.authentication.is_authenticated):
            request['client'] = self.authentication.id
        json_request = json.dumps(request)
        headers = {
            "Content-Type": "application/json"
            }
        # Make the POST request
        response = requests.post(URL_TO_PERSIST_RECYCLING_TRASACTION, headers=headers, data=json_request)


        URL_TO_PERSIST_RECYCLING_HISTORY = "https://rvm-production.up.railway.app/rvm/api/recyclingHistory/add"

        request = []
        recyclingTransaction_id = response.json()["id"]
        for rerecyclableItem in self.recyclableItemList.keys():
            recyclingHistory = {}
            recyclingHistory['recyclingTransaction'] = recyclingTransaction_id
            recyclingHistory['recyclableItem'] = classes.index(rerecyclableItem) + 1
            recyclingHistory['quantity'] = self.recyclableItemList[rerecyclableItem]
            request.append(recyclingHistory)
            
        json_request = json.dumps(request)
        headers = {
            "Content-Type": "application/json"
            }
        # Make the POST request
        print(json_request)
        response = requests.post(URL_TO_PERSIST_RECYCLING_HISTORY, headers=headers, data=json_request)

        print(response)
        return response
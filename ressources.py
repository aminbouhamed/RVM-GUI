from recyclingSession import RecyclingSession
import tflite_runtime.interpreter as tflite
import tensorflow as tf

def startNewRecyclingSession():
    global currentRecyclingSession
    currentRecyclingSession = RecyclingSession()

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


# Define global variables for the models
object_detection_interpreter = None
volume_brand_classification_interpreter = None

def load_object_detection_model():
    global object_detection_interpreter
    object_detection_interpreter = tflite.Interpreter('models/object_detection_model_tflite/saved_model/object_detection_model.tflite')
    object_detection_interpreter.allocate_tensors()

def load_volume_brand_classification_model():
    global volume_brand_classification_interpreter
    volume_brand_classification_interpreter = tflite.Interpreter(model_path="models/volume_brand_classification_model_tflite.tflite")
    volume_brand_classification_interpreter.allocate_tensors()

def load_models():
    load_object_detection_model()
    load_volume_brand_classification_model()

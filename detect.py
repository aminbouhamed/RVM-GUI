import requests


def load_labels(path='models/object_detection_model_tflite/labels.txt'):
  #Loads the labels file. Supports files with or without index numbers.
  with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    labels = {}
    for row_number, content in enumerate(lines):
      pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
      if len(pair) == 2 and pair[0].strip().isdigit():
        labels[int(pair[0])] = pair[1].strip()
      else:
        labels[row_number] = pair[0].strip()
  return labels

def set_input_tensor(interpreter, image):
  #Sets the input tensor.
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = np.expand_dims(image, axis=0)

def get_output_tensor(interpreter, index):
  #Returns the output tensor at the given index
  output_details = interpreter.get_output_details()[int(index)]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor

def detect_objects(interpreter, image, threshold):
  #Returns a list of detection results, each a dictionary of object info.
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  # Get all output details
  boxes = get_output_tensor(interpreter, 1)
  classes = get_output_tensor(interpreter, 3)
  scores = get_output_tensor(interpreter, 0)
  count = int(get_output_tensor(interpreter, 2))
  results = []
  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
  return results


def object_detection(img_file):
   """ URL_TO_OBJECT_DETECTION = "http://192.168.1.16/object_detection"
    response = requests.post(URL_TO_OBJECT_DETECTION, files=img_file)
    return response
    """
  labels = load_labels()
  _, input_height, input_width, _ = ressources.object_detection_interpreter.get_input_details()[0]['shape']
  res = detect_objects(ressources.object_detection_interpreter, img, 0.4)
  print(res)
  return [obj['class_id'] for obj in res]
    

def volume_brand_classification(img_file):
  """URL_TO_VOLUME_BRAND_CLASSIFICATION = "http://192.168.1.16/volume_brand_classification"
  response = requests.post(URL_TO_VOLUME_BRAND_CLASSIFICATION, files=img_file)
  return response"""
  input_details = ressources.volume_brand_classification_interpreter.get_input_details()
  output_details = ressources.volume_brand_classification_interpreter.get_output_details()
  input_shape = input_details[0]['shape']
  img = img/255.0
  img = img.astype(np.float32)
  img = np.expand_dims(img, axis=0)
  ressources.volume_brand_classification_interpreter.set_tensor(input_details[0]['index'], img)
  ressources.volume_brand_classification_interpreter.invoke()
  output_data = ressources.volume_brand_classification_interpreter.get_tensor(output_details[0]['index'])
  predicted_class = np.argmax(output_data)
  print(ressources.classes[predicted_class])
  return ressources.classes[predicted_class]
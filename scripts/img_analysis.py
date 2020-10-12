from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("../models/modelo_moedas_igor.h5") #copiado do models p/ facilitar nome
detector.setJsonPath("../models/json/detection_config.json") #como esse n muda o nome, faz ref direta
detector.loadModel()
path_in = "../images_in/"
path_out = "../images_out/"
filename = "real-2.jpg"
detections = detector.detectObjectsFromImage(input_image=path_in+filename, output_image_path=path_out+filename)
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
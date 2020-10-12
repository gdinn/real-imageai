from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="1real")
metrics = trainer.evaluateModel(
  model_path="../custom_model/1real/models", 
  json_path="../custom_model/1real/json/detection_config.json", 
  iou_threshold=0.5, object_threshold=0.3, 
  nms_threshold=0.5
)
print(metrics)
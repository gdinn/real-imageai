from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="../custom_model/1real")
trainer.setTrainConfig(
  object_names_array=["1real"], 
  num_experiments=30,
  train_from_pretrained_model="../models/yolo.h5"
)
trainer.trainModel()

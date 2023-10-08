import os
import numpy as np
import cv2
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer


def predictUsingModel(imagename):
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 4
    cfg.MODEL.WEIGHTS = "model_final.pth"
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
    predictor = DefaultPredictor(cfg)
    img = cv2.imread(imagename)
    outputs = predictor(img)
    v = Visualizer(img[:, :, ::-1],
                   {"thing_classes": ['Arduino_Nano', 'ESP8266', 'Heltec_ESP32_Lora', 'Raspberry_Pi_3']},
                   scale=0.8,
                   instance_mode=ColorMode.SEGMENTATION
                   )
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    cv2.imwrite(imagename, cv2.cvtColor(v.get_image()[:, :, ::-1], cv2.COLOR_BGR2RGB))
    print("completed")

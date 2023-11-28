import contextlib
from copy import copy
from pathlib import Path

import cv2
import numpy as np
import pytest
import torch
from PIL import Image
from torchvision.transforms import ToTensor

from ultralytics import RTDETR, YOLO
from ultralytics.cfg import TASK2DATA
from ultralytics.data.build import load_inference_source
from ultralytics.utils import ASSETS, DEFAULT_CFG, LINUX, MACOS, ONLINE, ROOT, SETTINGS, WINDOWS
from ultralytics.utils.downloads import download
from ultralytics.utils.torch_utils import TORCH_1_9

CFG = 'ultralytics/cfg/models/v8/my_yolov8_CBAM.yaml'
SOURCE = ASSETS / 'bus.jpg'


def test_model_forward():
    model = YOLO(CFG)
    model(source=None, imgsz=32, augment=True)  # also test no source and augment
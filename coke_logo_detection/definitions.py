import os

DEBUG = False
PATH_PKG = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(PATH_PKG, "coke_model/cokelogo.xml")
IMAGE_DIR = os.path.join(PATH_PKG,"image")
IMAGE_PATH = os.path.join(PATH_PKG,'image/coke.jpg')
CROPPED_IMAGE = os.path.join(IMAGE_DIR,"cropped_image.jpg")
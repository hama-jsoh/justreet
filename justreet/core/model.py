from parser import SceneParser, ObjectDetector


# 모델 초기화
class YOLOv5(ObjectDetector):
    def train(self):
        print("train2")


class ResNet(SceneParser):
    def train(self):
        print("train2")
from justreet import Justreet
from model import ResNet, YOLOv5


class SPTrainer(Justreet):
    def __init__(self) -> None:
        self.use_resnet = ResNet()

    def display(self):
        print("train...")
        

class ODTrainer(Justreet):
    def __init__(self) -> None:
        self.use_yolov5 = YOLOv5()
    
    def display(self):
        print("train...")


if __name__ == "__main__":
    sp = SPTrainer()
    od = ODTrainer()

    sp.TrainSP()
    od.TrainOD()
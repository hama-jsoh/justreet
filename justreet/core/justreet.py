from abc import ABCMeta, abstractmethod


class Justreet(metaclass=ABCMeta):
    def TrainSP(self):
        self.use_resnet.train()

    def TrainOD(self):
        self.use_yolov5.train()

    @abstractmethod
    def display(self):
        pass
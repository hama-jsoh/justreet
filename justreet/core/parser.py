from abc import ABCMeta, abstractmethod


class SceneParser(metaclass=ABCMeta):
    @abstractmethod
    def train(self):
        pass


class ObjectDetector(metaclass=ABCMeta):
    @abstractmethod
    def train(self):
        pass
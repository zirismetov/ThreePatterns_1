from abc import ABCMeta, abstractmethod

import args as args
import kwargs as kwargs


class IObservable (metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """subscri"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """subscri"""
    @staticmethod
    @abstractmethod
    def notify(observer):
        """subscri"""

class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(*args, **kwargs)

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        """Recieve"""

class Observer(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, *args, **kwargs):
        print("we know what you are doing", args, kwargs)

subject = Subject()
obs = Observer(subject)
subject.notify("Hello city")





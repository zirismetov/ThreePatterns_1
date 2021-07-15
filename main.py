from abc import ABCMeta,abstractmethod
from random import seed
from random import randint
import random

#Observer
class IObservable (metaclass=ABCMeta):

    @abstractmethod
    def subscribe(observer):
        """subscri"""

    @abstractmethod
    def unsubscribe(observer):
        """subscri"""

    @abstractmethod
    def alert(observer):
        """subscri"""

class IObserver(metaclass=ABCMeta):

    @abstractmethod
    def alert(observable, *args, **kwargs):
        """Recieve"""

class InventorySingleton():
    __instance = None
    def __init__(self, gold):
        if InventorySingleton.__instance != None:
            raise Exception("Only one inventory allowed to use!")
        else:
            self.gold = gold
            InventorySingleton.__instance = self

class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def alert(self, *args, **kwargs):
        for observer in self._observers:
            observer.alert(*args, **kwargs)
            break


class RandomAction:
    value = 0
    valueG = 0
    @staticmethod
    def randomChoice():
        value = random.randint(0, 2)
        return int(value)
    @staticmethod
    def randomGold():
        valueG = random.randint(1, 10)
        return int(valueG)



class Goblin(IObserver):

    def act(self):


        choice = RandomAction.randomChoice()
        amount = RandomAction.randomGold()
        try:
            if choice == 0:
                print(f" View gold in inventory: {p.gold}")
            elif choice == 1:
                p.gold = p.gold + amount
                print(f"Gold in inventory was increased: {p.gold}")
            elif choice ==2:
                p.gold = p.gold - amount
                subject.alert(p.gold)
        except AssertionError as _e:
            print("error : " + _e)


    def __init__(self, observable):
        observable.subscribe(self)


    def alert(self, *args, **kwargs):
        print("We know what you are doing (-), gold left: ", args, kwargs)





        # print("factory : " + t.get_type())




subject = Subject()
g1 = Goblin(subject)
g2 = Goblin(subject)
g3 = Goblin(subject)
# Default gold 100
p = InventorySingleton(100)
g1.act()
g2.act()
g3.act()















# from abc import ABCMeta,abstractmethod
# from random import seed
# from random import randint
import random


#
# #Observer
# class IObservable (metaclass=ABCMeta):
#
#     @abstractmethod
#     def subscribe(observer):
#         """subscri"""
#
#     @abstractmethod
#     def unsubscribe(observer):
#         """subscri"""
#
#     @abstractmethod
#     def alert(observer):
#         """subscri"""
#
# class IObserver(metaclass=ABCMeta):
#
#     @abstractmethod
#     def alert(observable, *args):
#         """Recieve"""
#
# class InventorySingleton():
#     __instance = None
#     def __init__(self, gold):
#         if InventorySingleton.__instance != None:
#             raise Exception("Only one inventory allowed to use!")
#         else:
#             self.gold = gold
#             InventorySingleton.__instance = self
#
# class Subject(IObservable):
#     def __init__(self):
#         self._observers = set()
#
#     def subscribe(self, observer):
#         self._observers.add(observer)
#
#     def unsubscribe(self, observer):
#         self._observers.remove(observer)
#
#     def alert(self, *args):
#         for observer in self._observers:
#             observer.alert(*args)
#             break
#
#
# class RandomAction:
#     value = 0
#     valueG = 0
#     @staticmethod
#     def randomChoice():
#         value = random.randint(0, 2)
#         return int(value)
#     @staticmethod
#     def randomGold():
#         valueG = random.randint(1, 10)
#         return int(valueG)
#
#
#
# class Goblin(IObserver):
#
#     def act(self):
#
#
#         choice = RandomAction.randomChoice()
#         amount = RandomAction.randomGold()
#         try:
#             if choice == 0:
#                 print(f" View gold in inventory: {p.gold}")
#             elif choice == 1:
#                 p.gold = p.gold + amount
#                 print(f"Gold in inventory was increased: {p.gold}")
#             elif choice ==2:
#                 p.gold = p.gold - amount
#                 subject.alert(p.gold)
#         except AssertionError as _e:
#             print("error : " + _e)
#
#
#     def __init__(self, observable):
#         observable.subscribe(self)
#
#
#     def alert(self, *args, **kwargs):
#         print("We know what you are doing (-), gold left: ", args, kwargs)
#
#
#         # print("factory : " + t.get_type())
#
#
#
#
# subject = Subject()
# g1 = Goblin(subject)
# g2 = Goblin(subject)
# g3 = Goblin(subject)
# # Default gold 100
# p = InventorySingleton(100)
# g1.act()
# g3.act()
# g2.act()

class SharedResources():
    __instance = None

    def __init__(self):
        self.gold = 10
        self.__listOfobservers = []
        if SharedResources.__instance == None:
            SharedResources.__instance = self

    def print_gold(self):
        return self.gold

    def add_observers(self, observer):
        self.__listOfobservers.append(observer)

    def notify(self):
        # Iterating through list of subscribers and calling alert methods in each object
        for obs in self.__listOfobservers:
            obs()

    def act_factory(self):
        choice = int(random.randint(0, 2))
        # choice = 2
        # print(choice)
        if choice == 0:
            return gActView().act()
        elif choice == 1:
            return gActAdd().act()
        elif choice == 2:
            return gActRemove().act()

    @staticmethod
    def get_instance():
        if SharedResources.__instance == None:
            SharedResources()
        return SharedResources.__instance


class Goblin():
    def __init__(self, action):
        self.action = action.lower()
        self.extra = False

    def act(self):
        SharedResources.get_instance().add_observers(self.alert)

        if self.action == "view":
            print(SharedResources.get_instance().print_gold())

        elif self.action == "add":
            SharedResources.get_instance().gold += 1
            print(SharedResources.get_instance().print_gold())

        elif self.action == "remove":
            SharedResources.get_instance().gold -= 2
            # notifying other objects about gold reduction
            SharedResources.get_instance().notify()

    def alert(self):
        print(
            f"we all know what you are doing! Obj: {str(self)}, gold left: {SharedResources.get_instance().print_gold()}")
        SharedResources.get_instance().act_factory()


class gActView(Goblin):
    def __init__(self):
        pass

    def act(self):
        print(f"NEW View method  {SharedResources.get_instance().print_gold()}")


class gActAdd(Goblin):
    def __init__(self):
        pass

    def act(self):
        SharedResources.get_instance().gold += 1
        print(f"NEW Method: add + {SharedResources.get_instance().print_gold()}")


class gActRemove(Goblin):
    def __init__(self):
        pass

    def act(self):
        SharedResources.get_instance().gold -= 2
        print(f"NEW Method: remove - {SharedResources.get_instance().print_gold()}")



g2 = Goblin("add")
g3 = Goblin("adD")
g1 = Goblin("remove")

g2.act()
g3.act()
g1.act()


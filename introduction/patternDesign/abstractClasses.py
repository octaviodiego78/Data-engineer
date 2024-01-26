
from abc import abstractmethod, ABC
from typing import List

#Strategy pattern 1
#Abstract Classes 
class AbstractVehicle(ABC):
    brand: str
    colour: str
    motor: str   #Sons neeed to have all this variables

    #To use a class that is a son from this class you need to have the go_forward method in the son class
    #The method doesn't need to do the same just to be defined on all instances

    @abstractmethod
    def go_forward(self):
        raise NotImplementedError("Not implemented")
    

class Car(AbstractVehicle):

    def __init__(self, brand: str, colour: str, motor: str):
        self.brand = brand
        self.colour = colour
        self.motor = motor

    def go_forward(self):
        ...

car1 = Car("BMW","red","v2")


###-----------------



class AbstractSortingAlgorithm(ABC):

    @abstractmethod
    def sort(arr: List[int])-> List[int]:
        raise NotImplementedError("Not implemented")
    
class FirstSortingAlgorithm(AbstractSortingAlgorithm):

    def __init__(self, arr: List[int]):
        self.arr = arr

    def sort(self):
        print("Initial array:",self.arr)
        res = []
        temp_arr = self.arr.copy()

        for i in range(len(self.arr)):
            res.append(min(temp_arr))
            temp_arr.remove(min(temp_arr))

        self.arr = res


class SecondSortingAlgorithm(AbstractSortingAlgorithm):
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.sort_helper(self.arr)   #This helps to make sure a method is there so code doesn't break
                                    #However the function could call another better function to do the same

    @staticmethod
    def sort_helper(arr):
        #Insert another sorting method
        ...


def _sort(arr: List[int], strategy: AbstractSortingAlgorithm):
    """
    _sort function receives an array and recieves a class that is a son from AbstractSortingAlgorithm
    cause we know sort is an abstract method and all sons from it should have said methods
    """
    strat_obj =strategy(arr)
    strat_obj.sort()
    print("Sorted array:",strat_obj.arr)


_sort([5,3,6,7,4,9,1,2,1],FirstSortingAlgorithm)


        

    


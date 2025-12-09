from abc import ABC, abstractmethod


class RestaurantLister(ABC):

    @abstractmethod
    def listRestaurants(self, list, order):
        pass


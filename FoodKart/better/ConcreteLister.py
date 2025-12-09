from better.interfaces import RestaurantLister


class RatingsLister(RestaurantLister):

    def listRestaurants(self, list, order):
        desc = True
        if order == "asc":
            desc = False
        list = sorted(list, key=lambda x: x.rating, reverse=desc)
        return list


class PricesLister(RestaurantLister):

    def listRestaurants(self, list, order):
        desc = True
        if order == "asc":
            desc = False
        list = sorted(list, key=lambda x: x.dish.price, reverse=desc)
        return list
class IceCream:
    zero_scoops = 0
    max_scoops = 3

    def __init__(self):
        self.scoops = self.zero_scoops

    def add(self, scoops):
        self.scoops += scoops
        if self.scoops > self.max_scoops:
            excess = self.scoops - self.max_scoops
            self.scoops = self.max_scoops
            print(f"Too many scoops, {excess} fell down!!!")
        else:
            print(f"{scoops} added")

    def eat(self, scoops):
        if self.scoops < scoops:
            print("cannot eat invisible scoops")
        else:
            self.scoops -= scoops
            print(f"{scoops} eaten")


class IceCreamTruck:
    def __init__(self):
        self.sold = 0

    def order(self, ice_cream, scoops):
        ice_cream = IceCream()
        ice_cream.add(scoops)
        self.sold += scoops

    def add(self, scoops):
        ice_cream = IceCream()
        ice_cream.add(scoops)
        self.sold += scoops


class DeluxeIceCreamTruck(IceCreamTruck):
    def order(self, scoops):
        pass







class Tire:
    def needs_service(self, wear_array):
        raise NotImplementedError("This method needs to be overridden in subclasses")

class CarriganTire(Tire):
    def needs_service(self, wear_array):
        return any(wear >= 0.9 for wear in wear_array)

class OctoprimeTire(Tire):
    def needs_service(self, wear_array):
        return sum(wear_array) >= 3

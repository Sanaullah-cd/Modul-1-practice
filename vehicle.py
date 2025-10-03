

class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def engine_start(self):
        return f"{self.year} {self.make} {self.model}: Engine started."

    def engine_stop(self):
        return f"{self.year} {self.make} {self.model}: Engine stopped."

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    """Derived class for cars"""
    def __init__(self, make, model, year, doors: int, transmission: str):
        super().__init__(make, model, year)
        self.doors = doors
        self.transmission = transmission

    def __str__(self):
        return f"Car: {super().__str__()} | {self.doors} doors, {self.transmission} transmission"


class Motorcycle(Vehicle):
    """Derived class for motorcycles"""
    def __init__(self, make, model, year, body_type: str, has_storage_box: bool):
        super().__init__(make, model, year)
        self.body_type = body_type
        self.has_storage_box = has_storage_box

    def __str__(self):
        storage = "with storage box" if self.has_storage_box else "no storage box"
        return f"Motorcycle: {super().__str__()} | {self.body_type}, {storage}"


class Garage:
    """Garage uses composition to hold vehicles"""
    def __init__(self, name: str):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def list_vehicles(self):
        return [str(v) for v in self.vehicles]

    def __str__(self):
        return f"Garage '{self.name}' with {len(self.vehicles)} vehicles."


class Fleet:
    """Fleet uses composition to hold garages"""
    def __init__(self):
        self.garages = []

    def add_garage(self, garage: Garage):
        self.garages.append(garage)

    def remove_garage(self, garage: Garage):
        if garage in self.garages:
            self.garages.remove(garage)

    def search_vehicle(self, keyword: str):
        results = []
        for garage in self.garages:
            for vehicle in garage.vehicles:
                if keyword.lower() in str(vehicle).lower():
                    results.append((garage.name, str(vehicle)))
        return results

    def __str__(self):
        return f"Fleet with {len(self.garages)} garages."
    

# --- Testing the application ---
if __name__ == "__main__":
    # Create vehicles
    car1 = Car("Toyota", "Camry", 2020, 4, "Automatic")
    car2 = Car("Honda", "Civic", 2019, 4, "Manual")
    moto1 = Motorcycle("Yamaha", "R15", 2021, "Sport", False)
    moto2 = Motorcycle("Harley-Davidson", "Street 750", 2018, "Cruiser", True)

    # Create garages
    garage1 = Garage("Downtown Garage")
    garage2 = Garage("Airport Garage")

    # Add vehicles to garages
    garage1.add_vehicle(car1)
    garage1.add_vehicle(moto1)
    garage2.add_vehicle(car2)
    garage2.add_vehicle(moto2)

    # Create fleet and add garages
    fleet = Fleet()
    fleet.add_garage(garage1)
    fleet.add_garage(garage2)

    # Display garages and vehicles
    print(garage1)
    for v in garage1.list_vehicles():
        print(" -", v)

    print(garage2)
    for v in garage2.list_vehicles():
        print(" -", v)

    # Test search
    print("\nSearch results for 'Honda':")
    results = fleet.search_vehicle("Honda")
    for g, v in results:
        print(f"Found in {g}: {v}")

    # Remove vehicle and garage
    garage1.remove_vehicle(moto1)
    fleet.remove_garage(garage2)

    print("\nAfter removal:")
    print(garage1)
    print(fleet)

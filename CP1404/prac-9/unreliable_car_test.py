from unreliable_car import UnreliableCar


def test_unreliable_car():
    car = UnreliableCar("Unreliable Car", 100, 50)
    distance = 50

    print(f"{car.name}:")
    print(f"Attempting to drive {distance} km...")
    distance_driven = car.drive(distance)
    if distance_driven == 0:
        print("The car failed to start!")
    else:
        print(f"The car drove {distance_driven} km.")


test_unreliable_car()


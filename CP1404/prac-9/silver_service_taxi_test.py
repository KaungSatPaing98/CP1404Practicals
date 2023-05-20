from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    taxi = SilverServiceTaxi("Hummer", 200, 2.46, 4)
    distance = 18

    print(f"{taxi.name}:")
    print(f"Attempting to drive {distance} km...")
    taxi.drive(distance)
    fare = taxi.get_fare()
    print(f"The fare for the trip is ${fare:.2f}.")


test_silver_service_taxi()


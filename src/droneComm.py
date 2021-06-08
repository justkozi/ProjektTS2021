from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the Vehicle (in this case a simulator running the same computer)
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)

waypoints = [
    {"id": 1, "lat": 37.619198, "lon": -122.376186, "alt": 25.000000, "Colour": "A"},
    {"id": 2, "lat": 37.618968, "lon": -122.375626, "alt": 25.000000, "Colour": "A"},
    {"id": 3, "lat": 37.618712, "lon": -122.375034, "alt": 25.000000, "Colour": "B"},
    {"id": 4, "lat": 37.618482, "lon": -122.374486, "alt": 25.000000, "Colour": "X"},
    {"id": 5, "lat": 37.618244, "lon": -122.373948, "alt": 25.000000, "Colour": "X"},
    {"id": 6, "lat": 37.618593, "lon": -122.373668, "alt": 25.000000, "Colour": "X"},
    {"id": 7, "lat": 37.618849, "lon": -122.374141, "alt": 25.000000, "Colour": "A"},
    {"id": 8, "lat": 37.619113, "lon": -122.374722, "alt": 25.000000, "Colour": "X"},
    {"id": 9, "lat": 37.619326, "lon": -122.375239, "alt": 25.000000, "Colour": "B"},
    {"id": 10, "lat": 37.619530, "lon": -122.375831, "alt": 25.000000, "Colour": "B"},
    {"id": 11, "lat": 37.619863, "lon": -122.375605, "alt": 25.000000, "Colour": "B"},
    {"id": 12, "lat": 37.619684, "lon": -122.374916, "alt": 25.000000, "Colour": "X"},
    {"id": 13, "lat": 37.619496, "lon": -122.374410, "alt": 25.000000, "Colour": "X"},
    {"id": 14, "lat": 37.619283, "lon": -122.373819, "alt": 25.000000, "Colour": "A"},
    {"id": 15, "lat": 37.619113, "lon": -122.373248, "alt": 25.000000, "Colour": "B"},
    {"id": 16, "lat": 37.619377, "lon": -122.373076, "alt": 25.000000, "Colour": "A"},
    {"id": 17, "lat": 37.619616, "lon": -122.373776, "alt": 25.000000, "Colour": "A"},
    {"id": 18, "lat": 37.619854, "lon": -122.374346, "alt": 25.000000, "Colour": "X"},
    {"id": 19, "lat": 37.620008, "lon": -122.374755, "alt": 25.000000, "Colour": "B"},
    {"id": 20, "lat": 37.620246, "lon": -122.375293, "alt": 25.000000, "Colour": "X"},
    {"id": 21, "lat": 37.620510, "lon": -122.375067, "alt": 25.000000, "Colour": "B"},
    {"id": 22, "lat": 37.620400, "lon": -122.374507, "alt": 25.000000, "Colour": "A"},
    {"id": 23, "lat": 37.620229, "lon": -122.373926, "alt": 25.000000, "Colour": "B"},
    {"id": 24, "lat": 37.620221, "lon": -122.373915, "alt": 25.000000, "Colour": "B"},
    {"id": 25, "lat": 37.620127, "lon": -122.373550, "alt": 25.000000, "Colour": "X"},
    {"id": 26, "lat": 37.619956, "lon": -122.373141, "alt": 25.000000, "Colour": "B"}
]

visited = []


def start_mission():
    arm_and_takeoff(20)
    return True


def points_avalible():
    if (len(waypoints) > len(visited)):
        return True
    else:
        return False


def fly_to_next():
    for point in waypoints:
        if point not in visited:
            go_to_position(point["id"], point["lat"], point["lon"], point["alt"], 5)
            visited.append(point)
            # print(visited)
            return True


def check_current_colour():
    return visited[-1]["Colour"]


def end_mission():
    print("Returning to Launch")
    vehicle.mode = VehicleMode("RTL")

    while (vehicle.armed):
        print('.', end='')
        time.sleep(1)

    # Close vehicle object before exiting script
    print("Close vehicle object")
    vehicle.close()


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        # print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


def go_to_position(id, lat, lon, alt, spd=20.0):
    vehicle.airspeed = spd
    point = LocationGlobalRelative(lat, lon, alt)
    vehicle.simple_goto(point)

    while True:
        # print("Position: \nLat: %s\nLon: %s\nAlt: %s" % (
        #     str(vehicle.location.global_relative_frame.lat),
        #     str(vehicle.location.global_relative_frame.lon),
        #     str(vehicle.location.global_relative_frame.alt)))
        # Break and return from function just below target altitude.

        if abs(vehicle.location.global_relative_frame.alt - alt) < 0.5 and \
                abs(vehicle.location.global_relative_frame.lat - lat) < 0.0005 and \
                abs(vehicle.location.global_relative_frame.lon - lon) < 0.0005:
            print("Reached position ", id)
            break
        time.sleep(1)

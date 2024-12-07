import math
import csv
import time
import random  # For simulating ToF data (replace with real sensor data)

# File paths
output_file = '../data/updated_map.csv'

# Initialize robot's current position and angle
current_position = [0.0, 0.0]  # (x, y) in millimeters
theta = 0.0  # Angle in degrees (robot's facing direction)

# Initialize output file with headers
def initialize_output_file():
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['robot_x', 'robot_y', 'tof_x', 'tof_y', 'depth'])

# Update robot's position based on movement
def update_position(move_distance):
    global current_position, theta
    current_position[0] += move_distance * math.cos(math.radians(theta))
    current_position[1] += move_distance * math.sin(math.radians(theta))

# Simulate appending ToF data for the robot's current position
def log_data(position):
    # Simulated ToF data as a 2D grid
    tof_data = [[random.randint(200, 2000) for _ in range(10)] for _ in range(10)]  # Replace with actual ToF data
    with open(output_file, 'a', newline='') as file:
        writer = csv.writer(file)
        for y, row in enumerate(tof_data):
            for x, depth in enumerate(row):
                # Adjusted ToF positions relative to robot's current position
                writer.writerow([position[0], position[1], position[0] + x, position[1] + y, depth])

# Simulate robot movement and log ToF data
def simulate_movement():
    initialize_output_file()  # Ensure the file is ready before logging
    for step in range(10):  # Simulate 10 steps of movement
        move_distance = 100.0  # Example: Move 100 mm per step (replace with actual distance)
        update_position(move_distance)  # Update robot's position
        log_data(current_position)  # Log ToF data at the new position
        print(f"Step {step + 1}: Robot moved to {current_position}")
        time.sleep(1)  # Simulate delay between updates

if __name__ == "__main__":
    simulate_movement()

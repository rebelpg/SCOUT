import os
import csv
import numpy as np
import ArducamDepthCamera as ac
import time

# File to store depth and robot position data
output_file = '../data/sensor_data.csv'

# Ensure data directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Dummy odometry values for SCOUT (replace with real calculations)
robot_x, robot_y = 0, 0  # Initial position

def log_tof_data():
    global robot_x, robot_y  # Use global variables for position tracking
    
    cam = ac.ArducamCamera()
    ret = cam.open(ac.TOFConnect.CSI, 0)
    if ret != 0:
        print("Failed to open camera. Error code:", ret)
        return

    ret = cam.start(ac.TOFOutput.DEPTH)
    if ret != 0:
        print("Failed to start camera. Error code:", ret)
        cam.close()
        return

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['timestamp', 'robot_x', 'robot_y', 'x', 'y', 'depth'])

        print("Logging data... Press Ctrl+C to stop.")
        try:
            while True:
                # Simulate robot movement (update position; replace with real odometry logic)
                robot_x += 0.1  # Move 0.1 units in X
                robot_y += 0.1  # Move 0.1 units in Y

                frame = cam.requestFrame(2000)
                if frame and isinstance(frame, ac.DepthData):
                    depth_buf = frame.getDepthData()
                    for y, row in enumerate(depth_buf):
                        for x, depth in enumerate(row):
                            # Log timestamp, robot position, and depth data
                            writer.writerow([time.time(), robot_x, robot_y, x, y, depth])
                    cam.releaseFrame(frame)

                # Pause to simulate sampling rate (adjust as needed)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nData logging stopped.")
    
    cam.stop()
    cam.close()
    print(f"Data logged to {output_file}")

if __name__ == "__main__":
    log_tof_data()

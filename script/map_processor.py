import csv
import matplotlib.pyplot as plt

# Input and output file paths
input_file = '../data/sensor_data.csv'
output_file = '../data/processed_map.png'

def process_map():
    points = []

    # Check if the input file exists and read data
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            if not header or len(header) < 3:
                raise ValueError("Input file does not have the correct header: ['x', 'y', 'depth']")

            for row in reader:
                if len(row) != 3:
                    continue  # Skip invalid rows
                x, y, depth = map(float, row)
                points.append((x, y))
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error while reading the input file: {e}")
        return

    # Generate and save the map
    if points:
        for x, y in points:
            plt.scatter(x, y, c='blue', s=1)  # Adjust marker size for better visibility

        plt.title("Mapped Environment")
        plt.xlabel("X (mm)")
        plt.ylabel("Y (mm)")
        plt.savefig(output_file)
        plt.show()
        print(f"Map saved as '{output_file}'")
    else:
        print("No valid data points found to plot.")

if __name__ == "__main__":
    process_map()

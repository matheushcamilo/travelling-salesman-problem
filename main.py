from tsp import brute_force_tsp
from utils import read_points_from_file


def main():
    points = read_points_from_file()
    if not points:
        print("No valid coordinates found in file")
        return

    best_route, min_distance = brute_force_tsp(points)

    print("\nBest route found:")
    for point in best_route:
        print(point)

    print(f"\nMin distance: {min_distance:.2f}")


if __name__ == "__main__":
    main()

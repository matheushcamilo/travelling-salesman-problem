def read_points_from_file(filename="delivery_points.txt"):
    """Reads points from file and returns a list of coordinates"""
    points = []
    try:
        with open(filename, "r") as file:
            for line in file:
                x, y = map(float, line.strip().split(","))
                points.append((x, y))
        return points
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

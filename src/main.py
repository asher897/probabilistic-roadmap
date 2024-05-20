from prm import PRM, Coordinate
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    # Establish coordinates
    x_range = (0, 100)
    y_range = (0, 100)
    obs_coords = [
        (Coordinate(5, 30), Coordinate(15, 15)),
        (Coordinate(30, 60), Coordinate(40, 2)),
        (Coordinate(50, 80), Coordinate(70, 60)),
    ]

    # obs_coords = [
    #     (Coordinate(20, 50), Coordinate(20, 10)),
    #     (Coordinate(20, 50), Coordinate(90, 50)),
    #     (Coordinate(30, 40), Coordinate(40, 30)),
    # ]
    start_point = Coordinate(10, 10)
    goal_point = Coordinate(80, 30)

    # Create prm instance
    prm_instnace = PRM(x_range, y_range, obs_coords)

    # Run algorithm
    prm_instnace.generate_map(start_point, goal_point)


if __name__ == "__main__":
    main()
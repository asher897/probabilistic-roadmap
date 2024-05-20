from prm import PRM, Coordinate


def main():
    starting_and_goal = input()
    coords = starting_and_goal.split(";")
    start_point = Coordinate(int(coords[0].split(",")[0]), int(coords[0].split(",")[1]))
    goal_point = Coordinate(int(coords[1].split(",")[0]), int(coords[1].split(",")[1]))

    obs_coords = []
    obs_coord = input()
    while obs_coord != str(-1):
        coords = obs_coord.split(";")
        tl_coords = coords[0].split(",")
        br_coords = coords[1].split(",")
        obs_coords.append((
            Coordinate(int(tl_coords[0]), int(tl_coords[1])),
            Coordinate(int(br_coords[0]), int(br_coords[1]))
        ))
        obs_coord = input()




    # Establish coordinates
    x_range = (0, 100)
    y_range = (0, 100)
    # obs_coords = [
    #     (Coordinate(5, 30), Coordinate(15, 15)),
    #     (Coordinate(30, 60), Coordinate(40, 2)),
    #     (Coordinate(50, 80), Coordinate(70, 60)),
    # ]
    #
    # # obs_coords = [
    # #     (Coordinate(20, 50), Coordinate(20, 10)),
    # #     (Coordinate(20, 50), Coordinate(90, 50)),
    # #     (Coordinate(30, 40), Coordinate(40, 30)),
    # # ]
    # start_point = Coordinate(10, 10)
    # goal_point = Coordinate(80, 30)

    # Create prm instance
    prm_instnace = PRM(x_range, y_range, obs_coords)

    # Run algorithm
    prm_instnace.generate_map(start_point, goal_point)


if __name__ == "__main__":
    main()

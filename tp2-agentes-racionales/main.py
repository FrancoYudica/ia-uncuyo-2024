from environment import Environment


def print_environment(
        environment: Environment,
        agent_position: tuple):
    
    for row in range(environment.nrows):
        row_str = ""
        for col in range(environment.ncols):
            if env.is_cell_dirty(row, col):
                row_str += "d"
            else:
                row_str += "*"

            row_str += " "

        print(row_str)


if __name__ == "__main__":

    # Initializes environment
    n_rows = 10
    n_columns = 10
    dirt_ratio = 0.25
    environment_seed = 12345
    env = Environment(n_rows, n_columns, dirt_ratio)
    env.randomize(environment_seed)


    print_environment(env, (0, 0))

    for iteration in range(1000):
        pass

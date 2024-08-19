from environment import Environment
from agent import Agent
import random
import time
import os
import argparse

def print_environment(
        environment: Environment,
        agent_position: tuple):
    
    def print_horizontal_row(cols):
        print("--" * (cols + 1) + "-")

    print_horizontal_row(env.ncols)
    for row in range(environment.nrows):
        row_str = "| "
        for col in range(environment.ncols):
            
            if agent_position[0] == row and agent_position[1] == col:
                row_str += "A"

            elif env.is_cell_dirty(row, col):
                row_str += "◯"
            
            elif env.is_cell_walked(row, col):
                row_str += "✱"
            else:
                row_str += " "

            row_str += " "
        row_str += "|"
        print(row_str)
    print_horizontal_row(env.ncols)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Agent that cleans it's environment")

    parser.add_argument(
        '--render', 
        type=bool, 
        help="Include this flag to render the environment while agent cleans",
        default=False)
    parser.add_argument(
        '--fps', 
        type=int, 
        help='Sets the framerate. Works if render is enabled',
        default=60)
    parser.add_argument(
        '--iterations', 
        type=int, 
        help='Sets the maximum amount of iterations. By default iterations are limitless',
        default=0)
    parser.add_argument(
        '--size', 
        type=int,
        help='Sets the size of the environment N as a square NxN.',
        default=16)
    
    parser.add_argument(
        '--env_seed', 
        type=int,
        help='Sets the environment seed, used to generate the environment',
        default=0)

    parser.add_argument(
        '--dirt_ratio', 
        type=float,
        help='Sets the initial dirt ratio of the environment.',
        default=0.25)
    
    args = parser.parse_args()

    render = args.render
    fps = args.fps
    iterations_count = args.iterations
    n_rows = n_columns = args.size
    dirt_ratio = args.dirt_ratio
    environment_seed = args.env_seed
    # Initializes environment
    env = Environment(n_rows, n_columns, dirt_ratio)
    env.randomize(environment_seed)

    # Initializes agent
    agent = Agent(0, 0, env)

    # Overrides env seed with random seed
    random.seed(None)

    t0 = time.time()

    # Runs main loop
    iteration = 0
    while iterations_count == 0 or iteration < iterations_count:

        if env.dirty_cell_count == 0:
            break

        if render:
            print(f"Iteration {iteration + 1}/{iterations_count}")
            print(f"- Dirty cells {env.dirty_cell_count}")
            print(f"- Dirt ratio {env.current_dirt_ratio}")
            print(f"- Elapsed time: {time.time() - t0}")
            print_environment(env, (agent.row, agent.col))
            time.sleep(1.0 / fps)
            os.system("clear")
        agent.think()
        iteration += 1

    if env.dirty_cell_count == 0:
        print(f"Finished in iteration {iteration + 1}")
    else:
        print(f"Unable to finish after {iteration + 1} iterations")
        print(f"Remaining dirt cells: {env.dirty_cell_count}")
        print(f"Final dirt ratio: {env.current_dirt_ratio}")
        print(f"Time taken: {time.time() - t0}")
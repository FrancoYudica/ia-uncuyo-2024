from environment import Environment
from agent import Agent
import random
import time
import os

def print_environment(
        env: Environment,
        agent_position: tuple):
    
    def print_horizontal_row(cols):
        print("--" * (cols + 1) + "-")

    print_horizontal_row(env.ncols)
    for row in range(env.nrows):
        row_str = "| "
        for col in range(env.ncols):
            
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

def run_simulation(
        render,
        fps,
        iterations_count,
        env_size,
        env_seed,
        env_dirt_ratio,
        agent: Agent,
        verbose=True) -> float:
    """Runs the simulation and returns the final dirt ratio"""
    
    # Initializes environment
    env = Environment(
        env_size, 
        env_size, 
        env_dirt_ratio)
    env.randomize(env_seed)

    agent.env = env
    # Overrides env seed with random seed
    random.seed(None)

    t0 = time.time()

    # Runs main loop
    iteration = 0
    while iterations_count == 0 or iteration < iterations_count:

        env.walk_cell(agent.row, agent.col)

        if env.dirty_cell_count == 0:
            break

        if render:
            if verbose:
                print(f"Iteration {iteration + 1}/{iterations_count}")
                print(f"- Dirty cells {env.dirty_cell_count}")
                print(f"- Dirt ratio {env.current_dirt_ratio}")
                print(f"- Elapsed time: {time.time() - t0}")
            print_environment(env, (agent.row, agent.col))
            time.sleep(1.0 / fps)
            os.system("clear")
        agent.think()
        iteration += 1

    if verbose:
        if env.dirty_cell_count == 0:
            print(f"Finished in iteration {iteration + 1}")
        else:
            print(f"Unable to finish after {iteration + 1} iterations")
            print(f"Remaining dirt cells: {env.dirty_cell_count}")
            print(f"Final dirt ratio: {env.current_dirt_ratio}")
        print(f"Time taken: {time.time() - t0}")

    return env.get_performance()
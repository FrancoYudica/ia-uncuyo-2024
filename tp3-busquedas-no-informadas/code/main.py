import gymnasium as gym
from gymnasium import wrappers
from map import Map
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.random_walk import random_walk
from algorithms.ucs import ucs
from algorithms.a_star import a_star

from algorithms.walk_results import WalkResults
from common import build_path_from_actions
from plotting import plot_results, save_csv
import os
import time

def render_results(
        map: Map, 
        results: WalkResults):

    if results is None:
        return
    
    # Environment setup
    env = gym.make(
        'FrozenLake-v1', 
        desc=map.map, 
        map_name="Test", 
        is_slippery=False,
        render_mode="human")
    
    # Sets time ~ action count limit
    env = wrappers.TimeLimit(env, 1000)
    
    env.reset()

    done = truncated = False
    for action in results.actions:
        _, _, done, truncated, _ = env.step(action)
        env.render()
        time.sleep(1.0 / 5.0)
    
    if done:
        print("SUCCESS: Reached the end of the frozen lake!")

    elif truncated:
        print("FAILED: Couldn't reach the end of the lake...")


def save_results(
        results, 
        folder_name):
    plot_results(
        results=results,
        title="Time taken",
        access_result_data=lambda result: result.time_taken,
        save_filepath=f"../images/{folder_name}/time_taken.png",
        y_label="Time taken (seconds)")
    
    plot_results(
        results=results,
        title="Explored cells",
        access_result_data=lambda result: result.explored_cells,
        save_filepath=f"../images/{folder_name}/explored_cells.png",
        y_label="Explored cell count")

    plot_results(
        results=results,
        title="Actions count",
        access_result_data=lambda result: result.calculate_cost(),
        save_filepath=f"../images/{folder_name}/actions_count.png",
        y_label="Actions count")

    plot_results(
        results=results,
        title="Actions cost",
        access_result_data=lambda result: result.calculate_cost(cost_by_action=True),
        save_filepath=f"../images/{folder_name}/actions_cost.png",
        y_label="Actions cost")


if __name__ == "__main__":
    
    results = None

    algorithms = {
        "BFS": bfs,
        "DFS": lambda map: dfs(map, 900),
        "DFS Limited 10": lambda map: dfs(map, 10),
        "Random walk": lambda map: random_walk(map),
        "UCS": ucs,
        "A*": a_star
    }
    
    all_results = {algo_name: [] for algo_name in algorithms.keys()}

    for i in range(30):

        map = Map(
            n=100,
            hole_ratio=0.08,
            seed=i)

        print(f"Executing algorithms on Map(n={map.n}, hole_ratio={map.hole_ratio}, seed={map.seed})")

        for algorithm_name in algorithms:

            algorithm_function = algorithms[algorithm_name]
            print(f"    * Executing algorithm: {algorithm_name}")
            results = algorithm_function(map)

            if results is not None:
                all_results[algorithm_name].append(results)
                # render_results(map, results)
            else:
                results = WalkResults()
                all_results[algorithm_name].append(results)
                print(f"            {algorithm_name} couldn't reach goal...")

    save_csv(all_results, "../no-informada-results.csv")

    random_walk_results = all_results.pop("Random walk")

    # Non random results in all folder
    save_results(
        results=all_results,
        folder_name="all")
    
    # Random results in separated folder
    save_results(
        results={"Random walk": random_walk_results},
        folder_name="random")
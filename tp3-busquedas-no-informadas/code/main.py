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

    map = Map(
        n=100,
        hole_ratio=0.08,
        seed=10)

    print(f"Executing algorithms on Map(n={map.n}, hole_ratio={map.hole_ratio}, seed={map.seed})")
    
    for algorithm_name in algorithms:

        algorithm_function = algorithms[algorithm_name]
        print(f"    * Executing algorithm: {algorithm_name}")
        results = algorithm_function(map)

        if results is not None:
            print(f"        - Time taken {results.time_taken}")
            print(f"        - Total cost (Amount of actions) {results.calculate_cost(False)}")
            print(f"        - Total cost by actions {results.calculate_cost(True)}")
            # render_results(map, results)
        else:
            print(f"     Algorithm {algorithm_name} couldn't reach goal...")


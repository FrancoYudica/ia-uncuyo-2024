import gymnasium as gym
from gymnasium import wrappers
from map import Map
from algorithms.bfs import bfs
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
        next_state, _, done, truncated, _ = env.step(action)

        print(f"- Executed action {action} - Next state {next_state}")

        env.render()
        time.sleep(1.0 / 5.0)
    
    if done:
        print("SUCCESS: Reached the end of the frozen lake!")

    elif truncated:
        print("FAILED: Couldn't reach the end of the lake...")

    

if __name__ == "__main__":
    
    results = None

    algorithms = {
        "BFS": bfs
    }

    map = Map(
        n=100,
        hole_ratio=0.08,
        seed=10)

    for algorithm_name in algorithms:

        algorithm_function = algorithms[algorithm_name]
        print(f"Executing algorithm: {algorithm_name}")
        results = algorithm_function(map)

        if results is not None:
            print(results.time_taken)
            print(results.total_cost)
            render_results(map, results)
        else:
            print(f"Algorithm {algorithm_name} couldn't reach goal...")


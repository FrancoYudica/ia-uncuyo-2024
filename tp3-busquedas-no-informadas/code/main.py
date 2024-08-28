import gymnasium as gym
from gymnasium import wrappers
from map import Map
from algorithms.bfs import bfs
from common import build_path_from_actions


if __name__ == "__main__":
    
    map = Map(
        n=3,
        ice_ratio=0.5,
        seed=10)
    
    actions = bfs(map)

    if actions is not None:
        print(build_path_from_actions(map.start_pos, actions))

    print(map.map, map.start_pos, map.end_pos)

    # Environment setup
    env = gym.make(
        'FrozenLake-v1', 
        desc=map.map, 
        map_name="Test", 
        is_slippery=False)
    
    # Sets time ~ action count limit
    env = wrappers.TimeLimit(env, 1000)
    
    print(f"State count {env.observation_space.n}")
    print(f"Action count {env.action_space.n}")

    state = env.reset()
    print(f"Current state: {state}")

    done = truncated = False
    while not (done or truncated):

        # Picks random action
        action_number = env.action_space.sample()
        next_state, reward, done, truncated, _ = env.step(action_number)

        print(f"~- Executed action {action_number} \
                - Next state {next_state} \
                - Reward {reward} \
                - Done {done} \
                - Truncated {truncated} \
              ")
    
    if done:
        print("SUCCESS: Reached the end of the frozen lake!")

    elif truncated:
        print("FAILED: Couldn't reach the end of the lake...")
import gymnasium as gym
import random
from gymnasium import wrappers
from map import Map

if __name__ == "__main__":
    map = Map(5, 0.5, 0)
    print(map.map, map.start_pos, map.end_pos)

    # Environment setup
    env = gym.make(
        'FrozenLake-v1', 
        desc=map.map, 
        map_name="Test", 
        is_slippery=False)
    
    # Sets time ~ action count limit
    env = wrappers.TimeLimit(env, 10)
    
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
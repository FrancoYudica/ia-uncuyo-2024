import gymnasium as gym
import random
from gymnasium import wrappers

def generate_map(n: int,
                 ice_ratio: float,
                 seed: int) -> list:
    SOURCE_SYMBOL = "S"
    FROZEN_SYMBOL = "F"
    HOLE_SYMBOL = "H"
    GOAL_SYMBOL = "G"

    # Matrix that holds symbols [["S", "H"], ["F", "G"]]
    env_map = [[HOLE_SYMBOL] * n for _ in range(n)]

    random.seed(seed)

    def add_cell_random(cell_type):
        pos = (random.randrange(0, n), random.randrange(0, n))
        
        # The random position should override holes
        if env_map[pos[0]][pos[1]] != HOLE_SYMBOL:
            return False
        
        # Sets the frozen cell
        env_map[pos[0]][pos[1]] = cell_type
        return True

    # Adds source
    add_cell_random(SOURCE_SYMBOL)

    # Adds goal, ensuring it isn't placed over the SOURCE
    while not add_cell_random(GOAL_SYMBOL):
        pass

    # Amount of ice cells
    ice_cell_count = int(ice_ratio * n * n)
    
    # Adds all the required ice cells
    current_ice_cell_count = 0
    while current_ice_cell_count < ice_cell_count:
        if add_cell_random(FROZEN_SYMBOL):
            current_ice_cell_count += 1

    random.seed(None)

    # Transforms [["S", "H"], ["F", "G"]] to => ["SH", "FG"]
    # This transformation is in the required environment format 
    mapped = ["".join(sublist) for sublist in env_map]
    return mapped

if __name__ == "__main__":
    random_map = generate_map(5, 0.5, 0)
    print(random_map)

    # Environment setup
    env = gym.make(
        'FrozenLake-v1', 
        desc=random_map, 
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
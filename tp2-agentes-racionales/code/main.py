from agents.simple_reflexive_agent import SimpleReflexiveAgent
from agents.random_agent import RandomAgent
import argparse

from simulation import run_simulation

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

    # Initializes agent
    agent = SimpleReflexiveAgent()

    run_simulation(
        render=args.render,
        fps=args.fps,
        iterations_count=args.iterations,
        env_size=args.size,
        env_seed=args.env_seed,
        env_dirt_ratio=args.dirt_ratio, 
        agent=agent)

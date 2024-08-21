from agents.simple_reflexive_agent import SimpleReflexiveAgent
from agents.random_agent import RandomAgent
from simulation import run_simulation
from plotting import save_graphs, save_table, save_box_and_whiskers


def save_results(results):
    save_table(results, folder="../images")
    save_graphs(results, folder="../images/graphs")

    for size in results.keys():
        for dr in results[size].keys():
            save_box_and_whiskers(results, size, dr, folder="../images/box_and_whiskers")

class SimulationResults:
    def __init__(self) -> None:
        # Holds a list of size `iterations_count` with all
        # the results of each iteration. This could be used
        # for plotting
        self.agent_performance = []

    @property
    def average_performance(self):
        return sum(self.agent_performance) / len(self.agent_performance)

if __name__ == "__main__":

    args = {
        "render": False,
        "fps": 0,
        "iterations_count": 1000,
        "env_size": 20,
        "env_seed": 0,
        "env_dirt_ratio": 0.25,
        "verbose": False
    }

    test_agents = {
        "random_agent": RandomAgent(),
        "reflex_agent": SimpleReflexiveAgent()
    }

    results = {}

    # For each env size
    for env_size in [2, 4, 8, 16, 32, 64, 128, 256]:
        args["env_size"] = env_size

        # For each dirt ratio
        for dirt_ratio in [0.1, 0.2, 0.4, 0.8]:
            args["env_dirt_ratio"] = dirt_ratio
            
            # For each agent
            for agent_name in test_agents.keys():
                agent = test_agents[agent_name]
                agent_result = SimulationResults()

                # Iterates 10 times
                for i in range(10):
                    args["env_seed"] = i

                    # Resets agent position
                    agent.row = agent.col = 0

                    # Unpacks common arguments and runs
                    agent_iter_performance = run_simulation(**args, agent=agent)

                    # Stores simulation result
                    agent_result.agent_performance.append(agent_iter_performance)

                if env_size not in results:
                    results[env_size] = {}

                if dirt_ratio not in results[env_size]:
                    results[env_size][dirt_ratio] = {}

                results[env_size][dirt_ratio][agent_name] = agent_result

                print(f"Agent({agent_name}) Env({env_size}x{env_size}, dirt_ratio: {dirt_ratio}) \
                    AvgPerformance: {agent_result.average_performance}")
    
    save_results(results)

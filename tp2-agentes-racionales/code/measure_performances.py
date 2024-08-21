from agents.simple_reflexive_agent import SimpleReflexiveAgent
from agents.random_agent import RandomAgent
from simulation import run_simulation
import matplotlib.pyplot as plt

def save_table(results):

    # Prepare data for the table
    columns = ['Environment size', 'Dirt ratio', 'Random agent', 'Simple reflex agent']
    table_data = []

    for size, dirt_ratios in results.items():
        for dirt_ratio, performances in dirt_ratios.items():
            row = [
                size, 
                dirt_ratio, 
                round(performances['random_agent'], 3), 
                round(performances['simple_reflex_agent'], 3)
                ]
            table_data.append(row)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))  # Adjust size as needed

    # Hide the axes
    ax.xaxis.set_visible(False) 
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    # Create the table with column names
    table = ax.table(cellText=table_data, colLabels=columns, cellLoc='center', loc='center')

    # Customize table appearance
    table.auto_set_font_size(False)
    table.set_fontsize(10)

    plt.savefig(f"results_table.png", bbox_inches="tight")


def save_graphs(results):
    # Iterate over each dirt ratio
    for dirt_ratio in set(dr for size in results for dr in results[size]):
        plt.figure(figsize=(10, 6))

        # Prepare data for plotting
        sizes = sorted(results.keys())
        for agent in ['random_agent', 'simple_reflex_agent']:
            y = [results[size][dirt_ratio][agent] for size in sizes if dirt_ratio in results[size]]

            plt.plot(sizes, y, marker='o', label=f'{agent} (Dirt Ratio {dirt_ratio})')

        # Add labels, title, and legend
        plt.xlabel('Environment Size (Power of 2)')
        plt.ylabel('Performance')
        plt.title(f'Agent Performance vs Environment Size for Dirt Ratio {dirt_ratio}')

        # Set x-axis to log scale with base 2
        plt.xscale('log', base=2)
        plt.legend()
        plt.grid(True)
        plt.savefig(f"results_dirt_ratio({dirt_ratio}).png")


def save_results(results):
    save_table(results)
    save_graphs(results)


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
    random_agent = RandomAgent()
    reflexive_agent = SimpleReflexiveAgent()

    results = {}

    # For each env size
    for env_size in [2, 4, 8, 16, 32, 64, 128, 256]:
        args["env_size"] = env_size

        # For each dirt ratio
        for dirt_ratio in [0.1, 0.2, 0.4, 0.8]:
            args["env_dirt_ratio"] = dirt_ratio
            
            # Calculates the average performance over 'iterations_per_combination' iterations
            avg_random_performance = 0
            avg_reflexive_performance = 0

            iterations_per_combination = 10
            for i in range(iterations_per_combination):
                args["env_seed"] = i

                # Resets agent position
                random_agent.row = random_agent.col = 0
                reflexive_agent.row = reflexive_agent.col = 0

                # Unpacks common arguments and runs
                random_agent_performance = run_simulation(**args, agent=random_agent)
                reflexive_agent_performance = run_simulation(**args, agent=reflexive_agent)

                # Adds to average
                avg_random_performance += random_agent_performance / iterations_per_combination
                avg_reflexive_performance += reflexive_agent_performance / iterations_per_combination

            if env_size not in results:
                results[env_size] = {}

            results[env_size][dirt_ratio] = {
                "random_agent": avg_random_performance,
                "simple_reflex_agent": avg_reflexive_performance
            }

            # Debug print after each SIZE and DIRT_RATIO combination
            print(f"Env({env_size}x{env_size}, dirt_ratio: {dirt_ratio}) \
                  RandomAgentAvgPerformance: {avg_random_performance}    \
                  ReflexiveAgentAvgPerformance: {avg_reflexive_performance}")
    
    save_results(results)

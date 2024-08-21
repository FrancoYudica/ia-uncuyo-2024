import matplotlib.pyplot as plt
import os


def save_table(results, folder=""):

    # Prepare data for the table
    columns = ['Environment size', 'Dirt ratio', 'Random agent AVG', 'Simple reflex agent AVG']
    table_data = []

    for size, dirt_ratios in results.items():
        for dirt_ratio, performances in dirt_ratios.items():
            row = [size, dirt_ratio]

            for agent_name in performances.keys():
                simulation_results = performances[agent_name]
                row.append(round(simulation_results.average_performance, 3))
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

    plt.savefig(os.path.join(folder, "results_table.png"), bbox_inches="tight")


def save_graphs(results, folder=""):
    sizes = sorted(results.keys())
    dirt_ratios = set([dr for size in results for dr in results[size]])
    agent_names = set([agent_name for size in results.keys() for dr in results[size].keys() for agent_name in results[size][dr].keys()])
    # Iterate over each dirt ratio
    for dirt_ratio in dirt_ratios:
        plt.figure(figsize=(10, 6))

        # Prepare data for plotting
        for agent in agent_names:
            y = [results[size][dirt_ratio][agent].average_performance for size in sizes]
            plt.plot(sizes, y, marker="o", linestyle="--", label=f'{agent} (Dirt Ratio {dirt_ratio})')

        # Add labels, title, and legend
        plt.xlabel('Environment Size (Power of 2)')
        plt.ylabel('Performance')
        plt.title(f'Agent AVG Performance vs Environment Size for Dirt Ratio {dirt_ratio}')

        # Set x-axis to log scale with base 2
        plt.xscale('log', base=2)
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(folder, f"results_dirt_ratio({dirt_ratio}).png"))

def save_box_and_whiskers(results, size, dirt_ratio, folder=""):

    # Prepare the data for all agents
    performance_data = []
    agent_names = []

    for agent_name in results[size][dirt_ratio]:
        # Append the performance list of each agent
        performance_list = results[size][dirt_ratio][agent_name].agent_performance
        performance_data.append(performance_list)
        agent_names.append(agent_name)

    # Plot the box and whiskers chart for all agents
    plt.figure(figsize=(10, 6))

    plt.boxplot(performance_data)

    # Add labels, title, and x-ticks
    plt.xlabel('Agents')
    plt.ylabel('Performance')
    plt.title(f'Box Plot for Size: {size}, Dirt Ratio: {dirt_ratio}')

    # Set x-axis tick labels to the agent names
    plt.xticks(ticks=range(1, len(agent_names) + 1), labels=agent_names)

    # Save the plot
    plt.savefig(os.path.join(folder, f"box_size({size})_dr({dirt_ratio}).png"))
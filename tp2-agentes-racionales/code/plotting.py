import matplotlib.pyplot as plt
import os


def save_table(results, folder=""):

    # Prepare data for the table
    columns = [
        'Environment size', 
        'Dirt ratio', 
        'Random avg performance', 
        'Random avg iterations', 
        'Reflex avg performance', 
        'Reflex avg iterations']
    table_data = []

    for size, dirt_ratios in results.items():
        for dirt_ratio, performances in dirt_ratios.items():
            row = [size, dirt_ratio]

            for agent_name in performances.keys():
                simulation_results = performances[agent_name]
                row.append(round(simulation_results.average_performance, 3))
                row.append(simulation_results.average_iterations)
            table_data.append(row)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(16, 6))  # Adjust size as needed

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
    plt.close()


def save_graphs_performance(results, folder=""):
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
        plt.savefig(os.path.join(folder, f"performance_results_dirt_ratio({dirt_ratio}).png"))
        plt.close()

def save_graphs_iterations(results, folder=""):
    sizes = sorted(results.keys())
    dirt_ratios = set([dr for size in results for dr in results[size]])
    agent_names = set([agent_name for size in results.keys() for dr in results[size].keys() for agent_name in results[size][dr].keys()])
    # Iterate over each dirt ratio
    for dirt_ratio in dirt_ratios:
        plt.figure(figsize=(10, 6))

        # Prepare data for plotting
        for agent in agent_names:
            y = [results[size][dirt_ratio][agent].average_iterations for size in sizes]
            plt.plot(sizes, y, marker="o", linestyle="--", label=f'{agent} (Dirt Ratio {dirt_ratio})')

        # Add labels, title, and legend
        plt.xlabel('Environment Size (Power of 2)')
        plt.ylabel('Iterations')
        plt.title(f'Agent AVG Iterations vs Environment Size for Dirt Ratio {dirt_ratio}')

        # Set x-axis to log scale with base 2
        plt.xscale('log', base=2)
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(folder, f"iterations_results_dirt_ratio({dirt_ratio}).png"))
        plt.close()


def save_box_and_whiskers(results, size, folder=""):
    # Prepare the data for all dirt ratios
    performance_data = {}
    dirt_ratios = sorted(results[size].keys())
    agent_names = list(results[size][dirt_ratios[0]].keys())  # Assuming all dirt ratios have the same agents

    # Collect performance data for each agent and dirt ratio
    for agent_name in agent_names:
        performance_data[agent_name] = [
            results[size][dirt_ratio][agent_name].performances_list for dirt_ratio in dirt_ratios
        ]

    # Plot the box and whiskers chart
    plt.figure(figsize=(12, 8))
    
    # Colors for different agents
    colors = plt.cm.tab10.colors  # Get a set of colors

    # Plot each agent's performance data
    for i, agent_name in enumerate(agent_names):
        data = performance_data[agent_name]
        positions = [j + 1 + i * 0.2 for j in range(len(dirt_ratios))]
        color = colors[i % len(colors)]
        plt.boxplot(data, positions=positions, widths=0.2, patch_artist=True,
                    boxprops=dict(facecolor=color))

    plt.legend(agent_names, loc='upper right', labelcolor=colors, frameon=False)
    # Add labels, title, and x-ticks
    plt.xlabel('Dirt Ratio')
    plt.ylabel('Performance')
    plt.title(f'Box Plot for Size: {size}')

    # Set x-axis tick labels to the dirt ratios
    plt.xticks(ticks=range(1, len(dirt_ratios) + 1), labels=dirt_ratios)

    # Add a legend for the agents
    # plt.legend(agent_names, loc='upper right')

    # Save the plot
    plt.savefig(os.path.join(folder, f"box_size({size}).png"))
    plt.close()


# def save_box_and_whiskers(results, size, dirt_ratio, folder=""):

#     # Prepare the data for all agents
#     performance_data = []
#     agent_names = []

#     for agent_name in results[size][dirt_ratio]:
#         # Append the performance list of each agent
#         performance_list = results[size][dirt_ratio][agent_name].performances_list
#         performance_data.append(performance_list)
#         agent_names.append(agent_name)

#     # Plot the box and whiskers chart for all agents
#     plt.figure(figsize=(10, 6))

#     plt.boxplot(performance_data)

#     # Add labels, title, and x-ticks
#     plt.xlabel('Agents')
#     plt.ylabel('Performance')
#     plt.title(f'Box Plot for Size: {size}, Dirt Ratio: {dirt_ratio}')

#     # Set x-axis tick labels to the agent names
#     plt.xticks(ticks=range(1, len(agent_names) + 1), labels=agent_names)

#     # Save the plot
#     plt.savefig(os.path.join(folder, f"box_size({size})_dr({dirt_ratio}).png"))
#     plt.close()

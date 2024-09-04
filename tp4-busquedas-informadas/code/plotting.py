import matplotlib.pyplot as plt
import csv

def plot_results(
        results,
        title: str,
        save_filepath: str,
        y_label: str,
        access_result_data = lambda result: result.time_taken):

    # Extract the data for each algorithm
    data = []
    for algo_name in results.keys():
        data.append([access_result_data(res) for res in results[algo_name]])

    # Create the boxplot
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=results.keys())

    title_string = f"{title} by " + ", ".join(list(results.keys())[:-1]) + ", and " + list(results.keys())[-1]
    plt.title(title_string)
    plt.ylabel(f"{y_label}")
    plt.savefig(save_filepath)
    plt.close()

def save_csv(
        results,
        save_filepath):
    
    envs = list(range(1, 31))

    with open(save_filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([
            "algorithm_name", "env_n", "states_n", 
            "actions_count", "actions_cost", "time", "solution_found"
        ])
        
        for algorithm_name, executions in results.items():
            for env_n, walk_result in zip(envs, executions):
                
                actions_count = walk_result.calculate_cost(cost_by_action=False)
                actions_cost = walk_result.calculate_cost(cost_by_action=True)
                
                writer.writerow([
                    algorithm_name,
                    env_n,
                    walk_result.explored_cells,
                    actions_count,
                    actions_cost,
                    walk_result.time_taken,
                    bool(walk_result.actions)
                ])

if __name__ == "__main__":
    # Read the CSV file
    with open('../informada-results.csv', 'r') as file:
        reader = csv.reader(file)
        
        # Convert the CSV content to a Markdown table
        markdown_table = "| " + " | ".join(next(reader)) + " |\n"
        markdown_table += "| " + " | ".join(['-' * len(header) for header in markdown_table.split('|')[1:-1]]) + " |\n"
        
        for row in reader:
            markdown_table += "| " + " | ".join(row) + " |\n"

    # Output the Markdown table
    print(markdown_table)
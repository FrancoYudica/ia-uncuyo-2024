import csv
import statistics
import matplotlib.pyplot as plt
from local_search_algo.local_search_result import LocalSearchResult


def save_csv(results, save_filepath):

    # Determine unique queen counts from results
    queen_counts = set([result.board.size for result in results[list(results.keys())[0]]])

    with open(save_filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the CSV header
        writer.writerow([
            "queen_count", "algorithm_name", "success_rate", 
            "avg_time", "time_standard_deviation", 
            "avg_states", "states_standard_deviation"
        ])

        # Iterate over each algorithm and calculate statistics
        for algorithm_name, algorithm_results in results.items():
            for queen_count in queen_counts:
                # Filter the results for the current queen count
                filtered_results = [result for result in algorithm_results if result.board.size == queen_count]
                
                # Success rate: assume success if the board is solved (h_value == 0)
                success_rate = len([r for r in filtered_results if r.board.cached_threats == 0]) / len(filtered_results)
                
                # Average and standard deviation of time taken
                times = [result.time_taken for result in filtered_results]
                avg_time = sum(times) / len(times)
                time_std_dev = statistics.stdev(times) if len(times) > 1 else 0
                
                # Average and standard deviation of traversed states
                states = [result.traversed_states for result in filtered_results]
                avg_states = sum(states) / len(states)
                states_std_dev = statistics.stdev(states) if len(states) > 1 else 0
                
                # Write the row to the CSV file
                writer.writerow([
                    queen_count, algorithm_name, success_rate, 
                    avg_time, time_std_dev, 
                    avg_states, states_std_dev
                ])

def save_plot_execution_times(results, queen_count, save_filepath):
    algorithms = list(results.keys())
    
    # Collect execution times for each algorithm
    times_data = []
    for algorithm_name in algorithms:
        times = [result.time_taken for result in results[algorithm_name] if result.board.size == queen_count]
        times_data.append(times)

    # Create boxplot for execution times
    plt.figure(figsize=(10, 6))
    plt.boxplot(times_data, labels=algorithms, patch_artist=True)
    plt.title(f"Execution Times for All Algorithms in a board of size: {queen_count}")
    plt.ylabel("Execution Time (seconds)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_filepath)
    plt.close()

def save_plot_states_count(results, queen_count, save_filepath):
    algorithms = list(results.keys())
    
    # Collect traversed states count for each algorithm
    data = []
    for algorithm_name in algorithms:
        states = [result.traversed_states for result in results[algorithm_name] if result.board.size == queen_count]
        data.append(states)

    # Create boxplot for traversed states
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=algorithms, patch_artist=True)
    plt.title(f"Traversed states for All Algorithms in a board of size: {queen_count}")
    plt.ylabel("Traversed states count")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_filepath)
    plt.close()



def plot_h_values(result: LocalSearchResult, save_filepath):
    # Generate a list of indices (x-axis) based on the length of h_values
    x = list(range(len(result.h_values)))
    
    # Plot the h_values using a dotted line
    plt.figure(figsize=(8, 6))
    plt.plot(x, result.h_values, linestyle=':', marker='o', color='b')
    
    # Adding labels and title
    plt.title(f'h-values over iterations for Board Size {result.board.size}')
    plt.xlabel('Step')
    plt.ylabel('h-value')
    
    # Show grid for better visualization
    plt.grid(True)
    
    plt.savefig(save_filepath)
    plt.close()

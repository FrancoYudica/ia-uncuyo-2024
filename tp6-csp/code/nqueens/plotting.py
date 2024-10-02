import csv
import statistics
import matplotlib.pyplot as plt
from nqueens_utils import NQueensSearchResult, create_empty_board
from nqueens_backtracking import nqueens_backtracking
from nqueens_forward_chaining import nqueens_forward_chaining



def save_csv(
        results, 
        queen_counts, 
        save_filepath):

    with open(save_filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the CSV header
        writer.writerow([
            "algorithm_name", 
            "queen_count", 
            "traversed_state_count", 
            "time_taken"])

        # Iterate over each algorithm and calculate statistics
        for algorithm_name, algorithm_results in results.items():
            for queen_count in queen_counts:
                
                # Finds the result of the algorithm for the current queen count
                result: NQueensSearchResult = [result for result in algorithm_results if len(result.board) == queen_count][0]

                # Write the row to the CSV file
                writer.writerow([
                    queen_count, 
                    algorithm_name, 
                    result.traversed_states, 
                    result.time_taken])

import matplotlib.pyplot as plt

def plot_states(
        results, 
        queen_counts, 
        save_filepath):
    plt.figure(figsize=(8, 6))
    
    # Define a color map or list of styles for the algorithms
    styles = [
        {"color": "b", "linestyle": "--", "marker": "o"},
        {"color": "g", "linestyle": "--", "marker": "o"}
    ]
    
    # Plot each algorithm's results
    for i, (algorithm_name, algorithm_results) in enumerate(results.items()):
        plt.plot(
            queen_counts, 
            [result.traversed_states for result in algorithm_results],
            label=algorithm_name,  # Add label for the legend
            **styles[i])
    
    plt.title("Traversed States over Different Board Sizes for Multiple Algorithms")
    plt.xlabel("Board size")
    plt.ylabel("Traversed state count")
    plt.legend()
    
    # Set X-axis ticks to ensure all values are displayed
    plt.xticks(queen_counts)  # This ensures all board sizes are used as ticks
    
    # Show grid for better visualization
    plt.grid(True)
    
    # Save the plot
    plt.savefig(save_filepath)
    plt.close()


def plot_time_taken(
        results, 
        queen_counts, 
        save_filepath):
    plt.figure(figsize=(8, 6))
    
    # Define a color map or list of styles for the algorithms
    styles = [
        {"color": "b", "linestyle": "--", "marker": "o"},
        {"color": "g", "linestyle": "--", "marker": "o"}
    ]
    
    # Plot each algorithm's results
    for i, (algorithm_name, algorithm_results) in enumerate(results.items()):
        plt.plot(
            queen_counts, 
            [result.time_taken for result in algorithm_results],
            label=algorithm_name,
            **styles[i])
    
    plt.title("Time Taken over Different Board Sizes for Multiple Algorithms")
    plt.xlabel("Board size")
    plt.ylabel("Time taken")
    plt.legend()
    
    # Set X-axis ticks to ensure all values are displayed
    plt.xticks(queen_counts)  # This ensures all board sizes are used as ticks
    
    # Show grid for better visualization
    plt.grid(True)
    
    # Save the plot
    plt.savefig(save_filepath)
    plt.close()


def _save_results(results, queen_counts):
    save_csv(results, queen_counts, "../results.csv")

    plot_states(
        results, 
        queen_counts, 
        "../images/traverses_states_combined.png")

    plot_time_taken(
        results, 
        queen_counts, 
        "../images/time_taken_combined.png")

def gather_results_and_save():
    results = []

    queen_counts = [4, 8, 10, 12, 15, 17]
    algorithms = {
        "basic_backtracking": lambda board: nqueens_backtracking(board),
        "forward_chaining": lambda board: nqueens_forward_chaining(
            board, 
            [[i for i in range(len(board))] for _ in range(len(board))])  # Full domain for each variable
    }

    results = {algorithm_name: [] for algorithm_name in algorithms.keys()}

    for queen_count in queen_counts:

        board = create_empty_board(queen_count)

        for algorithm_name in algorithms:
            print(f"Executing {algorithm_name} in board of size {queen_count}")
            algo_func = algorithms[algorithm_name]
            result: NQueensSearchResult = algo_func(board)
            results[algorithm_name].append(result)

    _save_results(results, queen_counts)


if __name__ == "__main__":
    gather_results_and_save()
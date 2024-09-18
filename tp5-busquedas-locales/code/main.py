from chess_board_state import ChessBoardState
from local_search_algo.local_search_result import LocalSearchResult

from local_search_algo.hill_climb.random_restart_hill_climb import hill_climb
from local_search_algo.hill_climb.random_restart_hill_climb import random_restart_hill_climb
from local_search_algo.simulated_annealing.simulated_annealing import simulated_annealing
from plotting import save_csv, save_plot_execution_times, save_plot_states_count, plot_h_values

def hill_climb_test(board):
    print("RUNNING: HILL CLIMB")
    result: LocalSearchResult = hill_climb(board)

    print(f"Hill climb traversed {result.traversed_states} states in {result.time_taken} seconds")

    if result.board.cached_threats == 0:
        print("Success")
        print(result.board)

    else:
        print(f"Failure. Stuck at {result.board.cached_threats} threats")


def hill_climb_success_rate_test(
        random_board_count,
        board_size, 
        iterations_per_board):

    success_count = 0

    for _ in range(random_board_count):
        board = ChessBoardState(board_size)

        for _ in range(iterations_per_board):
            result: LocalSearchResult = hill_climb(board)

            if result.board.cached_threats == 0:
                success_count += 1

    total_samples = random_board_count * iterations_per_board
    print(f"Success count {success_count}/{total_samples}. Success rate: {success_count/total_samples}")    


def simulated_annealing_test(board):
    print("RUNNING: SIMULATED ANNEALING")
    result: LocalSearchResult = simulated_annealing(board, maximum_states=600)

    print(f"Traversed {result.traversed_states} states in {result.time_taken} seconds")

    if result.board.cached_threats == 0:
        print("Success")
        print(result.board)

    else:
        print(f"Failure. Stuck at {result.board.cached_threats} threats")


def random_restart_hill_climb_test(board):
    print("RUNNING: RANDOM RESTART HILL CLIMB")

    result: LocalSearchResult = random_restart_hill_climb(board)

    print(f"Random restart hill climb traversed {result.traversed_states} states in {result.time_taken} seconds")
    print(result.board)


def _save_results(results, queen_counts):
    save_csv(results, "../results.csv")

    for queen_count in queen_counts:

        # Saves execution times and states box&whiskers
        save_plot_execution_times(results, queen_count, f"../images/execution_time/box&whiskers_queen_count={queen_count}.png")
        save_plot_states_count(results, queen_count, f"../images/traversed_states/box&whiskers_queen_count={queen_count}.png")

        # For each pair (algorithm, queen_count) plots a single graph, showing h values over iterations, of the best LocalSearchResult
        for algorithm_name in results.keys():

            best_result: LocalSearchResult = None

            # Finds the closest result to success
            for local_search_result in results[algorithm_name]:
                
                # Filters for same queen count
                if local_search_result.board.size != queen_count:
                    continue
                
                if best_result is None:
                    best_result = local_search_result

                elif local_search_result.board.cached_threats < best_result.board.cached_threats:
                    best_result = local_search_result

                elif local_search_result.board.cached_threats == best_result.board.cached_threats:
                    if local_search_result.traversed_states < best_result.traversed_states:
                        best_result = local_search_result

            plot_h_values(best_result, f"../images/h_values/{algorithm_name}/queen_count={queen_count}.png")


def test_and_save():

    queen_counts = [4, 8, 10, 12, 15]
    maximum_states = 1000
    algorithms = {
        "hill_climb": lambda board: hill_climb(board, maximum_states, maximum_shoulder_iterations=10),
        # "random_restart_hill_climb": lambda board: random_restart_hill_climb(board, maximum_states, maximum_shoulder_iterations=10),
        "simulated_annealing": lambda board: simulated_annealing(board, maximum_states, maximum_iterations=maximum_states)
    }

    results = {algorithm_name: [] for algorithm_name in algorithms.keys()}

    for _ in range(30):

        for queen_count in queen_counts:
            board = ChessBoardState(queen_count)

            for algorithm_name in algorithms:
                print(f"Executing {algorithm_name} in board of size {queen_count}")
                algo_func = algorithms[algorithm_name]
                result: LocalSearchResult = algo_func(board)
                results[algorithm_name].append(result)

    _save_results(results, queen_counts)

if __name__ == "__main__":
    test_and_save()

    # board = ChessBoardState(8)
    # simulated_annealing_test(board)



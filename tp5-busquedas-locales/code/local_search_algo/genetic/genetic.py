from chess_board_state import ChessBoardState
from local_search_algo.utils import random_successor_chess_board
from local_search_algo.local_search_result import LocalSearchResult
from typing import List, Tuple
import random
import time
import math


def populate(
    initial_board, 
    population_size) -> List[ChessBoardState]:
    """Given the initial board, generates a random population"""

    population = [initial_board]

    for _ in range(population_size - 1):
        population.append(random_successor_chess_board(initial_board))

    return population

def selection_ranking(population, size):
    ranked_population = sorted(
        population, 
        key=lambda board: board.cached_threats)

    num_individuals = len(population)
    probabilities = [1/(i+1) for i in range(num_individuals)]
    selected_individuals = random.choices(
        ranked_population, 
        weights=probabilities, 
        k=size)
    return selected_individuals

def crossover(parent1, parent2) -> Tuple[ChessBoardState, ChessBoardState]:

    # Crossover index
    i = random.randrange(1, parent1.size)

    child1_columns = parent1.columns[:i] + parent2.columns[i:] 
    child2_columns = parent2.columns[:i] + parent1.columns[i:]
    return (
        ChessBoardState(
            size=parent1.size, 
            columns=child1_columns),
        ChessBoardState(
            size=parent1.size, 
            columns=child2_columns))

def uniform_crossover(parent1, parent2):
    child1_columns = []
    child2_columns = []
    for i in range(parent1.size):
        if random.random() < 0.5:
            child1_columns.append(parent1.columns[i])
            child2_columns.append(parent2.columns[i])
        else:
            child1_columns.append(parent2.columns[i])
            child2_columns.append(parent1.columns[i])
    return (
        ChessBoardState(
            size=parent1.size, 
            columns=child1_columns),
        ChessBoardState(
            size=parent1.size, 
            columns=child2_columns))


def mutate(board):
    """Swaps two columns"""
    n = board.size
    mutated_cols = board.columns[:]
    col1, col2 = random.sample(range(n), 2)
    mutated_cols[col1], mutated_cols[col2] = mutated_cols[col2], mutated_cols[col1]
    return ChessBoardState(
        size=board.size, 
        columns=mutated_cols)


def search_best_individual(population):
    best_board = population[0]
    best_board.recalculate_threats()
    for i in range(1, len(population)):
        board = population[i]
        board.recalculate_threats()
        if board.cached_threats < best_board.cached_threats:
            best_board = board

    return best_board

def genetic(
        initial_board: ChessBoardState,
        maximum_states: int = 100,
        population_size: int = 50,
        mutation_rate: float = 0.05) -> LocalSearchResult:

    result = LocalSearchResult()
    result.board = initial_board
    t0 = time.time()

    # population = populate(initial_board, population_size)
    population = []
    for i in range(population_size):
        population.append(ChessBoardState(initial_board.size, seed=i))

    for generation in range(maximum_states):

        # Checks if there is a solution individual
        result.board = search_best_individual(population)
        result.h_values.append(result.board.cached_threats)
        if result.board.cached_threats == 0:
            break

        # Selects the most suitable parents based on their score
        best_individuals = selection_ranking(population, int(population_size * 0.2))

        successors = []
        for i in range(0, len(population) - len(best_individuals), 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            child1, child2 = uniform_crossover(parent1, parent2)
            successors.append(child1)
            successors.append(child2)
        successors.extend(best_individuals)
        # Mutation
        population = [mutate(board) if random.random() < mutation_rate else board for board in population]
        # population = selection_ranking(population, population_size)
        population.sort(key=lambda board: board.cached_threats, reverse=True)
    result.traversed_states = generation + 1
    result.time_taken = time.time() - t0
    return result
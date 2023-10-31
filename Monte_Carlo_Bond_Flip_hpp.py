import numpy as np
from typing import List

def monte_carlo_bond_flip(
    membrane_node_position: List[List[float]],
    membrane_new_triangle_list: List[List[int]],
    membrane_triangle_pair_list: List[List[int]],
    membrane_node_pair_list: List[List[int]],
    membrane_num_of_node_pairs: int,
    membrane_num_of_nodes: int
):
    def triangle_pair_node_sorter(triangle_1, triangle_2, membrane_new_triangle_list):
        nodes_1 = list(set(membrane_new_triangle_list[triangle_1]) & set(membrane_new_triangle_list[triangle_2]))
        remaining_nodes = list(set(membrane_new_triangle_list[triangle_1] + membrane_new_triangle_list[triangle_2]) - set(nodes_1))
        sorted_nodes = [nodes_1[0], nodes_1[1], remaining_nodes[0], remaining_nodes[1]]
        return sorted_nodes

    def new_triangle_pair_node_sorter(
        triangle_A_node_A, triangle_A_node_B, triangle_A_node_C,
        triangle_B_node_D, triangle_A_neighbours, triangle_B_neighbours,
        membrane_new_triangle_list
    ):
        common_nodes = list(set(membrane_new_triangle_list[triangle_A_neighbours[0]]) & set(membrane_new_triangle_list[triangle_B_neighbours[0]]))
        nodes_A = [triangle_A_node_A, triangle_A_node_B, triangle_A_node_C]
        nodes_B = [triangle_B_node_D, common_nodes[0], common_nodes[1]]

        new_sorted_nodes = [
            [nodes_A[0], nodes_A[1], nodes_A[2], nodes_B[0]],
            [nodes_A[2], nodes_A[0], nodes_A[1], nodes_B[1]],
            [nodes_B[0], nodes_B[1], nodes_A[2], nodes_B[2]],
            [nodes_B[1], nodes_B[0], nodes_A[2], nodes_B[3]]
        ]

        triangle_A_new_neighbours = [
            triangle_A_neighbours[0],
            triangle_B_neighbours[0]
        ]

        triangle_B_new_neighbours = [
            triangle_B_neighbours[0],
            triangle_A_neighbours[0]
        ]

        return new_sorted_nodes, triangle_A_new_neighbours, triangle_B_new_neighbours

    # Your Python code can use the defined functions above to implement monte_carlo_bond_flip logic
    # Just replace the C++ code with the equivalent Python code based on these functions.

if __name__ == "__main__":
    # You can add code here to test the functions and logic if needed.

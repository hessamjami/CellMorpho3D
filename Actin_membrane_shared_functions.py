def membrane_actin_shared_node_identifier(membrane_node_position, actin_node_position):
    membrane_actin_shared_node_list = []

    for mem_node_counter, membrane_node in enumerate(membrane_node_position):
        for act_node_counter, actin_node in enumerate(actin_node_position):
            if membrane_node == actin_node:
                membrane_actin_shared_node_list.append([mem_node_counter, act_node_counter])
                break

    return membrane_actin_shared_node_list

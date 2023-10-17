def generate_node_pair_list():
    ECM_Node_Pair_list = []
    Node_Pairs = [-1, -1]
    ECM_Node_Pair_list.append(Node_Pairs)

    temp_double = 0.0
    Num_of_objects = 0

    with open("ECM", "r") as read:
        temp_double = float(read.readline())

        for i in range(ECM_num_of_Nodes):
            for _ in range(4):
                temp_double = float(read.readline())

        Num_of_objects = int(read.readline())

        for i in range(ECM_Surface_num_of_Triangles):
            for _ in range(8):
                temp_double = float(read.readline())

        for i in range(Num_of_objects - ECM_Surface_num_of_Triangles):
            for _ in range(5):
                temp_double = float(read.readline())

            ECM_pyramid_Node_1 = int(read.readline()) - 1
            ECM_pyramid_Node_2 = int(read.readline()) - 1
            ECM_pyramid_Node_3 = int(read.readline()) - 1
            ECM_pyramid_Node_4 = int(read.readline()) - 1

            repeated_pair_counter = [0] * 7

            for j in range(len(ECM_Node_Pair_list) - 1):
                node_pair = ECM_Node_Pair_list[j]

                if node_pair[0] == ECM_pyramid_Node_1 and node_pair[1] == ECM_pyramid_Node_2:
                    repeated_pair_counter[0] = 1
                if node_pair[0] == ECM_pyramid_Node_2 and node_pair[1] == ECM_pyramid_Node_3:
                    repeated_pair_counter[1] = 1
                if node_pair[0] == ECM_pyramid_Node_1 and node_pair[1] == ECM_pyramid_Node_3:
                    repeated_pair_counter[2] = 1
                if node_pair[0] == ECM_pyramid_Node_1 and node_pair[1] == ECM_pyramid_Node_4:
                    repeated_pair_counter[3] = 1
                if node_pair[0] == ECM_pyramid_Node_2 and node_pair[1] == ECM_pyramid_Node_4:
                    repeated_pair_counter[4] = 1
                if node_pair[0] == ECM_pyramid_Node_3 and node_pair[1] == ECM_pyramid_Node_4:
                    repeated_pair_counter[5] = 1
                if node_pair[0] == ECM_pyramid_Node_3 and node_pair[1] == ECM_pyramid_Node_2:
                    repeated_pair_counter[6] = 1

            if repeated_pair_counter[0] == 0:
                if (ECM_Node_Position[ECM_pyramid_Node_1][1] == -Membrane_Centre_distance_from_ECM and
                    ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM):
                    if ((ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM)):
                        Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list.append(Node_Pairs)
                    else:
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_1]
                        ECM_Node_Pair_list.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_2]
                    ECM_Node_Pair_list.append(Node_Pairs)

            if repeated_pair_counter[1] == 0:
                if (ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM and
                    ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM):
                    if ((ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM)):
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list.append(Node_Pairs)
                    else:
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_3]
                    ECM_Node_Pair_list.append(Node_Pairs)

            if repeated_pair_counter[2] == 0:
                if (ECM_Node_Position[ECM_pyramid_Node_1][1] == -Membrane_Centre_distance_from_ECM and
                    ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM):
                    if ((ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM)):
                        Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list.append(Node_Pairs)
                    else:
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_1]
                        ECM_Node_Pair_list.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_3]
                    ECM_Node_Pair_list.append(Node_Pairs)

            if repeated_pair_counter[3] == 0:
                if (ECM_Node_Position[ECM_pyramid_Node_1][1] == -Membrane_Centre_distance_from_ECM and
                    ECM_Node_Position[ECM_pyramid_Node_4][1] == -Membrane_Centre_distance_from_ECM):
                    if ((ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM)):
                        Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_4]
                        ECM_Node_Pair_list.append(Node_Pairs)
                    else:
                        Node_Pairs = [ECM_pyramid_Node_4, ECM_pyramid_Node_1]
                        ECM_Node_Pair_list.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_4]
                    ECM_Node_Pair_list.append(Node_Pairs)

            if repeated_pair_counter[4] == 0:
                if (ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM and
                    ECM_Node_Position[ECM_pyramid_Node_4][1] == -Membrane_Centre_distance_from_ECM):
                    if ((ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM)):
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_4]
                        ECM_Node_Pair_list.append(Node_Pairs)
                    else:
                        Node_Pairs = [ECM_pyramid_Node_4, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_4]
                    ECM_Node_Pair_list.append(Node_Pairs)

            if repeated_pair_counter[5] == 0:
                if (ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM and
                    ECM_Node_Position[ECM_pyramid_Node_4][1] == -Membrane_Centre_distance_from_ECM):
                    if ((ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM)):
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_4]
                        ECM_Node_Pair_list.append(Node_Pairs)
                    else:
                        Node_Pairs = [ECM_pyramid_Node_4, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_4]
                    ECM_Node_Pair_list.append(Node_Pairs)

            if repeated_pair_counter[6] == 0:
                if (ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM and
                    ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM):
                    if ((ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM) or
                        (ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                         ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM)):
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list.append(Node_Pairs)
                    else:
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_2]
                    ECM_Node_Pair_list.append(Node_Pairs)

    return ECM_Node_Pair_list

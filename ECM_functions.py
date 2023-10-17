import numpy as np


def ECM_Node_Pair_Identifier():
    ECM_Node_Pair_list_temp = []
    Node_Pairs = [-1, -1]
    ECM_Node_Pair_list_temp.append(Node_Pairs)

    temp_double = 0.0
    Num_of_objects = 0

    with open("ECM", "r") as read:
        temp_double = float(read.readline())  # Read the first value

        for i in range(ECM_num_of_Nodes):
            temp_double = float(read.readline())  # Skip lines for node positions
            temp_double = float(read.readline())
            temp_double = float(read.readline())
            temp_double = float(read.readline())

        Num_of_objects = int(read.readline())
        for i in range(ECM_Surface_num_of_Triangles):
            for _ in range(8):  # Skip lines for triangle coordinates
                temp_double = float(read.readline())

        for i in range(Num_of_objects - ECM_Surface_num_of_Triangles):
            for _ in range(5):  # Skip lines
                temp_double = float(read.readline())

            # Read 4 pyramid nodes
            ECM_pyramid_Node_1 = int(read.readline()) - 1
            ECM_pyramid_Node_2 = int(read.readline()) - 1
            ECM_pyramid_Node_3 = int(read.readline()) - 1
            ECM_pyramid_Node_4 = int(read.readline()) - 1

            # Check for repeated pairs
            temp_int_repeated_pair_counter_1 = 0
            temp_int_repeated_pair_counter_2 = 0
            temp_int_repeated_pair_counter_3 = 0
            temp_int_repeated_pair_counter_4 = 0
            temp_int_repeated_pair_counter_5 = 0
            temp_int_repeated_pair_counter_6 = 0

            for j in range(len(ECM_Node_Pair_list_temp) - 1):
                if (ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_1 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_2) or (
                        ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_2 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_1):
                    temp_int_repeated_pair_counter_1 = 1

                if (ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_2 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_3) or (
                        ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_3 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_2):
                    temp_int_repeated_pair_counter_2 = 1

                if (ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_1 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_3) or (
                        ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_3 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_1):
                    temp_int_repeated_pair_counter_3 = 1

                if (ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_1 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_4) or (
                        ECM_Node_Pair_list[j][0] == ECM_pyramid_Node_4 and ECM_Node_Pair_list[j][
                    1] == ECM_pyramid_Node_1):
                    temp_int_repeated_pair_counter_4 = 1

                if (ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_2 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_4) or (
                        ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_4 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_2):
                    temp_int_repeated_pair_counter_5 = 1

                if (ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_3 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_4) or (
                        ECM_Node_Pair_list_temp[j][0] == ECM_pyramid_Node_4 and ECM_Node_Pair_list_temp[j][
                    1] == ECM_pyramid_Node_3):
                    temp_int_repeated_pair_counter_6 = 1

            if temp_int_repeated_pair_counter_1 == 0:
                if ECM_Node_Position[ECM_pyramid_Node_1][1] == -Membrane_Centre_distance_from_ECM and \
                        ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM:
                    if (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                        ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                    elif (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                          ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_1]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_2]
                    ECM_Node_Pair_list_temp.append(Node_Pairs)

            if temp_int_repeated_pair_counter_2 == 0:
                if ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM and \
                        ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM:
                    if (ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                        ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                    elif (ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                          ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_3]
                    ECM_Node_Pair_list_temp.append(Node_Pairs)

            if temp_int_repeated_pair_counter_3 == 0:
                if ECM_Node_Position[ECM_pyramid_Node_1][1] == -Membrane_Centre_distance_from_ECM and \
                        ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM:
                    if (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                        ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                    elif (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                          ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_1]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_3]
                    ECM_Node_Pair_list_temp.append(Node_Pairs)

            if temp_int_repeated_pair_counter_4 == 0:
                if ECM_Node_Position[ECM_pyramid_Node_1][1] == -Membrane_Centre_distance_from_ECM and \
                        ECM_Node_Position[ECM_pyramid_Node_4][1] == -Membrane_Centre_distance_from_ECM:
                    if (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                        ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_4]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                    elif (ECM_Node_Position[ECM_pyramid_Node_1][2] == -Membrane_Centre_distance_from_ECM and
                          ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_1][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_4, ECM_pyramid_Node_1]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_1, ECM_pyramid_Node_4]
                    ECM_Node_Pair_list_temp.append(Node_Pairs)

            if temp_int_repeated_pair_counter_5 == 0:
                if ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM and \
                        ECM_Node_Position[ECM_pyramid_Node_4][1] == -Membrane_Centre_distance_from_ECM:
                    if (ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                        ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_4]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                    elif (ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM and
                          ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_4, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_4]
                    ECM_Node_Pair_list_temp.append(Node_Pairs)

            if temp_int_repeated_pair_counter_6 == 0:
                if ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM and \
                        ECM_Node_Position[ECM_pyramid_Node_4][1] == -Membrane_Centre_distance_from_ECM:
                    if (ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                        ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_4]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                    elif (ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                          ECM_Node_Position[ECM_pyramid_Node_4][2] == Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_4][2] == -Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_4, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_4]
                    ECM_Node_Pair_list_temp.append(Node_Pairs)

            if temp_int_repeated_pair_counter_7 == 0:
                if ECM_Node_Position[ECM_pyramid_Node_3][1] == -Membrane_Centre_distance_from_ECM and \
                        ECM_Node_Position[ECM_pyramid_Node_2][1] == -Membrane_Centre_distance_from_ECM:
                    if (ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                        ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_2]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                    elif (ECM_Node_Position[ECM_pyramid_Node_3][2] == -Membrane_Centre_distance_from_ECM and
                          ECM_Node_Position[ECM_pyramid_Node_2][2] == Membrane_Centre_distance_from_ECM) or (
                            ECM_Node_Position[ECM_pyramid_Node_3][2] == Membrane_Centre_distance_from_ECM and
                            ECM_Node_Position[ECM_pyramid_Node_2][2] == -Membrane_Centre_distance_from_ECM):
                        Node_Pairs = [ECM_pyramid_Node_2, ECM_pyramid_Node_3]
                        ECM_Node_Pair_list_temp.append(Node_Pairs)
                else:
                    Node_Pairs = [ECM_pyramid_Node_3, ECM_pyramid_Node_2]
                    ECM_Node_Pair_list_temp.append(Node_Pairs)

            # Increment the repeated pair counters
            temp_int_repeated_pair_counter_1 += 1
            temp_int_repeated_pair_counter_2 += 1
            temp_int_repeated_pair_counter_3 += 1
            temp_int_repeated_pair_counter_4 += 1
            temp_int_repeated_pair_counter_5 += 1
            temp_int_repeated_pair_counter_6 += 1
            temp_int_repeated_pair_counter_7 += 1

    return ECM_Node_Pair_list_temp

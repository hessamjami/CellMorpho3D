import numpy as np

def Actin_Node_Pair_Identifier():
    Actin_Node_Pair_list_temp = []
    Node_Pairs = [-1, -1]
    Actin_Node_Pair_list_temp.append(Node_Pairs)

    Actin_pyramid_Node_1 = 0
    Actin_pyramid_Node_2 = 0
    Actin_pyramid_Node_3 = 0
    Actin_pyramid_Node_4 = 0
    temp_double = 0.0
    temp_string = ""
    Num_of_objects = 0

    temp_int_repeated_pair_counter_1 = 0
    temp_int_repeated_pair_counter_2 = 0
    temp_int_repeated_pair_counter_3 = 0
    temp_int_repeated_pair_counter_4 = 0
    temp_int_repeated_pair_counter_5 = 0
    temp_int_repeated_pair_counter_6 = 0

    with open("RBCActin", "r") as read:
        for _ in range(6):
            temp_string = next(read).strip()

        temp_double = float(next(read).strip())

        for _ in range(Actin_num_of_Nodes):
            temp_double = float(next(read).strip())  # Skip node coordinates
            temp_double = float(next(read).strip())
            temp_double = float(next(read).strip())
            temp_double = float(next(read).strip())

        temp_string = next(read).strip()
        temp_string = next(read).strip()
        Num_of_objects = int(next(read).strip())

        for _ in range(Actin_num_of_triangles):
            # Skip the first five numbers in each line
            for _ in range(5):
                temp_double = float(next(read).strip())

        for _ in range(Num_of_objects - Actin_num_of_triangles):
            for _ in range(5):
                temp_double = float(next(read).strip())  # Skip unnecessary numbers
            # Read the 4 pyramid nodes
            Actin_pyramid_Node_1 = int(next(read).strip()) - 1
            Actin_pyramid_Node_2 = int(next(read).strip()) - 1
            Actin_pyramid_Node_3 = int(next(read).strip()) - 1
            Actin_pyramid_Node_4 = int(next(read).strip()) - 1

            for j in range(len(Actin_Node_Pair_list_temp) - 1):
                if ((Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_1 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_2) or
                    (Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_2 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_1)):
                    temp_int_repeated_pair_counter_1 = 1

                if ((Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_2 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_3) or
                    (Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_3 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_2)):
                    temp_int_repeated_pair_counter_2 = 1

                if ((Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_1 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_3) or
                    (Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_3 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_1)):
                    temp_int_repeated_pair_counter_3 = 1

                if ((Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_1 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_4) or
                    (Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_4 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_1)):
                    temp_int_repeated_pair_counter_4 = 1

                if ((Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_2 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_4) or
                    (Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_4 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_2)):
                    temp_int_repeated_pair_counter_5 = 1

                if ((Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_3 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_4) or
                    (Actin_Node_Pair_list_temp[j][0] == Actin_pyramid_Node_4 and Actin_Node_Pair_list_temp[j][1] == Actin_pyramid_Node_3)):
                    temp_int_repeated_pair_counter_6 = 1

            if temp_int_repeated_pair_counter_1 == 0:
                Actin_Node_Pair_list_temp[-1][0] = Actin_pyramid_Node_1
                Actin_Node_Pair_list_temp[-1][1] = Actin_pyramid_Node_2
                Actin_Node_Pair_list_temp.append(list(Node_Pairs))

            if temp_int_repeated_pair_counter_2 == 0:
                Actin_Node_Pair_list_temp[-1][0] = Actin_pyramid_Node_2
                Actin_Node_Pair_list_temp[-1][1] = Actin_pyramid_Node_3
                Actin_Node_Pair_list_temp.append(list(Node_Pairs))

            if temp_int_repeated_pair_counter_3 == 0:
                Actin_Node_Pair_list_temp[-1][0] = Actin_pyramid_Node_1
                Actin_Node_Pair_list_temp[-1][1] = Actin_pyramid_Node_3
                Actin_Node_Pair_list_temp.append(list(Node_Pairs))

            if temp_int_repeated_pair_counter_4 == 0:
                Actin_Node_Pair_list_temp[-1][0] = Actin_pyramid_Node_1
                Actin_Node_Pair_list_temp[-1][1] = Actin_pyramid_Node_4
                Actin_Node_Pair_list_temp.append(list(Node_Pairs))

            if temp_int_repeated_pair_counter_5 == 0:
                Actin_Node_Pair_list_temp[-1][0] = Actin_pyramid_Node_2
                Actin_Node_Pair_list_temp[-1][1] = Actin_pyramid_Node_4
                Actin_Node_Pair_list_temp.append(list(Node_Pairs))

            if temp_int_repeated_pair_counter_


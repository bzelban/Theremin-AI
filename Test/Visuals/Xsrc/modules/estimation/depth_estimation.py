import numpy as np
import math


class Hand_Depth_Estimation_Module():


    def depth_estimation(self, LEFT_HAND_DATA):
        Velocity = 0
        landmark_positions = [0.0]
        temp_mean = 0
        ct = 0

        if LEFT_HAND_DATA.multi_hand_landmarks:
            for num, hand in enumerate(LEFT_HAND_DATA.multi_hand_landmarks):
                for idx, classification in enumerate(LEFT_HAND_DATA.multi_handedness):
                    if classification.classification[0].index == 1:

                        #############################################################
                        # This part is for getting difference
                        # of 2 points by using analytical geometric calculation

                        Rx = hand.landmark[13].x - hand.landmark[0].x
                        Ry = hand.landmark[13].y - hand.landmark[0].y

                        Velocity = np.sqrt(Rx**2 + Ry**2)
                        Velocity = round(Velocity, 1)

                        Velocity = ((Velocity * 100) / 5) * 10

                        return int(Velocity)
                        ############################################################

                        # cz = math.log(np.abs(hand.landmark[idx].z))
                        # landmark_positions.append(round(abs(cz), 4))
                        # temp_mean = temp_mean + round(abs(cz), 3)

            # max_veloc = math.log(np.abs(np.max(landmark_positions)), 2)
            #
            # if max_veloc > 9:
            #     pass
            #     # print(max_veloc % 2.5)
            #     # print(max_veloc)
            # else:
            #     return Velocity


        else:
            return Velocity
import numpy as np


class Hand_Distance_Estimation_Module():

    def distance_estimation(self, RIGHT_HAND_DATA):

        frame_channel = (480, 640, 3)
        landmark_positions = [0]
        temp_position = 0

        if RIGHT_HAND_DATA:
            for hand_landmarks in RIGHT_HAND_DATA:
                for id, marks in enumerate(hand_landmarks.landmark):
                    height, width, channel = frame_channel
                    cx = int(marks.x * width)
                    landmark_positions.append(cx)

        temp_position = np.max(landmark_positions)

        if (temp_position > 0 and temp_position < 640):
            PITCHVALUE = round(temp_position / 10) + 10
            return PITCHVALUE
        else:
            PITCHVALUE = 0
            return PITCHVALUE
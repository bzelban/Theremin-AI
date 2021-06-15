import cv2
import mediapipe as pipe
import array as arr
import numpy as np
import queue as q


cam0 = cv2.VideoCapture(0)
pipe_hands = pipe.solutions.hands
hands = pipe_hands.Hands()
draw_utils = pipe.solutions.drawing_utils


class Hand_Detection_Module():

    def get_vision(self):
        success, window = cam0.read()  # shape is 640x480
        imgRGB = cv2.cvtColor(window, cv2.COLOR_BGR2RGB)
        return imgRGB

    def detection(self, VISUAL_DEBUG, queue):

        while True:
            frame = self.get_vision()
            res = hands.process(frame)

            '''
            res.multi_hand_landmarks[0] means Left Hand
            res.multi_hand_landmarks[1] means Right Hand
            
            if res.multi_hand_landmarks:
                for hand_landmarks in res.multi_hand_landmarks:
                    for id, marks in enumerate (hand_landmarks.landmark):
                        height, width, channel = window.shape
                        cx, cy = int(marks.x * width), int(marks.y * height)
                        landmark_positions.append(cx)

                draw_utils.draw_landmarks(window, hand_landmarks, pipe_hands.HAND_CONNECTIONS)

            temp_position = np.max(landmark_positions)
            landmark_positions = [0]
            '''
            if VISUAL_DEBUG:
                cv2.imshow("bench Window", window)
                cv2.waitKey(1)

            queue.put(res.multi_handedness)
            '''
            if (temp_position != None):
                if (temp_position > 0 and temp_position < 640):
                    print('HAND IN PROCESS')
                    req_position = temp_position
                    return req_position
                else:
                    req_position = -1
                    return req_position
            else:
                return -1
            '''

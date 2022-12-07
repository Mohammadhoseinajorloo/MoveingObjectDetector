import cv2

class Video:
    

class Frame:
    RECTANGLR_COLOR = (0, 255, 0)
    REGTANGLE_WIDTH = 10
    WINDOW_TITLE = 'MoveingObjectDetector'

    def __init__(self, frame):
        self.__frame = frame

    def blurred_frame(self):
        return cv2.GaussianBlur(self.__frame, (9,9), 1)

    def gray_scale(self):
        return cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
         
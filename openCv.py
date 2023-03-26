import cv2
import numpy as np

def squidgame():
    video = cv2.VideoCapture(0)

    video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if(video.isOpened()):
        ret, Head = video.read()
        while ret:
            ret, Tail = video.read()

            color = Head.copy()
            cv2.imshow('Color', color)

            if not ret:
                break

            Head_BW = cv2.cvtColor(Head, cv2.COLOR_BGR2GRAY)
            TAil_BW = cv2.cvtColor(Tail, cv2.COLOR_BGR2GRAY)
            cv2.imshow('BW', Head_BW)

            diff = cv2.absdiff(Head_BW, TAil_BW)
            cv2.imshow('Diff', diff)

            ret, diff_binary = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)
            cv2.imshow('Diff_binary', diff_binary)

            white_pixel = cv2.countNonZero(diff_binary)

            if white_pixel > 150:
                cv2.imshow('Color', red_frame(color))

            Head = Tail

            if cv2.waitKey(1) & 0xFF == 27:
                break

def red_frame(frame):
    red_img = np.full((480, 640, 3), (0, 0, 255), dtype=np.uint8)
    frame = cv2.addWeighted(frame, 0.5, red_img, 0.5, 0)
    return frame

squidgame()
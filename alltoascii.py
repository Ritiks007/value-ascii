import cv2
import numpy as np
import time

# ------------------------------------------------------------------------
#                     Global Variables
# ------------------------------------------------------------------------

# Terminal screen dimensions
tw = 240
th = 70

ext = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', "'", "'", "'", "'", '.', '.', '.', '-', '-', '-', '-', '-', '-', '-', ',', ',', ',', ',', ',', ',', ',', '_', '_', '_', '~', '~', '~', '~', '~', '~', '~', '"', '"', '"', '+', '+', '+', '+', '^', '^', '^', '!', '!', '!', '=', '=', '=', '=', '=', '=', '=', '*', '*', '*', '*', '*', '*', '*', '<', '<', '<', '|', '|', '|', '|', '\\', '\\', '\\', '?', '?', '?', '?', '?', '?', '?', '(', '(', '(', 'l', 'l', 'l', 'l', '7', '7', '7', 'v', 'v', 'v', 'v', 'r', 'r', 'r', 'r', 'r', 'r', '}', '}', '}', '}', '{', '{', '{', '4', '4', '4', '4', 'j', 'j', 'j', 'u', 'u', 'u', 'o', 'o', 'o', 'o', 'e', 'e', 'e', '5', '5', '5', '5', 'y', 'y', 'y', 'h', 'h', 'h', 'k', 'k', 'k', 'k', 'E', 'E', 'E', 'S', 'S', 'S', 'S', 'X', 'X', 'X', 'P', 'P', 'P', 'd', 'd', 'd', 'd', 'U', 'U', 'U', 'w', 'w', 'w', 'w', 'q', 'q', 'q', '0', '0', '0', 'H', 'H', 'H', 'H', '8', '8', '8', 'D', 'D', 'D', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'N', 'N', 'N', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', 'M', 'M', 'M', 'M', 'W', 'W', 'W', 'W', 'W', 'W', 'W']


# ------------------------------------------------------------------------
#                     Util Functions
# ------------------------------------------------------------------------

def clear():
    print("\033c", end="")

def mapSingle(im):
    clear()
    ascmap = ""
    for y in range(th):
        for x in range(tw):
            ascmap += ext[im[y][x]]
        ascmap += '\n'
    print(ascmap)

# ------------------------------------------------------------------------
#                     Main Driver Function
# ------------------------------------------------------------------------
if __name__ == "__main__":
    print('Choices:')
    print('1. image to ascii')
    print('2. camera to ascii')
    print('3. video to ascii')
    choice = input('Enter Your Choice: ')
    if choice == '1':
        th = 120
        filename = input('Enter Filename: ')
        im = cv2.imread(filename, 0)
        im = cv2.resize(im, (tw, th))
        mapSingle(im)
    elif choice == '2':
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            im = cv2.resize(gray, (tw, th))
            mapSingle(im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
    elif choice == '3':
        filename = input('Enter Filename: ')
        cap = cv2.VideoCapture(filename)
        while cap.isOpened():
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            im = cv2.resize(gray, (tw, th))
            mapSingle(im)
            time.sleep(0.010)
        cap.release()
    else :
        print('Wrong CHoice, Exiting...')

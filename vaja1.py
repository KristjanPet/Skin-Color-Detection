import cv2
import numpy as np
from numba import jit

@jit(nopython=True)
def search(frame):
    face = [0, 0, 0]
    for x in range(0, 320, 8): # width of the observed square
        for y in range(0, 240, 6): # height of the observed square
            approved = 0 # number of skin-colored pixels
            for i in range(y, y+48): # check each row in the square
                for j in range(x, x+64): # check each column in the square
                    blue  =  frame[i,j,0]
                    green =  frame[i,j,1]
                    red   =  frame[i,j,2]
                    if 100 <= blue <= 160 and 100 <= green <= 155 and 120 <= red <= 180: # if it's a skin color
                        approved += 1
            if approved > face[2]: # update if more skin is detected
                face = [x, y, approved]
    return face


cap = cv2.VideoCapture("test.mp4")
#cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Unable to open camera")
    


while True:
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.resize(frame, (320, 240)) # resize to 320x240
        face = search(frame) # search for face
        x = face[0]
        y = face[1]
        
        # Calculate and adjust the size of the rectangle based on the detected skin area
        if face[2] > 0:
            detected_width = int(1.5 * np.sqrt(face[2]))  # Adjust width based on skin area
            detected_height = int(1.2 * np.sqrt(face[2]))  # Adjust height based on skin area
        
        cv2.rectangle(frame, (x, y), (x+detected_width, y+detected_height), (255, 0, 0), 1) # draw rectangle
        cv2.imshow("Camera",frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break


width  = cap.get(3)  # float `width`
height = cap.get(4)  # float `height`
fps = cap.get(5)
    
print('fps:', fps)  # float `fps`
print('width, height:', width, height)

cap.release()
cv2.destroyAllWindows()
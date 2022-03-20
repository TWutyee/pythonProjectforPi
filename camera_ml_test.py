from picamera import PiCamera
from time import sleep
import numpy as np
import pandas as pd
# from gpiozero import Servo
# servo =Servo(2)
camera = PiCamera()

camera.resolution = (64,64)

sleep(2)
output = np.empty((64, 64, 3), dtype=np.uint8)

def camchk():
    camera.start_preview()
    sleep(5)
    camera.stop_preview()

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()

print("train the machine")
x=[]
y=[]
while (5 > 1):
    camchk()
    ch = input("enter l for light and d for dark and f for finish training")
    if (ch == 'l'):

        camera.capture(output, 'rgb')
        c = [(int(output[0, :, 0].mean())), (int(output[0, :, 1].mean())), (int(output[0, :, 2].mean()))]
        x.append(c)
        y.append(1)

    elif (ch == 'd'):
        camera.capture(output, 'rgb')
        c = [(int(output[0, :, 0].mean())), (int(output[0, :, 1].mean())), (int(output[0, :, 2].mean()))]
        x.append(c)
        y.append(0)

    elif (ch == 'f'):
        x = pd.DataFrame(x)
        y = pd.DataFrame(y)
        print(x)
        print(y)

        classifier.fit(x,y)
        break


    else:
        print('noob')

print("fun time")
print("press s to check")

while(5>1):
    camchk()
    ch = input("enter s to check and b to end")
    if(ch=='s'):
        camera.capture(output, 'rgb')
        c=[(int(output[0,:,0].mean())),(int(output[0,:,1].mean())),(int(output[0,:,2].mean()))]
        print("c"+str(c))
        y_pred = classifier.predict([c])
        if(y_pred == 1):
            print("light")
        else:
            print("dark")
    else:
        break

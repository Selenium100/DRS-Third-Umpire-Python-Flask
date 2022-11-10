import tkinter
import cv2 # pip install opencv-python
import PIL.Image,PIL.ImageTk #pip install pillow
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture("clip.mp4")



# width and height of out main screen

SET_WIDTH = 680

SET_HEIGHT = 334



#functions

def play(speed):

    print(f"You pressed Give out in {speed} speed")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame = stream.read()
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)


def out():

    print("Player is out")

    thread = threading.Thread(target=pending,args=("out",))

    thread.daemon = 1

    thread.start()



def not_out():

    print("Player is Not Out")

    thread = threading.Thread(target=pending,args=("not out",))

    thread.daemon = 1

    thread.start()



def pending(decission):

    # Display Decission Pending image

    frame = cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)

    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    canvas.image = frame

    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)

    # wait for 1 sec

    time.sleep(2)

    # Display Sponser image

    frame = cv2.cvtColor(cv2.imread("sponser.jpg"),cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)

    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    canvas.image = frame

    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)

    # wait for 1.5 sec

    time.sleep(1.5)

    # Display out/notout

    if decission =='out':

        dicssionimg = 'out.jpg'

    else:

         dicssionimg = 'not_out.jpeg'



    frame = cv2.cvtColor(cv2.imread(dicssionimg),cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)

    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    canvas.image = frame

    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)





#tkinter GUI starts from here

window = tkinter.Tk()

window.title("Third Umpire Decission Kit")

cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"),cv2.COLOR_BGR2RGB)

canvas = tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)

canvas.pack()


#Buttons to control playback

btn = tkinter.Button(window,text="<< previous (fast)",width=100,command=partial(play,-25))

btn.pack()


btn = tkinter.Button(window,text="<< previous (slow)",width=100,command=partial(play,-2))

btn.pack()


btn = tkinter.Button(window,text="Next (slow) >>",width=100,command=partial(play,2))

btn.pack()


btn = tkinter.Button(window,text="Next (fast) >>",width=100,command=partial(play,25))

btn.pack()


btn = tkinter.Button(window,text="Give Out",width=100,command=out)

btn.pack()


btn = tkinter.Button(window,text="Give Not Out",width=100,command=not_out)

btn.pack()


window.mainloop()
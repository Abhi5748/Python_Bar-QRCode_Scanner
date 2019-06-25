from pyzbar import pyzbar
import argparse
import cv2
from tkinter import *


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image")
args = vars(ap.parse_args())
master=Tk()
master.title("BARCODE SCANNER")
master.geometry("600x400")
value= Entry(master)
def main(image):
    if image is None:
        camera_port = 0
 
        ramp_frames = 30

        camera = cv2.VideoCapture(camera_port)
     
        def get_image():
            retval, im = camera.read()
            return im
    
        for i in range(ramp_frames):
            temp = get_image()
        
        print("Taking image...")
        camera_capture = get_image()

        file = r"C:\Users\ABHINAV RAMESH\Desktop\Python project\webcam.jpg"
    
        cv2.imwrite(file, camera_capture)
        del(camera)
    
        image=cv2.imread("webcam.jpg")
    
    else:

        image = cv2.imread(image)
    barcodes=pyzbar.decode(image)

    file = open('data.txt', 'w')

    for barcode in barcodes:
        
        (x,y,w,h) = barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{}({})".format(barcodeData,barcodeType)
        cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

        file.write(barcodeData)
        file.write("\n")
        file.write(barcodeType)

    file.close()
    
    cv2.imshow("Image",image)
    cv2.waitKey(0)

def gettext():
    image = value.get()
    main(image)

def display():
    img = Label(master,text="Enter IMAGE Name:")
    
    submit=Button(master,text="SUBMIT",command=gettext)
    img.place(x=100,y=200)
    value.place(x=120,y=250)
    
    submit.place(x=120,y=300)

def sett():
    
    main(None)

    
getname=Button(master,text="ENTER IMAGE",command=display)
getname.place(x=100,y=100)
getimage=Button(master,text="SCAN IMAGE",command=sett)
getimage.place(x=400,y=100)


master.mainloop()

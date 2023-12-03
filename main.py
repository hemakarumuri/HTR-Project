from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract
#from fpdf import FPDF
#from translate import Translator

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
root = Tk()
root.title('OCR Project') 

newline= Label(root)
uploaded_img=Label(root)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )


def extract(path):
    f = open("file.txt","w")
    Actual_image = cv2.imread(path)
    Sample_img = cv2.resize(Actual_image,(400,350))
    Image_ht,Image_wd,Image_thickness = Sample_img.shape
    Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BGR2RGB)
    texts = pytesseract.image_to_data(Sample_img) 
    mytext=""
    prevy=0
    for cnt,text in enumerate(texts.splitlines()):
        if cnt==0:
            continue
        text = text.split()
        if len(text)==12:
            x,y,w,h = int(text[6]),int(text[7]),int(text[8]),int(text[9])
            if(len(mytext)==0):
                prey=y
            if(prevy-y>=10 or y-prevy>=10):
                print(mytext+text[11])
                f.write(mytext)
                Label(root,text=mytext,font=('Times',15,'bold')).pack()
                mytext=""
            mytext = mytext + text[11]+" "
            prevy=y
            #f.write()
    Label(root,text=mytext,font=('Times',15,'bold')).pack()
    #f.write(text)
    f.close()


def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda:
                       extract(path),bg="#2f2f77",fg="gray",
                       pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.pack()

def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img_resized=image.resize((400,200))
        img=ImageTk.PhotoImage(img_resized)
        #img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass


uploadbtn1 = Button(root,text="Hand Written Text Recognition",command=upload,
                   bg="#2f2f77",fg="gray",height=2,width=25,
                   font=('Times',15,'bold')).pack()
#print('\n')
#print('\n')
#uploadbtn1.place(x=400,y=50)
uploadbtn = Button(root,text="Upload an image",command=upload,
                   bg="#2f2f77",fg="gray",height=2,width=20,
                   font=('Times',15,'bold')).pack()
#uploadbtn.place(x=400,y=80)
#extractlangBtn.pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()

root.mainloop()

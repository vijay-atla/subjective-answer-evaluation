import re, math
import numpy as np
from tkinter import messagebox
import PIL.Image
import pytesseract
from collections import Counter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import tkinter
from tkinter import messagebox
from vision import detect_document

root = tkinter.Tk()
root.title("Subjective Answer Evaluation")
root.geometry("1200x720")
root.configure(bg='light blue')

global answer_path
global image_path
global answer
global student_answer

from collections import defaultdict
vector = defaultdict(list)
arrayList = []
WORD = re.compile(r'\w+')

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def uploadAnswers():
    global answer_path
    global answer
    answer = ""
    answer_path = askopenfilename(initialdir = "Answers")
    answerlabel.config(text=answer_path)
    with open(answer_path, "r") as file:
      for line in file:
       line = line.strip('\n')
       line = line+" "
       answer+=line 

def uploadImage():
    global image_path
    global student_answer
    image_path = askopenfilename(initialdir = "images")

    
    answerlabel2.config(text=image_path)
    
    student_answer=detect_document(image_path)
    text.delete('1.0',END);
    text.insert(END,student_answer+"\n\n")
    
    print(student_answer)

def evaluate():
  try:
    grade =""
    vector1 = text_to_vector(answer)
    vector2 = text_to_vector(student_answer)
    cosine = get_cosine(vector1, vector2)
    cosine = cosine * 100;
    if cosine >= 90:
       grade = "Excellent"
    if cosine >= 80 and cosine < 90:
       grade = "Very Good"
    if cosine >= 70 and cosine < 80:
       grade = "Good"
    if cosine >= 50 and cosine < 70:
       grade = "Ok"
    if cosine >= 35 and cosine < 50:
       grade = "Poor"
    if cosine < 35:
       grade = "Very Poor"
    text.insert(END,"Your score : "+str(cosine)+"\n")
    text.insert(END,"Your Grade : "+str(grade)+"\n")
    messagebox.showinfo("Dataset filtered successfully","Your score : "+str(cosine)+"\nYour Grade : "+grade)
  except NameError:
     messagebox.showwarning("warning","Please Upload the file first") 


answerlabel0 = Label(root,bg='light blue')
answerlabel0.pack()

upload = Button(root, text="Upload key Answers", activebackground='#345',activeforeground='white', command=uploadAnswers)
upload.pack()

answerlabel = Label(root,fg='green',bg='light blue')
answerlabel.pack()
answerlabel0 = Label(root,bg='light blue')
answerlabel0.pack()


imagebutton = Button(root, text="Upload Student Answer Image", activebackground='#345',activeforeground='white', command=uploadImage)
imagebutton.pack()

answerlabel2 = Label(root,fg='green',bg='light blue')
answerlabel2.pack()
answerlabel0 = Label(root,bg='light blue')
answerlabel0.pack()

evaluate = Button(root, text="Evaluate Answer", activebackground='#345',activeforeground='white', command=evaluate)
evaluate.pack()

answerlabel3 = Label(root,bg='light blue')
answerlabel3.pack()
answerlabel0 = Label(root,bg='light blue')
answerlabel0.pack()
answerlabel0 = Label(root,bg='light blue')
answerlabel0.pack()


text=Text(root, height=30  ,width=120,bg= 'light yellow')
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.pack()

root.mainloop()

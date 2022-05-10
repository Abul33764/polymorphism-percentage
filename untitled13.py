from tkinter import *
root = Tk()
root.title("polymorphism")
root.geometry("200x200")

class grade_3():
    def __init__(self,math,language,social_studies):
        self.math= math
        self.language=language
        self.social_studies=social_studies
    def percentage(self):
        total_score =self.math+self.language+self.social_studies
        percentage = (total_score*100)/300
        label["text"] =str(percentage) + "%"
class grade_4():
    def __init__(self,math,language,social_studies):
        self.math= math
        self.language=language
        self.social_studies=social_studies
    def percentage(self):
        total_score =self.math+self.language+self.social_studies
        percentage = (total_score*100)/300
        label1["text"] =str(percentage) + "%"
class grade_5():
    def __init__(self,math,language,social_studies):
        self.math= math
        self.language=language
        self.social_studies=social_studies
    def percentage(self):
        total_score =self.math+self.language+self.social_studies
        percentage = (total_score*100)/300
        label2["text"] =str(percentage) + "%"
    
obj3= grade_3(81,60,90)
obj4=grade_4(100,80,60)
obj5=grade_5(100,95,90)

label = Label(root)
label.pack()
btn = Button(root,text="GRADE 3",command=obj3.percentage)
btn.pack()
label1 = Label(root,)
label1.pack()
btn1 = Button(root,text="GRADE 4",command=obj4.percentage)
btn1.pack()
label2 = Label(root)
label2.pack()
btn2 = Button(root,text="GRADE 5",command=obj5.percentage)
btn2.pack()

root.mainloop()

         
         
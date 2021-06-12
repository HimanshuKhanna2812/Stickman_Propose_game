from tkinter import *
import tkinter.messagebox
class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("I am Robot")
        self.root.resizable(False,False)
        self.root.geometry("1150x550+100+50")
        self.root.config(bg="#000000")
        self.root.title("Skarsh Stickman-game")
        self.canvas = Canvas(self.root,width=1050,bd=2,relief="ridge",height=642,bg="black")
        self.canvas.pack()
        
        self.canvas.create_text(500,225,text="Stickman proposal video\n             using (tkinter)",fill="white",font="constantia 50 bold italic",tag="stickman") # count Down start
    
        self.root.after(1600,self.start)
        self.root.mainloop()
    def start(self):
        self.canvas.delete("stickman")
        self.canvas.create_text(500,225,text="Let's Start",fill="white",font="times 55 bold italic",tag="start") # count Down start
        self.root.after(600,self.countDown3)
    def countDown3(self):
        self.canvas.delete("stickman")
        self.canvas.create_text(500,300,text="3",fill="white",font="times 50 bold italic",tag="count")
        self.root.after(700,self.countDown2)
    def countDown2(self):
        self.canvas.delete("count")
        self.canvas.create_text(500,300,text="2",fill="white",font="times 50 bold italic",tag="count")
        self.root.after(700,self.countDown1)
    def countDown1(self):
        self.canvas.delete("count")
        self.canvas.create_text(500,300,text="1",fill="white",font="times 50 bold italic",tag="count")
        self.root.after(700,self.body)
    
    def body(self):
        self.canvas.delete("count")
        self.canvas.delete("start")
        self.canvas.create_line(0,480,1100,480,fill="white",width=2)   #background line
        self.canvas.create_rectangle(0,600,1100,482,width=2,fill='#0a6325')       # grass
        self.leg0()
    def leg0(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("hey")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")      
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("crush")
        self.canvas.delete("msg")
        self.canvas.create_line(54,441,55,400,fill="white",width=2,tag="leftleg")    #leftleg 1    - yhi hogi change isliye tag liya h
        self.canvas.create_line(51,480,54,441,fill="white",width=2,tag="leftleg")    #ulta pair 2
        self.canvas.create_line(70,437,55,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(40,481,70,437,fill="white",width=2,tag="rightleg")  
        
        self.canvas.create_line(42,342,55,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(42,342,60,376,fill="white",width=2,tag="lefthand")    #ulta hath 2  
        self.canvas.create_line(87,286,55,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(87,286,110,246,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_oval(20,200,90,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(50,220,57,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(70,220,77,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(55,270,55,400,fill="white",width=2,tag="center")    #centerstick
        #crush
        self.canvas.create_oval(920,200,990,270,width=2,fill="white",tag="crush")    #face
        self.canvas.create_oval(950,220,957,227,width=2,tag="crush")    #sidhi aankh
        self.canvas.create_oval(941,227,934,220,width=2,tag="crush")    #ulti aankh
        self.canvas.create_line(990,200,990,301,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(992,200,992,303,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(994,200,994,305,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(996,200,996,307,fill="white",width=1,tag="crush")    #hair4
        self.canvas.create_line(971,204,995,204,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(973,206,995,206,fill="white",width=1,tag="crush")  
        self.canvas.create_line(975,208,995,208,fill="white",width=1,tag="crush")  
        self.canvas.create_line(981,210,995,210,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(983,212,995,212,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(986,214,995,214,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(955,303,955,346,fill="white",width=2,tag="crush")    #haath
        self.canvas.create_line(945,380,955,346,fill="white",width=2,tag="crush")    #haath2
        self.canvas.create_line(959,270,959,280,fill="white",width=2,tag="crush")    #centerstick2
        self.canvas.create_line(955,270,955,280,fill="white",width=2,tag="crush") 
        self.canvas.create_line(938,443,942,430,fill="white",width=2,tag="crush")    #sidha pair
        self.canvas.create_line(939,481,938,443,fill="white",width=2,tag="crush")    #sidha pair 2
        self.canvas.create_line(956,448,955,430,fill="white",width=2,tag="crush")    #ulta pair
        self.canvas.create_line(956,448,965,483,fill="white",width=2,tag="crush")    #ulta pair2
        self.canvas.create_line(900,430,997,430,fill="white",width=2,tag="crush")  #surface
        self.canvas.create_line(900,430,936,370,fill="white",width=2,tag="crush")  #incline
        self.canvas.create_line(936,370,936,300,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(936,300,951,280,fill="white",width=2,tag="crush") # surface
        self.canvas.create_line(951,280,965,280,fill="white",width=2,tag="crush")  #neck
        self.canvas.create_line(965,280,965,370,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(965,370,997,430,fill="white",width=2,tag="crush")  #incline
           #face
        self.canvas.create_text(1020,175,text="*crush",tag="crush",font="times 19 bold",fill="red")
        self.canvas.create_rectangle(40,90,170,160,outline="white",width=1,tag="Mmsg") #rectangle
        self.canvas.create_text(103,130,text="Hey hii",font="constantia 25 bold ",fill="#46a2b0",tag="Fmsg") #hey hi 
        self.canvas.create_line(65,190,110,160,fill="white",width=1,tag="Mmsg") #line
        self.root.after(800,self.leg01)
        
    def leg01(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("hey")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")      
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("msg")
        self.canvas.create_line(54,441,55,400,fill="white",width=2,tag="leftleg")    #leftleg 1    - yhi hogi change isliye tag liya h
        self.canvas.create_line(51,480,54,441,fill="white",width=2,tag="leftleg")    #ulta pair 2
        self.canvas.create_line(70,437,55,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(40,481,70,437,fill="white",width=2,tag="rightleg")  
        
        self.canvas.create_line(42,342,55,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(42,342,60,376,fill="white",width=2,tag="lefthand")    #ulta hath 2  
        self.canvas.create_line(87,286,55,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(87,286,110,246,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_oval(20,200,90,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(50,220,57,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(70,220,77,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(55,270,55,400,fill="white",width=2,tag="center")    #centerstick
        self.canvas.create_rectangle(800,90,910,160,width=1,outline="white",tag="Fmsg") #rectangle
        self.canvas.create_text(853,130,text="Hlo..",font="constantia 25 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(930,190,860,160,fill="white",width=1,tag="Mmsg")  # line
        
        
        # ye apna leg kholega
        self.root.after(1200,self.leg1)
    
    def leg1(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("hey")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")      
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("Mmsg")
        self.canvas.delete("Fmsg")
        self.canvas.create_line(59,438,67,400,fill="white",width=2,tag="leftleg")    #leftleg 1    - yhi hogi change isliye tag liya h
        self.canvas.create_line(35,480,59,438,fill="white",width=2,tag="leftleg")    #ulta pair 2
        self.canvas.create_line(100,437,67,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(110,481,100,437,fill="white",width=2,tag="rightleg")  
        
        self.canvas.create_line(46,334,67,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(46,334,38,373,fill="white",width=2,tag="lefthand")    #ulta hath 2  
        self.canvas.create_line(82,340,67,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(82,340,106,370,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_oval(32,200,102,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(62,220,69,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(82,220,89,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(67,270,67,400,fill="white",width=2,tag="center")    #centerstick
        
        
        self.root.after(225,self.leg2)
    
    def leg2(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")    
        self.canvas.delete("lefteye")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(91,443,97,400,width=2,tag="leftleg",fill="white")    #ulta pair
        self.canvas.create_line(64,480,91,443,width=2,tag="leftleg",fill="white") 
        self.canvas.create_line(120,438,97,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(123,482,120,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(103,350,97,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(103,350,134,387,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(75,343,97,295,width=2,tag="lefthand",fill="white")    #ulta hath 1
        self.canvas.create_line(75,343,77,390,width=2,tag="lefthand",fill="white")    #ulta hath 2
        self.canvas.create_oval(63.5,200,133.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(93.5,220,100.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(113.5,220,120.5,227,width=2,tag="eye")    #sidhi aankh
       
        self.canvas.create_line(97,270,97,400,fill="white",width=2,tag="center")    #centerstick
        
        self.root.after(225,self.leg3)
     
    def leg3(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("righteye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(129,443,127,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(99,477,129,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(141,438,127,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(142,482,141,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(128,347,127,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(128,347,143,379,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(120,343,127,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(120,343,140,388,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(93.5,200,163.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(123.5,220,130.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(143.5,220,150.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(127,270,127,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg4)
    def leg4(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(154,443,157,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(151,477,154,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(176,441,157,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(144,470,176,441,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(140,348,157,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(140,348,153,375,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(161,343,157,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(161,343,177,382,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(123.5,200,193.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(153.5,220,160.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(173.5,220,180.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(157,270,157,400,fill="white",width=2,tag="center")    #centerstick
        
        self.root.after(225,self.leg5)
 
    def leg5(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("righthand2")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(179,443,187,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(162,477,179,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(211,438,187,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(204,477,211,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(211,345,187,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(211,345,232,373,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(160,340,187,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(160,340,180,383,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(153.5,200,223.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(183.5,220,190.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(203.5,220,210.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(187,270,187,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg6)

    def leg6(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("face")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.create_line(209,438,217,400,fill="white",width=2,tag="leftleg")    #leftleg 1    - yhi hogi change isliye tag liya h
        self.canvas.create_line(185,480,209,438,fill="white",width=2,tag="leftleg")    #ulta pair 2
        self.canvas.create_line(250,437,217,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(260,481,250,437,fill="white",width=2,tag="rightleg")  
        self.canvas.create_line(190,334,217,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(190,334,182,373,fill="white",width=2,tag="lefthand")    #ulta hath 2  
        self.canvas.create_line(242,337,217,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(242,337,270,370,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_oval(183.5,200,253.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(213.5,220,220.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(233.5,220,240.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(217,270,217,400,fill="white",width=2,tag="center")    #centerstick
        self.canvas.create_text(420,250,text="",font="times 24 bold",tag="hey")

        self.root.after(225,self.leg7)

    def leg7(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("face")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.create_line(241,443,247,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(214,480,241,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(270,438,247,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(273,482,270,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(253,350,247,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(253,350,284,387,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(225,343,247,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(225,343,227,390,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(213.5,200,283.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(243.5,220,250.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(263.5,220,270.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(247,270,247,400,fill="white",width=2,tag="center")    #centerstick
        self.canvas.create_text(420,250,text="",font="times 24 bold",tag="hey")
        self.root.after(225,self.leg8)

    def leg8(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
    
        self.canvas.create_line(279,443,277,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(249,477,279,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(291,438,277,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(292,482,291,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(278,347,277,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(278,347,293,379,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(270,343,277,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(270,343,290,388,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(243.5,200,313.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(273.5,220,280.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(293.5,220,300.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(277,270,277,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg9)
   
    def leg9(self):
	       
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(304,443,307,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(301,477,304,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(326,441,307,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(294,470,326,441,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(290,348,307,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(290,348,303,375,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(311,343,307,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(311,343,327,382,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(273.5,200,343.5,270,width=2,tag="face",fill="white")    #face
        self.canvas.create_oval(303.5,220,310.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(323.5,220,330.5,227,width=2,tag="eye")    #sidhi aankh
       
        self.canvas.create_line(307,270,307,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg10)
    def leg10(self):
	       
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(329,443,337,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(312,477,329,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(361,438,337,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(354,477,361,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(361,345,337,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(361,345,382,373,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(310,340,337,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(310,340,330,383,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(303.5,200,373.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(333.5,220,340.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(353.5,220,360.5,227,width=2,tag="eye")    #sidhi aankh
       
        self.canvas.create_line(337,270,337,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg11)
    def leg11(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("hey")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")      
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("Mmsg")
        self.canvas.delete("Fmsg")
        self.canvas.create_line(359,438,367,400,fill="white",width=2,tag="leftleg")    #leftleg 1    - yhi hogi change isliye tag liya h
        self.canvas.create_line(335,480,359,438,fill="white",width=2,tag="leftleg")    #ulta pair 2
        self.canvas.create_line(400,437,367,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(410,481,400,437,fill="white",width=2,tag="rightleg")  
        self.canvas.create_line(346,334,367,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(346,334,338,373,fill="white",width=2,tag="lefthand")    #ulta hath 2  
        self.canvas.create_line(382,340,367,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(382,340,406,370,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_oval(332,200,402,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(362,220,369,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(382,220,389,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(367,270,367,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg12)
    
    def leg12(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")    
        self.canvas.delete("lefteye")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(391,443,397,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(364,480,391,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(420,438,397,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(423,482,420,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(403,350,397,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(403,350,434,387,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(375,343,397,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(375,343,377,390,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(363.5,200,433.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(393.5,220,400.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(413.5,220,420.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(397,270,397,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg13)
     
    def leg13(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("righteye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(429,443,427,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(399,477,429,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(441,438,427,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(442,482,441,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(428,347,427,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(428,347,443,379,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(420,343,427,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(420,343,440,388,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(393.5,200,463.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(423.5,220,430.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(443.5,220,450.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(427,270,427,400,fill="white",width=2,tag="center")    #centerstick
        self.root.after(225,self.leg14)
        
        
        
        #yaha se krna ab 
    def leg14(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.create_line(454,443,457,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(451,477,454,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(476,441,457,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(444,470,476,441,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(440,348,457,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(440,348,453,375,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(461,343,457,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(461,343,477,382,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(423.5,200,493.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(453.5,220,460.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(473.5,220,480.5,227,width=2,tag="eye")    #sidhi aankh
       
        self.canvas.create_line(457,270,457,400,fill="white",width=2,tag="center")    #centerstick
        
        self.root.after(225,self.leg15)
 
    def leg15(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("righthand2")
        self.canvas.delete("lefthand")
        self.canvas.delete("crush")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("crush")
        self.canvas.create_line(479,443,487,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(462,477,479,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(511,438,487,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(504,477,511,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(511,345,487,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(511,345,532,373,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(460,340,487,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(460,340,480,383,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(453.5,200,523.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(483.5,220,490.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(503.5,220,510.5,227,width=2,tag="eye")    #sidhi aankh
       
        self.canvas.create_line(487,270,487,400,fill="white",width=2,tag="center")    #centerstick
        #crush
          
        self.canvas.create_oval(890,200,960,270,width=2,fill="white",tag="crush")    #face
        self.canvas.create_oval(920,220,927,227,width=2,tag="crush")    #sidhi aankh
        self.canvas.create_oval(911,227,904,220,width=2,tag="crush")    #ulti aankh
        self.canvas.create_line(960,200,960,301,width=1,tag="crush",fill="white")    #hair1
        self.canvas.create_line(962,200,962,303,width=1,tag="crush",fill="white")    #hair2
        self.canvas.create_line(964,200,964,305,width=1,tag="crush",fill="white")    #hair3
        self.canvas.create_line(966,200,966,307,width=1,tag="crush",fill="white")    #hair4
       # self.canvas.create_line(971,204,965,204,width=1,tag="crush",fill="white")    #hair3
        self.canvas.create_line(943,206,965,206,width=1,tag="crush",fill="white")  
        self.canvas.create_line(945,208,965,208,width=1,tag="crush",fill="white")  
        self.canvas.create_line(951,210,965,210,width=1,tag="crush",fill="white")    #hair1
        self.canvas.create_line(953,212,965,212,width=1,tag="crush",fill="white")    #hair2
        self.canvas.create_line(956,214,965,214,width=1,tag="crush",fill="white")    #hair3
        self.canvas.create_line(925,303,925,336,width=2,tag="crush",fill="white")    #haath
        self.canvas.create_line(915,380,925,336,width=2,tag="crush",fill="white")    #haath2
        self.canvas.create_line(929,270,929,280,width=2,tag="crush",fill="white")    #centerstick2
        self.canvas.create_line(925,270,925,280,width=2,tag="crush",fill="white") 
        self.canvas.create_line(909,447,918,430,width=2,tag="crush",fill="white")    #sidha pair
        self.canvas.create_line(917,481,909,447,width=2,tag="crush",fill="white")    #sidha pair 2
        self.canvas.create_line(930,482,930,430,width=2,tag="crush",fill="white")    #ulta pair2
        self.canvas.create_line(870,430,967,430,width=2,tag="crush",fill="white")  #surface
        self.canvas.create_line(870,430,906,370,width=2,tag="crush",fill="white")  #incline
        self.canvas.create_line(906,370,906,300,width=2,tag="crush",fill="white")  #sidhi
        self.canvas.create_line(906,300,921,280,width=2,tag="crush",fill="white") # surface
        self.canvas.create_line(921,280,935,280,width=2,fill="white",tag="crush")  #neck
        self.canvas.create_line(935,280,935,370,width=2,tag="crush",fill="white")  #sidhi
        self.canvas.create_line(935,370,967,430,width=2,tag="crush",fill="white")  #incline
        self.canvas.create_text(990,175,text="*crush",tag="crush",font="times 19 bold",fill="red")
        
        
        self.canvas.create_text(420,250,text="",font="times 24 bold",tag="hey")
        # ye middle finger band krega
        self.root.after(225,self.leg16)

    def leg16(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("face")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("crush")
        self.canvas.delete("crush")
        self.canvas.create_line(509,438,517,400,fill="white",width=2,tag="leftleg")    #leftleg 1    - yhi hogi change isliye tag liya h
        self.canvas.create_line(485,480,509,438,fill="white",width=2,tag="leftleg")    #ulta pair 2
        self.canvas.create_line(550,437,517,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(560,481,550,437,fill="white",width=2,tag="rightleg")  
        self.canvas.create_line(490,334,517,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(490,334,482,373,fill="white",width=2,tag="lefthand")    #ulta hath 2  
        self.canvas.create_line(542,337,517,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(542,337,570,370,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_oval(483.5,200,553.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(513.5,220,520.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(533.5,220,540.5,227,width=2,tag="eye")    #sidhi aankh
       
        self.canvas.create_line(517,270,517,400,fill="white",width=2,tag="center")    #centerstick
        #crush
          
        self.canvas.create_oval(860,200,930,270,width=2,fill="white",tag="crush")    #face
        self.canvas.create_oval(890,220,897,227,width=2,tag="crush")    #sidhi aankh
        self.canvas.create_oval(881,227,874,220,width=2,tag="crush")    #ulti aankh
        self.canvas.create_line(930,200,930,301,width=1,fill="white",tag="crush")    #hair1
        self.canvas.create_line(932,200,932,303,width=1,fill="white",tag="crush")    #hair2
        self.canvas.create_line(934,200,934,305,width=1,fill="white",tag="crush")    #hair3
        self.canvas.create_line(936,200,936,307,width=1,fill="white",tag="crush")    #hair4
       #  self.canvas.create_line(941,204,935,204,width=1,tag="crush")    #hair3
        self.canvas.create_line(913,206,935,206,width=1,fill="white",tag="crush")  
        self.canvas.create_line(915,208,935,208,width=1,fill="white",tag="crush")  
        self.canvas.create_line(921,210,935,210,width=1,fill="white",tag="crush")    #hair1
        self.canvas.create_line(923,212,935,212,width=1,fill="white",tag="crush")    #hair2
        self.canvas.create_line(926,214,935,214,width=1,fill="white",tag="crush")    #hair3
        self.canvas.create_line(895,303,895,336,width=2,fill="white",tag="crush")    #haath
        self.canvas.create_line(885,380,895,336,width=2,fill="white",tag="crush")    #haath2
        self.canvas.create_line(899,270,899,280,width=2,fill="white",tag="crush")    #centerstick2
        self.canvas.create_line(895,270,895,280,width=2,tag="crush",fill="white") 
        self.canvas.create_line(869,442,878,430,width=2,tag="crush",fill="white")    #sidha pair
        self.canvas.create_line(900,481,869,442,width=2,tag="crush",fill="white")    #sidha pair 2
        self.canvas.create_line(890,482,890,430,width=2,tag="crush",fill="white")    #ulta pair2
        self.canvas.create_line(840,430,937,430,width=2,fill="white",tag="crush")  #surface
        self.canvas.create_line(840,430,876,370,width=2,fill="white",tag="crush")  #incline
        self.canvas.create_line(876,370,876,300,width=2,fill="white",tag="crush")  #sidhi
        self.canvas.create_line(876,300,891,280,width=2,fill="white",tag="crush") # surface
        self.canvas.create_line(891,280,905,280,width=2,fill="white",tag="crush")  #neck
        self.canvas.create_line(905,280,905,370,width=2,fill="white",tag="crush")  #sidhi
        self.canvas.create_line(905,370,937,430,width=2,fill="white",tag="crush")  #incline
        self.canvas.create_text(960,175,text="*crush",tag="crush",font="times 19 bold",fill="red")
        self.root.after(225,self.leg17)

    def leg17(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("face")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("crush")
        self.canvas.delete("crush")
        self.canvas.create_line(541,443,547,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(514,480,541,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(570,438,547,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(573,482,570,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(553,350,547,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(553,350,584,387,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(525,343,547,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(525,343,527,390,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(513.5,200,583.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(543.5,220,550.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(563.5,220,570.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(547,270,547,400,fill="white",width=2,tag="center")    #centerstick
        #crush
          
        self.canvas.create_oval(830,200,900,270,width=2,fill="white",tag="crush")    #face
        self.canvas.create_oval(860,220,867,227,width=2,tag="crush")    #sidhi aankh
        self.canvas.create_oval(851,227,844,220,width=2,tag="crush")    #ulti aankh
        self.canvas.create_line(900,200,900,301,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(902,200,902,303,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(904,200,904,305,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(906,200,906,307,fill="white",width=1,tag="crush")    #hair4
        self.canvas.create_line(881,204,905,204,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(883,206,905,206,fill="white",width=1,tag="crush")  
        self.canvas.create_line(885,208,905,208,fill="white",width=1,tag="crush")  
        self.canvas.create_line(891,210,905,210,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(893,212,905,212,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(896,214,905,214,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(865,303,865,336,fill="white",width=2,tag="crush")    #haath
        self.canvas.create_line(855,380,865,336,fill="white",width=2,tag="crush")    #haath2
        self.canvas.create_line(869,270,869,280,fill="white",width=2,tag="crush")    #centerstick2
        self.canvas.create_line(865,270,865,280,fill="white",width=2,tag="crush") 
        self.canvas.create_line(844,442,850,430,width=2,tag="crush",fill="white")    #sidha pair
        self.canvas.create_line(856,477,844,442,width=2,tag="crush",fill="white")    #sidha pair 2
        self.canvas.create_line(870,482,870,430,width=2,tag="crush",fill="white")    #ulta pair2
        self.canvas.create_line(810,430,907,430,fill="white",width=2,tag="crush")  #surface
        self.canvas.create_line(810,430,846,370,fill="white",width=2,tag="crush")  #incline
        self.canvas.create_line(846,370,846,300,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(846,300,861,280,fill="white",width=2,tag="crush") # surface
        self.canvas.create_line(871,280,875,280,fill="white",width=2,tag="crush")  #neck
        self.canvas.create_line(875,280,875,370,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(875,370,907,430,fill="white",width=2,tag="crush")  #incline
     #   self.canvas.create_line(825,482,840,482,fill="white",width=9,tag="crush")    #ulta shoe
     #   self.canvas.create_line(845,483,857,475,fill="white",width=7,tag="crush")    #sidha shoe
        self.canvas.create_text(420,250,text="",font="times 24 bold",tag="hey")
        self.canvas.create_text(930,175,text="*crush",tag="crush",font="times 19 bold",fill="red")
        self.root.after(225,self.leg18)

    def leg18(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("crush")
        self.canvas.delete("crush")
        self.canvas.create_line(579,443,577,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(549,477,579,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(591,438,577,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(592,482,591,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(578,347,577,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(578,347,593,379,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(570,343,577,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(570,343,590,388,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(543.5,200,613.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(573.5,220,580.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(593.5,220,600.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(577,270,577,400,width=2,tag="center",fill="white") #centerstick
        
        #crush
        self.canvas.create_oval(800,200,870,270,width=2,fill="white",tag="crush")    #face
        self.canvas.create_oval(830,220,837,227,width=2,tag="crush")    #sidhi aankh
        self.canvas.create_oval(821,227,814,220,width=2,tag="crush")    #ulti aankh
        self.canvas.create_line(870,200,870,301,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(872,200,872,303,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(874,200,874,305,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(876,200,876,307,fill="white",width=1,tag="crush")    #hair4
        self.canvas.create_line(851,204,875,204,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(853,206,875,206,fill="white",width=1,tag="crush")  
        self.canvas.create_line(855,208,875,208,fill="white",width=1,tag="crush")  
        self.canvas.create_line(861,210,875,210,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(863,212,875,212,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(866,214,875,214,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(835,303,835,336,fill="white",width=2,tag="crush")    #haath
        self.canvas.create_line(825,380,835,336,fill="white",width=2,tag="crush")    #haath2
        self.canvas.create_line(839,270,839,280,fill="white",width=2,tag="crush")    #centerstick2
        self.canvas.create_line(835,270,835,280,fill="white",width=2,tag="crush") 
        self.canvas.create_line(817,441,826,430,width=2,tag="crush",fill="white")    #sidha pair
        self.canvas.create_line(818,481,817,441,width=2,tag="crush",fill="white")    #sidha pair 2
        self.canvas.create_line(854,482,840,430,width=2,tag="crush",fill="white")    #ulta pair2
        self.canvas.create_line(780,430,877,430,fill="white",width=2,tag="crush")  #surface
        self.canvas.create_line(780,430,816,370,fill="white",width=2,tag="crush")  #incline
        self.canvas.create_line(816,370,816,300,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(816,300,831,280,fill="white",width=2,tag="crush") # surface
        self.canvas.create_line(831,280,845,280,fill="white",width=2,tag="crush")  #neck
        self.canvas.create_line(845,280,845,370,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(845,370,877,430,fill="white",width=2,tag="crush")  #incline
     #   self.canvas.create_line(825,482,840,482,fill="white",width=9,tag="crush")    #ulta shoe
     #   self.canvas.create_line(845,483,857,475,fill="white",width=7,tag="crush")    #sidha shoe
        self.canvas.create_text(900,175,text="*crush",tag="crush",font="times 19 bold",fill="red")
        self.root.after(225,self.leg19)
   
    def leg19(self):	       
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("crush")
        self.canvas.delete("crush")
        self.canvas.create_line(604,443,607,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(601,477,604,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(626,441,607,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(594,470,626,441,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(590,348,607,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(590,348,603,375,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(611,343,607,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(611,343,627,382,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(573.5,200,643.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(603.5,220,610.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(623.5,220,630.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(607,270,607,400,fill="white",width=2,tag="center")    #centerstick
        
        #crush
        self.canvas.create_oval(770,200,840,270,width=2,fill="white",tag="crush")    #face
        self.canvas.create_oval(800,220,807,227,width=2,tag="crush")    #sidhi aankh
        self.canvas.create_oval(791,227,784,220,width=2,tag="crush")    #ulti aankh
        self.canvas.create_line(840,200,840,301,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(842,200,842,303,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(844,200,844,305,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(846,200,846,307,fill="white",width=1,tag="crush")    #hair4
        self.canvas.create_line(821,204,845,204,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(823,206,845,206,fill="white",width=1,tag="crush")  
        self.canvas.create_line(825,208,845,208,fill="white",width=1,tag="crush")  
        self.canvas.create_line(831,210,845,210,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(833,212,845,212,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(836,214,845,214,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(805,303,805,346,fill="white",width=2,tag="crush")    #haath
        self.canvas.create_line(795,380,805,346,fill="white",width=2,tag="crush")    #haath2
        self.canvas.create_line(809,270,809,280,fill="white",width=2,tag="crush")    #centerstick2
        self.canvas.create_line(805,270,805,280,fill="white",width=2,tag="crush") 
        self.canvas.create_line(789,447,798,430,width=2,tag="crush",fill="white")    #sidha pair
        self.canvas.create_line(797,481,789,447,width=2,tag="crush",fill="white")    #sidha pair 2
        self.canvas.create_line(810,482,810,430,width=2,tag="crush",fill="white")    #ulta pair2
        self.canvas.create_line(750,430,847,430,fill="white",width=2,tag="crush")  #surface
        self.canvas.create_line(750,430,786,370,fill="white",width=2,tag="crush")  #incline
        self.canvas.create_line(786,370,786,300,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(786,300,801,280,fill="white",width=2,tag="crush") # surface
        self.canvas.create_line(801,280,815,280,fill="white",width=2,tag="crush")  #neck
        self.canvas.create_line(815,280,815,370,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(815,370,847,430,fill="white",width=2,tag="crush")  #incline
     #   self.canvas.create_line(795,482,810,482,fill="white",width=8,tag="crush")    #ulta shoe
      #  self.canvas.create_line(815,483,827,475,fill="white",width=7,tag="crush")    #sidha shoe
        # ye apna leg kholega
        self.canvas.create_text(870,175,text="*crush",tag="crush",font="times 19 bold",fill="red")
        self.root.after(500,self.leg20)
    def leg20(self):
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        self.canvas.delete("crush")
        self.canvas.delete("crush")
        self.canvas.create_line(629,443,637,400,fill="white",width=2,tag="leftleg")    #ulta pair
        self.canvas.create_line(612,477,629,443,fill="white",width=2,tag="leftleg") 
        self.canvas.create_line(661,438,637,400,fill="white",width=2,tag="rightleg")  #sidha pair
        self.canvas.create_line(654,477,661,438,fill="white",width=2,tag="rightleg") 
        self.canvas.create_line(661,345,637,295,fill="white",width=2,tag="righthand")    #sidha hath 1
        self.canvas.create_line(661,345,682,373,fill="white",width=2,tag="righthand")    #sidha hath 
        self.canvas.create_line(610,340,637,295,fill="white",width=2,tag="lefthand")    #ulta hath 1
        self.canvas.create_line(610,340,630,383,fill="white",width=2,tag="lefthand")    #ulta hath 2
        self.canvas.create_oval(603.5,200,673.5,270,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(633.5,220,640.5,227,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(653.5,220,660.5,227,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(637,270,637,400,fill="white",width=2,tag="center")    #centerstick
        #crush
        self.canvas.create_oval(740,200,810,270,width=2,fill="white",tag="crush")    #face
        self.canvas.create_oval(770,220,777,227,width=2,tag="crush")    #sidhi aankh
        self.canvas.create_oval(761,227,754,220,width=2,tag="crush")    #ulti aankh
        self.canvas.create_line(810,200,810,301,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(812,200,812,303,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(814,200,814,305,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(816,200,816,307,fill="white",width=1,tag="crush")    #hair4
        self.canvas.create_line(791,204,815,204,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(793,206,815,206,fill="white",width=1,tag="crush")  
        self.canvas.create_line(795,208,815,208,fill="white",width=1,tag="crush")  
        self.canvas.create_line(801,210,815,210,fill="white",width=1,tag="crush")    #hair1
        self.canvas.create_line(803,212,815,212,fill="white",width=1,tag="crush")    #hair2
        self.canvas.create_line(806,214,815,214,fill="white",width=1,tag="crush")    #hair3
        self.canvas.create_line(775,303,775,346,fill="white",width=2,tag="crush")    #haath
        self.canvas.create_line(765,380,775,346,fill="white",width=2,tag="crush")    #haath2
        self.canvas.create_line(779,270,779,280,fill="white",width=2,tag="crush")    #centerstick2
        self.canvas.create_line(775,270,775,280,fill="white",width=2,tag="crush") 
        self.canvas.create_line(749,442,758,430,fill="white",width=2,tag="crush")    #sidha pair
        self.canvas.create_line(780,481,749,442,fill="white",width=2,tag="crush")    #sidha pair 2
        self.canvas.create_line(770,482,770,430,fill="white",width=2,tag="crush")    #ulta pair2
        self.canvas.create_line(720,430,817,430,fill="white",width=2,tag="crush")  #surface
        self.canvas.create_line(720,430,756,370,fill="white",width=2,tag="crush")  #incline
        self.canvas.create_line(756,370,756,300,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(756,300,771,280,fill="white",width=2,tag="crush") # surface
        self.canvas.create_line(771,280,785,280,fill="white",width=2,tag="crush")  #neck
        self.canvas.create_line(785,280,785,370,fill="white",width=2,tag="crush")  #sidhi
        self.canvas.create_line(785,370,817,430,fill="white",width=2,tag="crush")  #incline
         #   self.canvas.create_line(765,482,780,482,fill="white",width=8,tag="crush")    #ulta shoe
    #    self.canvas.create_line(785,483,797,475,fill="white",width=7,tag="crush")    #sidha shoe

        self.canvas.create_rectangle(510,100,700,150,outline="white",width=1,tag="Fmsg") #rectangle
        self.canvas.create_text(587,130,text="All good?",font="constantia 25 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,150,fill="white",width=1,tag="Mmsg")  # line
        self.canvas.create_text(840,175,text="*crush",tag="crush",font="times 19 bold",fill="red")

        # ye apna leg kholega
        self.root.after(1500,self.leg21)
    
    
    def leg21(self):
	       
        self.canvas.delete("Mmsg")
        self.canvas.delete("Fmsg")
        self.canvas.create_rectangle(750,100,1000,150,width=1,tag="Mmsg",outline="white")
        self.canvas.create_text(875,130,text="Yes, all well. You Say?",font="constantia 17 bold ",fill="#46a2b0",tag="Fmsg")
        self.canvas.create_line(770,190,840,150,fill="white",width=1,tag="Mmsg")
 
        self.root.after(1600,self.leg22)  
    def leg22(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(435,100,735,160,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(585,130,text="  yeahh, Im always good.",font="constantia 17 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,160,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1800,self.leg22p)  
    def leg22p(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(435,100,735,160,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(585,130,text="            hey,\n I want to tell u something.",font="constantia 17 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,160,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1900,self.leg23)  
    def leg23(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(794,100,940,140,width=1,tag="Mmsg",outline="white")
        self.canvas.create_text(875,120,text="Hmm,say",font="constantia 18 bold ",fill="#46a2b0",tag="Fmsg")
        self.canvas.create_line(770,190,840,140,fill="white",width=1,tag="Mmsg")
        self.root.after(1500,self.leg24) 

    def leg24(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(490,110,690,150,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(583,130,text="I like a Girl..",font="constantia 22 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,150,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1700,self.leg25)  

    def leg25(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(760,100,1000,150,width=1,tag="Mmsg",outline="white")
        self.canvas.create_text(875,130,text="ohh, really nice",font="constantia 18 bold ",fill="#46a2b0",tag="Fmsg")
        self.canvas.create_line(770,190,840,150,fill="white",width=1,tag="Mmsg")
        self.root.after(1700,self.leg26) 
    def leg26(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(417,100,750,160,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(583,130,text="                    Yes!\n But, I don't know how to tell her?",font="constantia 16 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,160,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1900,self.leg27)  
    def leg27(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(760,110,1000,150,width=1,tag="Mmsg",outline="white")
        self.canvas.create_text(875,130,text="just tell her...",font="constantia 18 bold ",fill="#46a2b0",tag="Fmsg")
        self.canvas.create_line(770,190,840,150,fill="white",width=1,tag="Mmsg")
        self.root.after(1700,self.leg28) 
    def leg28(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(438,100,750,170,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(587,130,text="                U r right..\n Ok, let me practice on u first..",font="constantia 16 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,170,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1800,self.leg29) 

#yaha ldka baithega
    def leg29(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.delete("leftleg")
        self.canvas.delete("rightleg")
        self.canvas.delete("righthand")
        self.canvas.delete("lefthand")
        self.canvas.delete("eye")
        self.canvas.delete("center")
        self.canvas.delete("face")
        
        self.canvas.create_line(639,473,647,430,width=2,tag="leftleg",fill="white")    #ulta pair
        self.canvas.create_line(599,474,639,473,width=2,tag="leftleg",fill="white") 
        self.canvas.create_line(684,431,647,430,width=2,tag="rightleg",fill="white")  #sidha pair
        self.canvas.create_line(679,480,684,431,width=2,tag="rightleg",fill="white") 
        self.canvas.create_line(681,370,647,340,width=2,tag="righthand",fill="white")    #sidha hath 1
        self.canvas.create_line(681,370,722,358,width=2,tag="righthand",fill="white")    #sidha hath 
        self.canvas.create_line(620,380,647,340,width=2,tag="lefthand",fill="white")    #ulta hath 1
        self.canvas.create_line(620,380,640,423,width=2,tag="lefthand",fill="white")    #ulta hath 2
        self.canvas.create_oval(613.5,240,683.5,310,width=2,fill="white",tag="face")    #face
        self.canvas.create_oval(643.5,260,650.5,267,width=2,tag="eye")    #ulti aankh
        self.canvas.create_oval(663.5,260,670.5,267,width=2,tag="eye")    #sidhi aankh
        self.canvas.create_line(647,310,647,430,width=2,tag="center",fill="white")    #centerstick
        self.canvas.create_line(722,340,722,367,width=4,fill="green",tag="rose")    #rose stick
        self.canvas.create_line(722,340,716,337,width=1,fill="red",tag="rose")#1
        self.canvas.create_line(722,340,716,340,width=1,fill="green",tag="rose")#2
        self.canvas.create_line(722,340,716,343,width=1,fill="green",tag="rose")#3
        self.canvas.create_line(722,340,727,337,width=1,fill="red",tag="rose")
        self.canvas.create_line(722,340,727,340,width=1,fill="green",tag="rose")
        self.canvas.create_line(722,340,727,343,width=1,fill="green",tag="rose")
        self.canvas.create_line(716,330,716,337,width=1,fill="red",tag="rose")##1 red
        self.canvas.create_line(717,331,717,337,width=1,fill="red",tag="rose")##2 red
        self.canvas.create_line(718,332,718,338,width=1,fill="red",tag="rose")##3 red
        self.canvas.create_line(719,331,719,339,width=1,fill="red",tag="rose")##4  red
        self.canvas.create_line(720,330,720,339,width=1,fill="red",tag="rose")##5 red
        self.canvas.create_line(721,328,721,339,width=1,fill="red",tag="rose")##6 red
        self.canvas.create_line(722,328,722,339,width=1,fill="red",tag="rose")##7 red
        self.canvas.create_line(723,330,723,339,width=1,fill="red",tag="rose")##8red
        self.canvas.create_line(724,331,724,339,width=1,fill="red",tag="rose")##9 red
        self.canvas.create_line(725,332,725,339,width=1,fill="red",tag="rose")##10 red
        self.canvas.create_line(726,331,726,339,width=1,fill="red",tag="rose")##11 red
        self.canvas.create_line(727,330,727,337,width=1,fill="red",tag="rose")
        
        self.canvas.create_rectangle(480,105,700,150,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(586,130,text="I really like u...",font="constantia 18 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,150,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1700,self.leg30) 
    def leg30(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(740,100,1000,150,width=1,tag="Mmsg",outline="white")
        self.canvas.create_text(875,130,text="I like u too.., Now tell her.",font="constantia 15 bold ",fill="#46a2b0",tag="Fmsg")
        self.canvas.create_line(770,190,840,150,fill="white",width=1,tag="Mmsg")
        self.root.after(1900,self.leg31) 
    def leg31(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(480,105,700,150,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(583,130,text="I already did...",font="constantia 18 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,190,590,150,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1500,self.leg32) 
    def leg32(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(760,100,1000,150,width=1,tag="Mmsg",outline="white")
        self.canvas.create_text(875,130,text="what",font="constantia 18 bold ",fill="#46a2b0",tag="Fmsg")
        self.canvas.create_line(770,190,840,150,fill="white",width=1,tag="Mmsg")
        self.root.after(1500,self.leg33) 
    def leg33(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(440,105,750,150,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(583,130,text=" Yes, That's you...",font="constantia 18 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,270,590,150,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(1500,self.leg34) 
#yaha msgbox aayega   
    def leg34(self):
        self.canvas.delete("Fmsg")
        self.canvas.delete("Mmsg")
        self.canvas.create_rectangle(440,105,750,150,width=1,tag="Fmsg",outline="white") #rectangle
        self.canvas.create_text(583,130,text=" Do u accept my proposal?",font="constantia 18 bold ",fill="#de2828",tag="Mmsg") #hlo
        self.canvas.create_line(638,270,590,150,fill="white",width=1,tag="Mmsg")  # line
        self.root.after(2000,self.message) 
#yaha msgbox aayega
    def message(self):
        
      
    	value=tkinter.messagebox.askquestion("confirm","Do you want to accept my proposal ?")
    	if value=="yes":
            self.canvas.delete("rose")
            self.canvas.delete("Fmsg")
            self.canvas.delete("Mmsg")
            self.canvas.delete("leftleg")
            self.canvas.delete("rightleg")
            self.canvas.delete("righthand")
            self.canvas.delete("lefthand")
            self.canvas.delete("eye")
            self.canvas.delete("crush")
            self.canvas.delete("center")
            self.canvas.delete("face")
            self.canvas.delete("crush")
            
            self.canvas.create_text(500,300,text="she: Yess I do\n He: Aww thankU ",font="times 44 bold",fill="red")
            self.canvas.create_text(500,100,text=" Hurray!! ",font="times 44 bold",fill="red")
            tkinter.messagebox.showinfo("congratulations...","Congratulations. buddy...")
    	else:
            self.canvas.delete("Fmsg")
            self.canvas.delete("Mmsg")
            self.canvas.delete("leftleg")
            self.canvas.delete("rightleg")
            self.canvas.delete("righthand")
            self.canvas.delete("lefthand")
            self.canvas.delete("eye")
            self.canvas.delete("crush")
            self.canvas.delete("center")
            self.canvas.delete("face")
            self.canvas.delete("crush")
            self.canvas.delete("rose")
            self.canvas.create_text(500,300,text="she: Sorry  \nHe: It's Ok\n      Always be happy",font="times 44 bold",fill="#46a2b0")
            

# yha se hoga program start
if __name__ == "__main__":
    Main()
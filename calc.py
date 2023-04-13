import speech_recognition as sr
import pygame as gui
import sys
import time
import pyttsx3
import math

w,h = 1600,900
white = (255,255,255)
skyblue = (0,255,255)

class KARAN_COMPUTES:
    def __init__(self):
        gui.init()
        gui.font.init()
        self.engine = pyttsx3.init()
#        voice = self.engine.getProperty('voices') #get the available voices
#        self.engine.setProperty('voice', voice[1].id) 
        gui_icon = gui.image.load('logo.png')
        gui.display.set_icon(gui_icon)
        self.str =''
        self.status = 'OFF'
        self.font0 = gui.font.Font("quake.TTF", 26)
        self.font = gui.font.Font("quake.TTF", 35)
        self.font2 = gui.font.Font("quake.TTF", 60)
        self.width = 1920
        self.height = 1080
        self.disp = gui.display.set_mode((self.width,self.height),0,0)
        self.img_back = gui.transform.scale(gui.image.load("bg.jpg"),(w-200,h-100))
        self.bglogo = gui.transform.scale(gui.image.load('bglogo.png'),(800,800))
        self.logo = gui.transform.scale(gui.image.load('logo.png'),(500,500))
        self.blitARI('')

    def blitARI(self,str):
        while True:
            a = 0
            self.disp.blit(self.img_back,(260,120))
            h1 = self.font.render("SPEECH RECOGNITION", True, white)
            h2 = self.font2.render("BASED CALCULATOR", True, skyblue)
            h3 = self.font0.render("BY KARAN", True, white)
            h1Rect = h1.get_rect()
            h1Rect.center = (950, 200)
            h2Rect = h2.get_rect()
            h2Rect.center = (950, 260)
            h3Rect = h3.get_rect()
            h3Rect.center = (950,880)
            self.disp.blit(h1,h1Rect)
            self.disp.blit(h2,h2Rect)
            self.disp.blit(h3,h3Rect)
            if(self.status=='ON'):
                self.disp.blit(self.bglogo,(550,150))
                self.str = self.recordAudioARI()
                self.status = 'OFF'
                a = 1
            text1 = self.font2.render(self.str, True, skyblue)
            text1Rect = text1.get_rect()
            text1Rect.center = (960, 810)
            self.disp.blit(self.bglogo,(550,150))
            self.disp.blit(self.logo,(700,290))
            self.disp.blit(text1,text1Rect)
            gui.display.update()
            if(a==1):
                time.sleep(2)
            for Eveu in gui.event.get():
                if Eveu.type == gui.KEYDOWN:
                    if Eveu.key == gui.K_RETURN:
                        if(self.status=='OFF'):
                            self.status = 'ON'
                        else:
                            self.status = 'OFF'
                        pass
                    if Eveu.key == gui.K_ESCAPE:
                        gui.display.quit()
                        sys.exit()
                        
    def recordAudioARI(self):
        degree = ""
        r = sr.Recognizer()
        r.dynamic_energy_threshold = False
        r.energy_threshold = 480
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source=source)
            print('Listening')
            try:
                audio = r.listen(source,timeout=2,phrase_time_limit=4)
            except:
                return 'Time Out'
            data = ''
            try :
                data = r.recognize_google(audio)
                print(data)
                if('power' in data):
                    data = data.strip().replace("power",'**')
                
                elif("minus" in data):
                    data = data.strip().replace("minus","-")
                
                elif("multiply" in data):
                    data = data.strip().replace("multiply","*")
                
                elif("x" in data):
                    data = data.strip().replace("x","*")
                
                elif("divide" in data):
                    data = data.strip().replace("divide","/")
                
                elif("/" in data):
                    data = data.strip()
                
                elif "sin" in data:
                    degree = int(data.split()[1])
                    data = "math.sin("+str(int(data.split()[1]))+")"                

                elif "tan" in data:
                    degree = int(data.split()[1])
                    data = "math.tan("+str(int(data.split()[1]))+")"
                
                elif "kosi" in data:        #kosikand 30
                    degree = int(data.split()[1])
                    data = "1/math.sin("+str(degree)+")"

                elif "second" in data or "sick" in data:        #second 30
                    degree = int(data.split()[1])
                    data = "1/math.cos("+str(degree)+")"

                elif "cot" in data or "got" in data:        #got 30
                    degree = int(data.split()[1])
                    data = "1/math.tan("+str(degree)+")"

                elif "cos" in data:
                    degree = int(data.split()[1])
                    data = "math.cos("+str(int(data.split()[1]))+")"

                elif "log" in data:
                    try:
                        degree = int(data.split()[1])
                        data = "math.log("+str(int(data.split()[1]))+")"
                    except:
                        return
                try:
                    eval(data)
                except:
                    return "Try Again Please"

                if "1/math.tan" in data:
                    data_to_be_eval = str(1/math.tan(math.pi/(180/degree)))
                    data = "cot("+str(degree)+")"
                    self.speak(data+' = %.1f'%eval(data_to_be_eval))
                    return data+' = %.1f'%eval(data_to_be_eval)

                if "1/math.cos" in data:
                    data_to_be_eval = str(1/math.cos(math.pi/(180/degree)))
                    data = "sec("+str(degree)+")"
                    self.speak(data+' = %.1f'%eval(data_to_be_eval))
                    return data+' = %.1f'%eval(data_to_be_eval)

                elif "1/math.sin" in data:
                    data_to_be_eval = str(1/math.sin(math.pi/(180/degree)))
                    data = "cosec("+str(degree)+")"
                    self.speak(data+' = %.1f'%eval(data_to_be_eval))
                    return data+' = %.1f'%eval(data_to_be_eval)

                elif "math.sin" in data:
                    data_to_be_eval = str(math.sin(math.pi/(180/degree)))
                    data = "sin("+str(degree)+")"
                    self.speak(data+' = %.1f'%eval(data_to_be_eval))
                    return data+' = %.1f'%eval(data_to_be_eval)
                
                elif "math.cos" in data:
                    data_to_be_eval = str(math.cos(math.pi/(180/degree)))
                    data = "cos("+str(degree)+")"
                    self.speak(data+' = %.1f'%eval(data_to_be_eval))
                    return data+' = %.1f'%eval(data_to_be_eval)

                elif "math.tan" in data:
                    data_to_be_eval = str(math.tan(math.pi/(180/degree)))
                    data = "tan("+str(degree)+")"
                    self.speak(data+' = %.1f'%eval(data_to_be_eval))
                    return data+' = %.1f'%eval(data_to_be_eval)

                elif "math.log" in data:
                    data_to_be_eval = str(math.log(degree))
                    data = "log("+str(degree)+")"
                    self.speak(data+' = %.4f'%eval(data_to_be_eval))
                    return data+' = %.4f'%eval(data_to_be_eval)


                else:
                    self.speak(data+' = '+str(eval(data)))
                return data+' = '+str(eval(data))
            except sr.UnknownValueError:
                return "Error"
            except sr.RequestError as e:
                return "Request Error"

    def speak(self,txt):
        self.engine.say(txt)
        self.engine.runAndWait()

t = KARAN_COMPUTES()

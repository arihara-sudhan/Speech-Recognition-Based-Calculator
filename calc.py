import speech_recognition as sr
from playsound import playsound
import pygame
import sys
import time

w,h = 1600,900
white = (255,255,255)
skyblue = (0,255,255)

class ARI_COMPUTES:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.str =''
        self.status = 'OFF'
        self.font0 = pygame.font.Font("quake.ttf", 26)
        self.font = pygame.font.Font("quake.ttf", 35)
        self.font2 = pygame.font.Font("quake.ttf", 60)
        self.width = 1920
        self.height = 1080
        self.disp = pygame.display.set_mode((self.width,self.height),0,0)
        self.img_back = pygame.transform.scale(pygame.image.load("bg.jpg"),(w-200,h-100))
        self.bglogo = pygame.transform.scale(pygame.image.load('bglogo.png'),(800,800))
        self.logo = pygame.transform.scale(pygame.image.load('logo.png'),(500,500))
        self.blitARI('')

    def blitARI(self,str):
        while True:
            a = 0
            self.disp.blit(self.img_back,(260,120))
            h1 = self.font.render("SPEECH RECOGNITION", True, white)
            h2 = self.font2.render("BASED CALCULATOR", True, skyblue)
            h3 = self.font0.render("BY ARIHARASUDHAN", True, white)
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
            pygame.display.update()
            if(a==1):
                time.sleep(4)
            for Eveu in pygame.event.get():
                if Eveu.type == pygame.KEYDOWN:
                    if Eveu.key == pygame.K_RETURN:
                        if(self.status=='OFF'):
                            self.status = 'ON'
                        else:
                            self.status = 'OFF'
                        pass
                    if Eveu.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                        sys.exit()


    def recordAudioARI(self):
        r = sr.Recognizer()
        r.dynamic_energy_threshold = False
        r.energy_threshold = 480
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source=source)
            print('Listening')
            try:
                audio = r.listen(source,timeout=2)
            except:
                return 'Time Out'
            data = ''
            try :
                data = r.recognize_google(audio)
                if('power' in data):
                    data = data.strip().replace("power",'**')
                if("minus" in data):
                    data = data.strip().replace("minus","-")
                if("multiply" in data):
                    data = data.strip().replace("multiply","*")
                if("x" in data):
                    data = data.strip().replace("x","*")
                if("divide" in data):
                    data = data.strip().replace("divide","/")
                if("/" in data):
                    data = data.strip()
                print(data)
                try:
                    eval(data)
                except:
                    return "Try Again Please"
                return data+' = '+str(eval(data))
            except sr.UnknownValueError:
                return "Error"
            except sr.RequestError as e:
                return "Request Error"
t = ARI_COMPUTES()




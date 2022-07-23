import cv2 as eye
from cvzone.HandTrackingModule import HandDetector as hdari
import time

class ARI_PATTERNS:
	def __init__(self):
		self.goon = False
		self.matched  = False
		self.reg = True
		self.Appendable1 = True
		self.Appendable2 = True
		self.Appendable3 = True
		self.Appendable4 = True
		self.Appendable5 = True
		self.Appendable6 = True
		self.Appendable7 = True
		self.Appendable8 = True
		self.Appendable9 = True
		self.appendable1 = True
		self.appendable2 = True
		self.appendable3 = True
		self.appendable4 = True
		self.appendable5 = True
		self.appendable6 = True
		self.appendable7 = True
		self.appendable8 = True
		self.appendable9 = True
		self.poss = []
		self.recog = []
		self.succmsg = False
		self.point = None
		self.det = hdari(detectionCon=0.8,maxHands=1)
		self.pos = [[(250,200),(500,200),(750,200)],
					[(250,400),(500,400),(750,400)],
					[(250,600),(500,600),(750,600)]]
		self.color = (255,0,0)
		self.innercolor = (255,255,255)
		(self.w,self.h) = (1000,800)
		self.CAM = eye.VideoCapture(0)
		self.cam()
	def cam(self):
		self.color1 = self.innercolor
		self.text1 = 'SO YOUR PATTERN IS'
		self.pos1 = (235,100)
		while True:
			status,self.frame = self.CAM.read()
			self.frame = eye.resize(self.frame,(self.w,self.h))
			self.frame = eye.flip(self.frame,1)
			hands,self.frame = self.det.findHands(self.frame,flipType=False)
			for x in range(len(self.pos)):
				for y in range(len(self.pos[x])):
					eye.circle(self.frame,self.pos[x][y],29,self.color,-1)
					eye.circle(self.frame,self.pos[x][y],16,self.innercolor,-1)

			if hands:
				if(not self.reg and not self.goon):
					eye.putText(self.frame,"CLICK ENTER",(350, 100),eye.FONT_HERSHEY_DUPLEX,1.5,self.innercolor,2)
					for x in range(len(self.poss)-1):
						eye.line(self.frame,self.poss[x],self.poss[x+1],self.innercolor,3)
					eye.imshow('ARI',self.frame)
					eye.waitKey(0)
					self.goon = True
					self.point = None
				else:
					self.point = hands[0]['lmList'][8][0:2]					

			if(self.reg):
				eye.putText(self.frame,"DRAW YOUR PATTERN MR.ARI",(160, 100),eye.FONT_HERSHEY_DUPLEX,1.5,self.innercolor,2)
				if(self.point!=None and self.point[0] in range(self.pos[0][0][0]-10,self.pos[0][0][0]+10)
					and self.point[1] in range(self.pos[0][0][1]-10,self.pos[0][0][1]+10)):
					if self.point not in self.poss and self.appendable1:
						self.poss.append(self.pos[0][0])
						self.appendable1 = False

				if(self.point!=None and self.point[0] in range(self.pos[0][1][0]-10,self.pos[0][1][0]+10)
					and self.point[1] in range(self.pos[0][1][1]-10,self.pos[0][1][1]+10)):
					if self.point not in self.poss and self.appendable2:
						self.poss.append(self.pos[0][1])
						self.appendable2 = False

				if(self.point!=None and self.point[0] in range(self.pos[0][2][0]-10,self.pos[0][2][0]+10)
					and self.point[1] in range(self.pos[0][2][1]-10,self.pos[0][2][1]+10)):
					if self.point not in self.poss and self.appendable3:
						self.poss.append(self.pos[0][2])
						self.appendable3 = False

				if(self.point!=None and self.point[0] in range(self.pos[1][0][0]-10,self.pos[1][0][0]+10)
					and self.point[1] in range(self.pos[1][0][1]-10,self.pos[1][0][1]+10)):
					if self.point not in self.poss and self.appendable4:
						self.poss.append(self.pos[1][0])
						self.appendable4 = False

				if(self.point!=None and self.point[0] in range(self.pos[1][1][0]-10,self.pos[1][1][0]+10)
					and self.point[1] in range(self.pos[1][1][1]-10,self.pos[1][1][1]+10)):
					if self.point not in self.poss and self.appendable5:
						self.poss.append(self.pos[1][1])
						self.appendable5 = False

				if(self.point!=None and self.point[0] in range(self.pos[1][2][0]-10,self.pos[1][2][0]+10)
					and self.point[1] in range(self.pos[1][2][1]-10,self.pos[1][2][1]+10)):
					if self.point not in self.poss and self.appendable6:
						self.poss.append(self.pos[1][2])
						self.appendable6 = False

				if(self.point!=None and self.point[0] in range(self.pos[2][0][0]-10,self.pos[2][0][0]+10)
					and self.point[1] in range(self.pos[2][0][1]-10,self.pos[2][0][1]+10)):
					if self.point not in self.poss and self.appendable7:
						self.poss.append(self.pos[2][0])
						self.appendable7 = False

				if(self.point!=None and self.point[0] in range(self.pos[2][1][0]-10,self.pos[2][1][0]+10)
					and self.point[1] in range(self.pos[2][1][1]-10,self.pos[2][1][1]+10)):
					if self.point not in self.poss and self.appendable8:
						self.poss.append(self.pos[2][1])
						self.appendable8 = False

				if(self.point!=None and self.point[0] in range(self.pos[2][2][0]-10,self.pos[2][2][0]+10)
					and self.point[1] in range(self.pos[2][2][1]-10,self.pos[2][2][1]+10)):
					if self.point not in self.poss and self.appendable9:
						self.poss.append(self.pos[2][2])
						self.appendable9 = False

				if(len(self.poss)>1):
					for x in range(len(self.poss)-1):
						eye.line(self.frame,self.poss[x],self.poss[x+1],self.innercolor,5)
					if len(self.poss)==9:
						self.succmsg = True
						self.reg = False
			elif(self.goon):
				eye.putText(self.frame,self.text1,self.pos1,eye.FONT_HERSHEY_DUPLEX,1.5,self.color1,2)
				if(self.point!=None and self.point[0] in range(self.pos[0][0][0]-10,self.pos[0][0][0]+10)
					and self.point[1] in range(self.pos[0][0][1]-10,self.pos[0][0][1]+10)):
					if self.point not in self.recog and self.Appendable1:
						self.recog.append(self.pos[0][0])
						self.Appendable1 = False

				if(self.point!=None and self.point[0] in range(self.pos[0][1][0]-10,self.pos[0][1][0]+10)
					and self.point[1] in range(self.pos[0][1][1]-10,self.pos[0][1][1]+10)):
					if self.point not in self.recog and self.Appendable2:
						self.recog.append(self.pos[0][1])
						self.Appendable2 = False

				if(self.point!=None and self.point[0] in range(self.pos[0][2][0]-10,self.pos[0][2][0]+10)
					and self.point[1] in range(self.pos[0][2][1]-10,self.pos[0][2][1]+10)):
					if self.point not in self.recog and self.Appendable3:
						self.recog.append(self.pos[0][2])
						self.Appendable3 = False

				if(self.point!=None and self.point[0] in range(self.pos[1][0][0]-10,self.pos[1][0][0]+10)
					and self.point[1] in range(self.pos[1][0][1]-10,self.pos[1][0][1]+10)):
					if self.point not in self.recog and self.Appendable4:
						self.recog.append(self.pos[1][0])
						self.Appendable4 = False

				if(self.point!=None and self.point[0] in range(self.pos[1][1][0]-10,self.pos[1][1][0]+10)
					and self.point[1] in range(self.pos[1][1][1]-10,self.pos[1][1][1]+10)):
					if self.point not in self.recog and self.Appendable5:
						self.recog.append(self.pos[1][1])
						self.Appendable5 = False

				if(self.point!=None and self.point[0] in range(self.pos[1][2][0]-10,self.pos[1][2][0]+10)
					and self.point[1] in range(self.pos[1][2][1]-10,self.pos[1][2][1]+10)):
					if self.point not in self.recog and self.Appendable6:
						self.recog.append(self.pos[1][2])
						self.Appendable6 = False

				if(self.point!=None and self.point[0] in range(self.pos[2][0][0]-10,self.pos[2][0][0]+10)
					and self.point[1] in range(self.pos[2][0][1]-10,self.pos[2][0][1]+10)):
					if self.point not in self.recog and self.Appendable7:
						self.recog.append(self.pos[2][0])
						self.Appendable7 = False

				if(self.point!=None and self.point[0] in range(self.pos[2][1][0]-10,self.pos[2][1][0]+10)
					and self.point[1] in range(self.pos[2][1][1]-10,self.pos[2][1][1]+10)):
					if self.point not in self.recog and self.Appendable8:
						self.recog.append(self.pos[2][1])
						self.Appendable8 = False

				if(self.point!=None and self.point[0] in range(self.pos[2][2][0]-10,self.pos[2][2][0]+10)
					and self.point[1] in range(self.pos[2][2][1]-10,self.pos[2][2][1]+10)):
					if self.point not in self.recog and self.Appendable9:
						self.recog.append(self.pos[2][2])
						self.Appendable9 = False

				if(len(self.recog)>1):
					for x in range(len(self.recog)-1):
						eye.line(self.frame,self.recog[x],self.recog[x+1],self.color1,5)
					if(len(self.recog)==9):
						if(self.recog==self.poss):
							print(self.poss)
							self.text1 = "SUCCESFULLY MATCHED"
							self.CAM.release()
							eye.destroyAllWindows()
							import calc
							self.pos1 = (240, 100)
						else:
							self.text1 = "NOT MATCHED"
							self.pos1 = (350, 100)
							self.color1 = (0,0,255)
							self.recog = []
							self.point = None
							self.Appendable1 = True
							self.Appendable2 = True
							self.Appendable3 = True
							self.Appendable4 = True
							self.Appendable5 = True
							self.Appendable6 = True
							self.Appendable7 = True
							self.Appendable8 = True
							self.Appendable9 = True
			eye.imshow('ARI',self.frame)
			if eye.waitKey(1) & 0xFF ==ord('q'):
				break
		self.end()
	def end(self):
		self.CAM.release()
		eye.destroyAllWindows()

ARI_PATTERNS()
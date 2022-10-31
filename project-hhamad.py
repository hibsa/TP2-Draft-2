import math
import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((890,735))
screen.fill('Pink')
pygame.display.set_caption('Bloon Battles')
clock = pygame.time.Clock()

test_surface = pygame.image.load('graphics/map-11.png').convert_alpha()
game_bar = pygame.image.load('graphics/game-bar2.png').convert_alpha()

b = pygame.image.load('graphics/balloon.png').convert_alpha()
pop = pygame.image.load('popped-balloon.png').convert_alpha()

default_bird = pygame.image.load('graphics/default-bird.png').convert_alpha()
default_bird = pygame.transform.scale(default_bird,(250,250))
default_bird_rect = default_bird.get_rect(center=(500,100))

angry_bird = pygame.image.load('graphics/angry-bird.png').convert_alpha()
feather_dart = pygame.image.load('graphics/feather.png').convert_alpha()

font = pygame.font.Font(None,30)
healthBar = 50
roundStatus = None

# Displays a balloon
# When put in while loop, balloon moves to the end of the map
class Balloons:
    def __init__(self,b,x):

        #initiallizing variables
        self.x = x
        self.y = 85
        self.balloon = b

    ## ROUND 1
    #displays inputted balloon on screen + makes into rectangle
    #moves balloon at a slow speed when in main loop
    def round1(self):

        self.rect = self.balloon.get_rect(topleft=(self.x,self.y))
        screen.blit(self.balloon,self.rect)

        if self.x<495:
            self.x += 1
            
        if self.x>=494 and self.y<265:
            self.y += 1
        
        if self.y>=264 and self.x<640:
            self.x += 1
            
        if self.x>=639 and self.y<800:
            self.y += 1

    ## ROUND 2
    #displays inputted balloon on screen + makes into rectangle
    #moves balloon at a medium speed when in main loop
    def round2(self):

        self.rect = self.balloon.get_rect(topleft=(self.x,self.y))
        screen.blit(self.balloon,self.rect)
        
        if self.x<495:
            self.x += 1.5
            
        if self.x>=494 and self.y<265:
            self.y += 1.5
        
        if self.y>=264 and self.x<640:
            self.x += 1.5
            
        if self.x>=639 and self.y<800:
            self.y += 1.5

    def checkPassing(self):

        if self.rect.top>735:
            return True
        
        return False

    def isColliding(self,item):
##        self.rect = self.balloon.get_rect(topleft=(self.x,self.y))

        if self.rect.colliderect(item):
            return True

        return False

    def balloonPos(self):

        return (self.rect.centerx,self.rect.centery)

    ## ROUND 1 Balloons
    ## Contains 15 balloons 
    def round1Balloons(self):
        
        self.dB1 = Balloons(b,100)
        self.dB2 = Balloons(b,60)
        self.dB3 = Balloons(b,20)
        self.dB4 = Balloons(b,-20)
        self.dB5 = Balloons(b,-60)
        self.dB6 = Balloons(b,-100)
        self.dB7 = Balloons(b,-140)
        self.dB8 = Balloons(b,-180)
        self.dB9 = Balloons(b,-220)
        self.dB10 = Balloons(b,-260)
        self.dB11 = Balloons(b,-300)
        self.dB12 = Balloons(b,-340)
        self.dB13 = Balloons(b,-380)
        self.dB14 = Balloons(b,-420)
        self.dB15 = Balloons(b,-460)
            
        return [
        self.dB1,self.dB2,self.dB3,self.dB4,
        self.dB5,self.dB6,self.dB7,self.dB8,
        self.dB9,self.dB10,self.dB11,self.dB12,
        self.dB13,self.dB14,self.dB15]

    def round2Balloons(self):

        self.dB1 = Balloons(b,100)
        self.dB2 = Balloons(b,60)
        self.dB3 = Balloons(b,20)
        self.dB4 = Balloons(b,-20)
        self.dB5 = Balloons(b,-60)
        self.dB6 = Balloons(b,-100)
        self.dB7 = Balloons(b,-140)
        self.dB8 = Balloons(b,-180)
        self.dB9 = Balloons(b,-220)
        self.dB10 = Balloons(b,-260)
        self.dB11 = Balloons(b,-300)
        self.dB12 = Balloons(b,-340)
        self.dB13 = Balloons(b,-380)
        self.dB14 = Balloons(b,-420)
        self.dB15 = Balloons(b,-460)
        self.dB16 = Balloons(b,-500)
        self.dB17 = Balloons(b,-540)
        self.dB18 = Balloons(b,-580)
        self.dB19 = Balloons(b,-620)
        self.dB20 = Balloons(b,-660)
        self.dB21 = Balloons(b,-700)
        self.dB22 = Balloons(b,-740)
        self.dB23 = Balloons(b,-780)
        self.dB24 = Balloons(b,-820)
        self.dB25 = Balloons(b,-860)
            
        return [
        self.dB1,self.dB2,self.dB3,self.dB4,
        self.dB5,self.dB6,self.dB7,self.dB8,
        self.dB9,self.dB10,self.dB11,self.dB12,
        self.dB13,self.dB14,self.dB15,self.dB16,
        self.dB17,self.dB18,self.dB19,self.dB20,
        self.dB21,self.dB22,self.dB23]

class AllSpikes:
    def __init__(self):

        self.count = 0
        self.spikesDamage = 0
        currentX = 0
        currentY = 0
        self.moving = False
        
        self.spikesImg1 = pygame.image.load('graphics/spikes1.png').convert_alpha()
        self.spikesImg1 = pygame.transform.scale(self.spikesImg1,(150,150))
        
        self.spikesImg2 = pygame.image.load('graphics/spikes2.png').convert_alpha()
        self.spikesImg2 = pygame.transform.scale(self.spikesImg2,(150,150))
        
        self.spikesImg3 = pygame.image.load('graphics/spikes3.png').convert_alpha()
        self.spikesImg3 = pygame.transform.scale(self.spikesImg3,(150,150))

        self.moving = False
        self.placed = False
        self.spikesCord = (80,495)

        self.assignSpikes()
        self.displaySpikes()

    def displaySpikes(self):
        

        #updates image of spikes displayed on screen
        #spikes appear to be less for every two balloons popped
        if self.spikesDamage==0 or self.spikesDamage==1:
            self.item = self.spikesImg1
            self.itemR = self.item.get_rect(center=self.spikesCord)#(self.itemR.left,self.itemR.top))
        if self.spikesDamage==2 or self.spikesDamage==3:
            self.item = self.spikesImg2
            self.itemR = self.item.get_rect(center=self.spikesCord)#(self.itemR.left,self.itemR.top))
        if self.spikesDamage>=4:
            self.item = self.spikesImg3
            self.itemR = self.item.get_rect(center=self.spikesCord)#(self.itemR.left,self.itemR.top))

        #displays spikes on screen if they are still active
        #spikes are active if they've popped less than 6 balloons
        if self.spikesDamage!=6:
            screen.blit(self.item,self.itemR)

        #when current spikes are no longer active,
        #next spikes are displayed on screen
        #if player used all spikes (total 3), spikes disappear
        if self.spikesDamage==6 and self.count!=2:
            self.placed = False
            self.spikesCord = (80,495)
            self.spikesDamage=0
            self.count+=1
            
    def popBalloon(self,balloon):
        global displayBalloon1
        
        if balloon.isColliding(self.itemR):
            
            if balloon in displayBalloon1 and self.spikesDamage<6 and self.moving==False:
                displayBalloon1.remove(balloon)
                self.spikesDamage += 1
                screen.blit(pop,balloon)
                    
    def assignSpikes(self):

        self.spikes_select1 = self.spikesImg1
        self.spikes_select_rect1 = self.spikes_select1.get_rect(center=self.spikesCord)

        self.spikes_select2 = self.spikesImg1
        self.spikes_select_rect2 = self.spikes_select2.get_rect(center=self.spikesCord)

        self.spikes_select3 = self.spikesImg1
        self.spikes_select_rect3 = self.spikes_select3.get_rect(center=self.spikesCord)
        
        #updates current spikes displayed on screen
        if self.count==0:
            self.item,self.itemR = (self.spikes_select1,self.spikes_select_rect1)
            
        if self.count==1:
            self.item,self.itemR = (self.spikes_select2,self.spikes_select_rect2)
            
        if self.count==2:
            self.item,self.itemR = (self.spikes_select3,self.spikes_select_rect3)

    # source: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor 
    def moveSpikes(self,event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.itemR.collidepoint(event.pos):
                self.moving = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.moving = False
            self.placed = True

        elif event.type == pygame.MOUSEMOTION:
            if self.moving==True and self.placed==False:
                self.spikesCord = event.pos

class Bibbo(pygame.sprite.Sprite):
    
    def __init__(self):

        super().__init__()

        self.default_bird = pygame.image.load('bibbo.png').convert_alpha()
        self.default_bird = pygame.transform.rotate(self.default_bird, 180)
        self.rect = self.default_bird.get_rect(center=(600,250))

        #top left of bibbo's range
        self.rangeStr = (self.rect.left-50,self.rect.top-50)
        #bottom right of bibbo's range
        self.rangeFin = (self.rect.right+50,self.rect.bottom+50)
        #middle of bibbo's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)
        

        #bibbo's initial angle is 0
        self.angle = 0
        self.quad = None

        #initiallizing coordinates of darts
        self.x = self.rangeMid[0]
        self.y = self.rangeMid[1]

        self.angleTaken = False
        self.dartAngle = 0
        
        self.colliding = False
        self.canShoot = True

        self.currentTime = 0
        self.dartTime = 0
        self.counting = True
            
    def getAngle(self,balloon):

        self.balloonPos = balloon.balloonPos()
        
        if self.balloonPos[0]>self.rangeStr[0] and self.balloonPos[0]<self.rangeFin[0]:
            if self.balloonPos[1]>self.rangeStr[1] and self.balloonPos[1]<self.rangeFin[1]:
                self.colliding = True
                self.diffX = self.rangeMid[0]-self.balloonPos[0]
                self.diffY = self.rangeMid[1]-self.balloonPos[1]
                if self.diffY==0:
                    self.angleTemp = 0
                else: self.angleTemp = abs(math.degrees(math.atan(self.diffX/self.diffY)))
                self.checkQuad()
                if self.canShoot == True:
                    dart_group.add(bibboIns.createDart(balloon,self.balloonPos[0],
                                                       self.balloonPos[1]))
            else:
                self.colliding = False

    #changes the angle depending on which quadrant...
    #..the balloon is colliding with bibbo's range
    def checkQuad(self):

        quad00 = self.rangeStr
        quad01 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeStr[1])
        quad02 = (self.rangeFin[0],self.rangeStr[1])

        quad10 = (self.rangeStr[0],(self.rangeStr[1]+self.rangeFin[1])//2)
        quad11 = ((self.rangeStr[0]+self.rangeFin[0])//2,(self.rangeStr[1]+self.rangeFin[1])//2)
        quad12 = (self.rangeFin[0],(self.rangeStr[1]+self.rangeFin[1])//2)

        quad20 = (self.rangeStr[0],self.rangeFin[1])
        quad21 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeFin[1])
        quad22 = self.rangeFin

        x = self.balloonPos[0]
        y = self.balloonPos[1]

        if y>quad00[1] and y<quad10[1]:
            #quad 1
            if x>quad01[0] and x<quad02[0]:
                self.quad = 1
                self.angle = -self.angleTemp

            #quad 2
            elif x>quad00[0] and x<quad01[0]:
                self.quad = 2
                self.angle = self.angleTemp

        elif y>quad10[1] and y<quad20[1]:

            #quad 3
            if x>quad00[0] and x<quad01[0]:
                self.quad = 3
                self.angle = 180 - self.angleTemp

            #quad 4
            elif x>quad01[0] and x<quad02[0]:
                self.quad = 4
                self.angle = 180 + self.angleTemp

    # source: https://www.youtube.com/watch?v=_TU6BEyBieE
    def blitRotate(self):

        self.img = pygame.transform.rotate(self.default_bird,self.angle)
                
        screen.blit(self.img,(self.rect.centerx-int(self.img.get_width()/2),
                              self.rect.centery-int(self.img.get_height()/2)))

    def isShooting(self):
        
        if self.shooting:
            self.shooting = False
            return True
        else:
            return False

    def createDart(self,balloon,balloonX,balloonY):
        
        self.canShoot = False
        
        return Darts(self.angle,self.quad,balloon,self.rangeMid[0],self.rangeMid[1],
                        balloonX,balloonY)

    def updateDartTime(self):

        self.currentTime = pygame.time.get_ticks()

        if self.canShoot == False and self.counting == True:
            self.counting = False
            self.dartTime = pygame.time.get_ticks()

        elif self.currentTime - self.dartTime > 1000:
            self.counting = True
            self.canShoot = True

class Darts(pygame.sprite.Sprite):
    def __init__(self,angle,quad,balloon,x1,y1,x2,y2):
        super().__init__()

        self.feather_dart = pygame.image.load('feather.png').convert_alpha()
        self.feather_dart = pygame.transform.rotate(self.feather_dart, 180)
        self.image = pygame.transform.rotate(self.feather_dart, angle)

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.quad = quad
        self.m = angle/90

        self.balloon = balloon
        self.numPopped = 0

        self.rect = self.image.get_rect(center=(self.x1,self.y1))

    def update(self):
        
        if self.quad == 1:
            self.rect.x += 5*self.m
            self.rect.y -= 5
        if self.quad == 2:
            self.rect.x -= 5*self.m
            self.rect.y -= 5
        if self.quad == 3:
            self.rect.x -= 5*self.m
            self.rect.y += 5
        if self.quad == 4:
            self.rect.x += 5*self.m
            self.rect.y += 5
            
        if self.rect.x>1000 or self.rect.y>1000:
            self.kill()

    def popBalloon(self,balloon):
        global displayBalloon1

        if self.numPopped > 3:
            self.kill()

        if balloon.isColliding(self.rect):
            displayBalloon1.remove(balloon)
            screen.blit(pop,balloon)
            self.numPopped += 1
            
        


displayBalloon1 = Balloons(b,0).round2Balloons()

#creates instance of the spikes class
spikesIns = AllSpikes()
bibboIns = Bibbo()

playerGroup = pygame.sprite.Group()
playerGroup.add(bibboIns)

dart_group = pygame.sprite.Group()


# displays everything on game window
def drawWindow():
    global spikesDamage,healthBar
    
    screen.blit(test_surface,(0,0))
    
    for balloon in displayBalloon1:
        balloon.round2()
        
    screen.blit(game_bar,(0,0))

    spikesIns.assignSpikes()
    spikesIns.displaySpikes()
    
    bibboIns.updateDartTime()
    bibboIns.blitRotate()

    dart_group.draw(screen)
    dart_group.update()

    
    for balloon in displayBalloon1:
        spikesIns.popBalloon(balloon)
        bibboIns.getAngle(balloon)
        for dart in dart_group:
            dart.popBalloon(balloon)

    for balloon in displayBalloon1:
        if balloon.checkPassing():
            if balloon in displayBalloon1:
                displayBalloon1.remove(balloon)
                healthBar -= 1

    display_healthBar = font.render('HEALTH: '+ str(healthBar), False, 'white')
    screen.blit(display_healthBar,(20,40))        

def main():    
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            spikesIns.moveSpikes(event)

        drawWindow()

        #updates display every loop        
        pygame.display.update()
        clock.tick(60) #makes while loop run 60 times per second

main()







    


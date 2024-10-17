# random objects on each island - 1 in 20 chance of a flag or soemthing
import pygame
import random
import time
pygame.init()
clock=pygame.time.Clock()
cross = pygame.image.load('crosshair3.png')
cross=pygame.transform.scale(cross,(16,16))
icon_img= pygame.image.load('bluetriangle.png')
icon_img.set_colorkey((0, 0, 0))
water= pygame.image.load('water.png')
water.set_colorkey((0, 0, 0))
GrassActive=False
StoneActive=False
SandActive=False
GREENGO=True
GREYGO=False
YELLOWGO=False
LCscore=0
RCscore=0
textbox=pygame.sprite.Group()
##text wip
RED=(255,0,0)
GREEN=(0,255,0)
LIGHTBLUE=(44,87,93)
GREY=(128,128,128)
YELLOW=(255,255,0)
grassblockpositions = []
stoneblockpositions = []
sandblockpositions = []
gpo=[]
hpo=[]
cpo=[]
class Text(pygame.sprite.Sprite):
    def __init__(self, xsize, ysize, xloc, yloc, text, tsize, tcolour,bgcol):
        super().__init__()
        self.image = pygame.Surface([xsize, ysize])
        self.image.fill(bgcol)
        self.rect = self.image.get_rect()
        self.rect.x = xloc
        self.rect.y = yloc
        textbox.add(self)
        self.myfont = pygame.font.SysFont("bauhaus93", tsize)
        self.tsurf = self.myfont.render(str(text), True, tcolour)
        self.trect = self.tsurf.get_rect()
        self.tcolour = tcolour
        self.tsize = tsize
        

        self.image.blit(self.tsurf, self.trect)     
        key = pygame.key.get_pressed() # Get Keyboard Input
        if key[pygame.K_1]: # Check Key
            LIGHTBLUE2=(0,255,0)

    def updateText(self, text):
        self.image.fill(RED)
        self.tsurf = self.myfont.render(text, True, self.tcolour)
        self.trect = self.tsurf.get_rect()
        self.image.blit(self.tsurf, self.trect)
        
##
class MiniPlayer:
    def __init__(self):
        self.image=icon_img
        self.rect = pygame.Rect((50,51),(20,24)) # Create Player Rect
    def render(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))
        if self.rect.x < 0: # Simple Sides Collision
            self.rect.x = 50 # Reset Player Rect Coord
            self.rect.y = 51
        elif self.rect.x > 1984:
            self.rect.x = 50
            self.rect.y = 51            
        if self.rect.y < 0:
            self.rect.y = 51
            self.rect.x = 50            
        elif self.rect.y > 1984:
            self.rect.x = 50
            self.rect.y = 51
class Player:
    def __init__(self):
        self.image=cross
        self.rect = pygame.Rect((50,50),(16,16)) # Create Player Rect
    def move(self,camera_pos):
        pos_x,pos_y = camera_pos # Split camara_pos
        #
        key = pygame.key.get_pressed() # Get Keyboard Input
        if key[pygame.K_w]: # Check Key
            self.rect.y -= 8 # Move Player Rect Coord
            pos_y += 8 # Move Camara Coord Against Player Rect
        if key[pygame.K_a]:
            self.rect.x -= 8
            pos_x += 8
        if key[pygame.K_s]:
            self.rect.y += 8
            pos_y -= 8
        if key[pygame.K_d]:
            self.rect.x += 8
            pos_x -= 8
        if self.rect.x < 0: # Simple Sides Collision
            self.rect.x = 0 # Reset Player Rect Coord
            pos_x = camera_pos[0] #Reset Camera Pos Coord
        elif self.rect.x > 1984:
            self.rect.x = 1984
            pos_x = camera_pos[0]
        if self.rect.y < 0:
            self.rect.y = 0
            pos_y = camera_pos[1]
        elif self.rect.y > 1984:
            self.rect.y = 1984
            pos_y = camera_pos[1]
        return (pos_x,pos_y) # Return New Camera Pos
    def render(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))
class GrassBuild:
    def __init__(self):
        self.image=grass_img
        self.rect = pygame.Rect((70,70),(20,24)) # Create Player Rect
    def render(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))
print("The bigger the X/Y and island size, the more lag!")
xsize = int(input("Enter X size (20-200): "))
ysize = int(input("Enter Y size (20-200): "))
isles = int(input("Enter number of island seeds (3-100) - Warning , this cannot be more than the X/Y size: "))
multilayer=input("MultiLayer mode - y or n?(Lag warning):")
island_min_size = 30
island_max_size = 100
gixs = random.sample(range(1,xsize), isles)
giys = random.sample(range(1,ysize), isles)
sixs=random.sample(range(1,xsize), isles)
siys=random.sample(range(1,ysize), isles)
saixs=random.sample(range(1,xsize), isles)
saiys=random.sample(range(1,ysize), isles)
worldmap = [["0" for n in range(xsize)] for m in range(ysize)]
i = 0
while i < len(gixs):
    gx = gixs[i]
    gy = giys[i]    
    sx = sixs[i]
    sy = siys[i]    
    sax = saixs[i]
    say = saiys[i]
    island_size = 0
    while island_size < island_max_size:
        #move in random direction and create land there
        gx += random.randint(-1, 1)
        gy += random.randint(-1, 1)        
        sx += random.randint(-1, 1)
        sy += random.randint(-1, 1)
        sax += random.randint(-1, 1)
        say += random.randint(-1, 1)
        if gx in range(0, xsize) and gy in range(0, ysize):
            worldmap[gx][gy] = "1"
            island_size += 1
            
        if sx in range(0, xsize) and sy in range(0, ysize):
            worldmap[sx][sy] = "2"
            island_size += 1
        if sax in range(0, xsize) and say in range(0, ysize):
            worldmap[sax][say] = "3"
            island_size += 1
        else:
            if gx < 0: gx = 0
            elif gx >= xsize: gx = xsize-1
            if gy < 0: gy = 0
            elif gy >= ysize: gy = ysize-1

            if sx < 0: sx = 0
            elif sx >= xsize: sx = xsize-1
            if sy < 0: sy = 0
            elif sy >= ysize: sy = ysize-1
        if random.randint(island_size, island_max_size*2) < island_size:
            island_size = island_max_size
    i += 1
with open("map", "w") as f:
    for line in worldmap:
        for tile in line:
            f.write(tile)
        f.write("\n")
f = open('map')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()
grasspositions = []

stonepositions = []
sandpositions = []
wpositions=[]
selmat=[]
for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile==1:
                    grassblockpositions.append((0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5-40))
                if tile==2:
                    stoneblockpositions.append((0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5-14))
                if tile==3:
                    sandblockpositions.append((0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5-40))

for n in range(5):
    gpo.append (random.choice(grassblockpositions))
for n in range(2):
    hpo.append (random.choice(stoneblockpositions))
for n in range(5):
    cpo.append (random.choice(sandblockpositions))
def Main(display,clock):
    global LCscore
    global RCscore
    global GrassActive
    global StoneActive
    global SandActive
    global GREENGO
    global GREYGO
    global YELLOWGO
    world = pygame.Surface((2000,2000)) # Create Map Surface
    world.fill(colors["BLACK"]) # Fill Map Surface Black
    grass_img = pygame.image.load('grass.png').convert()
    grass_img.set_colorkey((0, 0, 0))
    stone_img = pygame.image.load('stone.png').convert()
    stone_img.set_colorkey((0, 0, 0))
    purplestone_img = pygame.image.load('purplestone.png').convert()
    purplestone_img.set_colorkey((0, 0, 0))
    greenstone_img = pygame.image.load('greenstone.png').convert()
    greenstone_img.set_colorkey((0, 0, 0))
    bluestone_img = pygame.image.load('bluestone.png').convert()
    bluestone_img.set_colorkey((0, 0, 0))
    sand_img = pygame.image.load('sand.png').convert()
    sand_img.set_colorkey((0, 0, 0))
    dirt_img = pygame.image.load('dirt.png').convert()
    dirt_img.set_colorkey((0, 0, 0))
    blue_img = pygame.image.load('blue.png').convert()
    blue_img.set_colorkey((0, 0, 0))
    tree_img = pygame.image.load('tree.png').convert()
    tree_img.set_colorkey((0, 0, 0))
    house_img = pygame.image.load('house.png').convert()
    house_img.set_colorkey((0, 0, 0))
    cactus_img = pygame.image.load('cactus.png').convert()
    cactus_img.set_colorkey((0, 0, 0))
    stonetype=[stone_img,purplestone_img,greenstone_img,bluestone_img]
    blocklist=[grass_img,sand_img,stone_img]
    for x in range(10):
        pygame.draw.rect(world,colors["BLUE"],((x*100,x*100),(20,20))) # Put Blue Rectagles On Map Surface    
    player = Player() # Initialize Player Class
    camera_pos = (192,192) # Create Camara Starting Position
    mp=MiniPlayer()
    
    while True:
        
        position = pygame.mouse.get_pos()
        mousex = position[0]
        mousey = position[1]
##        player.rect.x=mousex
##        player.rect.y=mousey
        clock.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    mp.rect.y-=5
                    mp.rect.x+=10
                    print(mp.rect.x,mp.rect.y)  
                if event.key==pygame.K_DOWN: # Check Key
                    mp.rect.y+=5
                    mp.rect.x-=10
                    print(mp.rect.x,mp.rect.y)
                if event.key==pygame.K_RIGHT: # Check Key
                    mp.rect.y+=5
                    mp.rect.x+=10
                    print(mp.rect.x,mp.rect.y)
                if event.key==pygame.K_LEFT: # Check Key
                    mp.rect.y-=5
                    mp.rect.x-=10
                    print(mp.rect.x,mp.rect.y)
                if event.key==pygame.K_SPACE: # Check Key
                    mp.rect.y-=14
                if event.key==pygame.K_LSHIFT: # Check Key
                    mp.rect.y+=14
                if event.key==pygame.K_1: # Check Key
                    GrassActive=True
                    StoneActive=False
                    SandActive=False
                    GREENGO=True
                    GREYGO=False
                    YELLOWGO=False
                    selmat.append(grass_img)
                    print(selmat)
                    
                if event.key==pygame.K_2: # Check Key
                    GrassActive=False
                    StoneActive=True
                    SandActive=False
                    GREENGO=False
                    GREYGO=True
                    YELLOWGO=False
                    selmat.append(stone_img)
                    print(selmat)
                    
                if event.key==pygame.K_3: # Check Key
                    GrassActive=False
                    StoneActive=False
                    SandActive=True
                    GREENGO=False
                    GREYGO=False
                    YELLOWGO=True
                    selmat.append(sand_img)
                    print(selmat)
                    
                 
##            if event.type == pygame.MOUSEBUTTONUP:
##                # add position to list
##                positions.append((mp.rect.x,mp.rect.y))
            left, middle, right =pygame.mouse.get_pressed()
            if left:
                if GrassActive== True:
                    grasspositions.append((mp.rect.x,mp.rect.y))
                if StoneActive== True:
                    stonepositions.append((mp.rect.x,mp.rect.y))
                if SandActive== True:
                    sandpositions.append((mp.rect.x,mp.rect.y))
                LCscore +=1
                
            if right:
                if (mp.rect.x,mp.rect.y) in grasspositions:
                    print(" ")
                    grasspositions.remove((mp.rect.x,mp.rect.y))
                if (mp.rect.x,mp.rect.y) in stonepositions:
                    print(" ")
                    stonepositions.remove((mp.rect.x,mp.rect.y))
                if (mp.rect.x,mp.rect.y) in sandpositions:
                    print(" ")
                    sandpositions.remove((mp.rect.x,mp.rect.y))
                if (mp.rect.x,mp.rect.y) not in grasspositions or (mp.rect.x,mp.rect.y) not in stonepositions or (mp.rect.x,mp.rect.y) not in sandpositions:
                    print(" ")
                    wpositions.append((mp.rect.x,mp.rect.y))
                RCscore+=1
        camera_pos = player.move(camera_pos) # Run Player Move Function And Return New Camera Pos
        display.fill(colors["DARKBLUE"]) # Fill The Background White To Avoid Smearing
        world.fill(colors["LIGHTBLUE"]) # Refresh The World So The Player Doesn't Smear
        
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile==1:
                    if multilayer == "y":
                        for n in reversed(range(1,5)):
                            if x % 2==0 and y % 2 == 0:
                                world.blit(stonetype[0], (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14 + n *14))
                            else:
                                world.blit(stonetype[2], (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14 + n * 14))
                        world.blit(dirt_img, (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14))
                    world.blit(grass_img, (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5))
                    


                if tile==2:
                    if multilayer =="y":
                        for n in reversed(range(1,5)):
                            if x % 2==0 and y % 2 == 0:
                                world.blit(stonetype[0], (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14 + n *14))
                            else:
                                world.blit(stonetype[3], (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14 + n * 14))
                        world.blit(stone_img, (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14))
                    world.blit(stone_img, (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5))
                if tile==3:
                    if multilayer == "y":
                        for n in reversed(range(1,5)):
                            if x % 2==0 and y % 2 == 0:
                                world.blit(stonetype[0], (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14 + n *14))
                            else:
                                world.blit(stonetype[1], (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14 + n * 14))
                        world.blit(dirt_img, (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5 + 14))
                    world.blit(sand_img, (0 + x * 10 - y * 10+300, 0 + x * 5 + y * 5))

        for wpos in wpositions:
            
            world.blit(water, wpos)
        for gpos in grasspositions:
            
                
            world.blit(grass_img,gpos)
            if len(selmat) == 0:
                world.blit(blue_img,gpos)
        for stpos in stonepositions:
            
                
            world.blit(stone_img,stpos)
            if len(selmat) == 0:
                world.blit(blue_img,stpos)
        for sapos in sandpositions:
            
                
            world.blit(sand_img,sapos)
            if len(selmat) == 0:
                world.blit(blue_img,sapos)
        for n in range(5):
            world.blit(tree_img,gpo[n])
        for n in range(2):
            world.blit(house_img,hpo[n])
        for n in range(5):
            world.blit(cactus_img,cpo[n])
        
        player.render(world) # Render The Player
        mp.render(world)
        if GREENGO==True:
            LCscoretext=Text(100,20,30,475,"Blocks Built:",16,RED,GREEN)
        LCscorenumber=Text(50,20,130,475,LCscore,16,RED,GREEN)
        RCscoretext=Text(132,20,30,455,"Blocks Deleted:",16,RED,GREEN)
        RCscorenumber=Text(50,20,162,455,RCscore,16,RED,GREEN)
        if GREYGO==True:
            LCscoretext=Text(100,20,30,475,"Blocks Built:",16,RED,GREY)
            LCscorenumber=Text(50,20,130,475,LCscore,16,RED,GREY)
            RCscoretext=Text(132,20,30,455,"Blocks Deleted:",16,RED,GREY)
            RCscorenumber=Text(50,20,162,455,RCscore,16,RED,GREY)
        if YELLOWGO==True:
            LCscoretext=Text(100,20,30,475,"Blocks Built:",16,RED,YELLOW)
            LCscorenumber=Text(50,20,130,475,LCscore,16,RED,YELLOW)
            RCscoretext=Text(132,20,30,455,"Blocks Deleted:",16,RED,YELLOW)
            RCscorenumber=Text(50,20,162,455,RCscore,16,RED,YELLOW)
##        else:
##            LCscoretext=Text(100,20,30,475,"Blocks Built:",16,RED,LIGHTBLUE)
##            LCscorenumber=Text(50,20,130,475,LCscore,16,RED,LIGHTBLUE)
##            RCscoretext=Text(132,20,30,455,"Blocks Deleted:",16,RED,LIGHTBLUE)
##            RCscorenumber=Text(50,20,162,455,RCscore,16,RED,LIGHTBLUE)

        textbox.update()
        display.blit(world,camera_pos) # Render Map To The Display
        textbox.draw(display)
        clock.tick(60)
        pygame.display.flip()
if __name__ in "__main__":
    display = pygame.display.set_mode((500,500))
    pygame.display.set_caption("WorldSpawner")
    clock = pygame.time.Clock()
    
    global colors # Define Colors
    colors = {
    "WHITE":(255,255,255),
    "RED"  :(255,0,0),
    "GREEN":(0,255,0),
    "BLUE" :(0,0,255),
    "GREY":(128,128,128),
    "YELLOW":(255,255,0),
    "BLACK":(0,0,0),
    "LIGHTBLUE":(44,87,93),
    "DARKBLUE":(87,166,178)
    }
    Main(display,clock) # Run Main Loop

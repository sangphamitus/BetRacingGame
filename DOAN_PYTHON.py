import random
import time
import pygame, sys
from pygame.locals import *
import pygame
import os
from playsound import playsound
# from pygame.locals import *
import winsound
import random
import csv

size_Car = 80
## Các bảng màu theo chuẩn RGB ##
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIGHTRED = (255,99,71) 
GREEN = (0,255,0)
LIGHTGREEN = (144,238,144)
GREEN_2 = (85,107,47)
BLUE = (0,0,255)
LIGHTBLUE = (0,191,255)
GRAY = (105,105,105)
LIGHTGRAY = (169,169,169)
BLUEGRAY = (119,136,153)
PURPLE = (75,0,130)
YELLOW = (255,255,0)
ORANGE = (255,69,0)
DARKBLUE = (25,25,112)
PINK = (255,105,180)
#---Hình nền game--------------------------------
BG1 = pygame.image.load('BG1.png')
BG2 = pygame.image.load('Background_ChooseCar.png')
BG3 = pygame.image.load('Background_Money.png')
BG5 = pygame.image.load('Background_Rank.png')
BG6 = pygame.image.load('Background6.png')
BG7 = pygame.image.load('Background7.png')
BG8 = pygame.image.load('Background8.png')

#-----------------HÌNH XE-----------------------
#---------------====SET1====---------------------
Xe1 = pygame.image.load('Xe1.png')
Xe1_1 = pygame.image.load('Xe1.1.png')
Xe2 = pygame.image.load('Xe2.png')
Xe2_1 = pygame.image.load('Xe2.1.png')
Xe3 = pygame.image.load('Xe3.png')
Xe3_1 = pygame.image.load('Xe3.1.png')
Xe4 = pygame.image.load('Xe4.png')
Xe4_1 = pygame.image.load('Xe4.1.png')
Xe5 = pygame.image.load('Xe5.png')
Xe5_1 = pygame.image.load('Xe5.1.png')
#---------------====SET2====---------------------
Xe1_2 = pygame.image.load('1.png')
Xe2_2 = pygame.image.load('2.png')
Xe3_2 = pygame.image.load('3.png')
Xe4_2 = pygame.image.load('4.png')
Xe5_2 = pygame.image.load('5.png')
Xe1_2_1 = pygame.image.load('1.png')
Xe2_2_1 = pygame.image.load('2.png')
Xe3_2_1 = pygame.image.load('3.png')
Xe4_2_1 = pygame.image.load('4.png')
Xe5_2_1 = pygame.image.load('5.png')
#---------------====SET3====---------------------
Xe1_3 = pygame.image.load('6.png')
Xe2_3 = pygame.image.load('7.png')
Xe3_3 = pygame.image.load('8.png')
Xe4_3 = pygame.image.load('9.png')
Xe5_3 = pygame.image.load('10.png')
Xe1_3_1 = pygame.image.load('6.png')
Xe2_3_1 = pygame.image.load('7.png')
Xe3_3_1 = pygame.image.load('8.png')
Xe4_3_1 = pygame.image.load('9.png')
Xe5_3_1 = pygame.image.load('10.png')
#---------------====SET4====---------------------
Xe1_4 = pygame.image.load('11.png')
Xe2_4 = pygame.image.load('12.png')
Xe3_4 = pygame.image.load('13.png')
Xe4_4 = pygame.image.load('14.png')
Xe5_4 = pygame.image.load('15.png')
Xe1_4_1 = pygame.image.load('11.png')
Xe2_4_1 = pygame.image.load('12.png')
Xe3_4_1 = pygame.image.load('13.png')
Xe4_4_1 = pygame.image.load('14.png')
Xe5_4_1 = pygame.image.load('15.png')
#---------------====SET5====---------------------
Xe1_5 = pygame.image.load('16.png')
Xe2_5 = pygame.image.load('17.png')
Xe3_5 = pygame.image.load('18.png')
Xe4_5 = pygame.image.load('19.png')
Xe5_5 = pygame.image.load('20.png')
Xe1_5_1 = pygame.image.load('16.png')
Xe2_5_1 = pygame.image.load('17.png')
Xe3_5_1 = pygame.image.load('18.png')
Xe4_5_1 = pygame.image.load('19.png')
Xe5_5_1 = pygame.image.load('20.png')
#---Hình chướng ngại vật--------------------------
obs1 = pygame.image.load('Hole.png')
obs2 = pygame.image.load('bomb.png')
obs3 = pygame.image.load('sand.png')
obs4 = pygame.image.load('horse.png')
obs5 = pygame.image.load('oil.png')
obs6 = pygame.image.load('thorns.png')
obs7 = pygame.image.load('water.png')
#--------------------------------------------------
width_obs1 = obs1.get_width()
width_obs2 = obs2.get_width()
width_obs3 = obs3.get_width()
width_obs4 = obs4.get_width()
width_obs5 = obs5.get_width()
width_obs6 = obs6.get_width()
width_obs7 = obs7.get_width()
#--------------------------------------------------
pygame.init()

### Xác định FPS ###
FPS = 30
fpsClock = pygame.time.Clock()

WINDOWWIDTH = 900 # Chiều dài cửa sổ
WINDOWHEIGHT = 600 # Chiều cao cửa sổ

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Gambling Car')

picture = ['BG1.png','Background_ChooseCar.png','Background_Money.png','Background_Rank.png','Background8.png']
imaged_1 = pygame.transform.scale(pygame.image.load(picture[0]),(1150,650))
imaged_2 = pygame.transform.scale(pygame.image.load(picture[1]),(1150,650))
imaged_3 = pygame.transform.scale(pygame.image.load(picture[2]),(1150,650))
imaged_4 = pygame.transform.scale(pygame.image.load(picture[3]),(1150,650))
imaged_5 = pygame.transform.scale(pygame.image.load(picture[4]),(1150,650))

## Cách lấy kích thước của hình ##
#height = BG4.get_height()

def minigame1(nguoichoi,tka):
    
    filetes= open("data/ "+nguoichoi,"r")
    money = int(filetes.readline())
    hang1 =filetes.readline()
    hang2=filetes.readline()
    filetes.close()

    bg = pygame.image.load("bg.png")
    keo = pygame.image.load("keo.png")
    keo1 = pygame.image.load("keo1.png")
    bua = pygame.image.load("bua.png")
    bua1 = pygame.image.load("bua1.png")
    bao = pygame.image.load("bao.png")
    bao1 = pygame.image.load("bao1.png") 
    lose = pygame.image.load("lose.png")
    win = pygame.image.load("win.png")
    draw = pygame.image.load("draw.png")
    cpt = pygame.image.load("player.png")
    computer = random.randint(1,3)
    player = 0
    run = True
    ran = True
    thangsa = False
    danhse =False
    def comim(computer):
        if computer == 1: 
            DISPLAYSURF.blit(keo, (370,200))
        elif computer == 2:
            DISPLAYSURF.blit(bua, (370,200))
        elif computer == 3:
            DISPLAYSURF.blit(bao, (370,200))
        pygame.display.flip()
            

    while run:
        
        mx, my = pygame.mouse.get_pos()
        DISPLAYSURF.blit(bg, (0,0))
        DISPLAYSURF.blit(keo, (50,50))
        DISPLAYSURF.blit(bua, (50,200))
        DISPLAYSURF.blit(bao, (50,350)) 
        DISPLAYSURF.blit(cpt, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE) or (tka==5):
                    run = False 
                    fileout= open("data/ "+nguoichoi,"w+")
                    fileout.write(str(money))
                    fileout.write("\n")
                    fileout.write(hang1)
                    fileout.write(hang2)
                    fileout.close()
                    return 100
                if event.key == pygame.K_r:
                    fileout= open("data/ "+nguoichoi,"w+")
                    if thangsa == True:
                        money= money+500
                    fileout.write(str(money))
                    fileout.write("\n")
                    fileout.write(hang1)
                    fileout.write(hang2)
                    fileout.close()
                    return 0
            if (event.type == pygame.MOUSEBUTTONDOWN)&(danhse == False):
                if (50<=mx<=200) and (100<=my<=150):
                    player = 1
                    DISPLAYSURF.blit(keo1, (50,50))
                    danhse = True
                elif (50<=mx<=200) and (200<=my<=300):
                    player = 2
                    DISPLAYSURF.blit(bua1, (50,200))
                    danhse = True
                elif (50<=mx<=200) and (350<=my<=450):
                    player = 3
                    DISPLAYSURF.blit(bao1, (50,350))
                    danhse = True
        if player == computer:
            comim(computer)
            DISPLAYSURF.blit(draw, (100,150))
        elif player == 1:
            if computer == 2:
                comim(computer)
                DISPLAYSURF.blit(lose, (100,150))
            else:
                comim(computer)
                DISPLAYSURF.blit(win, (100,145))
                thangsa=True
        elif player == 2:
            if computer == 1:
                comim(computer)
                DISPLAYSURF.blit(win,(100,145))
                thangsa=True
            else:
                comim(computer)
                DISPLAYSURF.blit(lose, (100,150))
        elif player == 3:
            if computer == 2:
                comim(computer)
                DISPLAYSURF.blit(win,(100,145))
                thangsa=True
            else:
                comim(computer)
                DISPLAYSURF.blit(lose, (100,150))

        pygame.display.flip()
'''''''''''''''''''''''''''''''''''''''''''''
GIAO DIỆN ĐĂNG NHẬP
'''''''''''''''''''''''''''''''''''''''''''''
def dangnhap():
    pygame.mixer.init()
    pygame.mixer.music.load('login.mp3')
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((1150, 650))
    open('data/DATA.csv', 'a+')
    def SaveAccount(_id, _pass):
        with open('data/DATA.csv', 'a+') as data:
            data.write(_id + ';' + _pass + '\n')
            data.close()
    def xuatprofile(_id):
        with open('data/ '+_id + '.csv', 'w+') as data:
            data.write('2000')
            data.write('\n')
            data.write("0 0 0 \n")
            data.write("1 1 1 \n")
            data.close()
    def docfile(_id, _pass):
        ktra = 2
        with open('data/DATA.csv') as data:
            csv_reader = csv.reader(data, delimiter=';')
            for row in csv_reader:
                if f'{row[0]}' == _id:
                    if f'{row[1]}' == _pass: return 0
                    else: return 1
                elif f'{row[0]}' != _id:
                    ktra = 2
            return ktra       
    def XacNhanDK(_id, _pass, _secret):
        out = False
        error = False
        background = pygame.image.load('BG1.png')
        font = pygame.font.Font(None, 22)
        _confirm = ''
        _secret1 = ''
        confirm_box = pygame.Rect(525, 390, 250, 32)
        confirm_btn = pygame.Rect(515, 440, 120, 32)
        return_btn = pygame.Rect(515, 490, 120, 32)
        color_btnCF = (255,100,0)
        color_btnRT = (220, 220, 220)
        id_surface = font.render(_id, True, 'black')
        pass_surface = font.render(_secret, True, 'black')
        txt_id = font.render('ID: ', True, 'black')
        txt_pass = font.render('Mat khau:', True, 'black')
        txt_confirm = font.render('Xac nhan mat khau:', True, 'black')
        txt_return = font.render('Quay lai', True, 'white')
        txt_XacNhan = font.render('Xac nhan', True, 'white')
        rect_DangKy = pygame.Surface((450,300))
        rect_DangKy.set_alpha(200)
        rect_DangKy.fill((230,230,230))
        warning = font.render('Khong trung khop', True, 'red')
        while not out:
            screen.blit(pygame.transform.scale(background,(1150,650)),pygame.Rect(0,0,120,20))
            screen.blit(rect_DangKy, (350,260))
            pygame.draw.rect(screen, (255,255,255), (350,260,450,300),5)
            confirm_surface = font.render(_secret1, True, 'dodgerblue2')
            pygame.draw.rect(screen, 'dodgerblue2', confirm_box, 2)
            screen.blit(txt_id, (450, 300))
            screen.blit(txt_pass, (397, 335))
            screen.blit(txt_confirm, (370, 398))
            screen.blit(id_surface, (500, 300))
            screen.blit(pass_surface, (500, 340))
            screen.blit(confirm_surface, (confirm_box.x+5, confirm_box.y+10))
            pygame.draw.rect(screen, color_btnCF, confirm_btn)
            pygame.draw.rect(screen, color_btnRT, return_btn)
            screen.blit(txt_XacNhan, (confirm_btn.x+28, confirm_btn.y + 9))
            screen.blit(txt_return, (return_btn.x+28, return_btn.y + 9))
            if error == True: screen.blit(warning, (525, 365))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        _confirm = _confirm[:-1]
                        _secret1 = _secret1[:-1]
                    elif len(_id) < 20 and event.key != pygame.K_SEMICOLON and event.key != pygame.K_RETURN:
                        _confirm += event.unicode
                        _secret1 += '*'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if confirm_btn.collidepoint(event.pos):
                        color_btnCF = (170, 70, 0)
                    if return_btn.collidepoint(event.pos):
                        color_btnRT = (160, 160, 160)
                if event.type == pygame.MOUSEBUTTONUP:
                    if confirm_btn.collidepoint(event.pos):
                        color_btnCF = (255,100,0)
                        if _pass == _confirm:
                            SaveAccount(_id, _pass)
                            xuatprofile(_id)
                            out = True
                        else:  error = True
                    if return_btn.collidepoint(event.pos):
                        color_btnRT = (200, 200, 200)
                        out = True    
    def maindna():
        font = pygame.font.Font(None, 22)
        clock = pygame.time.Clock()
        id_box = pygame.Rect(470, 310, 300, 32)
        pass_box = pygame.Rect(470, 370, 300, 32)
        DangNhap_btn = pygame.Rect(520, 430, 120, 32)
        DangKy_btn = pygame.Rect(520, 480, 120, 32)
        color_btnDK = (255,100,0)
        color_btnDN = (100, 200, 250)
        color_inactive = pygame.Color('cyan4')
        color_active = pygame.Color('dodgerblue2')
        idcolor = color_inactive
        passcolor = color_inactive
        idactive = False
        passactive = False
        done = False
        error1 = False   #Lỗi không nhập dữ liệu
        error2 = False   #Lỗi nhập sai dữ liệu
        error3 = False   #Lỗi đăng ký tài khoản đã có rồi
        _id = ''
        _pass = ''
        _secret = ''
        background = pygame.image.load('BG1.png')
        rect_DangNhap = pygame.Surface((450,300))
        rect_DangNhap.set_alpha(200)
        rect_DangNhap.fill((230,230,230))
        rect_erase = pygame.Surface((300,30))
        rect_erase.set_alpha(0)
        rect_erase.fill((230,230,230))
        #rect_DangNhap.set_alpha(100)
        while not done:
            screen.blit(pygame.transform.scale(background,(1150,650)),pygame.Rect(0,0,120,20))
            screen.blit(rect_DangNhap, (350,260))
            pygame.draw.rect(screen, (255,255,255), (350,260,450,300),5)
            # Dữ liệu text
            id_surface = font.render(_id, True, idcolor)
            pass_surface = font.render(_secret, True, passcolor)
            txt_id = font.render('ID: ', True, 'black')
            txt_pass = font.render('Mat khau:', True, 'black')
            txt_DangNhap = font.render('Dang Nhap', True, 'white')
            txt_DangKy = font.render('Dang Ky', True, 'white')
            warning1 = font.render('Ban chua nhap ID hoac mat khau', True, 'red')
            warning2 = font.render('ID hoac mat khau sai', True, 'red')
            warning3 = font.render('Tai khoan da ton tai', True, 'red')
            # Xuất text từ bàn phím
            screen.blit(id_surface, (id_box.x+5, id_box.y+10))
            screen.blit(pass_surface, (pass_box.x+5, pass_box.y+10))
            # Vẽ box và text
            screen.blit(txt_id, (id_box.x - 40, id_box.y + 10))
            screen.blit(txt_pass, (pass_box.x - 94, pass_box.y + 10))
            pygame.draw.rect(screen, idcolor, id_box, 2)
            pygame.draw.rect(screen, passcolor, pass_box, 2)
            pygame.draw.rect(screen, color_btnDN, DangNhap_btn)
            screen.blit(txt_DangNhap, (DangNhap_btn.x+18, DangNhap_btn.y + 9))
            pygame.draw.rect(screen, color_btnDK, DangKy_btn)
            screen.blit(txt_DangKy, (DangKy_btn.x+29, DangKy_btn.y + 9))
            if error1 == True:
                screen.blit(rect_erase, (400,200))
                screen.blit(warning1, (470, 280))
            if error2 == True:
                screen.blit(rect_erase, (400,200))
                screen.blit(warning2, (470,280))
            if error3 == True:
                screen.blit(rect_erase, (400,200))
                screen.blit(warning3, (470,280))
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN: #Sự kiện nhấn chuột
                    if id_box.collidepoint(event.pos): #Nhấp vào box id
                        idactive = not idactive
                    else:
                        idactive = False
                    idcolor = color_active if idactive else color_inactive
                    if pass_box.collidepoint(event.pos): #Nhấp vào box password
                        passactive = not passactive
                    else:
                        passactive = False
                    passcolor = color_active if passactive else color_inactive
                    if DangNhap_btn.collidepoint(event.pos): #Nhấp vào nút Đăng nhập
                        color_btnDN = (85, 150, 185)
                    if DangKy_btn.collidepoint(event.pos): #Nhấp vào nút Đăng ký
                        color_btnDK = (170, 70, 0)
                if event.type == pygame.MOUSEBUTTONUP: #Sự kiện nhả chuột
                    if DangNhap_btn.collidepoint(event.pos):  #Sau khi nhấn nút Đăng nhập
                        color_btnDN = (100, 200, 250)
                        if _id == '' or _pass == '':
                            error1 = True
                            error2 = False
                            error3 = False
                        else:
                            if docfile(_id, _pass) == 0:
                                done = True
                                nguoichoi = _id + '.csv'
                            else:
                                error2 = True
                                error1 = False
                                error3 = False
                    if DangKy_btn.collidepoint(event.pos):    #Sau khi nhấn nút Đăng ký
                        color_btnDK = (255,100,0)
                        if _id == '' or _pass == '':
                            error1 = True
                            error2 = False
                            error3 = False
                        else:
                            if docfile(_id, _pass) == 2:
                                XacNhanDK(_id, _pass, _secret)
                            else:
                                error3 = True
                                error1 = False
                                error2 = False
                if event.type == pygame.KEYDOWN:  #Sự kiện gõ phím
                    if idactive:
                        if event.key == pygame.K_BACKSPACE:
                            _id = _id[:-1]
                        elif len(_id) < 20 and event.key != pygame.K_SEMICOLON and event.key != pygame.K_RETURN:
                            _id += event.unicode
                    if passactive:
                        if event.key == pygame.K_BACKSPACE:
                            _pass = _pass[:-1]
                            _secret = _secret[:-1]
                        elif len(_pass) < 20 and event.key != pygame.K_SEMICOLON and event.key != pygame.K_RETURN:
                            _pass += event.unicode
                            _secret += '*'
                            
            pygame.display.flip()
            clock.tick(30)
        return nguoichoi
    return maindna()
    pygame.QUIT
'''
Cua hang
'''       
def store(_id=''):
    pygame.mixer.init()
    pygame.mixer.music.load('micshop\shop.mp3')
    pygame.mixer.music.play(-1)

    buysound=pygame.mixer.Sound('micshop\donebuy.mp3')
    mcl=pygame.mixer.Sound('micshop\mouseclicka.mp3')

    #nhac
    #cua so
    # khai bao dulieu
    lst = [0.75,2.5]
    lst2= [4,10,17,23]
    money = 0
    pages = 1 
    tabs = 1 
    namespell = [['Tang toc','KHOA','PHA CHUONG NGAI VAT'],
                ['RAINBOW','CARTOON CHARACTER','WITCHERS']]  
    moneyspell = [[2000,20,20],[3000,3000,3000]]
    buyspell = [[1,1,1],[1,1,1]]
    slspell = [0,0,0]
    countmaxsad = 0
    maxtabs = 2  # 1spell 2backgound 3skinlan 4skincar 
    items = 6
    picture = ['spell1.jpg','spell2.jpg','spell3.jpg']
    picture2= ['6.png','15.png','16.png']
    fontchu = 'consolas'
    pygame.init()
    #tao cua so
    widthxmas = WINDOWWIDTH
    heightxmas = WINDOWHEIGHT
    width = widthxmas
    height = 800 * width //1300
    DISPLAYSUF=pygame.display.set_mode((widthxmas,heightxmas), HWSURFACE|DOUBLEBUF|RESIZABLE)
    #pygame.display.set_caption('Store')
    #color
    red = pygame.Color(255,0,0)
    blue = pygame.Color(65,105,255)
    black = pygame.Color(0,0,0)
    white = pygame.Color(255,255,255)
    gray = pygame.Color(128,128,128)
    yellow = pygame.Color(249,244,0)
    red1 = pygame.Color(150,50,50)
    lightblue  = pygame.Color(110,232,231)
    duckgreen = pygame.Color(42,69,71)
    lightred = pygame.Color(252,97,96)
    blackrd = pygame.Color(70,22,26)
    chamf= pygame.Color(18,19,32)
    metalyellow = pygame.Color(224,194,88)
    lime = pygame.Color(0,255,0)
    darkyellow = pygame.Color(102,102,0)
    olive = pygame.Color(46,139,87)
    #load hình anh
    imgbook = pygame.image.load('picshop/background.png')
    imgarrow = pygame.image.load('picshop/arrow.png')
    imgRarrow = pygame.image.load('picshop/RightAr.png')
    imgLarrow = pygame.image.load('picshop/LeftAr.png')
    imgCover=pygame.image.load('picshop/cover.PNG')
    imgbox = pygame.image.load('picshop/mbox.png')
    #chuong trinh
    #      0    1      2      3      4      5     6      7         8        9       10      11    12           13     14     15
    mau = [red ,blue ,black ,white ,gray ,yellow,red1,lightblue,duckgreen,lightred,blackrd,chamf,metalyellow,lime,darkyellow,olive]
    def inchuoi(chuoi='',x=10,y=10,c=1,si=1):
        gfont= pygame.font.SysFont(fontchu,((si*height)//800))
        gmoney = gfont.render(chuoi,True,mau[c])
        grect = gmoney.get_rect()
        grect.midright = (x , y)
        DISPLAYSUF.blit(gmoney,grect)
    

    def showps(x=1,y=1,tab=1,maxo=1):
        #scale ảnh lá bài 
        for i in range(1,maxtabs+1):
            if (tab == i):
                pygame.draw.rect(DISPLAYSUF,blue,(width*(1/7-1/20+i/20),height*(2/7-1/20),width*1/30,height*1/25))
                pygame.draw.rect(DISPLAYSUF,lightblue,(width*(1/7-1/20+i/20),height*(2/7-1/20),width*1/30,height*1/25),2)
            else:
                pygame.draw.rect(DISPLAYSUF,red1,(width*(1/7-1/20+i/20),height*(2/7-1/20),width*1/30,height*1/25))
                pygame.draw.rect(DISPLAYSUF,lightred,(width*(1/7-1/20+i/20),height*(2/7-1/20),width*1/30,height*1/25),2)
        imagspel= pygame.image.load("picshop/bottle.png")
        DISPLAYSUF.blit(pygame.transform.scale(imagspel,(width*22//1300, height *28//800)),pygame.Rect(width*(1/7-1/20+1/20+1/100),height*(2/7-1/20+1/300),width*1/30,height*1/25))
        '''
        pygame.draw.rect(DISPLAYSUF,red,(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10),width*(5/40+1/30),height*(1/6+1/100+1/80+1/80)),4)
        pygame.draw.rect(DISPLAYSUF,red1,(width*(x/32 + 1/90+1/120),height*(1.75*y/10 + 1/17+1/10+1/250),width*(5/40+1/30-1/500),height*(1/6+1/100+1/80-1/200+1/80)))
        '''
        if tabs-1 !=0:
            framed = pygame.image.load("picshop/redframe2.jpg")
            DISPLAYSUF.blit(pygame.transform.scale(framed,(width*207//1300,height*165//800)),pygame.Rect(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10),0,0))
            inchuoi("$"+str(moneyspell[tabs-1][sospell]),width*(x/32 +1/90+1/6-1/50),height*(1.75*y/10+1/4 +1/12),12,20)
            ghep = picture2[sospell]
            imagek = pygame.image.load(ghep)
            DISPLAYSUF.blit(pygame.transform.scale(imagek,(width*80//1300,height*87//800)),pygame.Rect(width*(x/32 + 1/90+1/30+1/40)//1,height*(1.75*y/10 + 1/17+1/10+1/20)//1,120,20))    
        '''
        if tabs-1 ==0:   
                DISPLAYSUF.blit(pygame.transform.scale(imgCover,(width*100//1300, height *128//800)),pygame.Rect(width*(6/7+1/20),height*(2/7-1/20+1/10),width*1/30,height*1/25))
                ghep = str('picshop/')+picture[sospell]
                imagek = pygame.image.load(ghep)
                DISPLAYSUF.blit(pygame.transform.scale(imagek,(width*80//1300,height*87//800)),pygame.Rect(width*(x/32 + 1/90+1/30+1/40)//1,height*(1.75*y/10 + 1/17+1/10+1/20)//1,120,20))
            #DISPLAYSUF.blit(pygame.transform.scale(pygame.image.load(picture[i]),width*128//1300,height*128//800),pygame.Rect(width*(x/32 + 1/90+1/120)//1,height*(1.75*y/10 + 1/17+1/10+1/250)//1,width*(5/40+1/30-1/500)//1,height*(1/6+1/100+1/80-1/200+1/80)//1))
        '''
        '''
        pygame.draw.line(DISPLAYSUF,lightred,(width*1/7,height*2/7),(width*6/7,height*2/7),2) 
        pygame.draw.rect(DISPLAYSUF,red,(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10),width*(5/40+1/30),height*(1/7+1/150)),4)
        '''
            
        if buyspell[tabs-1][sospell] ==0:
            inchuoi("[ĐÃ SỞ HỮU]",width*(x/32+1/10+1/30 ),height*(1.75*y/10 + 1/4+ 1/25-1/30),12,20)
        '''
        if tabs-1 ==0:    
            pygame.draw.rect(DISPLAYSUF,duckgreen,(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10+1/6+1/100+1/80+1/40),width*(5/40+1/30),height*(1/20)))
            pygame.draw.rect(DISPLAYSUF,darkyellow,(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10+1/6+1/100+1/80+1/40),width*(5/40+1/30-1/8),height*(1/20)))
            pygame.draw.rect(DISPLAYSUF,darkyellow,(width*(x/32+1/7-1/500),height*(1.75*y/10 + 1/17+1/10+1/6+1/100+1/80+1/40),width*(5/40+1/30-1/8),height*(1/20)))
            pygame.draw.rect(DISPLAYSUF,yellow,(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10+1/6+1/100+1/80+1/40),width*(5/40+1/30-1/8),height*(1/20)),4)
            pygame.draw.rect(DISPLAYSUF,yellow,(width*(x/32+1/7-1/500),height*(1.75*y/10 + 1/17+1/10+1/6+1/100+1/80+1/40),width*(5/40+1/30-1/8),height*(1/20)),4)
            inchuoi(str(slspell[sospell]),width*(x/32+1/10),height*(1.75*y/10 + 1/17+1/10+1/6+1/35+1/50+1/40),3,20)   
            inchuoi("-",width*(x/32+1/25),height*(1.75*y/10 + 1/17+1/10+1/6+1/35+1/50+1/40),5,20)
            inchuoi("+",width*(x/32+1/5-1/25+1/400),height*(1.75*y/10 + 1/17+1/10+1/6+1/35+1/50+1/40),5,20)
            inchuoi("Amount in backpack : "+str(buyspell[0][sospell]-1),width*(x/32+1/6),height*(1.75*y/10 + 1/17+1/10+1/6+1/35+1/50+1/40+1/20),9,15) 
        
        if (value != 0) & (tabs-1==0) :    
            pygame.draw.rect(DISPLAYSUF,duckgreen,(width*(1/2+1/3+1/15),height*(1/5+1/3+1/15),width*(1/11),height*(1/15)))
            pygame.draw.rect(DISPLAYSUF,lime,(width*(1/2+1/3+1/15),height*(1/5+1/3+1/15),width*(1/11),height*(1/15)),4)
            inchuoi("BUY",width*(1/2+1/3+1/8+1/100),height*(1/5+1/3+1/10),13,30)
        '''
        if (tabs-1 !=0):
            if ((pages + 1 <= maxo) & (sospell < len(namespell[tabs-1])-1 )):
                DISPLAYSUF.blit(pygame.transform.scale(imgCover,(width*100//1300, height *128//800)),pygame.Rect(width*(1/7-1/10),height*(2/7-1/20+1/10),width*1/30,height*1/25))
                DISPLAYSUF.blit(pygame.transform.scale(imgRarrow,(width*100//1300, height *128//800)),pygame.Rect(width*(6/7+1/20),height*(2/7-1/20+1/10),width*1/30,height*1/25))
            elif (pages - 1 >= 1 )&( sospell >=0) :
                DISPLAYSUF.blit(pygame.transform.scale(imgCover,(width*100//1300, height *128//800)),pygame.Rect(width*(6/7+1/20),height*(2/7-1/20+1/10),width*1/30,height*1/25))
                DISPLAYSUF.blit(pygame.transform.scale(imgLarrow,(width*100//1300, height *128//800)),pygame.Rect(width*(1/7-1/10),height*(2/7-1/20+1/10),width*1/30,height*1/25))
        if (tabs -1==0):
            framed = pygame.image.load("picshop/redframe2.jpg")
            DISPLAYSUF.blit(pygame.transform.scale(framed,(width*400//1300,height*400//800)),pygame.Rect(width*(1/90+1/10),height*(1/4+1/30),0,0))
            DISPLAYSUF.blit(pygame.transform.scale(imgbox,(width*400//1300,height*400//800)),pygame.Rect(width*(1/90+1/10),height*(1/4+1/30),0,0))
            inchuoi("$"+str(moneyspell[0][0]),width*(1/3+1/30),height*(5/7+1/30),12,40)  
            pygame.draw.rect(DISPLAYSUF,duckgreen,(width*(1/9),height*(8/10+1/150),width*(5/17+1/100),height*(1/15)))
            pygame.draw.rect(DISPLAYSUF,darkyellow,(width*(1/9),height*(8/10+1/150),width*(5/40+1/30-1/9),height*(1/15)))
            pygame.draw.rect(DISPLAYSUF,darkyellow,(width*(1/2-1/8-1/150),height*(8/10+1/150),width*(5/40+1/30-1/9),height*(1/15)))
            pygame.draw.rect(DISPLAYSUF,yellow,(width*(1/9),height*(8/10+1/150),width*(5/40+1/30-1/9),height*(1/15)),4)
            pygame.draw.rect(DISPLAYSUF,yellow,(width*(1/2-1/8-1/150),height*(8/10+1/150),width*(5/40+1/30-1/9),height*(1/15)),4)
            inchuoi("-",width*(1/2-1/3-1/45),height*(8/10+6/150),5,50)
            inchuoi("+",width*(1/2-1/10+1/300),height*(8/10+6/150),5,50)
            inchuoi(str(countmaxsad),width*(1/2-1/10+1/300+1/2-1/3-1/45)/2,height*(8/10+6/150),3,50) 
            if countmaxsad !=0 : 
                pygame.draw.rect(DISPLAYSUF,duckgreen,(width*(1/2-1/10+1/50),height*(8/10+1/150),width*(5/40+1/30-1/9),height*(1/15)))
                pygame.draw.rect(DISPLAYSUF,lime,(width*(1/2-1/10+1/50),height*(8/10+1/150),width*(5/40+1/30-1/9),height*(1/15)),4)
                inchuoi("o",width*(1/2-1/10+1/18),height*(8/10+6/150),13,50)
        
            
            
    def but(x=1,y=1,xm=1,ym=1):
        if buyspell[tabs-1][spellchose] >=1:
            framed = pygame.image.load("picshop/redframe2sec.jpg")
            DISPLAYSUF.blit(pygame.transform.scale(framed,(width*207//1300,height*165//800)),pygame.Rect(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10),0,0))
            '''
            pygame.draw.rect(DISPLAYSUF,blue,(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10),width*(5/40+1/30),height*(1/6+1/100+1/80+1/80)),4)
            pygame.draw.rect(DISPLAYSUF,duckgreen,(width*(x/32 + 1/90+1/120),height*(1.75*y/10 + 1/17+1/10+1/250),width*(5/40+1/30-1/500),height*(1/6+1/100+1/80-1/200+1/80)))
            pygame.draw.rect(DISPLAYSUF,blue,(width*(x/32 + 1/90+1/150),height*(1.75*y/10 + 1/17+1/10),width*(5/40+1/30),height*(1/7+1/150)),4)
            '''
            inchuoi("$"+str(moneyspell[tabs-1][spellchose]),width*(x/32 +1/90+1/6-1/50),height*(1.75*y/10+1/4 +1/12),12,20)
            '''
            if tabs -1 ==0:
                    ghep = str('picshop/')+picture[spellchose]
                    imagek = pygame.image.load(ghep)
                    DISPLAYSUF.blit(pygame.transform.scale(imagek,(width*80//1300,height*87//800)),pygame.Rect(width*(x/32 + 1/90+1/30+1/40)//1,height*(1.75*y/10 + 1/17+1/10+1/20)//1,120,20))
            '''
            ghep = picture2[spellchose]
            imagek = pygame.image.load(ghep)
            DISPLAYSUF.blit(pygame.transform.scale(imagek,(width*80//1300,height*87//800)),pygame.Rect(width*(x/32 + 1/90+1/30+1/40)//1,height*(1.75*y/10 + 1/17+1/10+1/20)//1,120,20))    
            pygame.draw.rect(DISPLAYSUF,black,(xm,ym,width*(1/5),height*(1/5)))
            pygame.draw.rect(DISPLAYSUF,metalyellow,(xm,ym,width*(1/5),height*(1/5)),3)
            inchuoi(namespell[tabs-1][spellchose],xm+width*(1/6+1/100),ym+height*(1/80+1/80),3,20)
            inchuoi("Price: ",xm+width*(1/12),ym+height*(1/80+1/80+1/35),9,20)
            inchuoi("$"+str(moneyspell[tabs-1][spellchose]),xm+width*(1/6+1/100),ym+height*(1/80+1/80+1/35),5,20)

    def clary():
        DISPLAYSUF.fill(white)
        #scale ảnh sáchsách
        DISPLAYSUF.blit(pygame.transform.scale(imgbook,(widthxmas,heightxmas)),pygame.Rect(0,0,120,20))
        DISPLAYSUF.blit(pygame.transform.scale(imgarrow,(width*75//1300,height*75//800)),pygame.Rect(width*23//1300,0,0,0))
    def mouseclick(x=1,y=1,w=1,h=1,chose = 1):
        Xchose =-1
        Ychose =-1
        
        if chose==1:
            #inchuoi(str(x)+' '+str(y),100,100,5,20)
            if (y>=(232*h)//800) and (y<=(395*h)//800):
                if (x>=(184*w)//1300) and (x<=(390*w)//1300): 
                    Xchose =0
                    Ychose =0
                if (x>=(426*w)//1300) and (x<=(633*w)//1300):
                    Xchose =1
                    Ychose =0
                if (x>=(711*w)//1300) and (x<=(920*w)//1300):
                    Xchose =2
                    Ychose =0
                if (x>=(956*w)//1300) and (x<=(1160*w)//1300):
                    Xchose =3
                    Ychose =0        
            if (y>=(477*h)//800) and (y<=(642*h)//800):
                if (x>=(184*w)//1300) and (x<=(390*w)//1300):
                    Xchose =0
                    Ychose =1
                if (x>=(426*w)//1300) and (x<=(633*w)//1300):
                    Xchose =1
                    Ychose =1
                if (x>=(711*w)//1300) and (x<=(920*w)//1300):
                    Xchose =2
                    Ychose =1
                if (x>=(956*w)//1300) and (x<=(1160*w)//1300):
                    Xchose =3
                    Ychose =1    
            return Xchose,Ychose 
        elif chose==2:
            #for events in pygame.event.get():
                if (y>=(438*h)//800) and (y<=(479*h)//800):
                    if (x>=(184*w)//1300) and (x<=(229*w)//1300): 
                        Xchose =0
                        Ychose =0
                    if (x>=(426*w)//1300) and (x<=(473*w)//1300):
                        Xchose =1
                        Ychose =0
                    if (x>=(711*w)//1300) and (x<=(758*w)//1300):
                        Xchose =2
                        Ychose =0
                    if (x>=(956*w)//1300) and (x<=(1001*w)//1300):
                        Xchose =3
                        Ychose =0        
                elif (y>=(718*h)//800) and (y<=(760*h)//800):
                    if (x>=(184*w)//1300) and (x<=(229*w)//1300): 
                        Xchose =0
                        Ychose =1
                    if (x>=(426*w)//1300) and (x<=(473*w)//1300):
                        Xchose =1
                        Ychose =1
                    if (x>=(711*w)//1300) and (x<=(758*w)//1300):
                        Xchose =2
                        Ychose =1
                    if (x>=(956*w)//1300) and (x<=(1001*w)//1300):
                        Xchose =3
                        Ychose =1
                return Xchose, Ychose 
        elif chose==3:
        # for events in pygame.event.get():
                if (y>=(438*h)//800) and (y<=(479*h)//800):
                    if (x>=(342*w)//1300) and (x<=(389*w)//1300): 
                        Xchose =0
                        Ychose =0
                    if (x>=(588*w)//1300) and (x<=(633*w)//1300):
                        Xchose =1
                        Ychose =0
                    if (x>=(872*w)//1300) and (x<=(917*w)//1300):
                        Xchose =2
                        Ychose =0
                    if (x>=(1115*w)//1300) and (x<=(1161*w)//1300):
                        Xchose =3
                        Ychose =0        
                elif (y>=(718*h)//800) and (y<=(760*h)//800):
                    if (x>=(342*w)//1300) and (x<=(389*w)//1300): 
                        Xchose =0
                        Ychose =1
                    if (x>=(588*w)//1300) and (x<=(633*w)//1300):
                        Xchose =1
                        Ychose =1
                    if (x>=(872*w)//1300) and (x<=(917*w)//1300):
                        Xchose =2
                        Ychose =1
                    if (x>=(1115*w)//1300) and (x<=(1161*w)//1300):
                        Xchose =3
                        Ychose =1    
                return Xchose, Ychose
    def mouseclickex(x=1,y=1,h=1,w=1):
            et= False
            if (y>=(9*h)//800) and (y<=(65*h)//800):
                if (x>=(32*w)//1300) and (x<=(90*w)//1300):
                    et = True
            return et
    def tabschage(x=1,y=1,w=1,h=1):
        noak=0
        if (y>=(189*h)//800 ) and (y<=(220*h)//800):
            if (x>=(184*w)//1300) and (x<=(229*w)//1300):
                noak =1
            if (x>=(250*w)//1300) and (x<=(293*w)//1300):
                noak =2
            if (x>=(315*w)//1300) and (x<=(358*w)//1300):
                noak =3
            if (x>=(380*w)//1300) and (x<=(422*w)//1300):
                noak =4
        return noak
    def pageschage(x=1,y=1,w=1,h=1):
        drecta =0
        if(y>=(298*h)//800) and ( y<=(367*h)//800):
            if (x>=(65*w)//1300) and (x<=(142*w)//1300):
                drecta =-1
            if (x>=(1190*w)//1300) and (x<=(1268*w)//1300):
                drecta = 1
        return drecta
    def magic(x=1,y=1,w=1,h=1):
        kals = 0
        if(y>=(643*h)//800) and ( y<=(700*h)//800):
            if (x>=(144*w)//1300) and (x<=(206*w)//1300):
                kals =-1
            if (x>=(476*w)//1300) and (x<=(540*w)//1300):
                kals = 1
            if (x>=(545*w)//1300) and (x<=(608*w)//1300):
                kals = 2
        return kals
    def magic2(x=1,y=1,slas=0): # x+1/10  y +1/6 
        framed = pygame.image.load("picshop/redframe2.jpg")
        DISPLAYSUF.blit(pygame.transform.scale(framed,(width*100//1300,height*100//800)),pygame.Rect(width*(1/2+x/10),height*(1/4+1/30+y/6),0,0))
        ghep = str('picshop/')+picture[slas]
        imagek = pygame.image.load(ghep)
        DISPLAYSUF.blit(pygame.transform.scale(imagek,(width*80//1300,height*80//800)),pygame.Rect(width*(1/2+1/120+x/10),height*(1/4+1/30+1/70+y/6),0,0))
        inchuoi("+" +str(slspell[slas]),width*(1/2+1/14+x/10),height*(1/4+1/20+y/6),1,25)
        inchuoi("AIB: "+str(buyspell[0][slas]-1),width*(1/2+1/13+x/10),height*(1/4+1/6+1/200+y/6),9,20)
    def inputf(_id):
        os.system("cls")
        filetes= open('data/ '+_id,"r")
        money = int(filetes.readline())
        line = filetes.readline()
        las=line.split(" ")
        if not ((line==" ") | (line =="\n")| (line == "")): 
            for i in range(0,len(las)-1):
                buyspell[0][i] += int(las[i])
    # while True:
        for i in range(1,4):
            line=filetes.readline()
            if (line==" ") | (line =="\n")| (line == ""): 
                break
            las=line.split(" ")
            for j in range(0,len(buyspell[i])):
                buyspell[i][j]=int(las[j])
        return money
    def outputf():
        fileout = open('data/ '+_id,"w+")
        fileout.write(str(money))
        fileout.write("\n")
        for j in range(0,len(buyspell[0])):
            fileout.write(str(buyspell[0][j]-1)+" ")
        fileout.write("\n")
        for i in range(1,maxtabs):
            for j in range(0,len(buyspell[i])):
                if buyspell[i][j] == 0:
                    fileout.write("0")
                else:
                    fileout.write("1")
                fileout.write(" ")
            fileout.write(" \n")
        fileout.close
    buttonback =0
    sospell=0 
    mx=0    
    my=0
    soluong=1
    value = 0
    buybua=0
    needfile =True
    bjia=0
    '''
    s=True
    playsound("shop.mp3",s)
    '''
    while True:
        if (needfile==True):
            money = inputf(_id)
            needfile = False
        if len(namespell[tabs-1]) % 8 !=0 :
            maxpages = len(namespell[tabs-1])//8+1
        else:
            maxpages = len(namespell[tabs-1])//8
        #pygame.time.delay(20)
        clary() 
        
        if ((buttonback == 0) & ( sospell >0)): sospell -=8
        check =0  
        sospell = 8*(pages-1)
        if (sospell <= len(namespell[tabs-1])-1):    
            for i in range(0,len(lst)):
                if (check==1): break
            # if (sospell == len(namespell[tabs-1])-1)|((sospell % 8) ==0): break
                for j in range(0,len(lst2)):
                    if (((sospell % 8) ==0)): 
                        showps(lst2[0],lst[0],tabs,maxpages)
                        if (sospell < len(namespell[tabs-1])-1): sospell +=1
                    elif (i!=0)|(j!=0): 
                        #if (sospell < len(namespell[tabs-1])-1): sospell +=1
                    # continue
                        showps(lst2[j],lst[i],tabs,maxpages)
                        if (sospell == len(namespell[tabs-1])-1): 
                            check=1
                            break
                        sospell +=1
        inchuoi("FILTERS",width*(1/7+1/25),height*(2/7-1/16),9,15)
        show = str("$"+str(money))
        inchuoi(show,width*(2/7),height*(2/7-1/9),5,20)
        inchuoi("MONEY",width*(2/7-1/100),height*(2/7-1/7),9,15)
        if (tabs-1 ==0):
            show = str(" - $"+str(countmaxsad*moneyspell[0][0]))
            inchuoi(show,width*(2/7+1/10),height*(2/7-1/9),9,20)
        #inchuoi("Pages: "+str(pages),width,height//9,1,20)
        #inchuoi("Tabs "+str(tabs),width,height//7 ,1,20)
        #but(lst2[Xchose],lst[Ychose])
        #spellchose = Xchose + Ychose *4 +(pages-1)*8
        #mx,my = pygame.mouse.get_pos()
        #inchuoi(str(mx)+' '+str(my),100,100,5,20)
        if (tabs-1!=0):
            mx,my = pygame.mouse.get_pos()
            Xchose,Ychose = mouseclick(mx,my,width,height,1)
            spellchose = Xchose + Ychose *4 +(pages-1)*8
            if (Xchose>=0) and(Ychose>=0):
                if (spellchose < len(buyspell[tabs-1])):
                    but(lst2[Xchose],lst[Ychose],mx,my)
        
        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                width= DISPLAYSUF.get_width()
                height = 800 * width // 1300
                DISPLAYSUF= pygame.display.set_mode((width,height),HWSURFACE|DOUBLEBUF|RESIZABLE)
                '''
            if event.type == pygame.KEYDOWN:
            
                if ((event.key == pygame.K_PAGEUP) & (tabs + 1 <= maxtabs)) :
                    tabs +=1
                    buttonback=0
                    sospell =0 
                    pages=1
                elif ((event.key == pygame.K_PAGEDOWN) & (tabs - 1 >= 1)) :
                    tabs -=1 
                    buttonback=0
                    sospell =0
                    pages=1
                
                if ((event.key == pygame.K_r) & ((pages + 1 <= maxpages) | (sospell < len(namespell[tabs-1])-1 ))) :
                    pages +=1
                    buttonback=1
                elif ((event.key == pygame.K_l) & (pages - 1 >= 1 )&( sospell >=0)) :
                    pages -=1 
                    buttonback =0
            
                if event.key == pygame.K_ESCAPE:
                    outputf()
                    pygame.quit()
                '''
            if event.type == pygame.QUIT:
                outputf()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mcl.play()
                mx,my = pygame.mouse.get_pos()
                if (mouseclickex(my,mx,width,height) == True):
                    outputf()
                    return 10
                if (pageschage(mx,my,width,height)==1) &((pages + 1 <= maxpages) | (sospell < len(namespell[tabs-1])-1 )):
                    pages +=1
                    buttonback=1
                if (pageschage(mx,my,width,height)==-1) & (pages - 1 >= 1 )&( sospell >=0):
                    pages -=1 
                    buttonback =0
                if (tabschage(mx,my,width,height)!=0):
                    tabs = tabschage(mx,my,width,height)
                    buttonback=0
                    sospell =0 
                    pages=1
                Xchose,Ychose =mouseclick(mx,my,width,height,1)
                if (tabs-1 !=0):
                  if (Xchose>=0) and(Ychose>=0):
                    spellchose = Xchose + Ychose *4 +(pages-1)*8
                    if (spellchose < len(buyspell[tabs-1])):
                        if buyspell[tabs-1][spellchose] == 1 :
                            if (money >= moneyspell[tabs-1][spellchose]):
                                buysound.play()
                                buyspell[tabs-1][spellchose]=0
                                money -=moneyspell[tabs-1][spellchose]
                else: 
                    ckl=magic(mx,my,width,height)
                    if (countmaxsad-1>= 0 ) &(ckl ==-1 ):
                        countmaxsad -=1
                    if (((countmaxsad +1 )*moneyspell[0][0]) <= money )&(ckl == 1):
                        countmaxsad +=1
                    if (countmaxsad !=0 ) & (ckl ==2 ):
                        buysound.play()
                        money -= countmaxsad*moneyspell[0][0]
                        for z in range(0,countmaxsad):
                            opa = random.randint(1,len(namespell[0]))
                            slspell[opa-1]+=1
                            xla=0
                            yla=0
                        for i in range(0,len(slspell)):
                            buyspell[0][i] += slspell[i]
                            if slspell[i] !=0:
                                magic2(xla,yla,i)
                                xla +=1 
                            if (xla ==4):
                                xla =0
                                yla +=1
                            slspell[i]=0
                        countmaxsad = 0 
                        pygame.display.flip()
                        pygame.time.wait(4000)
                        

                '''
                else:
                    value =0
                    Xchoses, Ychoses =mouseclick(mx,my,width,height,2)
                    spellcoute = Xchoses + Ychoses*4 + (pages -1 )*8
                    if (Xchoses>=0) & (Ychoses >=0):
                        if (slspell[spellcoute]>0):
                            slspell[spellcoute] -=1
                    Xchoses,Ychoses = mouseclick(mx,my,width,height,3)
                    if (Xchoses>=0) & (Ychoses >=0):  
                        for i in range(0,len(slspell)):
                            value += slspell[i]*moneyspell[0][i]
                        if value + moneyspell[0][Xchoses +Ychoses*4 + (pages-1)*8] <= money:
                            slspell[Xchoses +Ychoses*4 + (pages-1)*8] +=1
                    value = 0
                    for i in range(0,len(slspell)):
                        value += slspell[i]*moneyspell[0][i]
                    if (my>=(478*height)//800) and (my<=(534*height)//800):
                        if(mx>=(1168*width)//1300) and (mx<=(1288*width)//1300):
                        if  value <=money:
                            buysound.play()
                            money -= value
                            for i in range(0,len(slspell)):
                                buyspell[0][i] += slspell[i]
                                slspell[i]=0
                            value = 0
                '''
                
        pygame.display.flip()   
def inputfgams(idll=""):
        global line,line2,dickt,dickt2
        os.system("cls")
        filetes= open("data/ "+ idll,"r")
        money = int(filetes.readline())
        line = filetes.readline()
        line2 = filetes.readline()
        filetes.close
        dickt = line.split(" ")
        dickt2=line2.split(" ")
        return money
def outputfgams(money="",_id=""):
    fileout = open('data/ '+_id ,"w+")
    fileout.write(str(money))
    fileout.write('\n')
    fileout.write(dickt[0]+" "+dickt[1]+" "+dickt[2]+" \n")
    fileout.write(line2)
    fileout.close
def ranDom_Kind_Pos_Obstacle(select):
    KindOfObstacle = 0
    PostionOfObstacle = 0
    if(select==1):
        KindOfObstacle = random.randint(1,7)
        PostionOfObstacle = random.randrange(200,700,50)
    elif(select==2):
        KindOfObstacle = random.randint(1,7)
        PostionOfObstacle = random.randrange(200,700,50)
    elif(select==3):
        KindOfObstacle = random.randint(1,7)
        PostionOfObstacle = random.randrange(200,700,50)
    elif(select==4):
        KindOfObstacle = random.randint(1,7)
        PostionOfObstacle = random.randrange(200,700,50)
    elif(select==5):
        KindOfObstacle = random.randint(1,7)
        PostionOfObstacle = random.randrange(200,700,50)
    return KindOfObstacle,PostionOfObstacle
def ranDom_speed_Car(select):
    randSpeed = 0
    if(select == 1): # vận tốc xe người chơi bằng một nửa vận tốc các xe còn lại
        randSpeed_Main_Player = random.randint(1,4)
        if(randSpeed_Main_Player == 1):
            randSpeed = 0.22
        elif(randSpeed_Main_Player == 2):
            randSpeed = 0.25
        elif(randSpeed_Main_Player == 3):
            randSpeed = 0.2
        elif(randSpeed_Main_Player == 4):
            randSpeed = 0.18
    elif(select == 2):
        randSpeed_Player = random.randint(1,4)
        if(randSpeed_Player == 1):
            randSpeed = 0.28
        elif(randSpeed_Player == 2):
            randSpeed = 0.24
        elif(randSpeed_Player == 3):
            randSpeed = 0.16
        elif(randSpeed_Player == 4):
            randSpeed = 0.2
    elif(select == 3):
        randSpeed_Player = random.randint(1,4)
        if(randSpeed_Player == 1):
            randSpeed = 0.24
        elif(randSpeed_Player == 2):
            randSpeed = 0.3
        elif(randSpeed_Player == 3):
            randSpeed = 0.17
        elif(randSpeed_Player == 4):
            randSpeed = 0.2
    elif(select == 4):
        randSpeed_Player = random.randint(1,4)
        if(randSpeed_Player == 1):
            randSpeed = 0.26
        elif(randSpeed_Player == 2):
            randSpeed = 0.22
        elif(randSpeed_Player == 3):
            randSpeed = 0.18
        elif(randSpeed_Player == 4):
            randSpeed = 0.2
    elif(select == 5):
        randSpeed_Player = random.randint(1,4)
        if(randSpeed_Player == 1):
            randSpeed = 0.26
        elif(randSpeed_Player == 2):
            randSpeed = 0.24
        elif(randSpeed_Player == 3):
            randSpeed = 0.21
        elif(randSpeed_Player == 4):
            randSpeed = 0.18
    return randSpeed
           
class Car():
    def __init__(self,kind,size_car,set):
        self.x = 0
        self.surface = kind
        self.surface_1 = kind
        self.sizeCar = size_car
        self.Set = set

    def draw(self,pos):
        self.locate = pos
        if(self.surface == 1 + 5*self.Set):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe1, (self.x,self.locate))#Vẽ xe trên màn hình
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe1_2, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe1_3, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe1_4, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe1_5, (self.x,self.locate))
        elif(self.surface == 26):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe1_1, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe1_2_1, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe1_3_1, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe1_4_1, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe1_5_1, (self.x,self.locate))

        elif(self.surface == 2 + 5*self.Set):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe2, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe2_2, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe2_3, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe2_4, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe2_5, (self.x,self.locate))
        elif(self.surface == 27):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe2_1, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe2_2_1, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe2_3_1, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe2_4_1, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe2_5_1, (self.x,self.locate))

        elif(self.surface == 3 + 5*self.Set):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe3, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe3_2, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe3_3, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe3_4, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe3_5, (self.x,self.locate))
        elif(self.surface == 28):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe3_1, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe3_2_1, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe3_3_1, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe3_4_1, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe3_5_1, (self.x,self.locate))

        elif(self.surface == 4 + 5*self.Set):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe4, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe4_2, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe4_3, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe4_4, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe4_5, (self.x,self.locate))
        elif(self.surface == 29):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe4_1, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe4_2_1, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe4_3_1, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe4_4_1, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe4_5_1, (self.x,self.locate))

        elif(self.surface == 5 + 5*self.Set):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe5, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe5_2, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe5_3, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe5_4, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe5_5, (self.x,self.locate))
        elif(self.surface == 30):
            if(self.Set == 0):
                DISPLAYSURF.blit(Xe5_1, (self.x,self.locate))
            elif(self.Set == 1):
                DISPLAYSURF.blit(Xe5_2_1, (self.x,self.locate))
            elif(self.Set == 2):
                DISPLAYSURF.blit(Xe5_3_1, (self.x,self.locate))
            elif(self.Set == 3):
                DISPLAYSURF.blit(Xe5_4_1, (self.x,self.locate))
            elif(self.Set == 4):
                DISPLAYSURF.blit(Xe5_5_1, (self.x,self.locate))

    def update(self,speed,image = 0,goBack = 0):
        if(goBack == 0):
            self.x += speed
        if(goBack == 1):
            self.x = 0
        if(goBack == 2):
            self.x = WINDOWWIDTH - 50
        if(image == 1 or image == 6 or image == 11 or image == 16 or image == 21 ):
            self.surface = 26
        elif(image == 2 or image == 7 or image == 12 or image == 17 or image == 22):
            self.surface = 27
        elif(image == 3 or image == 8 or image == 13 or image == 18 or image == 23):
            self.surface = 28
        elif(image == 4 or image == 9 or image == 14 or image == 19 or image == 24):
            self.surface = 29
        elif(image == 5 or image == 10 or image == 15 or image == 20 or image == 25):
            self.surface = 30
        elif(image == 0):
            self.surface = self.surface_1
        return [self.x+size_Car,self.x]  
class Background():
    def __init__(self,select):
        self.img1 = BG1
        self.img2 = BG2
        self.img3 = BG3
        self.img5 = BG5
        self.img6 = BG2
        self.img7 = BG7
        self.img8 = BG8
        self.img11 = imaged_1
        self.img12 = imaged_2
        self.img13 = imaged_3
        self.img14 = imaged_4
        self.img15 = imaged_5
        self.chon = select

    def draw(self):
        if(self.chon==3):
            DISPLAYSURF.blit(self.img3,(0,0))
        elif(self.chon==5):
            DISPLAYSURF.blit(self.img5,(0,0))
        elif(self.chon==1):
            DISPLAYSURF.blit(self.img1,(0,0))
        elif(self.chon==6):
            DISPLAYSURF.blit(self.img6,(0,0))
        elif(self.chon==7):
            DISPLAYSURF.blit(self.img7,(0,0))
        elif(self.chon==8):
            DISPLAYSURF.blit(self.img8,(0,0))
        elif(self.chon==2):
            DISPLAYSURF.blit(self.img2,(0,0))
        elif(self.chon==11):
            DISPLAYSURF.blit(self.img11,(0,0))
        elif(self.chon==12):
            DISPLAYSURF.blit(self.img12,(0,0))
        elif(self.chon==13):
            DISPLAYSURF.blit(self.img13,(0,0))
        elif(self.chon==14):
            DISPLAYSURF.blit(self.img14,(0,0))
        elif(self.chon==15):
            DISPLAYSURF.blit(self.img15,(0,0))       
class Obstacle():

    def __init__(self,select):
        self.chon = select

    def draw(self,posX,posY):
        self.locationX = posX
        self.locationY = posY

        if(self.chon==1):
            DISPLAYSURF.blit(obs1, (self.locationX,self.locationY))
            self.size_obstacle = width_obs1
        if(self.chon==2):
            DISPLAYSURF.blit(obs2, (self.locationX,self.locationY))
            self.size_obstacle = width_obs2
        if(self.chon==3):
            DISPLAYSURF.blit(obs3, (self.locationX,self.locationY))
            self.size_obstacle = width_obs3
        if(self.chon==4):
            DISPLAYSURF.blit(obs4, (self.locationX,self.locationY))
            self.size_obstacle = width_obs4
        if(self.chon==5):
            DISPLAYSURF.blit(obs5, (self.locationX,self.locationY))
            self.size_obstacle = width_obs5
        if(self.chon==6):
            DISPLAYSURF.blit(obs6, (self.locationX,self.locationY))
            self.size_obstacle = width_obs6
        if(self.chon==7):
            DISPLAYSURF.blit(obs7, (self.locationX,self.locationY))
            self.size_obstacle = width_obs7
        return [self.locationX,self.locationX+self.size_obstacle]

#Sắp xếp thứ hạng dựa vào thời gian
def Rank_Arrange(b):
    a = list(b)
    c = list(b)
    f1,f2,f3,f4,f5 = 0,0,0,0,0
    f1 = min(a)
    check1 = f1 in a
    while(check1 == True):
        a.remove(f1)
        if(f1 not in a):
            check1 = False
    if(len(a) != 0):
        f2 = min(a)
        check2 = f2 in a
        while(check2 == True):
            a.remove(f2)
            if(f2 not in a):
                check2 = False
    if(len(a) !=0):
        f3 = min(a)
        check3 = f3 in a
        while(check3 == True):
            a.remove(f3)
            if(f3 not in a):
                check3 = False
    if(len(a) !=0):
        f4 = min(a)
        check4 = f4 in a
        while(check4 == True):
            a.remove(f4)
            if(f4 not in a):
                check4 = False
    if(len(a) != 0):
        f5 = a[0]
    if(f1 != 0 and f2 ==0 and f3 == 0 and f4 == 0 and f5 == 0):
        for i in range(5):
            c[i] = 1
    if(f1 != 0 and f2 !=0 and f3 == 0 and f4 == 0 and f5 == 0):
        for i in range(5):
            if(c[i]== f1):
                c[i]=1
            elif(c[i]>=f2):
                c[i]=2
    if(f1 != 0 and f2 !=0 and f3 != 0 and f4 == 0 and f5 == 0):
        for i in range(5):
            if(c[i]== f1):
                c[i]=1
            elif(c[i]==f2):
                c[i]=2
            elif(c[i]>=f3):
                c[i]=3
    if(f1 != 0 and f2 !=0 and f3 != 0 and f4 != 0 and f5 == 0):
        for i in range(5):
            if(c[i]== f1):
                c[i]=1
            elif(c[i]==f2):
                c[i]=2
            elif(c[i]==f3):
                c[i]=3
            elif(c[i]>=f4):
                c[i]=4
    if(f1 != 0 and f2 !=0 and f3 != 0 and f4 != 0 and f5 != 0):
        for i in range(5):
            if(c[i]== f1):
                c[i]=1
            elif(c[i]==f2):
                c[i]=2
            elif(c[i]==f3):
                c[i]=3
            elif(c[i]==f4):
                c[i]=4
            else:
                c[i]=5
    return c
def Money(money):
    font = pygame.font.SysFont('consolas', 30)
    moneySuface = font.render(str(int(money))+'$', True,YELLOW,BLACK)
    DISPLAYSURF.blit(moneySuface, (10,20))


def Time_Display(h1 = '0',h2= '0',m1 = '0',m2= '0',s1= '0',s2= '0',position_X = 0,position_Y= 0,Info = '',adjust = 30,Text_Color = BLACK,Color= 0):
    font = pygame.font.SysFont('consolas', adjust)
    if(Color == 0):
        Time = font.render(Info+': '+h1+''+h2+':'+m1+''+m2+':'+s1+''+s2, True, Text_Color)
    else:
        Time = font.render(Info+': '+h1+''+h2+':'+m1+''+m2+':'+s1+''+s2, True, Text_Color,Color)
    DISPLAYSURF.blit(Time, (position_X, position_Y))
def Convert_Time(localtime,select):
    hour,minute,second = 0,0,0
    result1 = time.strftime("%I", localtime)
    h1 = str((list (str(result1)))[0])
    h2 = str((list (str(result1)))[1])
    result2 = time.strftime("%M", localtime)
    m1 = str((list (str(result2)))[0])
    m2 = str((list (str(result2)))[1])
    result3 = time.strftime("%S", localtime)
    s1 = str((list (str(result3)))[0])
    s2 = str((list (str(result3)))[1])
    if(int(h1)==0 and int(h2) == 0):
        hour = 0
    elif(int(h1) == 0 and int(h2) <= 9):
        hour = int(h2)
    elif(int(h1) > 0):
        hour = int(h1)*10+int(h2)

    if(int(m1) == 0 and int(m2) == 0):
        minute = 0
    elif(int(m1) == 0 and int(m2)>0):
        minute = int(m2)
    elif(int(m1)>0):
        minute = 10*int(m1)+int(m2)

    if(int(s1) == 0 and int(s2) == 0):
        second = 0
    elif(int(s1) == 0 and int(s2) >0):
        second = int(s2)
    elif(int(s1)>0):
        second = 10*int(s1) +int(s2)
    if(select == 1):
        return minute,second # dùng để tính toán liên quan tới thời gian
    elif(select==2):
        return h1,h2,m1,m2,s1,s2 # h1,h2,m1,m2,s1,s2 : dạng chuỗi
def Time_Go(m_end,s_end,m_start,s_start):
    m,s = 0,0
    count_second = 0
    if(s_end < s_start):
        s = (60 - s_start)+ s_end
        if(m_end - m_start >= 1):
            count_second = s + (m_end - m_start -1)*60
    elif(s_end >= s_start):
        s = s_end - s_start
        count_second = s + (m_end - m_start)*60

    if(count_second <= 60):
        m = 0
    elif(count_second > 60):
        m = m_end - m_start
    return m,s,count_second
                     
def Button(Info,x,y,width,height,light_color,color,light_color_text,color_text,select,adjust1 =0,size_font = 25,adjust2 = 0):

    mouse = pygame.mouse.get_pos() #nhận tọa độ của con chuột trên màn hình
    click = pygame.mouse.get_pressed()
    
    if(mouse[0]>=x-width/2 and mouse[0] <= x+width/2 and mouse[1]>=y and mouse[1]<=y+height):
        if(click[0]==True):
            return 1
    #In màu đậm hơn khi con chuột vào ô
    if(mouse[0]>=x-width/2 and mouse[0] <= x+width/2 and mouse[1]>=y and mouse[1]<=y+height):
        pygame.draw.rect(DISPLAYSURF, color, (x-width/2, y, width, height))
        font = pygame.font.SysFont('consolas', size_font)
        Text = font.render(Info, True, color_text)
    else:#In màu nhạt hơn khi con chuột ra khỏi ô
        pygame.draw.rect(DISPLAYSURF, light_color, (x-width/2, y, width, height))
        font = pygame.font.SysFont('consolas', size_font)
        Text = font.render(Info, True, light_color_text)
    if(select == 1):
        DISPLAYSURF.blit(Text, (int(x-79+adjust1), y+10+adjust2))
    elif(select==2):
        DISPLAYSURF.blit(Text, (int(x-33+adjust1), y+10+adjust2))
    elif(select == 3):
        DISPLAYSURF.blit(Text, (int(x-115+adjust1), y+10+adjust2))
def Pause(bg):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                elif event.key ==pygame.K_q:
                    pygame.quit()
                    quit()

        bg.draw()
        font = pygame.font.SysFont('consolas', 30)
        commentSuface = font.render('Nhấn C để tiếp tục hoặc Q để thoát.', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 260))
        pygame.display.update()
        fpsClock.tick(FPS)
def Menu_Button():
    #Button(Info,x,y,width,height,light_color,color,light_color_text,color_text,select,adjust1 =0,size_font = 25,adjust2 = 0)
    a = Button('Start Game',150,WINDOWHEIGHT-300,220,45,LIGHTGRAY,GRAY,BLACK,WHITE,1,6)
    #b = Button('Save/Load Game',150,WINDOWHEIGHT-250,220,45,LIGHTGRAY,GRAY,BLACK,WHITE,3,16)
    c = Button('Settings',150,WINDOWHEIGHT-250,220,45,LIGHTGRAY,GRAY,BLACK,WHITE,1,22)
    d = Button('Store',150,WINDOWHEIGHT-200,220,45,LIGHTGRAY,GRAY,BLACK,WHITE,2,-5)
    e = Button('Quit',150,WINDOWHEIGHT - 150,220,45,LIGHTGRAY,GRAY,BLACK,WHITE,2,4)
    f = Button('=',WINDOWWIDTH - 87,WINDOWHEIGHT - 40,45,30,LIGHTGRAY,GRAY,BLACK,WHITE,2,22,40,-13)# Bảng hướng dẫn
    g = Button('*',WINDOWWIDTH - 32,WINDOWHEIGHT - 40,45,30,LIGHTGRAY,GRAY,BLACK,WHITE,2,22,40,-7) # History
    m = Button('Mini game',WINDOWWIDTH - 60,WINDOWHEIGHT - 80,100,30,LIGHTGRAY,GRAY,BLACK,WHITE,1,33,18,-4)
    #h = Button('Back',WINDOWWIDTH*(15/16)+20,560,50,35,LIGHTGRAY,GRAY,BLACK,WHITE,2,10,21,-4)
    if(a == 1):
        return 1
    if(c == 1):
        return 2
    if(d==1): 
        return 3
    if(m ==1):
        return 4
    if(e == 1):
        outputfgams(money,idll)
        pygame.quit()
        quit()
  
#Xử lí va chạm với bùa/chướng ngại vật
def CollisionObs(car,obstacle):
    if ((int(car[0])<=int(obstacle[0])) and (int(car[1]) <= int(obstacle[1]))) or ((int(car[0])>int(obstacle[0])) and (int(car[1]) > int(obstacle[1]))): #Xử lí khi đầu xe đâm vào chướng ngại vật
        return True
    return False

#Xử lí các giai đoạn trong game:
def Choose_DISPLAYSUFSize(bg):
    size1 = size2 = size3 = 1
    flag = 0
    OK = 1
    back = -1
    kind = 0
    ChooseSize = True
    while ChooseSize:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg.draw()
        font1 = pygame.font.SysFont('consolas', 27)
        if(size1 == 1):
            if(flag == 0):
                SIZE1 = Button('900 x 600',(WINDOWWIDTH/2)-150,WINDOWHEIGHT - 340,120,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,32,20)
            elif(flag != 0):
                SIZE1 = Button('900 x 600',(WINDOWWIDTH/2)-150,WINDOWHEIGHT - 340,120,40,GRAY,GRAY,WHITE,WHITE,1,32,20)
        if(SIZE1 == 1 and flag == 0):
            flag = 1
            size2 = size3 = 0

        if(size2 == 1):
            if(flag == 0):
                SIZE2 = Button('1150 x 600',(WINDOWWIDTH/2)-10,WINDOWHEIGHT - 340,130,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,26,20)
            elif(flag != 0):
                SIZE2 = Button('1150 x 600',(WINDOWWIDTH/2)-10,WINDOWHEIGHT - 340,130,40,GRAY,GRAY,WHITE,WHITE,1,26,20)
        if(SIZE2 == 1 and flag == 0):
            flag = 2
            size1 = size3 = 0

        if(size3 == 1):
            if(flag == 0):
                SIZE3 = Button('Error',(WINDOWWIDTH/2)+135,WINDOWHEIGHT - 340,130,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,21,20)
            elif(flag != 0):
                SIZE3 = Button('Error',(WINDOWWIDTH/2)+135,WINDOWHEIGHT - 340,130,40,GRAY,GRAY,WHITE,WHITE,1,21,20)
        if(SIZE3 == 1 and flag == 0):
            flag = 3
            size1 = size2 = 0

        if(flag != 0 and OK == 1):
            Undo = Button('Undo',50,WINDOWHEIGHT-45,80,40,LIGHTGREEN,BLUE,BLACK,WHITE,2,-2,32,-4)
            if(Undo == 1):
                size1 = size2 = size3 = 1
                flag = 0
        if(OK == 1):
            comment1 = font1.render('Choose your screen size', True,DARKBLUE)
            DISPLAYSURF.blit(comment1, ((WINDOWWIDTH/2)-175,WINDOWHEIGHT - 380))
            f = Button('OK',WINDOWWIDTH-140,WINDOWHEIGHT - 45,70,40,BLUEGRAY,GRAY,BLACK,WHITE,2,15,32,-4)
        if((flag == 1 or flag == 2 or flag == 3) and f == 1):
            OK = 0
            kind = flag

        if(OK == 0):
            NEXT = Button('NEXT',WINDOWWIDTH-50,WINDOWHEIGHT - 45,80,40,BLUEGRAY,GRAY,BLACK,WHITE,2,-2,32,-4)
            if(NEXT == 1 and OK == 0):
                return [flag,flag]
        if(OK == 1):
            BACK = Button('BACK',WINDOWWIDTH-225,WINDOWHEIGHT - 45,80,40,BLUEGRAY,GRAY,BLACK,WHITE,2,-2,32,-4)
            if(BACK == 1):
                return [back,flag]

        pygame.display.update()
        fpsClock.tick(FPS)
def Choose_PlayingCar(bg):
    car1 = car2 = car3 = car4 = car5 = 1
    flag = 0
    OK = 1
    next = -1
    back = 0
    nex = 0
    kind = 0
    ChooseCar = True
    while ChooseCar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg.draw()
        font1 = pygame.font.SysFont('consolas', 27)

        #Button(Info,x,y,width,height,light_color,color,light_color_text,color_text,select,adjust1 =0,size_font = 25,adjust2 = 0)
        if(car1 == 1):
            Name1 = ['Black','Sang','Shark','Bird','WitchP']
            if(nex == 0):
                DISPLAYSURF.blit(Xe1, ((WINDOWWIDTH*(2/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 1):
                DISPLAYSURF.blit(Xe1_2, ((WINDOWWIDTH*(2/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 2):
                DISPLAYSURF.blit(Xe1_3, ((WINDOWWIDTH*(2/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 3):
                DISPLAYSURF.blit(Xe1_4, ((WINDOWWIDTH*(2/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 4):
                DISPLAYSURF.blit(Xe1_5, ((WINDOWWIDTH*(2/9))//1,(WINDOWHEIGHT*(1/3))//1))
            if(flag == 0):
                a = Button(Name1[nex],(WINDOWWIDTH*(4/15))//1,(WINDOWHEIGHT*(13/30))//1,85,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,52,20)
            elif(flag != 0):
                 a = Button(Name1[nex],(WINDOWWIDTH*(4/15))//1,(WINDOWHEIGHT*(13/30))//1,85,40,GRAY,GRAY,WHITE,WHITE,1,52,20)
        if(a == 1 and flag == 0):
            car2 = car3 = car4 = car5 = 0
            if(nex == 0):
                flag += 1
            elif(nex == 1):
                flag += 6
            elif(nex == 2):
                flag += 11
            elif(nex == 3):
                flag += 16
            elif(nex == 4):
                flag += 21

        if(car2 == 1):
            Name2 = ['Silver','Khoa','Ghost','Sonic','WitchG']
            if(nex == 0):
                DISPLAYSURF.blit(Xe2, ((WINDOWWIDTH*(1/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 1):
                DISPLAYSURF.blit(Xe2_2, ((WINDOWWIDTH*(1/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 2):
                DISPLAYSURF.blit(Xe2_3, ((WINDOWWIDTH*(1/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 3):
                DISPLAYSURF.blit(Xe2_4, ((WINDOWWIDTH*(1/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 4):
                DISPLAYSURF.blit(Xe2_5, ((WINDOWWIDTH*(1/3))//1,(WINDOWHEIGHT*(1/3))//1))
            if(flag == 0):
                b = Button(Name2[nex],(WINDOWWIDTH*(17/45))//1,(WINDOWHEIGHT*(13/30))//1,85,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,48,20)
            elif(flag != 0):
                 b = Button(Name2[nex],(WINDOWWIDTH*(17/45))//1,(WINDOWHEIGHT*(13/30))//1,85,40,GRAY,GRAY,WHITE,WHITE,1,48,20)
        if(b == 1 and flag == 0):
            car1 = car3 = car4 = car5 = 0
            if(nex == 0):
                flag += 2
            elif(nex == 1):
                flag += 7
            elif(nex == 2):
                flag += 12
            elif(nex == 3):
                flag += 17
            elif(nex == 4):
                flag += 22

        if(car3 == 1):
            Name3 = ['Blue','Quân','Mummy','Hero','WitchR']
            if(nex == 0):
                DISPLAYSURF.blit(Xe3, ((WINDOWWIDTH*(4/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 1):
                DISPLAYSURF.blit(Xe3_2, ((WINDOWWIDTH*(4/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 2):
                DISPLAYSURF.blit(Xe3_3, ((WINDOWWIDTH*(4/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 3):
                DISPLAYSURF.blit(Xe3_4, ((WINDOWWIDTH*(4/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 4):
                DISPLAYSURF.blit(Xe3_5, ((WINDOWWIDTH*(4/9))//1,(WINDOWHEIGHT*(1/3))//1))
            if(flag == 0):
                c = Button(Name3[nex],(WINDOWWIDTH*(22/45))//1,(WINDOWHEIGHT*(13/30))//1,85,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,56,20)
            elif(flag != 0):
                 c = Button(Name3[nex],(WINDOWWIDTH*(22/45))//1,(WINDOWHEIGHT*(13/30))//1,85,40,GRAY,GRAY,WHITE,WHITE,1,56,20)
        if(c == 1 and flag == 0):
            car1 = car2 = car4 = car5 = 0
            if(nex == 0):
                flag += 3
            elif(nex == 1):
                flag += 8
            elif(nex == 2):
                flag += 13
            elif(nex == 3):
                flag += 18
            elif(nex == 4):
                flag += 23

        if(car4 == 1):
            Name4 = ['Green','Thủy','Fish','Batman','WitchY']
            if(nex == 0):
                DISPLAYSURF.blit(Xe4, ((WINDOWWIDTH*(5/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 1):
                DISPLAYSURF.blit(Xe4_2, ((WINDOWWIDTH*(5/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 2):
                DISPLAYSURF.blit(Xe4_3, ((WINDOWWIDTH*(5/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 3):
                DISPLAYSURF.blit(Xe4_4, ((WINDOWWIDTH*(5/9))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 4):
                DISPLAYSURF.blit(Xe4_5, ((WINDOWWIDTH*(5/9))//1,(WINDOWHEIGHT*(1/3))//1))
            if(flag == 0):
                d = Button(Name4[nex],(WINDOWWIDTH*(3/5))//1,(WINDOWHEIGHT*(13/30))//1,85,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,52,20)
            elif(flag != 0):
                 d = Button(Name4[nex],(WINDOWWIDTH*(3/5))//1,(WINDOWHEIGHT*(13/30))//1,85,40,GRAY,GRAY,WHITE,WHITE,1,52,20)
        if(d == 1 and flag == 0):
            car1 = car2 = car3 = car5 = 0
            if(nex == 0):
                flag += 4
            elif(nex == 1):
                flag += 9
            elif(nex == 2):
                flag += 14
            elif(nex == 3):
                flag += 19
            elif(nex == 4):
                flag += 24

        if(car5 == 1):
            Name5 = ['Pink','Phi','Pica','Goku','WitchB']
            if(nex == 0):
                DISPLAYSURF.blit(Xe5, ((WINDOWWIDTH*(2/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 1):
                DISPLAYSURF.blit(Xe5_2, ((WINDOWWIDTH*(2/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 2):
                DISPLAYSURF.blit(Xe5_3, ((WINDOWWIDTH*(2/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 3):
                DISPLAYSURF.blit(Xe5_4, ((WINDOWWIDTH*(2/3))//1,(WINDOWHEIGHT*(1/3))//1))
            elif(nex == 4):
                DISPLAYSURF.blit(Xe5_5, ((WINDOWWIDTH*(2/3))//1,(WINDOWHEIGHT*(1/3))//1))
            if(flag == 0):
                e = Button(Name5[nex],(WINDOWWIDTH*(32/45))//1,(WINDOWHEIGHT*(13/30))//1,85,40,LIGHTGRAY,GRAY,BLACK,WHITE,1,56,20)
            elif(flag != 0):
                 e = Button(Name5[nex],(WINDOWWIDTH*(32/45))//1,(WINDOWHEIGHT*(13/30))//1,85,40,GRAY,GRAY,WHITE,WHITE,1,56,20)
        if(e == 1 and flag == 0):
            car1 = car2 = car3 = car4 = 0
            if(nex == 0):
                flag += 5
            elif(nex == 1):
                flag += 10
            elif(nex == 2):
                flag += 15
            elif(nex == 3):
                flag += 20
            elif(nex == 4):
                flag += 25

        if(flag != 0 and OK == 1):
            Undo = Button('Undo',50,WINDOWHEIGHT-45,80,40,LIGHTGREEN,BLUE,BLACK,WHITE,2,-2,32,-4)
            if(Undo == 1):
                car1 = car2 = car3 = car4 = car5 = 1
                flag = 0
        if(OK == 1):
            comment1 = font1.render('Choose your own racing car', True,DARKBLUE)
            commentSize1 = comment1.get_size()
            DISPLAYSURF.blit(comment1, ((int((WINDOWWIDTH - commentSize1[0])/2)),(WINDOWHEIGHT*(1/4))//1))
            f = Button('OK',WINDOWWIDTH-140,WINDOWHEIGHT - 45,70,40,BLUEGRAY,GRAY,BLACK,WHITE,2,15,32,-4)
        if(OK == 0):
            comment2 = font1.render('Your car is ready now', True,DARKBLUE)
            commentSize2 = comment2.get_size()
            DISPLAYSURF.blit(comment2, ((int((WINDOWWIDTH - commentSize2[0])/2)),(WINDOWHEIGHT*(1/4))//1))
        if(flag == (1+nex*5)  or flag == (2 + nex*5) or flag == (3 + nex*5) or flag == (4 + nex*5) or flag == (5 + nex*5) )and (f == 1):
            OK = 0
            kind = nex
        NEXT = Button('NEXT',WINDOWWIDTH-50,WINDOWHEIGHT - 45,80,40,BLUEGRAY,GRAY,BLACK,WHITE,2,-2,32,-4)
        if(NEXT == 1 and OK == 0):
            return [flag,next,kind]
        if(OK == 1):
            BACK = Button('BACK',WINDOWWIDTH-225,WINDOWHEIGHT - 45,80,40,BLUEGRAY,GRAY,BLACK,WHITE,2,-2,32,-4)
            if(BACK == 1):
                return [back,next,kind]
        if(OK == 1):
            if(nex == 0):
                Set1 = Button('SET1',80,WINDOWHEIGHT-115,120,30,RED,RED,WHITE,WHITE,2,6,25,-7)
            else:
                Set1 = Button('SET1',80,WINDOWHEIGHT-115,120,30,BLUEGRAY,GRAY,BLACK,WHITE,2,6,25,-7)
            if(nex == 1):
                Set2 = Button('SET2',202,WINDOWHEIGHT-115,120,30,RED,RED,WHITE,WHITE,2,6,25,-7)
            else:
                Set2 = Button('SET2',202,WINDOWHEIGHT-115,120,30,BLUEGRAY,GRAY,BLACK,WHITE,2,6,25,-7)
            if(nex == 2):
                Set3 = Button('SET3',324,WINDOWHEIGHT-115,120,30,RED,RED,WHITE,WHITE,2,6,25,-7)
            else:
                Set3 = Button('SET3',324,WINDOWHEIGHT-115,120,30,BLUEGRAY,GRAY,BLACK,WHITE,2,6,25,-7)
            
            if(nex == 3):
                Set4 = Button('SET4',446,WINDOWHEIGHT-115,120,30,RED,RED,WHITE,WHITE,2,6,25,-7)
            else:
                Set4 = Button('SET4',446,WINDOWHEIGHT-115,120,30,BLUEGRAY,GRAY,BLACK,WHITE,2,6,25,-7)
         
            if(nex == 4):
                Set5 = Button('SET5',568,WINDOWHEIGHT-115,120,30,RED,RED,WHITE,WHITE,2,6,25,-7)
            else:
                Set5 = Button('SET5',568,WINDOWHEIGHT-115,120,30,BLUEGRAY,GRAY,BLACK,WHITE,2,6,25,-7)

            if(Set1 == 1):
                nex = 0
            elif(Set2 == 1):
                nex = 1
            elif(Set3 == 1)&(int(dickt2[0]) == 0):
                nex = 2
            elif(Set4 == 1)&(int(dickt2[1]) == 0):
                nex = 3
            elif(Set5 == 1)&(int(dickt2[2]) == 0):
                nex = 4
        pygame.display.update()
        fpsClock.tick(FPS)
def Buy_Ticket(bg,money):
    flag = 0
    OK = 1
    play = -1
    back = 0
    Money_Copy = money
    Money_Return = money
    Appear1 = Appear2 = Appear3 = Appear4 = Appear5 = 1
    BuyTicket = True
    while BuyTicket:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg.draw()
        Money(Money_Copy)
        font1 = pygame.font.SysFont('consolas', 27)
        font2 = pygame.font.SysFont('consolas', 35)
        commentInstruction1 = font1.render('CHOOSE PLACED PRICE TO PLAY', True,YELLOW,DARKBLUE)
        commentInstruction5 = font1.render('Top|---Bonus---', True,DARKBLUE,YELLOW)
        commentInstruction2 = font1.render(' 1 | Placed x 3', True,DARKBLUE,YELLOW)
        commentInstruction3 = font1.render(' 2 | Placed x 2', True,DARKBLUE,YELLOW)
        commentInstruction4 = font1.render(' 3 | Placed x 1', True,DARKBLUE,YELLOW)

        DISPLAYSURF.blit(commentInstruction1, ((WINDOWWIDTH*(41/180))//1,(WINDOWHEIGHT*(1/6))//1))
        DISPLAYSURF.blit(commentInstruction5, ((WINDOWWIDTH*(13/18))//1,(WINDOWHEIGHT*(13/60))//1))
        DISPLAYSURF.blit(commentInstruction2, ((WINDOWWIDTH*(13/18))//1,(WINDOWHEIGHT*(4/15))//1))
        DISPLAYSURF.blit(commentInstruction3, ((WINDOWWIDTH*(13/18))//1,(WINDOWHEIGHT*(19/60))//1))
        DISPLAYSURF.blit(commentInstruction4, ((WINDOWWIDTH*(13/18))//1,(WINDOWHEIGHT*(11/30))//1))

        #Button(Info,x,y,width,height,light_color,color,light_color_text,color_text,select,adjust1 =0,size_font = 25,adjust2 = 0)
        if(Appear1 == 1):
            comment1 = font2.render('Amateurs', True,WHITE,ORANGE)
            DISPLAYSURF.blit(comment1, ((WINDOWWIDTH*(41/180))//1,160))
            if(flag == 0):
                a = Button('100',(WINDOWWIDTH*(103/180))//1,145,100,70,WHITE,LIGHTBLUE,BLACK,WHITE,1,52,33,10)
            elif(flag != 0):
                 a = Button('100',(WINDOWWIDTH*(103/180))//1,145,100,70,LIGHTBLUE,LIGHTBLUE,WHITE,WHITE,1,52,33,10)
        if(a == 1 and flag == 0):
            Appear2 = Appear3 = Appear4 = Appear5 = 0
            flag += 1
            Money_Copy = Money_Copy - 100

        if(Appear2 == 1):
            comment2 = font2.render('Beginner', True,WHITE,ORANGE)
            DISPLAYSURF.blit(comment2, ((WINDOWWIDTH*(41/180))//1,240))
            if(flag == 0):
                b = Button('200',(WINDOWWIDTH*(103/180))//1,220,100,70,WHITE,GREEN,BLACK,WHITE,1,52,33,10)
            elif(flag != 0):
                 b = Button('200',(WINDOWWIDTH*(103/180))//1,220,100,70,GREEN,GREEN,WHITE,WHITE,1,52,33,10)
        if(b == 1 and flag == 0):
            Appear1 = Appear3 = Appear4 = Appear5 = 0
            flag += 2
            Money_Copy = Money_Copy - 200

        if(Appear3 == 1):
            comment3 = font2.render('Intermediate', True,WHITE,ORANGE)
            DISPLAYSURF.blit(comment3, ((WINDOWWIDTH*(41/180))//1,315))
            if(flag == 0):
                c = Button('500',(WINDOWWIDTH*(103/180))//1,295,100,70,WHITE,ORANGE,BLACK,WHITE,1,52,33,10)
            elif(flag != 0):
                 c = Button('500',(WINDOWWIDTH*(103/180))//1,295,100,70,ORANGE,ORANGE,WHITE,WHITE,1,52,33,10)
        if(c == 1 and flag == 0):
            Appear1 = Appear2 = Appear4 = Appear5 = 0
            flag += 3
            Money_Copy = Money_Copy - 500

        if(Appear4 == 1):
            comment4 = font2.render('Expert', True,WHITE,ORANGE)
            DISPLAYSURF.blit(comment4, ((WINDOWWIDTH*(41/180))//1,390))
            if(flag == 0):
                d = Button('1000',(WINDOWWIDTH*(103/180))//1,370,100,70,WHITE,PURPLE,BLACK,WHITE,1,43,33,10)
            elif(flag != 0):
                 d = Button('1000',(WINDOWWIDTH*(103/180))//1,370,100,70,PURPLE,PURPLE,WHITE,WHITE,1,43,33,10)
        if(d == 1 and flag == 0):
            Appear1 = Appear2 = Appear3 = Appear5 = 0
            flag += 4
            Money_Copy = Money_Copy - 1000

        if(Appear5 == 1):
            comment5 = font2.render('Super-Expert', True,WHITE,ORANGE)
            DISPLAYSURF.blit(comment5, ((WINDOWWIDTH*(41/180))//1,465))
            if(flag == 0):
                e = Button('2000',(WINDOWWIDTH*(103/180))//1,445,100,70,WHITE,RED,BLACK,WHITE,1,43,33,10)
            elif(flag != 0):
                 e = Button('2000',(WINDOWWIDTH*(103/180))//1,445,100,70,RED,RED,WHITE,WHITE,1,43,33,10)
        if(e == 1 and flag == 0):
            Appear1 = Appear2 = Appear3 = Appear4 = 0
            flag += 5
            Money_Copy = Money_Copy - 2000

        if(flag != 0 and OK == 1):
            Undo = Button('Undo',50,WINDOWHEIGHT-45,80,40,LIGHTGREEN,BLUE,BLACK,WHITE,2,-2,32,-4)
            if(Undo == 1):
                Appear1 = Appear2 = Appear3 = Appear4 = Appear5 = 1
                Money_Copy = Money_Return
                flag = 0
        if(OK == 1):
            f = Button('OK',WINDOWWIDTH-140,WINDOWHEIGHT - 45,70,40,BLUEGRAY,GRAY,BLACK,WHITE,2,15,32,-4)
        if(flag == 1 and f == 1) or (flag == 2 and f == 1) or (flag == 3 and f == 1) or (flag == 4 and f == 1) or (flag == 5 and f == 1):
            OK = 0
        PLAY = Button('PLAY',WINDOWWIDTH-50,WINDOWHEIGHT - 45,80,40,BLUEGRAY,GRAY,BLACK,WHITE,2,-2,32,-4)
        if(PLAY == 1 and OK == 0):
            return [flag,play]
        if(OK == 1):
            BACK = Button('BACK',WINDOWWIDTH-225,WINDOWHEIGHT - 45,80,40,BLUEGRAY,GRAY,BLACK,WHITE,2,-2,32,-4)
            if(BACK == 1):
                return [back,play]
        pygame.display.update()
        fpsClock.tick(FPS)
def Before_PlayGame(bg):
    stop_DISPLAYSUF = True
    while stop_DISPLAYSUF:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    stop_DISPLAYSUF = False
        bg.draw()
        font = pygame.font.SysFont('consolas', 30)
        waitingSuface = font.render('Press "space" to play game', True,RED)
        commentSize = waitingSuface.get_size()
        DISPLAYSURF.blit(waitingSuface, (int((WINDOWWIDTH - commentSize[0])/2), 260))
        pygame.display.update()
        fpsClock.tick(FPS)
def Game_Menu(bg,money):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.draw()
        Money(money)
        Menu_Button()
        if(Menu_Button() == 1):
            return 1
        elif(Menu_Button() == 2):
            return 2
        elif(Menu_Button()==3):
            return 3
        elif(Menu_Button()==4):
            return 4
        pygame.display.update()
def Game_Over(bg,rank,NamePlayer):
    GameOver = True
    while GameOver:
        turn = 0
        Name = list(NamePlayer)
        top1 = top2 = top3 = top4 = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.draw()
        EXIT= Button('EXIT',(WINDOWWIDTH*(49/60))//1,(WINDOWHEIGHT*(37/40))//1,80,40,GREEN,BLUE,BLACK,WHITE,2,-2,32,-4)
        if(EXIT == 1):
            return 0
        while(turn<=4):
            font = pygame.font.SysFont('consolas', 18)
            if(rank[turn] == 1):
                player1 = font.render(Name[turn], True, WHITE)
                textSize1 = player1.get_size()
                DISPLAYSURF.blit(player1, (int((WINDOWWIDTH - textSize1[0])/2), ((WINDOWHEIGHT*(7/40))//1)+((WINDOWHEIGHT*(1/30))//1)*top1))
                top1 += 1
                turn += 1
            elif(rank[turn] == 2):
                player2 = font.render(Name[turn], True, WHITE)
                textSize2 = player2.get_size()
                DISPLAYSURF.blit(player2, (int((WINDOWWIDTH - textSize2[0])/2), ((WINDOWHEIGHT*(53/120))//1)+((WINDOWHEIGHT*(1/30))//1)*top2))
                top2 += 1
                turn += 1
            elif(rank[turn] == 3):
                player3 = font.render(Name[turn], True, WHITE)
                textSize3 = player3.get_size()
                DISPLAYSURF.blit(player3, (int((WINDOWWIDTH - textSize3[0])/2), ((WINDOWHEIGHT*(27/40))//1)+((WINDOWHEIGHT*(1/30))//1)*top3))
                top3 += 1
                turn += 1
            elif(rank[turn] == 4):
                player4 = font.render(Name[turn], True, WHITE)
                textSize4 = player4.get_size()
                DISPLAYSURF.blit(player4, (int((WINDOWWIDTH - textSize4[0])/2), ((WINDOWHEIGHT*(64/75))//1)+((WINDOWHEIGHT*(1/24))//1)*top4))
                turn += 1
                top4 += 1
            elif(rank[turn] == 5):
                player5 = font.render(Name[turn], True, WHITE)
                textSize5 = player5.get_size()
                DISPLAYSURF.blit(player5, (int((WINDOWWIDTH - textSize5[0])/2), ((WINDOWHEIGHT*(179/200))//1)))
                turn += 1

        pygame.display.update()
        fpsClock.tick(FPS)
def Game_Play(car1,car2,car3,car4,car5,time_Start,bg4,randSelect1,randSelect2,Car1,Car2,Car3,Car4,Car5,NamePlayer): 
    #Ngẫu nhiên vị trí xuất phát của xe trên màn hình theo trục Y:
    Position_Car = [(WINDOWHEIGHT*(53/600))//1,(WINDOWHEIGHT*(37/150))//1,(WINDOWHEIGHT*(5/12))//1,(WINDOWHEIGHT*(7/12))//1,(WINDOWHEIGHT*(89/120))//1]
    PositionY_Car1 = Position_Car[random.randint(0,4)]
    Position_Car.remove(PositionY_Car1)
    PositionY_Car2 = Position_Car[random.randint(0,3)]
    Position_Car.remove(PositionY_Car2)
    PositionY_Car3 = Position_Car[random.randint(0,2)]
    Position_Car.remove(PositionY_Car3)
    PositionY_Car4 = Position_Car[random.randint(0,1)]
    Position_Car.remove(PositionY_Car4)
    PositionY_Car5 = Position_Car[0]

    #Khai báo loại chướng ngại vật, vị trí chướng ngại vật mỗi xe.
    a1,a = ranDom_Kind_Pos_Obstacle(1)
    b1,b = ranDom_Kind_Pos_Obstacle(2)
    c1,c = ranDom_Kind_Pos_Obstacle(3)
    d1,d = ranDom_Kind_Pos_Obstacle(4)
    e1,e = ranDom_Kind_Pos_Obstacle(5)

    #Khai báo tốc độ xe chạy trong game:
    randSpeed1 = ranDom_speed_Car(1)
    randSpeed2 = ranDom_speed_Car(2)
    randSpeed3 = ranDom_speed_Car(3)
    randSpeed4 = ranDom_speed_Car(4)
    randSpeed5 = ranDom_speed_Car(5)

    obss1 = Obstacle(a1)
    obss2 = Obstacle(b1)
    obss3 = Obstacle(c1)
    obss4 = Obstacle(d1)
    obss5 = Obstacle(e1)

    speed1 = randSpeed1
    spd1 = randSpeed1
    speed2 = randSpeed2
    spd2 = randSpeed2
    speed3 = randSpeed3
    spd3 = randSpeed3
    speed4 = randSpeed4
    spd4 = randSpeed4
    speed5 = randSpeed5
    spd5 = randSpeed5

    Acce,lock,punch,bonus = 0,0,0,0
    AccelerateSpeed = 0
    a2 = b2 = c2 = d2 = e2 = 0

    Select1 = Select2 = Select3 = 0 
    Selection = [1,2,3,4,5]
    Select1 = Selection[random.randint(0,4)]
    Selection.remove(Select1)
    Select2 = Selection[random.randint(0,3)]
    Selection.remove(Select2)
    Select3 = Selection[random.randint(0,2)]

    support = random.randint(0,2)

    Back_Speed = -0.5
    Slow_Speed = 0.05
    Time_Pause = 4
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    Pause(bg1)
        m_Cal,s_Cal= Convert_Time(time_Start,1)
        bg4.draw()
        if(car1.update(speed1)[1] > 100 and speed1 > 0 and a2 == 0 and (Select1 == 1 or Select2 == 1)):
            obss_Car1 = obss1.draw(a,PositionY_Car1)
        if(car2.update(speed2)[1] > 100 and speed2 > 0 and b2 == 0 and (Select1 == 2 or Select2 == 2)):
            obss_Car2 = obss2.draw(b,PositionY_Car2)
        if(car3.update(speed3)[1] > 100 and speed3 > 0 and c2 == 0 and (Select1 == 3 or Select2 == 3)):
            obss_Car3 = obss3.draw(c,PositionY_Car3)
        if(car4.update(speed4)[1] > 100 and speed4 > 0 and d2 == 0 and (Select1 == 4 or Select2 == 4)):
            obss_Car4 = obss4.draw(d,PositionY_Car4)
        if(car5.update(speed5)[1] > 100 and speed5 > 0 and e2 == 0 and (Select1 == 5 or Select2 == 5)):
            obss_Car5 = obss5.draw(e,PositionY_Car5)

        #--------      --------      --------   Xe 1   --------      --------         --------   
        time_All = time.localtime()
        mCal,sCal= Convert_Time(time_All,1)
        while (speed1 != 0 and a2 == 0):
            time_Stop1 = time.localtime()
            m_1_Stop,s_1_Stop= Convert_Time(time_Stop1,1)
            m1,s1,S1_Cal = Time_Go(m_1_Stop,s_1_Stop,m_Cal,s_Cal)
            break
        m1,s1,check_S1 = Time_Go(mCal,sCal,m_Cal,s_Cal)
        goBack1 = 0
        check_time1 = False
        if((Select1 == 1 or Select2 == 1) and speed1 > 0 and car1.update(speed1)[1] > 102):
            if(a1 == 4 and a2 == 0 and speed1 > 0):
                if CollisionObs(car1.update(speed1),obss_Car1) == False:
                    speed1 = Back_Speed
                    a2 = 1
            elif(a1 == 2):
                if CollisionObs(car1.update(speed1),obss_Car1) == False:
                    speed1 = 0
                    a2 = 1
            elif(a1 == 5):
                if CollisionObs(car1.update(speed1),obss_Car1) == False:
                    speed1 += 0.3
                    a2 = 1
            elif(a1 == 6 and a2 == 0):
                if CollisionObs(car1.update(speed1),obss_Car1) == False:
                    goBack1 = 1
                    speed1 = randSpeed1
                    a2 = 1
            elif(a1 == 7 and a2 == 0):
                if CollisionObs(car1.update(speed1),obss_Car1) == False:
                    speed1 = Back_Speed
                    a2 = 1
            elif(a1 == 1 and a2 == 0):
                if CollisionObs(car1.update(speed1),obss_Car1) == False:
                    goBack1 = 2
                    speed1 = randSpeed1
                    a2 = 1
            elif(a2 == 0):
                if CollisionObs(car1.update(speed1),obss_Car1) == False:
                    speed1 = Slow_Speed
                else:
                    speed1 = spd1
        if(car1.update(speed1)[1]<0 or ((check_S1 > S1_Cal + Time_Pause) and speed1 == 0)):
            speed1 = spd1
        while (int(car1.update(speed1)[1]) <= WINDOWWIDTH - 60):
            time_End = time.localtime()
            h_1,h_2,m_1,m_2,s_1,s_2 = Convert_Time(time_End,2)
            m_1_Cal,s_1_Cal= Convert_Time(time_End,1)
            break
        #--------      --------      --------   Xe 2   --------      --------         --------  
        while (speed2 != 0 and b2 == 0):
            time_Stop2 = time.localtime()
            m_2_Stop,s_2_Stop= Convert_Time(time_Stop2,1)
            m1,s1,S2_Cal = Time_Go(m_2_Stop,s_2_Stop,m_Cal,s_Cal)
            break
        m1,s1,check_S2 = Time_Go(mCal,sCal,m_Cal,s_Cal)
        goBack2 = 0
        check_time2 = False
        if((Select1 == 2 or Select2 == 2) and speed2 > 0 and car2.update(speed2)[1] > 102):
            if(b1 == 4 and b2 == 0 and speed2 > 0):
                if CollisionObs(car2.update(speed2),obss_Car2) == False:
                    speed2 = Back_Speed
                    b2 = 1
            elif(b1 == 2):
                if CollisionObs(car2.update(speed2),obss_Car2) == False:
                    speed2 = 0
                    b2 = 1
            elif(b1 == 5):
                if CollisionObs(car2.update(speed2),obss_Car2) == False:
                    speed2 += 0.3
                    b2 = 1
            elif(b1 == 6 and b2 == 0):
                if CollisionObs(car2.update(speed2),obss_Car2) == False:
                    goBack2 = 1
                    speed2 = randSpeed2
                    b2 = 1
            elif(b1 == 7 and b2 == 0):
                if CollisionObs(car2.update(speed2),obss_Car2) == False:
                    speed2 = Back_Speed
                    b2 = 1
            elif(b1 == 1 and b2 == 0):
                if CollisionObs(car2.update(speed2),obss_Car2) == False:
                    goBack2 = 2
                    speed2 = randSpeed2
                    b2 = 1
            elif(b2 == 0):
                if CollisionObs(car2.update(speed2),obss_Car2) == False:
                    speed2 = Slow_Speed
                else:
                    speed2 = spd2
        if(car2.update(speed2)[1]<0 or ((check_S2 > S2_Cal + Time_Pause) and speed2 == 0)):
            speed2 = spd2
        while (int(car2.update(speed2)[1]) <= WINDOWWIDTH - 60):
            time_End = time.localtime()
            h_1_2,h_2_2,m_1_2,m_2_2,s_1_2,s_2_2 = Convert_Time(time_End,2)
            m_2_Cal,s_2_Cal= Convert_Time(time_End,1)
            break
        ##--------      --------      --------   Xe 3   --------      --------         --------
        while (speed3 != 0 and c2 == 0):
            time_Stop3 = time.localtime()
            m_3_Stop,s_3_Stop= Convert_Time(time_Stop3,1)
            m1,s1,S3_Cal = Time_Go(m_3_Stop,s_3_Stop,m_Cal,s_Cal)
            break
        m1,s1,check_S3 = Time_Go(mCal,sCal,m_Cal,s_Cal)
        goBack3 = 0
        check_time3 = False
        if((Select1 == 3 or Select2 == 3) and speed3 > 0 and car3.update(speed3)[1] > 102):
            if(c1 == 4 and c2 == 0 and speed3 > 0):
                if CollisionObs(car3.update(speed3),obss_Car3) == False:
                    speed3 = Back_Speed
                    c2 = 1
            elif(c1 == 2):
                if CollisionObs(car3.update(speed3),obss_Car3) == False:
                    speed3 = 0
                    c2 = 1
            elif(c1 == 5):
                if CollisionObs(car3.update(speed3),obss_Car3) == False:
                    speed3 += 0.3
                    c2 = 1
            elif(c1 == 6 and c2 == 0):
                if CollisionObs(car3.update(speed3),obss_Car3) == False:
                    goBack3 = 1
                    speed3 = randSpeed3
                    c2 = 1
            elif(c1 == 7 and c2 == 0):
                if CollisionObs(car3.update(speed3),obss_Car3) == False:
                    speed3 = Back_Speed
                    c2 = 1
            elif(c1 == 1 and c2 == 0):
                if CollisionObs(car3.update(speed3),obss_Car3) == False:
                    goBack3 = 2
                    speed3 = randSpeed3
                    c2 = 1
            elif(c2 == 0):
                if CollisionObs(car3.update(speed3),obss_Car3) == False:
                    speed3 = Slow_Speed
                else:
                    speed3 = spd3
        if(car3.update(speed3)[1]<0 or ((check_S3 > S3_Cal + Time_Pause) and speed3 == 0)):
            speed3 = spd3
        while (int(car3.update(speed3)[1]) <= WINDOWWIDTH - 60):
            time_End = time.localtime()
            h_1_3,h_2_3,m_1_3,m_2_3,s_1_3,s_2_3 = Convert_Time(time_End,2)
            m_3_Cal,s_3_Cal= Convert_Time(time_End,1)
            break
        ##--------      --------      --------   Xe 4   --------      --------         --------  
        while (speed4 != 0 and d2 == 0):
            time_Stop4 = time.localtime()
            m_4_Stop,s_4_Stop= Convert_Time(time_Stop4,1)
            m1,s1,S4_Cal = Time_Go(m_4_Stop,s_4_Stop,m_Cal,s_Cal)
            break
        m1,s1,check_S4 = Time_Go(mCal,sCal,m_Cal,s_Cal)
        goBack4 = 0
        check_time4 = False
        if((Select1 == 4 or Select2 == 4) and speed4 > 0 and car4.update(speed4)[1] > 102):
            if(d1 == 4 and d2 == 0 and speed4 > 0):
                if CollisionObs(car4.update(speed4),obss_Car4) == False:
                    speed4 = Back_Speed
                    d2 = 1
            elif(d1 == 2):
                if CollisionObs(car4.update(speed4),obss_Car4) == False:
                    speed4 = 0
                    d2 = 1
            elif(d1 == 5):
                if CollisionObs(car4.update(speed4),obss_Car4) == False:
                    speed4 += 0.3
                    d2 = 1
            elif(d1 == 6 and d2 == 0):
                if CollisionObs(car4.update(speed4),obss_Car4) == False:
                    goBack4 = 1
                    speed4 = randSpeed4
                    d2 = 1
            elif(d1 == 7 and d2 == 0):
                if CollisionObs(car1.update(speed4),obss_Car4) == False:
                    speed4 = Back_Speed
                    d2 = 1
            elif(d1 == 1 and d2 == 0):
                if CollisionObs(car4.update(speed4),obss_Car4) == False:
                    goBack4 = 2
                    speed4 = randSpeed4
                    d2 = 1
            elif(d2 == 0):
                if CollisionObs(car4.update(speed4),obss_Car4) == False:
                    speed4 = Slow_Speed
                else:
                    speed4 = spd4
        if(car4.update(speed4)[1]<0 or ((check_S4 > S4_Cal + Time_Pause) and speed4 == 0)):
            speed4 = spd4
        while (int(car4.update(speed4)[1]) <= WINDOWWIDTH - 60):
            time_End = time.localtime()
            h_1_4,h_2_4,m_1_4,m_2_4,s_1_4,s_2_4 = Convert_Time(time_End,2)
            m_4_Cal,s_4_Cal= Convert_Time(time_End,1)
            break
        ##--------      --------      --------   Xe 5   --------      --------         --------  
        while (speed5 != 0 and e2 == 0):
            time_Stop5 = time.localtime()
            m_5_Stop,s_5_Stop= Convert_Time(time_Stop5,1)
            m1,s1,S5_Cal = Time_Go(m_5_Stop,s_5_Stop,m_Cal,s_Cal)
            break
        m1,s1,check_S5 = Time_Go(mCal,sCal,m_Cal,s_Cal)
        goBack5 = 0
        check_time5 = False
        if((Select1 == 5 or Select2 == 5) and speed5 > 0 and car5.update(speed5)[1] > 102):
            if(e1 == 4 and e2 == 0 and speed5 > 0):
                if CollisionObs(car5.update(speed5),obss_Car5) == False:
                    speed5 = Back_Speed
                    e2 = 1
            elif(e1 == 2):
                if CollisionObs(car5.update(speed5),obss_Car5) == False:
                    speed5 = 0
                    e2 = 1
            elif(e1 == 5):
                if CollisionObs(car5.update(speed5),obss_Car5) == False:
                    speed5 += 0.3
                    e2 = 1
            elif(e1 == 6 and e2 == 0):
                if CollisionObs(car5.update(speed5),obss_Car5) == False:
                    goBack5 = 1
                    speed5 = randSpeed5
                    e2 = 1
            elif(e1 == 7 and e2 == 0):
                if CollisionObs(car5.update(speed5),obss_Car5) == False:
                    speed5 = Back_Speed
                    e1 = 1
            elif(e1 == 1 and e2 == 0):
                if CollisionObs(car5.update(speed5),obss_Car5) == False:
                    goBack5 = 2
                    speed5 = randSpeed5
                    e2 = 1
            elif(e2 == 0):
                if CollisionObs(car5.update(speed5),obss_Car5) == False:
                    speed5 = Slow_Speed
                else:
                    speed5 = spd5
        if(car5.update(speed5)[1]<0 or ((check_S5 > S5_Cal + Time_Pause) and speed5 == 0)):
            speed5 = spd5
        while (int(car5.update(speed5)[1]) <= WINDOWWIDTH - 60):
            time_End = time.localtime()
            h_1_5,h_2_5,m_1_5,m_2_5,s_1_5,s_2_5 = Convert_Time(time_End,2)
            m_5_Cal,s_5_Cal= Convert_Time(time_End,1)
            break
        ##--------      --------      --------          --------      --------         --------

        font = pygame.font.SysFont('consolas', 20)
        waitingSuface = font.render('<'+NamePlayer[0]+'>', True,WHITE)
        commentSize = waitingSuface.get_size()
        DISPLAYSURF.blit(waitingSuface, (car1.update(speed1)[1], PositionY_Car1-13))
        if(speed1 >= 0):
            car1.update(speed1,0,goBack1)
        elif(speed1 < 0):
            car1.update(speed1,Car1)
        if(speed2 >= 0):
            car2.update(speed2,0,goBack2)
        elif(speed2 < 0):
            car2.update(speed2,Car2)
        if(speed3 >= 0):
            car3.update(speed3,0,goBack3)
        elif(speed3 < 0):
            car3.update(speed3,Car3)
        if(speed4 >= 0):
            car4.update(speed4,0,goBack4)
        elif(speed4 < 0):
            car4.update(speed4,Car4)
        if(speed5 >= 0):
            car5.update(speed5,0,goBack5)
        elif(speed5 < 0):
            car5.update(speed5,Car5)
        car1.draw(PositionY_Car1)
        car2.draw(PositionY_Car2)
        car3.draw(PositionY_Car3)
        car4.draw(PositionY_Car4)
        car5.draw(PositionY_Car5)
        #-----#------#------#------#------#------#------#-----#------#-----#----#----#------#-----#------#-----#----#----#
        
        #-----#------#------#------#------#------#------#-----#------#-----#----#----#------#-----#------#-----#----#----#
        
        if (int(dickt[0])>=1):
          if(Acce<3 and speed1 > 0 and support == 0):
            Accelerate = Button('Accelerate',(WINDOWWIDTH*(7/12))//1,(WINDOWHEIGHT*(37/40))//1,115,40,GREEN,BLUE,BLACK,WHITE,2,-20,20,0)
            if(Accelerate == 1):
                Acce +=1
                speed1 += 0.1
                spd1 += 0.1
                dickt[0] = str(int(dickt[0])-1)
        #Bonus = Button('Bonus$',WINDOWWIDTH*(3/4)-50,WINDOWHEIGHT - 45,70,40,YELLOW,BLUE,BLACK,WHITE,2,2,20,0)
        if (int(dickt[1])>=1):
          if(lock <1 and support == 1):
            Lock = Button('Lock',(WINDOWWIDTH*(7/12))//1,(WINDOWHEIGHT*(37/40))//1,70,40,RED,BLUE,YELLOW,WHITE,2,10,20,0)
            if(Lock == 1):
                speed2 = speed3 = speed4 = speed5 = 0
                lock += 1
                dickt[1] = str(int(dickt[1])-1)
        if (int(dickt[2])>=1):
          if(support == 2 and speed1 > 0):
            Break = Button('Break',(WINDOWWIDTH*(7/12))//1,(WINDOWHEIGHT*(37/40))//1,70,40,GRAY,BLUE,BLACK,WHITE,2,5,20,0)
            if(Break == 1 and (Select1 == 1 or Select2 == 1)):
                if(Select1 == 1):
                    Select1 = Select3
                elif(Select2 == 1):
                    Select2 = Select3
                speed1 = spd1
                dickt[2] = str(int(dickt[2])-1)

        if(int(car1.update(speed1)[1]) > WINDOWWIDTH - 60):
            check_time1 = True
            Time_Display(h_1,h_2,m_1,m_2,s_1,s_2,50,PositionY_Car1+20,'Finish',20,WHITE)
            m1_go,s1_go,check_second_1 = Time_Go(m_1_Cal,s_1_Cal,m_Cal,s_Cal)

        if(int(car2.update(speed2)[1]) > WINDOWWIDTH - 60):
            check_time2 = True
            Time_Display(h_1_2,h_2_2,m_1_2,m_2_2,s_1_2,s_2_2,50,PositionY_Car2+20,'Finish',20,WHITE)
            m2_go,s2_go,check_second_2 = Time_Go(m_2_Cal,s_2_Cal,m_Cal,s_Cal)

        if(int(car3.update(speed3)[1]) > WINDOWWIDTH - 60):
            check_time3 = True
            Time_Display(h_1_3,h_2_3,m_1_3,m_2_3,s_1_3,s_2_3,50,PositionY_Car3+20,'Finish',20,WHITE)
            m3_go,s3_go,check_second_3 = Time_Go(m_3_Cal,s_3_Cal,m_Cal,s_Cal)

        if(int(car4.update(speed4)[1]) > WINDOWWIDTH - 60):
            check_time4 = True
            Time_Display(h_1_4,h_2_4,m_1_4,m_2_4,s_1_4,s_2_4,50,PositionY_Car4+20,'Finish',20,WHITE)
            m4_go,s4_go,check_second_4 = Time_Go(m_4_Cal,s_4_Cal,m_Cal,s_Cal)

        if(int(car5.update(speed5)[1]) > WINDOWWIDTH - 60):
            check_time5 = True
            Time_Display(h_1_5,h_2_5,m_1_5,m_2_5,s_1_5,s_2_5,50,PositionY_Car5+20,'Finish',20,WHITE)
            m5_go,s5_go,check_second_5 = Time_Go(m_5_Cal,s_5_Cal,m_Cal,s_Cal)

        rank1,rank2,rank3,rank4,rank5 = 0,0,0,0,0
        if(check_time1 == True and check_time2 == True and check_time3 == True and check_time4 == True and check_time5 == True):
            rank = Rank_Arrange([check_second_1,check_second_2,check_second_3,check_second_4,check_second_5])
            rank1,rank2,rank3,rank4,rank5 = int(rank[0]),int(rank[1]),int(rank[2]),int(rank[3]),int(rank[4])
            Next = Button('Next',WINDOWWIDTH*(3/4)+175,WINDOWHEIGHT - 45,80,40,GREEN,BLUE,BLACK,WHITE,2,-2,32,-4)
            if(Next == 1):
                return [True,rank1,rank2,rank3,rank4,rank5]
        pygame.display.update()
        fpsClock.tick(FPS)       
def Main_Game(idll):
    global WINDOWWIDTH,WINDOWHEIGHT
    w,h = 900,600
    money = inputfgams(idll)
    Placed_Money = 0
    kind = 0
    tiale=0
    while True:
        if(kind == 0):
            bg1 =Background(1)
            bg2 = Background(2)
            bg3 = Background(3)
            bg4 = Background(8)
            bg5 = Background(5)
        if(kind == 1):
            bg1 =Background(11)
            bg2 = Background(12)
            bg3 = Background(13)
            bg4 = Background(15)
            bg5 = Background(14)

        Car1 = 1
        Set = 0
        Play = Game_Menu(bg1,money)
        def InChoseSize():
            nonlocal kind,h,w
            ChoseSize = True
            while ChoseSize:
                a = Choose_DISPLAYSUFSize(bg2)
                if(a[0] == -1):
                    ChoseSize = False
                elif(a[1] == 1):
                    w = 900
                    h = 600
                    ChoseSize = False
                    kind = 0
                elif(a[1] == 2):
                    w = 1150
                    h = 650
                    ChoseSize = False
                    kind = 1
        kla= idll.split(".")
        Player = kla[0]
        NamePlayer=[Player,'Team LEAD','Team TESTER','Team DEV','Team B.A']
        
        if (Play ==4)&(int(money)<=2000) :   
            pygame.mixer.init()
            pygame.mixer.music.load('login.mp3')
            pygame.mixer.music.play(-1)
            outputfgams(money,idll)
            DISPLAYSURF = pygame.display.set_mode((500, 500))
            ks=pygame.image.load("kals.png")
            DISPLAYSURF.blit(pygame.transform.scale(ks,(500, 500)),pygame.Rect(0,0,120,20))
            while True:
                tiale+=1
                if (minigame1(idll,tiale) ==100) or(tiale==5):
                   money = inputfgams(idll)
                   break
        if Play ==3 :
            outputfgams(money,idll)
            while True:
               if store(idll) ==10:
                   money = inputfgams(idll)
                   break
        if(Play == 2):
            InChoseSize()
        WINDOWWIDTH = w
        WINDOWHEIGHT = h
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        In_BuyTicket = False

        if(Play == 1):
            ChooseCar = True
            while ChooseCar and money > 0:
                a = Choose_PlayingCar(bg2)
                Set = a[2]
                if(a[0] == 0):
                    ChooseCar = False
                elif(a[0] == 1 +5*Set):
                    ChooseCar = False
                    Car1 = 1 +5*Set
                    if(a[1] == -1):
                        In_BuyTicket = True
                elif(a[0] == 2 +5*Set):
                    ChooseCar = False
                    Car1 = 2 +5*Set
                    if(a[1] == -1):
                        In_BuyTicket = True
                elif(a[0] == 3 +5*Set):
                    ChooseCar = False
                    Car1 = 3 +5*Set
                    if(a[1] == -1):
                        In_BuyTicket = True
                elif(a[0] == 4 +5*Set):
                    ChooseCar = False
                    Car1 = 4 +5*Set
                    if(a[1] == -1):
                        In_BuyTicket = True
                elif(a[0] == 5 +5*Set):
                    ChooseCar = False
                    Car1 = 5 +5*Set
                    if(a[1] == -1):
                        In_BuyTicket = True

        num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        Car2 = Car3 = Car4 = Car5 = 0
        if(Car1 != 0):
            num.remove(Car1)
        if(Car1 >= 1 and Car1 <= 5):
            Car2,Car3,Car4,Car5 = num[0],num[1],num[2],num[3]
        elif(Car1 >= 6 and Car1 <= 10):
            Car2,Car3,Car4,Car5 = num[5],num[6],num[7],num[8]
        elif(Car1 >= 11 and Car1 <= 15):
            Car2,Car3,Car4,Car5 = num[10],num[11],num[12],num[13]
        elif(Car1 >= 16 and Car1 <= 20):
            Car2,Car3,Car4,Car5 = num[15],num[16],num[17],num[18]
        elif(Car1 >= 17 and Car1 <= 25):
            Car2,Car3,Car4,Car5 = num[20],num[21],num[22],num[23]
        PlyGame = False
        while In_BuyTicket and money > 0:
            a = Buy_Ticket(bg3,money) #a[0] là flag, a[1] là Play
            if(a[0] == 0):
                In_BuyTicket = False
            elif(a[0] == 1):
                money = money - 100
                In_BuyTicket = False
                if(a[1] == -1):
                    Placed_Money = 100
                    PlyGame = True
            elif(a[0] == 2):
                money = money - 200
                In_BuyTicket = False
                if(a[1] == -1):
                    Placed_Money = 200
                    PlyGame = True
            elif(a[0] == 3):
                money = money - 500
                In_BuyTicket = False
                if(a[1] == -1):
                    Placed_Money = 500
                    PlyGame = True
            elif(a[0] == 4):
                money = money - 1000
                In_BuyTicket = False
                if(a[1] == -1):
                    Placed_Money = 1000
                    PlyGame = True
            elif(a[0] == 5):
                money = money - 2000
                In_BuyTicket = False
                if(a[1] == -1):
                    Placed_Money = 2000
                    PlyGame = True

        In_StarGame = PlyGame
        while In_StarGame == 1:
            pygame.mixer.init()
            pygame.mixer.music.load('racing.mp3')
            pygame.mixer.music.play(-1)
            Before_PlayGame(bg2)
            Entry_Play_Game = In_StarGame
            while Entry_Play_Game == True:
                rank1 = rank2 = rank3 = rank4 = rank5 = 0
                time_Start = time.localtime()
                randSelect1 = random.randint(1,5)
                select = [1,2,3,4,5]
                select.remove(randSelect1)
                randSelect2 = int(select[random.randint(0,3)])
                car1 = Car(Car1,80,Set)
                car2 = Car(Car2,80,Set)
                car3 = Car(Car3,80,Set)
                car4 = Car(Car4,80,Set)
                car5 = Car(Car5,80,Set)
                rank = Game_Play(car1,car2,car3,car4,car5,time_Start,bg4,randSelect1,randSelect2,Car1,Car2,Car3,Car4,Car5,NamePlayer)
                check = bool(rank[0])
                rank_1,rank_2,rank_3,rank_4,rank_5 = int(rank[1]),int(rank[2]),int(rank[3]),int(rank[4]),int(rank[5])
                if(rank_1 == 1):
                    vicsound=pygame.mixer.Sound('vic1.mp3')
                    vicsound.play()
                    money = money + Placed_Money*3
                elif(rank_1 == 2):
                    vicsound=pygame.mixer.Sound('vic1.mp3')
                    vicsound.play()
                    money = money + Placed_Money*2
                elif(rank_1 == 3):
                    vicsound=pygame.mixer.Sound('vic1.mp3')
                    vicsound.play()
                    money = money + Placed_Money*1
                elif(rank_1 == 4 or rank_1 == 5):
                    money = money + Placed_Money*0
                if(check == True):
                    GoOut = check
                    while GoOut:
                        o = int(Game_Over(bg5,[rank_1,rank_2,rank_3,rank_4,rank_5],NamePlayer))
                        if(o == 0):
                            GoOut,Entry_Play_Game,In_StarGame = False,False,False

if __name__== "__main__":
    jakc = dangnhap()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    Main_Game(jakc)


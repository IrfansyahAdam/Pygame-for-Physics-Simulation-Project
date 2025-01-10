#mulai

#import modul
import pygame, sys, math
from pygame.locals import *
pygame.init()

#setting tampilan
window = pygame.display.set_mode((1200,600))
pygame.display.set_caption("simulasi gerak parabola")

#inisialisasi warna
putih = (255,255,255)
biru = [110,190,230]
kuning = [249,199,8]
hitam = ( 0, 0, 0)
merah = (255, 0, 0)
coklat = (165, 42, 42)

#mendefinisikan variabel waktu program
clock = pygame.time.Clock()

#mendefinisikan variabel
h     = 40
pos_x = 335
pos_y = 418
pos_xl= 0
t = 0
v_0 = 0
theta = 0
g = 9.8
posxkur = 0
posykur = 0
aq = 0
pencet = True
kecepatan = 0
surface = pygame.Surface((1200,600))
surface = surface.convert_alpha()
surface.fill((0,0,0,0))
size = 15
v0_x = v_0 * math.cos(math.radians(theta))
v0_y = v_0 * math.sin(math.radians(theta))
y_maxl = 0
t_ymax = 0
v_y    = v0_y

#menetapkan variabel untuk keluar program
run = True

#membuat fungsi memutar gambar
def putar_gambar(gambar, sudut):
    cover_gambar         = gambar.get_rect ()
    putar                = pygame.transform.rotate(gambar, sudut)
    putar_cover          = cover_gambar.copy()
    putar_cover.center   = putar.get_rect () .center
    putar                = putar.subsurface(putar_cover).copy()
    return putar

#program utama
while run:

#mendapatkan posisi
    for event in pygame.event.get() :

#membuat kondisi untuk keluar program
        if event.type == pygame.QUIT:
            run = False
    
#mendapatkan posisi kursor dan klik
    kursor = pygame.mouse.get_pos ()
    klik   = pygame.mouse.get_pressed()

#mengatur warna layar
    window.fill (putih)
    background = pygame.image.load ('background.png')
    window.blit(background,  [0,0])

#membuat bola
    pygame.draw.circle(window, kuning, [pos_x,pos_y-h],6)

#menampilkan gambar
    pygame.draw.rect(window,putih, [970,60,200,200])
    badan_pistol = pygame.image.load('pistol.png')
    orang = pygame.image.load('orang.png')
    window.blit(putar_gambar(badan_pistol, theta),[300,395-h])
    window.blit (orang, [130, 400-h])
    pygame.draw.rect(window, kuning, [975,65,20,20])
    pygame.draw.rect(window, kuning, [975,90,20,20])
    pygame.draw.polygon(window, hitam, ((984,68), (977,82), (992,82)))    
    pygame.draw.polygon(window, hitam, ((992,93), (977,93), (984,107)))
    pygame.draw.rect(window, kuning, [975,115,20,20])
    pygame.draw.rect(window, kuning, [975,140,20,20])
    pygame.draw.polygon(window, hitam, ((984,118), (977,132), (992,132)))
    pygame.draw.polygon(window, hitam, ((992,143), (977,143), (984,157)))
    font1 = pygame.font.Font(None,20)
    font2 = pygame.font.Font(None,50)
    Kecepatan_awal = font1.render("kecepatan awal = "+str(kecepatan),True,hitam)
    H_awal = font1.render("Tinggi awal = "+str(h),True,hitam)
    X_max = font1.render ("X max = "+str(pos_xl),True, hitam)
    Y_max = font1.render ("Y max = "+str(y_maxl),True,hitam )
    T = font1.render("waktu total = "+str(t), True,hitam)
    T_max = font1.render("waktu pada Y max ="+str(t_ymax), True,hitam)
    window.blit(Kecepatan_awal,[1000,80])
    window.blit(H_awal,[1000,130])
    tombol_play     = pygame.image.load('tombol_play.png')
    window.blit(tombol_play,[1050,10])
    sudut = font1.render("Sudut Elevasi =" +str(theta),True, hitam)
    keterangan = font2.render("Tekan spasi untuk memulai simulasi kembali.",True,putih)
    window.blit(sudut,[1000,180])
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] :
        aq = 0
        pos_x = 335
        pos_y = 418
        v_0 = 0
        v_y = 0
        v0_x = 0

#gerak mulut pistol
    if 400 > kursor [0] > 300 and 480- h > kursor[1] > 350 - h:
        if klik[0] :
            posx2 = kursor[0] - posxkur
            posy2 = kursor[1] - posykur

            a = posy2 or posx2
            theta -= a
            if theta > 90 :
                theta = 90
            if theta < 0:
                theta = 0

#menambah kecepatan
    if 975 + 20 > kursor[0] > 975 and 65 + 20 > kursor[1] > 65:
        if klik[0]:
            kecepatan += 5

#mengurangi kecepatan
    if 975 + 20 > kursor[0] > 975 and 90 + 20 > kursor[1] > 90:
        if klik[0]:
            kecepatan -= 5
            if kecepatan <= 0:
                kecepatan = 0

#menambah tinggi
    if 975 + 20 > kursor[0] > 975 and 115 + 20 > kursor[1] > 115:
        if klik[0]:
            h += 5
            if h >= 225:
                h = 225

#mengurangi tinggi 
    if 975 + 20 > kursor[0] > 975 and 140 + 20 > kursor[1] > 140:
        if klik[0]:
            h -= 5
            if h <= 40:
                h = 40

#tembak
    if 1050 + 120 > kursor[0] > 1050 and 10 + 50 > kursor[1] > 10:
        if klik[0]:
            if pencet == True:
                v_0   = kecepatan
                aq    = 1
                v0_x  = v_0 * math.cos(math.radians(theta))
                v0_y  = v_0 * math.sin(math.radians(theta))
                y_max = v_0**2*math.sin(math.radians(theta))**2/(2*g)
                x_terjauh = v_0**2*math.sin(math.radians(2*theta))/(2*g)
                t_ymax = round(x_terjauh/v0_x,2)
                y_maxl = round(y_max,2)
                v_y    = v0_y

#gerak
    if aq == 1:
        v_y   = v_y - g
        t = t+1

    pos_x = pos_x + v0_x
    pos_y = pos_y - v_y

    if aq == 2:
        v_0 = 0
        pos_x = pos_x
        pos_xl = round(pos_x,2)
        pos_y = pos_y
        v_y = 0
        v0_x = 0
        window.blit(X_max,[1000,170])
        window.blit(Y_max,[1000,185])
        window.blit(T,[1000,200])
        window.blit(T_max,[1000,215])
        window.blit(keterangan,[50,550])
    if pos_y - h >= 550:
        aq = 2
        window.blit
    posxkur = kursor[0]
    posykur = kursor[1]

#mengupdate tampilan
    pygame.display.flip()
    
#mengatur kecepatan program
    clock.tick(24)

#keluar program
pygame.quit()


                        





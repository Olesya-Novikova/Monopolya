# -*- coding: utf8 -*- 
import pygame
import os
import random

def load_image(name):
    fullname = os.path.join('monopolya_images', name)
    image = pygame.image.load(fullname)
    return image
    
class Pole(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)
        self.screen = screen
        self.image = load_image("pole.png")
        self.rect = self.image.get_rect()
        self.rect.x = (1000 - self.rect.w) // 2
        self.rect.y = 120
    
    def update(self):
        pygame.draw.line(self.screen, (0, 0, 0), (self.rect.x, 0), (self.rect.x, 650), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.rect.x + self.rect.w, 0), (self.rect.x + self.rect.w, 650), 3)

class Knopki(pygame.sprite.Sprite):
    def __init__(self, group, name, screen):
        super().__init__(group)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.name = name
        if name == 'kubik.png':
            self.rect.x = (1000 - self.rect.w) // 2
            self.rect.y = 10
            self.f = pygame.font.SysFont('Arial', 18)
            self.text = self.f.render('Выпало:', True, (0, 0, 0))
            self.screen.blit(self.text, (self.rect.x, self.rect.h + 10))
        elif self.name == 'konec.png':
            self.rect.x = (1000 - self.rect.w) // 2
            self.rect.y = pole.rect.y - 55
        elif self.name == 'kupit.png':
            self.rect.x = pole.rect.x + 160
            self.rect.y = pole.rect.y + 340
        elif self.name == 'net.png':
            
            self.rect.x = pole.rect.x + 160
            self.rect.y = pole.rect.y + 390
        elif self.name == 'Иди.png':
            self.rect.x = pole.rect.x + 160
            self.rect.y = pole.rect.y + 340
        elif self.name == 'poluc.png':
            self.rect.x = pole.rect.x + 160
            self.rect.y = pole.rect.y + 340            
        else:
            self.rect.x = pole.rect.x + 210
            self.rect.y = pole.rect.y + 340
        self.f3 = pygame.font.SysFont('Arial', 18)
        self.text3 = self.f3.render('', True, (0, 0, 0))
    
    def update(self):
        global knop, flag
        if self.name == 'kubik.png':
            self.screen.blit(self.text, (self.rect.x, self.rect.h + 10))
        elif self.name == 'vhod.png' and not flag:
            self.screen.blit(self.text3, (pole.rect.x + 700, pole.rect.y + 450))
        elif self.name == 'Иди.png' or self.name == 'poluc.png':
            if hod == 1:
                self.screen.blit(og.text, (pole.rect.x + 5, pole.rect.y - 20))
            else:
                self.screen.blit(tb.text, (pole.rect.x + 5, pole.rect.y - 20))
            
    
    def do(self, pos):
        global brosil, hod, a, kazna1, kazna2, knop, screen, kartochki, y1, x1, y2, x2, lift1, lift2, flag, shans, budjet, i1, i2
        if self.name == 'kubik.png' and  self.rect.collidepoint(pos):
            a =  random.randint(1, 6)
            self.text = self.f.render('Выпало:' + str(a), True, (0, 0, 0))
            if hod == 1:
                if not og.tur or a == 6:
                    og.tur = False
                    brosil = True
                    og.hodit = True
                    tb.hodit = True
                else:
                    brosil = False
                    flag = True
                    hod *= -1
                    karta_sprites.empty()
                    if len(knop.sprites()) > 2:
                        knop.remove(knop.sprites()[3])
                        knop.remove(knop.sprites()[2])
            else:
                if not tb.tur or a == 6:
                    tb.tur = False
                    brosil = True
                    og.hodit = True
                    tb.hodit = True
                else:
                    brosil = False
                    flag = True
                    hod *= -1
                    karta_sprites.empty()
                    if len(knop.sprites()) > 2:
                        knop.remove(knop.sprites()[3])
                        knop.remove(knop.sprites()[2])
        elif self.name == 'konec.png' and  self.rect.collidepoint(pos) and len(knop.sprites()) != 3:
            og.plat = ''
            tb.plat = ''
            brosil = False
            flag = True
            hod *= -1
            karta_sprites.empty()
            if len(knop.sprites()) > 2:
                knop.remove(knop.sprites()[3])
                knop.remove(knop.sprites()[2])
        elif self.name == 'kupit.png' and self.rect.collidepoint(pos):
            if hod == 1:
                if kazna1 >= og.cen[og.poloz - 1]:
                    og.karta[og.poloz - 1] = 1
                    tb.karta[og.poloz - 1] = 1
                    kazna1 -= og.cen[og.poloz - 1]
                    if 'Лифт' in og.kab[og.poloz - 1]:
                        lift1 += 1
            else:
                if kazna2 >= tb.cen[tb.poloz - 1]:
                    tb.karta[tb.poloz - 1] = 2
                    og.karta[tb.poloz - 1] = 2
                    kazna2 -= tb.cen[tb.poloz - 1]
                    if 'Лифт' in tb.kab[tb.poloz - 1]:
                        lift2 += 1
            knop.remove(knop.sprites()[3])
            knop.remove(knop.sprites()[2])
            karta_sprites.empty()
            if hod == 1 and og.karta[og.poloz - 1] == 1:
                im = pygame.transform.scale(load_image(og.kab[og.poloz - 1]), (50, 80))
                screen.blit(im, (x1, y1))
                if y1 <= 560:
                    y1 += 40
                else:
                    y1 = 50
                    x1 = 70
                kartochki.append([im, x1, y1])
            elif hod == -1 and tb.karta[tb.poloz - 1] == 2:
                im = pygame.transform.scale(load_image(og.kab[tb.poloz - 1]), (50, 80))
                screen.blit(im, (x2, y2))
                if y2 <= 560:
                    y2 += 40
                else:
                    y2 = 50
                    x2 = 840
                kartochki.append([im, x2, y2])
        elif self.name == 'net.png' and self.rect.collidepoint(pos):
            knop.remove(knop.sprites()[2])
            knop.remove(knop.sprites()[2])
            karta_sprites.empty()
        elif self.name == 'vhod.png' and self.rect.collidepoint(pos):
            x = random.randint(1, 6)
            flag = False
            knop.remove(knop.sprites()[2])
            self.text3 = self.f3.render('Вам выпало:' + str(x), True, (0, 0, 0))
            self.screen.blit(self.text3, (pole.rect.x + 260, pole.rect.y + 360))
            if hod == 1:
                if og.karta[8] == 2 and og.karta[17] == 2:
                    kazna1 -= x * 10
                    kazna2 += x * 10
                else:
                    kazna1 -= x * 5
                    kazna2 += x * 5
            else:
                if og.karta[8] == 1 and og.karta[17] == 1:
                    kazna2 -= x * 10
                    kazna1 += x * 10
                else:
                    kazna2 -= x * 5
                    kazna1 += x * 5
        elif self.name == 'Иди.png' and self.rect.collidepoint(pos):
            if shans[i1] == 'лифт':
                if hod == 1:
                    og.poloz = 22
                    og.rect.x = pole.rect.x + 21
                    og.rect.y = 340
                    if og.karta[og.poloz - 1] == 2:
                        kazna1 -= lift2 * 30
                        kazna2 += lift2 * 30
                    elif og.karta[21] == 0:
                        kupit = Knopki(knop, 'kupit.png', screen)
                        otmena = Knopki(knop, 'net.png', screen)
                else:
                    tb.poloz = 22
                    tb.rect.x = pole.rect.x + 21
                    tb.rect.y = 385
                    if tb.karta[tb.poloz - 1] == 1:
                        kazna1 += lift1 * 30
                        kazna2 -= lift1 * 30
                    elif tb.karta[21] == 0:
                        kupit = Knopki(knop, 'kupit.png', screen)
                        otmena = Knopki(knop, 'net.png', screen)
                karta_sprites.empty()
                knop.remove(knop.sprites()[2])
                im = Karta(karta_sprites, og.kab[21])
                i1 += 1
                if i1 > len(shans) - 1:
                    i1 = 0
            elif shans[i1] == 'библиотека':
                if hod == 1:
                    og.poloz = 1
                    og.rect.x = pole.rect.x + 21
                    og.rect.y = 130
                    kazna1 += 150
                else:
                    tb.poloz = 1
                    tb.rect.x = pole.rect.x + 21
                    tb.rect.y = 175
                    kazna2 += 150
                knop.remove(knop.sprites()[2])
                i1 += 1
                if i1 > len(shans) - 1:
                    i1 = 0
            elif shans[i1] == 'дино':
                karta_sprites.empty()
                if hod == 1:
                    og.poloz = 21
                    og.rect.x = pole.rect.x + 21
                    og.rect.y = 410
                    if og.karta[20] == 2:
                        kazna1 -= og.cen[20]
                        kazna2 += og.cen[20]
                    elif og.karta[20] == 0:
                        kupit = Knopki(knop, 'kupit.png', screen)
                        otmena = Knopki(knop, 'net.png', screen)
                    im = Karta(karta_sprites, og.kab[20])
                else:
                    tb.poloz = 21
                    tb.rect.x = pole.rect.x + 21
                    tb.rect.y = 455
                    if tb.karta[20] == 1:
                        kazna2 -= tb.cen[20]
                        kazna1 += tb.cen[20]
                    elif tb.karta[20] == 0:
                        kupit = Knopki(knop, 'kupit.png', screen)
                        otmena = Knopki(knop, 'net.png', screen)
                    im = Karta(karta_sprites, tb.kab[20])
                knop.remove(knop.sprites()[2])
                i1 += 1
                if i1 > len(shans) - 1:
                    i1 = 0
            elif shans[i1] == 'директор':
                if hod == 1:
                    og.poloz = 7
                    og.rect.x = pole.rect.x + 441
                    og.rect.y = 130
                    og.tur = True
                else:
                    tb.poloz = 7
                    tb.rect.x = pole.rect.x + 441
                    tb.rect.y = 175
                    tb.tur = True
                karta_sprites.empty()
                knop.remove(knop.sprites()[2])
                i1 += 1
                if i1 > len(shans) - 1:
                    i1 = 0
            else:
                karta_sprites.empty()
                knop.remove(knop.sprites()[2])
                if hod == 1:
                    og.poloz = 20
                    og.rect.x = pole.rect.x + 21
                    og.rect.y = 480
                    if og.karta[19] == 2:
                        kazna1 -= og.cen[19]
                        kazna2 += og.cen[19]
                    elif og.karta[19] == 0:
                        kupit = Knopki(knop, 'kupit.png', screen)
                        otmena = Knopki(knop, 'net.png', screen)
                    im = Karta(karta_sprites, og.kab[19])
                else:
                    tb.poloz = 20
                    tb.rect.x = pole.rect.x + 21
                    tb.rect.y = 525
                    if tb.karta[19] == 1:
                        kazna2 -= tb.cen[19]
                        kazna1 += tb.cen[19]
                    elif tb.karta[20] == 0:
                        kupit = Knopki(knop, 'kupit.png', screen)
                        otmena = Knopki(knop, 'net.png', screen)
                    im = Karta(karta_sprites, tb.kab[19])
                i1 += 1
                if i1 > len(shans) - 1:
                    i1 = 0
        elif self.name == 'poluc.png':
            knop.remove(knop.sprites()[2])
            karta_sprites.empty()
            if budjet[i2] == 'др':
                if hod == 1:
                    kazna1 -= 20
                else:
                    kazna2 -= 20
            elif budjet[i2] == 'подарок':
                if hod == 1:
                    kazna1 += 50
                else:
                    kazna2 += 50
            elif budjet[i2] == 'друг':
                if hod == 1:
                    kazna1 += 25
                    kazna2 -= 25
                else:
                    kazna1 -= 25
                    kazna2 += 25
            elif budjet[i2] == 'конкурс':
                if hod == 1:
                    kazna1 += 10
                else:
                    kazna2 += 10
            else:
                if hod == 1:
                    kazna1 -= 100
                else:
                    kazna2 -= 100
            i2 += 1
            if i2 > len(budjet) - 1:
                i2 = 0
                
            

class Player(pygame.sprite.Sprite):
    def __init__(self, group, name):
        super().__init__(group)
        self.image = load_image(name)
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.x = pole.rect.x + 21
        if self.name == 'computer.png':
            self.rect.y = 130
        else:
            self.rect.y = 175
        self.poloz = 1
        self.hodit = True
        self.karta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cen = [0, 60, 0, 150, 60, 100, 0, 120, 200, 150, 180, 200, 0, 220, 240, 150, 0, 200, 0, 300, 320, 150, 0, 400]
        self.kab = [0, 'Карта1.png', 0, 'Лифт1.png', 'Карта2.png', 'Карта3.png', 0, 'Карта4.png', 'Вход1.png', 'Лифт2.png', 'Карта5.png', 'Карта6.png', 0, 'Карта7.png', 'Карта8.png', 'Лифт3.png', 'Шанс.png', 'Вход2.png', 0, 'Карта9.png', 'Карта10.png', 'Лифт4.png', 'Бюджет.png', 'Карта11.png']
        self.viplati = [0, 5, 0, 0, 7, 10, 0, 15, 0, 0, 20, 22, 0, 27, 30, 0, 0, 0, 0, 35, 37, 0, 0, 45]
        self.tur = False
        self.f = pygame.font.SysFont('Arial', 18)
        self.s = ''
        self.text = self.f.render(self.s, True, (0, 0, 0))
        self.plat = ''
        
    
    def update(self):
        global brosil, hod, a, karta_sprite, kazna1, kazna2, lift1, lift2, shans, budjet, i1, i2
        if brosil and self.hodit:
            self.hodit = False
            if self.poloz >= 1 and self.poloz < 7:
                if self.poloz + a <= 7:
                    self.rect.x += 70 * a
                else:
                    self.rect.x += 70 * (7 - self.poloz)
                    a -= 7
                    a += self.poloz
                    if self.name == 'computer.png':
                        self.rect.y += 70 * a + 14
                    else:
                        self.rect.y += 70 * a
                    a += 7
                    a -= self.poloz
            elif self.poloz >= 7 and self.poloz < 13:
                if self.poloz + a <= 13:
                    self.rect.y += 70 * a
                else:
                    if self.name == 'aptechka.png':
                        self.rect.y += 70 * (13 - self.poloz) + 14
                    else:
                        self.rect.y += 70 * (13 - self.poloz)
                    a -= 13
                    a += self.poloz
                    self.rect.x -= 70 * a
                    a += 13
                    a -= self.poloz                    
            elif self.poloz >= 13 and self.poloz < 19:
                if self.poloz + a <= 19:
                    self.rect.x -= 70 * a
                else:
                    self.rect.x -= 70 * (19 - self.poloz) + 14
                    a -= 19
                    a += self.poloz
                    if self.name == 'aptechka.png':
                        self.rect.y -= 70 * a + 14
                    else:
                        self.rect.y -= 70 * a
                    a += 19
                    a -= self.poloz                    
            elif self.poloz >= 19 and self.poloz <= 24:
                if self.poloz + a <= 24:
                    self.rect.y -= 70 * a
                else:
                    if self.name == 'computer.png':
                        self.rect.y = 130
                        kazna1 += 150
                    else:
                        self.rect.y = 175
                        kazna2 += 150
                    self.rect.x = pole.rect.x + 21
                    a -= 25
                    a += self.poloz
                    self.rect.x += 70 * a
                    a += 25
                    a -= self.poloz
            self.poloz += a
            if self.poloz > 24:
                self.poloz -= 24
            if self.kab[self.poloz - 1] != 0:
                im = Karta(karta_sprites, self.kab[self.poloz - 1])
                if self.karta[self.poloz - 1] == 0 and self.kab[self.poloz - 1] != 'Шанс.png' and self.kab[self.poloz - 1] != 'Бюджет.png':
                    kupit = Knopki(knop, 'kupit.png', screen)
                    otmena = Knopki(knop, 'net.png', screen)
                if self.viplati[self.poloz - 1] != 0:
                    if hod == 1 and self.karta[self.poloz - 1] == 2:
                        kazna1 -= self.viplati[self.poloz - 1]
                        kazna2 += self.viplati[self.poloz - 1]
                        self.plat = 'Вы попали на чужое поле.'
                    elif hod == -1 and self.karta[self.poloz - 1] == 1:
                        kazna2 -= self.viplati[self.poloz - 1]
                        kazna1 += self.viplati[self.poloz - 1]
                        self.plat = 'Вы попали на чужое поле.'
                    self.text = self.f.render(self.plat, True, (0, 0, 0))
                elif 'Лифт' in self.kab[self.poloz - 1]:
                    if hod == 1 and self.karta[self.poloz - 1] == 2:
                        kazna1 -= lift2 * 30
                        kazna2 += lift2 * 30
                    elif hod == -1 and self.karta[self.poloz - 1] == 1:
                        kazna2 -= lift1 * 30
                        kazna1 += lift1 * 30
                elif 'Вход' in self.kab[self.poloz - 1]:
                    if hod == 1 and self.karta[self.poloz - 1] == 2:
                        vhod = Knopki(knop, 'vhod.png', screen)
                    elif hod == -1 and self.karta[self.poloz - 1] == 1:
                        vhod = Knopki(knop, 'vhod.png', screen)
                elif self.poloz == 17:
                    if shans[i1] == 'лифт':
                        self.s = 'Пройдите до ближайшего лифта.'
                    elif shans[i1] == 'библиотека':
                        self.s = 'Пройдите в бибилиотеку'
                    elif shans[i1] == 'дино':
                        self.s = 'Урок вот-вот начнётся. Идите в класс Google динозавриков.'
                    elif shans[i1] == 'директор':
                        self.s = 'О нет! Вы пробежали по коридору. Отправляйтесь к директору.'
                    else:
                        self.s = 'Перейдите на 3 поля вперёд.'
                    self.text = self.f.render(self.s, True, (0, 0, 0))
                    idti = Knopki(knop, 'Иди.png', screen)
                elif self.poloz == 23:
                    if budjet[i2] == 'др':
                        self.s = 'Сдайте 20су на день рождения директору.'
                    elif budjet[i2] == 'подарок':
                        self.s = 'Отлично работаете! Получите 50су.'
                    elif budjet[i2] == 'друг':
                        self.s = 'В школе проводится тайный друг. Получите 25су от другого игрока.'
                    elif budjet[i2] == 'конкурс':
                        self.s = 'Вы выиграли конкурс по ОБЖ! Ваш приз 10су.'
                    else:
                        self.s = 'О нет! Вы выбили дверь! Сдайте 100су на починку!'
                    pol = Knopki(knop, 'poluc.png', screen)
                    self.text = self.f.render(self.s, True, (0, 0, 0))
            elif self.poloz == 3:
                if hod == 1:
                    kazna1 -= 150
                else:
                    kazna2 -= 150
                self.plat = 'Нужно сдать 150су на ремонт школы.'
                self.text = self.f.render(self.plat, True, (0, 0, 0))
            elif self.poloz == 19:
                self.s = 'Вы у директора. Бросайте кубик, пока вам не выпадет 6.'
                self.text = self.f.render(self.s, True, (0, 0, 0))
                self.tur = True
                self.rect.x = pole.rect.x + 461
                if self.name == 'computer.png':
                    self.rect.y = 130
                else:
                    self.rect.y = 175
                self.poloz = 7
            

class Karta(pygame.sprite.Sprite):
    def __init__(self, group, name):
        super().__init__(group)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = pole.rect.x + 180
        self.rect.y = pole.rect.y + 90
                        

done = True
pygame.init()
size = (1000, 650)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
pygame.display.flip()
pole_sprite = pygame.sprite.Group()
pole = Pole(pole_sprite, screen)
knop = pygame.sprite.Group()
kubik = Knopki(knop, 'kubik.png', screen)
konec = Knopki(knop, 'konec.png', screen)
kazna1 = 1000
kazna2 = 1000
lift1 = 0
lift2 = 0
f1 = pygame.font.SysFont('Arial', 18)
text1 = f1.render('Состояние:' + str(kazna1), True, (0, 0, 0))
screen.blit(text1, (20, 20))
f2 = pygame.font.SysFont('Arial', 18)
text2 = f1.render('Состояние:' + str(kazna2), True, (0, 0, 0))
screen.blit(text2, (870, 20))
player_sprite = pygame.sprite.Group()
og = Player(player_sprite, 'computer.png')
tb = Player(player_sprite, 'aptechka.png')
karta_sprites = pygame.sprite.Group()
flag = True
shans = ['лифт', 'библиотека', 'дино', 'директор', 'вперёд']
random.shuffle(shans)
i1 = 0
budjet = ['др', 'подарок', 'друг', 'конкурс', 'дверь']
random.shuffle(budjet)
i2 = 0

hod = 1
a = 0
brosil = False
kartochki = []
y1 = 50
x1 = 10
y2 = 50
x2 = 770

pygame.draw.circle(screen, (255, 0, 0), (240, 20), 10)
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(knop.sprites()) > 3:
                knop.sprites()[2].do(event.pos)
            if len(knop.sprites()) > 3:
                knop.sprites()[3].do(event.pos)
            if len(knop.sprites()) == 3:
                knop.sprites()[2].do(event.pos)
            if not brosil:
                kubik.do(event.pos)
            else:
                konec.do(event.pos)
    screen.fill((255, 255, 255))
    text1 = f1.render('Состояние:' + str(kazna1), True, (0, 0, 0))
    text2 = f1.render('Состояние:' + str(kazna2), True, (0, 0, 0))
    screen.blit(text1, (20, 20))
    screen.blit(text2, (870, 20))   
    pole_sprite.draw(screen)
    pole_sprite.update()
    knop.draw(screen)
    knop.update()
    karta_sprites.draw(screen)
    player_sprite.draw(screen)
    for item in kartochki:
        screen.blit(item[0], (item[1], item[2]))
    if hod == 1:
        og.update()
        pygame.draw.circle(screen, (255, 0, 0), (200, 20), 10)
        if og.tur:
            screen.blit(og.text, (pole.rect.x + 5, pole.rect.y - 20))
        if og.plat != '':
            screen.blit(og.text, (pole.rect.x + 5, pole.rect.y - 20))
    else:
        tb.update()
        pygame.draw.circle(screen, (255, 0, 0), (800, 20), 10)
        if tb.tur:
            screen.blit(tb.text, (pole.rect.x + 5, pole.rect.y - 20))
        if tb.plat != '':
            screen.blit(tb.text, (pole.rect.x + 5, pole.rect.y - 20))
    pygame.display.flip()
pygame.quit()
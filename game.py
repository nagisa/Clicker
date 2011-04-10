#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       clicker.py
#
#       Copyright 2011 Simonas Kazlauskas <simonas@kazlauskas.me>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


import pygame
import sys
import time
import random

result = 0
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Are you fast enough?')

def show_result(text):
    global background
    background = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
    set_background(background)
    font = pygame.font.Font(None, 50)
    text = font.render(' '*100+str(text)+' '*100, True, (0, 0, 0), background)
    textRect = text.get_rect()

    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    screen.blit(text, textRect)
    pygame.display.update()

def show_time(time):
    font = pygame.font.Font(None, 25)
    text = font.render('Time left(seconds): '+str(time)+' '*100, True, (0, 0, 0), background)
    textRect = text.get_rect()

    textRect.x = screen.get_rect().x+5
    textRect.y = screen.get_rect().y+5

    screen.blit(text, textRect)
    pygame.display.update()

def set_background(bg):
    screen.fill(bg)
    pygame.display.flip()

background = (255,255,255)
set_background(background)

screen.fill(background)
pygame.display.flip()


font = pygame.font.Font(None, 50)
text = font.render('Click to start! Warning - very flashy!', True, (0, 0, 0), (255, 255, 255))
textRect = text.get_rect()

textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

screen.blit(text, textRect)
pygame.display.update()

timeleft = 60
show_time(timeleft)

while True:
    if result>0 and timeleft>0:
        timeleft = 60-(int(time.time())-timestart)
        show_time(timeleft)
    elif result>0 and timeleft<=0:
        show_result('Your result is: '+str(result)+'. You\'re great!')
        break
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        sys.exit()
    elif pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
            if result == 0:
                timestart = int(time.time())
            result += 1
            show_result(result)

while True:
    show_time('0. If you want to play again, restart this application.')
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        sys.exit()

# -*- coding: utf-8 -*-
import keyboard
from os import system, name
from colorama import Back, init
init()
options = []
title = ''
opt_return = ''
cur_option = 0
out_i = 0
selected = 0
def dec_option(args):
    global cur_option, options
    if not cur_option == len(options) - 1:
        cur_option += 1
    reload()
def inc_option(args):
    global cur_option, options
    if not cur_option == 0:
        cur_option -= 1
    reload()
def reload():
    global out_i, selected
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    if not title == '':
        print(title)
    for out_i in range(0, len(options)):
        if out_i == cur_option:
            print(Back.BLUE, options[out_i], Back.RESET)
            selected = out_i
        else:
            print(options[out_i])
def showmenu():
    keyboard.on_press_key('down', dec_option)
    keyboard.on_press_key('up', inc_option)
    reload()
    keyboard.wait('enter')
    return options[selected]
from mcpi.minecraft import Minecraft
from mcpi.vec3 import *
from block_names import *
from mcpi.block import *
from bombs import bomba
from bigheavy import big_heavy
from teleportrandom import teleport
from pynput import keyboard

import time

mc = Minecraft.create()
i_global = 0

time_init_alt = 0
time_init_alt_r = 0

def on_press(key):
    global mc
    global i_global
    i_global += 1
    if key == keyboard.Key.alt:
        global time_init_alt
        time_init_alt = time.process_time()
    elif key == keyboard.Key.alt_r:
        global time_init_alt_r
        time_init_alt_r = time.process_time()
    elif key == keyboard.Key.caps_lock:
        mc.postToChat("Key CAPS LOCK")
        teleport()

def on_release(key):
    global mc
    global i_global
    global time_init_alt_r
    i_global += 1
    if key == keyboard.Key.alt:
        new_time_init_alt = time.process_time()
        global time_init_alt
        diff = new_time_init_alt - time_init_alt
        bomba(diff)
    elif key == keyboard.Key.alt_r:
        global time_init_alt_r
        new_time_init_alt_r = time.process_time()
        diff = new_time_init_alt_r - time_init_alt_r
        big_heavy(diff)

# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release ) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))


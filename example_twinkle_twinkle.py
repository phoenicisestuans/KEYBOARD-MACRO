from Hotkeys import Hotkeys
from MusicalTimings import MusicTiming
from KeyPress import KeyBdInput, HardwareInput, MouseInput, Input_I, Input, UseKeyboard
import time

# Sets the hotkeys for each note to the default config
h = Hotkeys()
# If your hotkeys are not the defualt set them here

# This library makes it so instead of manually timing
# how long each note is held you can automatically get
# the appropriate length based on bpm. Use get functions
t = MusicTiming()

# The order on these functions matter, bpm is beats for minute
# and the set_new_times function takes that bpm as a ration to 60
# and converts the number of seconds on each type of note accordingly
# Change the number in the parenthesis to change the bpm
t.set_bpm(100)
t.set_new_times()

# Begin your song here. If you need to hold a note
# keep in mind that only sleeping (time.sleep()) between
# the press and release doesn't work. You also need a delay
# between the release and the next key press (unless changing
# notes in the middle of a slur)

# Set a delay so you can tab into your song
time.sleep(15)

UseKeyboard.PressKey(h.getC())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getC())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getC())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getC())
time.sleep(t.eighth_note)


UseKeyboard.PressKey(h.getG())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getG())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getG())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getG())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getA())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getA())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getA())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getA())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getG())
time.sleep(t.dotted_quarter)
UseKeyboard.ReleaseKey(h.getG())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getF())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getF())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getF())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getF())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getE())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getE())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getE())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getE())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getD())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getD())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getD())
time.sleep(t.eighth_note)
UseKeyboard.ReleaseKey(h.getD())
time.sleep(t.eighth_note)

UseKeyboard.PressKey(h.getC())
time.sleep(t.dotted_quarter)
UseKeyboard.ReleaseKey(h.getC())
time.sleep(t.eighth_note)
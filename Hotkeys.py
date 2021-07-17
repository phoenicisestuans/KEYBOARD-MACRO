# This is a library written to give alias's to notes on the MIDI keyboard
# especially in FFXIV or other softwares
# Copyright (C) 2021 Phoenix

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, 
# or, any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Keyboard inputs are selected for windows inputs only meant
# to be used with the KeyPress library also included here

from pynput.keyboard import Key

class Hotkeys:
    def __init__(self):
        self.set_def_hotkeys()
        
    def set_def_hotkeys(self):
        self.C=0x10
        self.C_sharp=0x03
        self.D=0x11
        self.D_sharp=0x04
        self.E=0x12
        self.F=0x13
        self.F_sharp=0x06
        self.G=0x14
        self.G_sharp=0x7
        self.A=0x15
        self.A_sharp=0x08
        self.B=0x16
        self.C_up=0x17
        self.up_octave=0x2a
        self.down_octave=0x1d
        
    def set_C_hotkey(self, C):
        self.C = C
    def set_C_sharp_hotkey(self, C_sharp):
        self.C_sharp = C_sharp
    def set_D_hotkey(self, D):
        self.D = D
    def set_D_sharp_hotkey(self, D_sharp):
        self.D_sharp = D_sharp
    def set_E_hotkey(self, E):
        self.E = E
    def set_F_hotkey(self, F):
        self.F = F
    def set_F_sharp_hotkey(self, F_sharp):
        self.F_sharp = F_sharp
    def set_G_hotkey(self, G):
        self.G = G
    def set_G_sharp_hotkey(self, G_sharp):
        self.G_sharp = G_sharp
    def set_A_hotkey(self, A):
        self.A = A
    def set_A_sharp_hotkey(self, A_sharp):
        self.A_sharp = A_sharp
    def set_B_hotkey(self, B):
        self.B = B
    def set_C_up_hotkey(self, C_up):
        self.C_up = C_up
    def set_up_octave(self, up_octave):
        self.up_octave = up_octave
    def set_down_octave(self, down_octave):
        self.down_octave = down_octave
    
    def getC(self):
        return self.C
    def getCsharp(self):
        return self.C_sharp
    def getD(self):
        return self.D
    def getD_sharp(self):
        return self.D_sharp
    def getE(self):
        return self.E
    def getF(self):
        return self.F
    def getF_sharp(self):
        return self.F_sharp
    def getG(self):
        return self.G
    def getG_sharp(self):
        return self.G_sharp
    def getA(self):
        return self.A
    def getA_sharp(self):
        return self.A_sharp
    def getB(self):
        return self.B
    def getC_up(self):
        return self.C_up
    def getup_octave(self):
        return self.up_octave
    def getdown_octave(self):
        return self.down_octave
    
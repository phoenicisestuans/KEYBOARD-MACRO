# This is a library written to convert note names that musicians
# would know into timings for delays in the main program
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


class MusicTiming:
    def __init__(self):
        self.bpm = float(60.0)
        self.whole_note = float(4.0)
        self.half_note = float(2.0)
        self.dotted_half = float(3.0)
        self.quarter_note = float(1.0)
        self.dotted_quarter = float(1.5)
        self.eighth_note = float(0.5)
        self.sixteenth_note = float(.25)
        self.triplet = float(1.0/3.0)
        self.set_new_times()
    def set_new_times(self):
        self.whole_note = self.whole_note * (60.0 / self.bpm)
        self.half_note = self.half_note * (60.0 / self.bpm)
        self.dotted_half = self.dotted_half * (60.0 / self.bpm)
        self.quarter_note = self.quarter_note * (60.0 / self.bpm)
        self.dotted_quarter = self.dotted_quarter * (60.0 / self.bpm)
        self.eighth_note = self.eighth_note * (60.0 / self.bpm)
        self.sixteenth_note = self.sixteenth_note * (60.0 / self.bpm)
        self.triplet =self.triplet * (60.0 / self.bpm)
        
    def set_bpm(self, bpm):
        self.bpm = float(bpm)
    
    def get_whole_note(self):
        return self.whole_note
    def get_half_note(self):
        return self.half_note
    def get_dotted_half(self):
        return self.dotted_half
    def get_quarter_note(self):
        return self.quarter_note
    def get_dotted_quarter(self):
        return self.dotted_quarter
    def get_eighth_note(self):
        return self.eighth_note
    def get_sixteenth_note(self):
        return self.sixteenth_note
    def get_bpm(self):
        return self.bpm
    def get_triplet(self):
        return self.triplet
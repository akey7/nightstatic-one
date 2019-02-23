import re

class NoteFreqs:
    """
    This class handles note frequencies and scales for easy tone generation
    """

    def __init__(self):
        """
        The constructor simply instantiates instance variables.
        """

        # self.nfstr_regex: A regex to validate strings passed in
        self.nfstr_regex = re.compile('[abcdefg]_m[ai][nj]or_[0-9-]\d_\d')

        # self._notes_dict_array_hz: Dictionary of notes through all their octaves
        self._notes_dict_array_hz = {
            'C': [8.176, 16.352, 32.703, 65.406, 130.81, 261.63, 523.25, 1046.5, 2093.0, 4186.0, 8372.0],
            'C#': [8.662, 17.324, 34.648, 69.296, 138.59, 277.18, 554.37, 1108.7, 2217.5, 4434.9, 8869.8],
            'Db': [8.662, 17.324, 34.648, 69.296, 138.59, 277.18, 554.37, 1108.7, 2217.5, 4434.9, 8869.8],
            'D': [9.177, 18.354, 36.708, 73.416, 146.83, 293.66, 587.33, 1174.7, 2349.3, 4698.6, 9397.3],
            'Eb': [9.723, 19.445, 38.891, 77.782, 155.56, 311.13, 622.25, 1244.5, 2489.0, 4978.0, 9956.1],
            'D#': [9.723, 19.445, 38.891, 77.782, 155.56, 311.13, 622.25, 1244.5, 2489.0, 4978.0, 9956.1],
            'E': [10.301, 20.602, 41.203, 82.407, 164.81, 329.63, 659.26, 1318.5, 2637.0, 5274.0, 10548.1],
            'F': [10.914, 21.827, 43.654, 87.307, 174.61, 349.23, 698.46, 1396.9, 2793.8, 5587.7, 11175.3],
            'F#': [11.563, 23.125, 46.249, 92.499, 185.0, 369.99, 739.99, 1480.0, 2960.0, 5919.9, 11839.8],
            'Gb': [11.563, 23.125, 46.249, 92.499, 185.0, 369.99, 739.99, 1480.0, 2960.0, 5919.9, 11839.8],
            'G': [12.25, 24.5, 48.999, 97.999, 196.0, 392.0, 783.99, 1568.0, 3136.0, 6271.9, 12543.9],
            'Ab': [12.979, 25.957, 51.913, 103.83, 207.65, 415.3, 830.61, 1661.2, 3322.4, 6644.9],
            'G#': [12.979, 25.957, 51.913, 103.83, 207.65, 415.3, 830.61, 1661.2, 3322.4, 6644.9],
            'A': [13.75, 27.5, 55.0, 110.0, 220.0, 440.0, 880.0, 1760.0, 3520.0, 7040.0],
            'Bb': [14.568, 29.135, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.7, 3729.3, 7458.6],
            'A#': [14.568, 29.135, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.7, 3729.3, 7458.6],
            'B': [15.434, 30.868, 61.735, 123.47, 246.94, 493.88, 987.77, 1975.5, 3951.1, 7902.1]
        }

        # self._scales: The layout of various scales given certain octaves
        # Tuple is format of (note, octave_offset)
        # Octave offset is the octave relative to root note of scale
        # 0 is in the same octave of root, +1 is an octave higher, etc
        # It ISN'T the absolute octave.

        self._scales = dict()
        self._scales['a_major'] = [('A', 0), ('B', 0), ('C#', 1), ('D', 1), ('E', 1), ('F#', 1), ('G#', 1)]
        self._scales['b_major'] = [('B', 0), ('C#', 0), ('D#', 0), ('E', 0), ('F#', 0), ('G#', 0), ('A#', 1)]
        self._scales['c_major'] = [('C', 0), ('D', 0), ('E', 0), ('F', 0), ('G', 0), ('A', 0), ('B', 0)]
        self._scales['d_major'] = [('D', 0), ('E', 0), ('F#', 0), ('G', 0), ('A', 0), ('B', 0), ('C#', 1)]
        self._scales['e_major'] = [('E', 0), ('F#', 0), ('G#', 0), ('A', 0), ('B', 0), ('C#', 1), ('D#', 1)]
        self._scales['f_major'] = [('F', 0), ('G', 0), ('A', 0), ('Bb', 0), ('C', 1), ('D', 1), ('E', 1)]
        self._scales['g_major'] = [('G', 0), ('A', 0), ('B', 0), ('C', 1), ('D', 1), ('E', 1), ('F#', 1)]
        self._scales['a_minor'] = [('A', 0), ('B', 0), ('C', 1), ('D', 1), ('E', 1), ('F', 1), ('G', 1)]
        self._scales['b_minor'] = [('B', 0), ('C#', 1), ('D', 1), ('E', 1), ('F#', 1), ('G', 1), ('A', 1)]
        self._scales['c_minor'] = [('C', 0), ('D', 0), ('Eb', 0), ('F', 0), ('G', 0), ('Ab', 0), ('Bb', 0)]
        self._scales['d_minor'] = [('D', 0), ('E', 0), ('F', 0), ('G', 0), ('A', 0), ('Bb', 0), ('C', 1)]
        self._scales['e_minor'] = [('E', 0), ('F#', 0), ('G', 0), ('A', 0), ('B', 0), ('C', 1), ('D', 1)]
        self._scales['f_minor'] = [('F', 0), ('G', 0), ('Ab', 0), ('Bb', 0), ('C', 1), ('Db', 1), ('Eb', 1)]
        self._scales['g_minor'] = [('G', 0), ('A', 0), ('Bb', 0), ('C', 1), ('D', 1), ('Eb', 1), ('F', 1)]

        # self._midi_note_hz: this is the list of MIDI notes all
        # the way up through their octaves. It should be indexed by integer.
        self._midi_note_hz = [8.176, 8.662, 9.177, 9.723, 10.301, 10.914,
            11.563, 12.25, 12.979, 13.75, 14.568, 15.434, 16.352, 17.324,
            18.354, 19.445, 20.602, 21.827, 23.125, 24.5, 25.957, 27.5,
            29.135, 30.868, 32.703, 34.648, 36.708, 38.891, 41.203,
            43.654, 46.249, 48.999, 51.913, 55.0, 58.27, 61.735, 65.406,
            69.296, 73.416, 77.782, 82.407, 87.307, 92.499, 97.999, 103.83,
            110.0, 116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 164.81,
            174.61, 185.0, 196.0, 207.65, 220.0, 233.08, 246.94, 261.63,
            277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.0, 415.3,
            440.0, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.26,
            698.46, 739.99, 783.99, 830.61, 880.0, 932.33, 987.77, 1046.5,
            1108.7, 1174.7, 1244.5, 1318.5, 1396.9, 1480.0, 1568.0, 1661.2,
            1760.0, 1864.7, 1975.5, 2093.0, 2217.5, 2349.3, 2489.0, 2637.0,
            2793.8, 2960.0, 3136.0, 3322.4, 3520.0, 3729.3, 3951.1, 4186.0,
            4434.9, 4698.6, 4978.0, 5274.0, 5587.7, 5919.9, 6271.9, 6644.9,
            7040.0, 7458.6, 7902.1, 8372.0, 8869.8, 9397.3, 9956.1, 10548.1,
            11175.3, 11839.8, 12543.9
        ]

    def note_freq(self, note, octave):
        """
        Given the string of a note:
        C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, Ab, A, A#, Bb, B

        And the octave: -1 to 9 inclusive

        Returns the frequency in hertz of the note.   

        :param note: The alphabetic letter of the note
        :param octave: -1 to 9 inclusive
        :return: Frequency in hertz
        """
        octave_idx = octave + 1
        return self._notes_dict_array_hz[note][octave_idx]

    def is_float(self, value):
        """
        Raises an Exception if a value is not a float

        :param value: The value to test for float-ness
        :return: True if the value is a float, raises a ValueError otherwise
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    # formats
    #
    # C4: C in octave 4

    def single_note_freq_from_str(self, nfstr):
        if self.is_float(nfstr):
            return float(nfstr)
        else:
            try:
                if len(nfstr) < 2 or len(nfstr) > 4:
                    raise Exception('Note "{}" is not valid'.format(nfstr))
                elif nfstr[1] in ['b', '#']:
                    return self.note_freq(nfstr[0:2], int(nfstr[2:]))
                else:
                    return self.note_freq(nfstr[0], int(nfstr[1:]))
            except ValueError:
                raise Exception('Note "{}" is not valid'.format(nfstr))

    def scale_freqs(self, *, scale, root_octave):
        if scale not in self._scales:
            raise Exception('Scale {} does not exist'.format(scale))
        if root_octave < -1 or root_octave > 8:
            raise Exception('Octave {} is out of bounds'.format(root_octave))
        return [self.note_freq(note=x, octave=y + root_octave) for x, y in self._scales[scale]]

    # c-major-04-1: C major rooted in 4, degree 1. Which is C4.

    def scale_freq_from_str(self, nfstr):
        if self.nfstr_regex.match(nfstr) is not None:
            nfstr_split = nfstr.split('_')
            scale = nfstr[:7]
            root_octave = int(nfstr_split[2])
            freqs = self.scale_freqs(scale=scale, root_octave=root_octave)
            degree = int(nfstr_split[3])
            if degree < 1 or degree > 7:
                raise Exception('Degree {} is out of bounds. nfstr {}'.format(degree, nfstr))
            return freqs[degree - 1]
        else:
            raise Exception('Note {} is not a valid note specification'.format(nfstr))


if __name__ == '__main__':
    nf = NoteFreqs()
    print(nf.scale_freqs(scale='c_major', root_octave=4))
    print(nf.scale_freqs(scale='a_minor', root_octave=4))
    print(nf.scale_freqs(scale='f_major', root_octave=4))
    print(nf.scale_freq_from_str('c_major_-1_3'))

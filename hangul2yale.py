#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, argparse
import pickle

table = pickle.load(open('table.pickle'))

def block (codepoint):
	'''Return the name of Hangul-related Unicode block.'''
	
	if 0xAC00 <= codepoint <= 0xD7A3:
		return 'syllables'
	elif 0x1100 <= codepoint <= 0x11FF:
		return 'jamo'
	elif 0x3130 <= codepoint <= 0x318F:
		return 'compatibility jamo'
	elif 0xA960 <= codepoint <= 0xA97F:
		return 'jamo extended-A'
	elif 0xD7B0 <= codepoint <= 0xD7FF:
		return 'jamo extended-B'
	else:
		return None

def convert (char):
	'''Return the romanization of a Hangul character.'''

	codepoint = ord (char)
	if block(codepoint) == 'syllables':
		num = codepoint - 44032
		return table['syllables']['choseong'][(num // 28) // 21] + table['syllables']['jungseong'][(num // 28) % 21] + table['syllables']['jongseong'][num % 28]

	elif block(codepoint) == 'jamo':
		num = codepoint - 4352
		if table['jamo'][num][3] == None:
			return char
		else:
			return table['jamo'][num][3]
	else:
		return char


def tweeks (charlist):
	'''Tweeks for minor rules'''

	pass

def convert_string (string):
	charlist = [convert(char) for char in string]
	return ''.join(charlist)

if __name__ == '__main__':

	#parser = argparse.ArgumentParser()
	#parser.add_argument('-w', dest='wu', action='store_false', help='maintains u/wu distinction after labials')
	#args = parser.parse_args()

	print convert_string(sys.argv[1].decode('utf-8'))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

'''

import sys, cgi, argparse

choseong = ('k', 'kk', 'n', 't', 'tt', 'l', 'm', 'p', 'pp', 's', 'ss', '', 'c', 'cc', 'ch', 'kh', 'th', 'ph', 'h')
jungseong = ('a', 'ay', 'ya', 'yay', 'e', 'ey', 'ye', 'yey', 'o', 'wa', 'way', 'oy', 'yo', 'wu', 'we', 'wey', 'wi', 'yu', 'u', 'uy', 'i')
jongseong = ('', 'k', 'kk', 'ks', 'n', 'nc', 'nh', 't', 'l', 'lk', 'lm', 'lp', 'ls', 'lth', 'lph', 'lh', 'm', 'p', 'ps', 's', 'ss', 'ng', 'c', 'ch', 'kh', 'th', 'ph', 'h')

def block (codepoint):
	'''Return the name of Hangul-related block.'''
	
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
	if block (codepoint):
		num = codepoint - 44032
		return choseong [(num // 28) // 21] + jungseong [(num // 28) % 21] + jongseong [num % 28]
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

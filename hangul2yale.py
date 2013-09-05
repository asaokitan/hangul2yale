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


def tweeks (string, charlist, **options):
	'''Tweeks for minor rules'''

	tweeked_charlist = charlist

	# discard u/wu distinction after labials
	if options['discard']:
		for (i, char) in enumerate(tweeked_charlist):
			if i == 0:
				continue
			
			if char == 'wu' and char[i-1] in ['p', 'ph', 'pp', 'm']:
				new_charlist[i] = 'u'
			
	return tweeked_charlist

def convert_string (string, **options):
	'''convert a Unicode-based string into Yale Romanization.'''

	charlist = [convert(char) for char in string]

	tweeked_charlist = tweeks(string, charlist, **options)

	return ''.join(tweeked_charlist)


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	
	parser.add_argument('string', action='store', help='a Unicode-based string to be converted into Yale Romanization')

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-d', '--disambiguate', action='store_true', help='indicate syllable boundaries with . when ambiguous in modern Korean')
	group.add_argument('-a', '--always', action='store_true', help='always indicate syllable boundaries with .')
	parser.add_argument('-w', '--discard', action='store_true', help='discard the u/wu distinction after labials')
	parser.add_argument('-o', '--oaraea', action='store_true', help='use o for araea instead of @')
	args = parser.parse_args()

	print convert_string(args.string.decode('utf-8'), **vars(args))

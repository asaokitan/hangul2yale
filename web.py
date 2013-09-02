#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import hangul2yale

# メイン
if __name__ == "__main__":

	print "Content-type: text/plain;charset=utf-8\n"

	form = cgi.FieldStorage()
	if form.getvalue('hangul'):

		hangul = form.getvalue('hangul').decode('utf-8')
		#dots = form.getvalue('dots')

		result = hangul2yale.convert_string(hangul)
	else:
		result = ''
	
	print cgi.escape(result).encode('utf-8')

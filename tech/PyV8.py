#coding=utf-8
import PyV8
import requests

jsfile = open('lib/encode/customjs/tripledes.js','r')
js = jsfile.read()
jsfile.close()

jsfile = open('lib/encode/customjs/mode-ecb.js','r')
js += jsfile.read()
jsfile.close()

jsfile = open('lib/encode/customjs/my.js','r')
js += jsfile.read()
jsfile.close()

def getEncPasswd(word):
	ctxt = PyV8.JSContext()
	with PyV8.JSLocker():
		ctxt.__enter__()
		ctxt.locals.password = word
		ctxt.eval(js)
		res = ctxt.locals.result
		ctxt.leave()
	return res.encode('utf-8')


# print getEncPasswd('admin')
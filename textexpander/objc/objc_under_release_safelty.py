#!/usr/bin/python
# encoding: utf-8

import re
import sys

result_retain="";


for line in sys.stdin:
     

	regex=r'(?P<class>\w+)[\s|\*]+(?P<object>[\w|_]+);'   


	reobj=re.compile(regex)

	url_list=[]
	for def_line in reobj.finditer(line):
		# def_line.group()
		class_name=def_line.group("class")	
		object_name=def_line.group("object")
		object_name=object_name.replace("_","")
		if (line.find("*")>0):
			result_retain+="    RELEASE_SAFELY( _%s );\n" % (object_name)



print result_retain






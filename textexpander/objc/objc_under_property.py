#!/usr/bin/python
# encoding: utf-8

import re
import sys

result_retain="";
reslut_assign=""

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
			result_retain+="@property (nonatomic, retain) %s *%s;\n" % (class_name,object_name)
		else:
			reslut_assign+="@property (nonatomic, assign) %s %s;\n" % (class_name,object_name)
			
			
print result_retain
print reslut_assign





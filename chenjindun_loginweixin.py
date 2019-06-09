Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  import itchat
█
SyntaxError: unexpected indent
>>> import itchat
█
>>> itchat.login()
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Loading the contact, this may take a little while.
Login successfully as 尘离
>>> friends = itchat.get_friends(update = True )[0:]
>>> male=female = other =0
>>> for i in friends[1:]:
	sex = i["Sex"];
	if sex ==1;
	
SyntaxError: invalid syntax
>>> friends = itchat.get_friends(update = True )[0:]
>>> male=female = other =0
>>> for i in friends[1:]:
	sex = i["Sex"]:
		
SyntaxError: invalid syntax
>>> for i in friends[1:]:
	sex = i["Sex"]
	if sex ==1:
		male +=1
		elif sex ==2:
			
SyntaxError: invalid syntax
>>> for i in friends[1:]:
	sex = i["Sex"]
	if sex ==1:
		male +=1
	elif sex ==2:
		female += 1
	else:
		other +=1

		
>>> total =len(friends[1:])
>>>  print("男性好友：%.2f%%" % (float(male) / total * 100))
男性好友：46.05%
SyntaxError: unexpected indent
>>> print("男性好友：%.2f%%" % (float(male) / total * 100))
男性好友：46.05%
SyntaxError: multiple statements found while compiling a single statement
>>> print("男性好友：%.2f%%" % (float(male) / total * 100))
男性好友：46.05%
SyntaxError: multiple statements found while compiling a single statement
>>> total =len(friends[1:])
>>> print("男性好友：%.2f%%" % (float(male) / total * 100))男性好友：46.05%
SyntaxError: invalid character in identifier
>>> print("男性好友：%.2f%%" % (float(male) / total * 100))
男性好友：67.30%
>>> print("女性好友：%.2f%%" % (float(female) / total * 100))
女性好友：28.93%
>>> print("其他：%.2f%%" % (float(other) / total * 100))
其他：3.77%
>>> 

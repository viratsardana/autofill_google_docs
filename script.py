import mechanize
import random
import string

def fill_form(i):
	br=mechanize.Browser()
	#br.set_all_readonly(False)
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	
	#br.set_debug_http(True)
	#br.set_debug_responses(True)
	
	response=br.open('https://docs.google.com/forms/d/1EQ2XZKOr46ZLhGROjdz1PhZMmuDCXIawIs3HzwhQdn8/viewform')
	
	"""print response.read()"""
	
	"""for form in br.forms():
		print str(form.attrs["id"])"""
	
	br.select_form(nr=0)
	
	
	
	#print br.form
	
	submit_name=""
	
	for control in br.form.controls:
		"""print control.name,control.type"""
		if control.type=="radio":
			print control.name,control.type
			l=len(list(control.items))
			r=random.randint(0,l-1)
			print r
			li=list(control.items)
			ans=li[r].name
			print ans
			"""print r
			print li[r].name"""
			"""for item in control.items:
				print item.name"""
			control.value=[ans]
		elif control.type=="text":
			#print names[i]
			control.value=names[i]
		elif control.type=="submit":
			submit_name=control.name
	response=br.submit()
	#print br.response().read()
		

names=[]

handler=open("names.txt")

for line in handler:
	names.append(line.split()[0])

"""
print names"""

i=0

for j in range(0,100):
	fill_form(i)
	i=i+1

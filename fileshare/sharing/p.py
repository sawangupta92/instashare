import subprocess
import os
# from models import *
os.chdir('/home/sawan/Desktop/instashare')
query='import'
# search=subprocess.check_output(['find', '-name', 'PRIVATE', '-exec', 'grep', '-R','-l', '-Hn', query, '{}', ';'])
# print search
# c=3
b=subprocess.check_output(["grep","-R", "imp", "/home/sawan/Desktop/instashare/media"])
print b
# b='sasas'
# a=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_3/user_2/PUBLIC"])

# print a
# if not subprocess.check_call(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c]):
# a=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c]).split("/home/sawan/Desktop/instashare/")
# b= a
# k=[]
# l=[]
# def s():
# 	for r in b:
# 		k.append(r.split(":")[0])
		# l.append(r.split(":")[1])
	# return k

# print s()
# a=subprocess.Popen(('find'), stdout=subprocess.PIPE)
# q=subprocess.Popen(('find','-name','PRIVATE'), stdout=subprocess.PIPE)
# e=subprocess.check_output(('grep','-R','import'),stdin=q.stdout)
# print e
# a=os.path.join("/home/sawan/Desktop/instashare/media/company_%d" %c_id,'PUBLIC')
# a=subprocess.check_output(('find','-name','PRIVATE','-exec','grep','-R','-Hn','import','{}',';'))
# print a
# a="/home/sawan/Desktop/instashare/hjhjkj"
# print a.split("/home/sawan/Desktop/instashare/")
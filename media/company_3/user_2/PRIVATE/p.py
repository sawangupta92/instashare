import subprocess
c=3
a=subprocess.check_output(["grep","-R","-l" ,"hello", "/home/sawan/Desktop/instashare/media/company_%d" %c])
print a
# a=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_3/user_1"])
# if not subprocess.check_call(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c]):
	# print a.subprocess.check_call(["grep","-R","-l", query, "/home/sawan/Desktop/instashare/media/company_%d" %c_id])
s=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c])
search=s.split("/home/sawan/Desktop/instashare/")
q=[]
for d in s.splitlines():
	q.append(d.split(":")[1])
print q
import subprocess
c=3
# a=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_3/user_1"])
# if not subprocess.check_call(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c]):
a=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c]).split("/home/sawan/Desktop/instashare/")
b= a
k=[]
l=[]
def s():
	for r in b:
		k.append(r.split(":")[0])
		# l.append(r.split(":")[1])
	return k
print s()

# a="/home/sawan/Desktop/instashare/hjhjkj"
# print a.split("/home/sawan/Desktop/instashare/")
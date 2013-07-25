import subprocess
c=3
# a=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_3/user_1"])
if not subprocess.check_call(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c]):
	a=subprocess.check_output(["grep","-R", "hello", "/home/sawan/Desktop/instashare/media/company_%d" %c])
	print a
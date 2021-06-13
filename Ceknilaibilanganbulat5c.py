#7. C. menampilkan bilangan bulat 0=100

#@author: Divira Salsabiil Susanto - 20083000178 - 2G

 #menampilkan bilangan bulat
 
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
	print ("===========================")
	print (" MENAMPILKAN BILANGAN BULAT")
	print ("===========================")

	n = input(">> Masukkan nilai = ")
	#cek nilai
	if int(n)>0 and int(n)<=100:
		if int(n)>80:    sts="BAIK SEKALI"
		elif int(n)>=65: sts="BAIK"
		elif int(n)>=55: sts="CUKUP"
		elif int(n)>=40: sts="KURANG"
		elif int(n)<40:  sts="KURANG SEKALI"
		else:
			sts="Ulang"
		print(sts)
	else:
		pesan=">>> Masukkan Nilai bilangan"
		print(pesan)

	jwbulangprog = input(">>> Ulang Program? y/t = ")
	if jwbulangprog=="t" or jwbulangprog=="T":
		break

#7. a. cekkelulusan

#@author: Divira Salsabiil Susanto - 20083000178 - 2G

jwb = "y"
while jwb=="y" or jwb=="Y":
	print ("=============")
	print("CEK KELULUSAN")
	print ("==============")
	n = input(">> Masukkan Nilai = ")
	#cek nilai
	if int(n)>60 :
		sts = "LULUS"
	else:
		sts = "ULANG"
	print(sts)
	#inputan untuk break
	jwb = input(">> Mulai lagi? y/t = ")
	if jwb == "t" or jwb =="T":
		break

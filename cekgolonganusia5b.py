
"""
Cek golongan usia menggunakan loop
- loop cek inputan range usia harus 0-100
- loop run program
"""
#7. B.cek tingkat usia
#cek golongan usia menggunkaan loop

jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
	print ("===================")
	print(" CEK TINGKAT USIA ")
	print ("====================")
 
	u = input(">> Masukkan usia = ")
	#cek batasan usia
	if int(u)>0 and int(u)<=100:
		if int(u)>=60:
			sts="LANSIA"
		elif int(u)>=35: sts="DEWASA"
		elif int(u)>=18: sts="PEMUDA"
		elif int(u)>=15: sts="REMAJA"
		else:
			sts="ANAK"
		print(sts)
	else:
		pesan=">>> Masukkan angka usia"
		print(pesan)

	jwbulangprog = input(">>> Ulang Program? y/t = ")
	if jwbulangprog=="t" or jwbulangprog=="T":
		break
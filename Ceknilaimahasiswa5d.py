#7. D. Penilaian mahasiswa mendapatkan huruf x

#@author: Divira Salsabiil Susanto - 20083000178 - 2G

print('===================')
print('PENILAIAN NILAI MAHASISWA')
print('===================')

x = input (">> Masukkan nilai = ")
	#cek nilai mahasiswa

if int(x)>=91:
	sts="A"
elif int(x)>=81:
	sts="B"
elif int(x)>=71:
	sts="C"
elif int(x)<71:
	sts="D"
else:
		sts="ulang"
print(sts)


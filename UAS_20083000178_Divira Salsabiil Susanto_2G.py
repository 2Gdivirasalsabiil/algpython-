from datetime import date, time, datetime
tanggalSlipGaji = date.today()

print("\n\t\t\t\t\tSLIP GAJI\n\t\t\t\tTanggal: ",tanggalSlipGaji,"\n")

nama = input("Nama\t\t\t\t\t\t\t")
golongan = int(input("Golongan\t\t\t\t\t"))
jenisKelamin = input("Jenis Kelamin\t\t\t\t\t")
jenisKelamin = jenisKelamin.upper()
statusKawin = input("Status Kawin\t\t\t\t\t")
statusKawin = statusKawin.upper()

gajiPokok = 0
if golongan == 1:
    gajiPokok = 2500000
elif golongan == 2:
    gajiPokok = 4500000
else:
    gajiPokok = 6500000

print("Gaji Pokok\t\t\t\t\t", gajiPokok)

tunjanganIstri = 0
if jenisKelamin == "LAKI-LAKI" and statusKawin == "KAWIN":
    if golongan == 1:
        tunjanganIstri = gajiPokok * 0.01
    elif golongan == 2:
        tunjanganIstri = gajiPokok * 0.03
    else:
        tunjanganIstri = gajiPokok * 0.05

print("Tunjangan Istri\t\t\t\t\t", int(tunjanganIstri))

statusAnak = input("Status Anak (punya/tidak) \t\t\t\t\t")
statusAnak = statusAnak.upper()
tunjanganAnak = 0
if statusAnak == "PUNYA" and statusKawin == "KAWIN":
    tunjanganAnak = gajiPokok * 0.02
print("Tunjangan Anak\t\t\t\t\t", int(tunjanganAnak))

gajiBruto = gajiPokok + tunjanganAnak + tunjanganIstri
print(">> Gaji Bruto \t\t\t\t\t", int(gajiBruto))

biayaJabatan = gajiBruto * 0.005
print("Biaya Jabatan \t\t\t\t\t", int(biayaJabatan))

print("Iuran Pensiun \t\t\t\t\t 15000")
print("Iuran Organisasi \t\t\t\t\t 3000")

gajiNetto = gajiBruto - (biayaJabatan + 19000)

print(">> Gaji Netto \t\t\t\t\t", int(gajiNetto))
from datetime import date, time, datetime
tanggalSlipGaji = date.today()

print("\n\t\t\t\t\tSLIP GAJI\n\t\t\t\tTanggal: ",tanggalSlipGaji,"\n")

nama = input("Nama\t\t\t\t\t\t\t")
golongan = int(input("Golongan\t\t\t\t\t"))
jenisKelamin = input("Jenis Kelamin\t\t\t\t\t")
jenisKelamin = jenisKelamin.upper()
statusKawin = input("Status Kawin\t\t\t\t\t")
statusKawin = statusKawin.upper()

gajiPokok = 0
if golongan == 1:
    gajiPokok = 2500000
elif golongan == 2:
    gajiPokok = 4500000
else:
    gajiPokok = 6500000

print("Gaji Pokok\t\t\t\t\t", gajiPokok)

tunjanganIstri = 0
if jenisKelamin == "LAKI-LAKI" and statusKawin == "KAWIN":
    if golongan == 1:
        tunjanganIstri = gajiPokok * 0.01
    elif golongan == 2:
        tunjanganIstri = gajiPokok * 0.03
    else:
        tunjanganIstri = gajiPokok * 0.05

print("Tunjangan Istri\t\t\t\t\t", int(tunjanganIstri))

statusAnak = input("Status Anak (punya/tidak) \t\t\t\t\t")
statusAnak = statusAnak.upper()
tunjanganAnak = 0
if statusAnak == "PUNYA" and statusKawin == "KAWIN":
    tunjanganAnak = gajiPokok * 0.02
print("Tunjangan Anak\t\t\t\t\t", int(tunjanganAnak))

gajiBruto = gajiPokok + tunjanganAnak + tunjanganIstri
print(">> Gaji Bruto \t\t\t\t\t", int(gajiBruto))

biayaJabatan = gajiBruto * 0.005
print("Biaya Jabatan \t\t\t\t\t", int(biayaJabatan))

print("Iuran Pensiun \t\t\t\t\t 15000")
print("Iuran Organisasi \t\t\t\t\t 3000")

gajiNetto = gajiBruto - (biayaJabatan + 19000)

print(">> Gaji Netto \t\t\t\t\t", int(gajiNetto))

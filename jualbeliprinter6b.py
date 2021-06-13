#@author: Divira Salsabiil Susanto - 20083000178

#Nilai awal variabel jmlBeli = Harga 1 Printer
HargaPrint = 660000
minDiskon = 1500000
persenDiskon = 0.15

#input jumlah beli
print("=====================================")
print("TRANSAKSI PEMBELIAN PRINTER EPSON T20")
print("===================================")
qty = input("Jumlah printer Epson T20 yg dibeli = ")
#input qty
if int(qty)>0:
    totAwal = "HargaPrint*qty"
else:
    TotBayar = "Ulang"
    
#cek nilai diskon
if int(qty)>minDiskon:
    TotBayar = minDiskon = totAwal*persenDiskon
else:
    TotBayar = nilaiDiskon = 0

#proses hitung total
TotBayar = int(totAwal)*int(minDiskon)

#tampil
print(TotBayar) 
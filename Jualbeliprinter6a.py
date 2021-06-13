#@author: Divira Salsabiil Susanto - 20083000178

#Nilai awal variabel jmlBeli = Harga 1 Printer
HargaPrint = 660000

#input jumlah beli
print("=====================================")
print("TRANSAKSI PEMBELIAN PRINTER EPSON T20")
print("===================================")
JmlBeli = input("Jumlah printer Epson T20 yg dibeli = ")

#proses hitung total
Total = int(HargaPrint)*int(JmlBeli)

#tampil
print("Total transaksi Pembelian Printer Epson T20 = Rp " + str (Total)) 
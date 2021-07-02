"""
@author: Divira Salsabiil Susanto
"""

print("")
print("===============================")
print(" Daftar Menu Makanan")
print("===============================")
print(" a = Nasi Goreng       Rp 15000")
print(" b = Lontong Goreng    Rp 14.900")
print(" c = Bakso Goreng      Rp 12.900")
print(" d = Rujak Goreng      Rp 13.000")
print(" e = Rujak Bakso       Rp 15.000")
print(" f = Rujak Bakso Pecel Rp 17.000")
print("================================")
print("")

print("")
print("===============================")
print(" Daftar Menu Minuman")
print("===============================")
print(" a = Teh Dingin/Hangat/Panas     Rp 2500")
print(" b = Kopi Dingin                 Rp 5000")
print(" c = Kopi Teh Panas              Rp 6.500")
print(" d = Coca Cola Dingin            Rp 3.500")
print(" e = Coca Cola Panas             Rp 5000")
print("================================")
print("")

kode =['a','b','c','d','e','f']
namaBarang = ['Nasi Goreng + Teh Dingin/Hangat/Panas','Lontong Goreng + Kopi Dingin','Bakso Goreng + Kopi Teh Panas',
              'Rujak Goreng + Coca Cola Dingin','Rujak Bakso + Coca Cola Panas','Rujak Bakso Pecel']
harga = [15000,14.900,12.900,13.000,15.000,17.000,2500,5000,6.500,3.500,5000]


#input pilihan
pilihan     = input(" Masukkan Kode Barang        = ")
#input qty
qty         = input(" Masukkan Jumlah Barang      = ")
#input bayar
Bayar       = input(" Masukkan Bayar Barang       = ")
#input kembalian
Kembalian   = input(" Masukkan Kembalian Barang   = ")

#hitung bayar
i = 0
while i<len(namaBarang):
    if kode[i] == pilihan:
        #ambil nama barang
        nm_brg = namaBarang[i]
        
        #ambil harga satuan
        hrgsat = harga[i]
    
        
    i+=1

while(True):
    i+= 1
    jawab = input("Transaksi lagi tidak? ")
    if jawab == 'tidak':
        break
    
tot_byr = hrgsat * int(qty)
#output
print(">>> NAMA BARANG       : " + nm_brg)
print(">>> HARGA BARANG       : " + str(hrgsat))
print(">>> JUMLAH BARANG      : " +qty)
print(("------------------------------"))
print(">>> TOTAL BAYAR      : " + str(tot_byr))

import random

papan_Minesweeper = [['?', '?', '?'],
                     ['?', '?', '?'],
                     ['?', '?', '?']]


baris = random.randint(0, 2) // untuk ngebatesin nilai masuk yang memungkinkan
kolom = random.randint(0, 2)
papan_Minesweeper[baris][kolom] = 'X'

while True:
   for baris in papan_Minesweeper :
       print(' '.join(baris))

   user_baris= int(input("masukan jumlah baris (0-2): "))
   user_kolom = int(input("masukan jumlah barang (0-2): "))

   if papan_Minesweeper[user_baris][user_kolom] == 'X':
       print("tepat sasaran,kamu memukul BOM!! nya. permainan selesai.")
       break

   papan_Minesweeper[user_baris][user_kolom] = 'O'

   if sum(baris.count('?') for baris in papan_Minesweeper) == 1:
       print("yeah kamu menang!!")
       break
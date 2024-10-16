# def mhs():
#     print("hello")

# def kali():
#     x = 6*4
#     print(x)

# # Membuat fungsi dengan parameter (panjang, lebar)
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("Luas persegi panjang:", luas)
# # Pemanggilan fungsi luas_persegi_panjang
# luas_persegi_panjang(4, 6)
# # Output:
# # Luas persegi : 24
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# hasil = luas_persegi(4) + luas_persegi(2)
# print(hasil)

# import os
# data_mahasiswa =[
#     {
#         "Nama" : "Andi",
#         "Nim" : "123"
#     },
#     {
#         "Nama" : "Budi",
#         "Nim" : "124"
#     },
#     {
#         "Nama" : "Ucup",
#         "Nim" : "125"
#     }
# ]

# def lihat_data():
#     print("===Lihat Data===")
#     for i in range(len(data_mahasiswa)):
#         print(f"data ke {i+1}")
#         print(f"Nama : {data_mahasiswa[i]['Nama']}")
#         print(f"Nim : {data_mahasiswa[i]['Nim']}")
#         print("="*10)

# def tambah_data():
#     print("== Tambah Data ==")
#     print("=" * 10)
#     input_nama = input("Nama\t: ")
#     input_nim = input("Nim\t: ")
#     data_mahasiswa.append({
#         "Nama" : input_nama,
#         "Nim" : input_nim
#     })
#     print(f"{input_nama} dengan NIM {input_nim} telah ditambahkan")
     
# def ubah_data():
#     print("== Ubah Data ==")
#     for i in range(len(data_mahasiswa)):
#         print(f"data ke {i+1}")
#         print(f"Nama : {data_mahasiswa[i]['Nama']}")
#         print(f"Nim : {data_mahasiswa[i]['Nim']}")
#         print("="*10)
#         index= int(input("masukkan index yang mau diedit : "))
#         if index > len(data_mahasiswa) or index < 0:
#             print("Index tidak ditemukan")
#             input("Enter.....")
#             os.system('cls || clear')
#         else:
#             nama_baru = input("masukkan nama anda :")
#             nim_baru = input("masukkan nim anda :")
#             data_mahasiswa[index-1]["Nama"] = nama_baru
#             data_mahasiswa[index-1]["Nim"] = nim_baru
#             print("data berhasil diubah")

# def hapus_data():
#     print("== Hapus Data ==")
#     for i in range(len(data_mahasiswa)):
#         print(f"data ke {i+1}")
#         print(f"Nama : {data_mahasiswa[i]['Nama']}")
#         print(f"Nim : {data_mahasiswa[i]['Nim']}")
#         print("="*10)
#         index = int(input("masukkan index yang ingin dihapus: "))
#         if index > len(data_mahasiswa) or index < 0:
#             print("Index tidak ditemukan")
#             input("Enter.....")
#             os.system('cls || clear')
#         else:
#             del_data = data_mahasiswa.pop(index-1)
#             print(f"{del_data['Nama']} dengan NIM {del_data['Nim']} telah dihapus")



# os.system('cls || clear')
# while True:
#     print("""
#     Menu
# Lihat Data  >> 1
# Tambah Data >> 2
# Edit Data   >> 3
# Hapus Data  >> 4
# Keluar      >> 5
# """)
#     pilih = input("Masukan Pilihan menu >> ")
#     os.system('cls || clear')
#     match(pilih):
#         case "1":
#             lihat_data()
#             input("Enter.....")
#             os.system('cls || clear')
#         case "2":
#             tambah_data()
#             input("Enter....")
#             os.system('cls || clear')
#         case "3":
#             ubah_data()
#             input("Enter.....")
#             os.system('cls || clear')
#         case "4":
#             hapus_data()
#             input("Enter......")
#             os.system('cls || clear')
#         case "5":
#             print("Bye bye")
#             exit()
#         case _:
#             print(f"Menu {pilih} tidak tersedia")
#             input("Enter.....")
#             os.system('cls || clear')
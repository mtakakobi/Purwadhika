# Gudang Stok 
# Create : 15
# Read : 10
# Update : 20
# Delete : 15
# Video Penjelasan : 25
# Integrasi Sistem dan Efisiensi Kode : 15

#import library
import tabulate # untuk merubah format print data menjadi bentuk tabel
    
inventory = [ #Variable besera data awal
    {
        'code':f'{0 :04d}',
        'name':'Koka kola 330 ml',
        'stok':10,
        'harga': 3500,
        'vendor' : 'PT. Koka kola Indonesia'
    },
        {
        'code':f'{1 :04d}',
        'name':'Koka kola 660 ml',
        'stok':17,
        'harga': 5500,
        'vendor' : 'PT. Koka kola Indonesia'
    },
    {
        'code':f'{2 :04d}',
        'name':'Panta 330 ml',
        'stok':8,
        'harga': 3500,
        'vendor' : 'PT. Panta Indonesia'
    },
    {
        'code':f'{3 :04d}',
        'name':'Panta 630 ml',
        'stok':19,
        'harga': 5500,
        'vendor' : 'PT. Panta Indonesia'
    }
]

list_code = [] # List untuk mempermudah pencarian indeks
for i in inventory: # Input Code awal ke list_code
    list_code.append(i['code'])
    
flag_save = True # Kondisi penanda apakah code masih berjalan atau tidak
header = ['Kode Barang','Nama Barang','Stok Barang','Harga Barang','Vendor']

def check_pm(num_pm): # Function untuk mempercepat proses pengecekan input primary key
    x = num_pm
    if 0 <= x <= 9999:
        x = f"{x :04d}"
    else:
        x = None
    return x

def print_table(row,header = ['Kode Barang','Nama Barang','Stok Barang','Harga Barang','Vendor']):
    print(f"\n{tabulate.tabulate(row,header,tablefmt='grid')}\n")
    
        

def show(): # Fungsi Menu Read Data
    list_show = [['1. Tampilkan Seluruh Data'],
                 ['2. Tampilkan Data Menurut Kode Barang'],
                 ['3. Kembali Ke Menu Utama']]
    print_table(list_show,['Perintah'])
    inp_show = int(input('Silahkan Masukkan Perintah yang ingin Dijalankan : '))
    if inp_show == 1:
        if len(inventory) > 0:
            print(list_code)
            print_table([x.values() for x in inventory])
            show()
        else:
            print('Maaf belum ada data')
            show()
    elif inp_show == 2:
        if len(inventory) > 0:
            inp_pm = int(input('Format kode = angka (max.4 Digit)\nMasukkan Data : '))
            inp_pm = check_pm(inp_pm)
            if inp_pm in list_code:
                print_table([inventory[list_code.index(inp_pm)].values()])
                show()
            else:
                print('Maaf Tidak Ada Data')
                show()
        else:
            print('Maaf Tidak Ada Data')
            show()    
    elif inp_show == 3:
        main()
    else:
        show()

def add(): # Fungsi Menu untuk menambah data
    list_add = [['1. Menambah Barang'],
                ['2. Kembali ke Menu Utama']]
    print_table(list_add,['Perintah'])
    inp_add = int(input('Silahkan Masukkan Perintah yang ingin Dijalankan : '))
    if inp_add == 1:
        inp_pm = int(input('Format kode = angka (max.4 Digit)\nMasukkan Data : '))
        inp_pm = check_pm(inp_pm)
        print(inp_pm)
        if inp_pm in list_code:
            print('Data sudah ada')
            add()
        else:
            inp_nama = input('Masukkan Nama barang : ')
            inp_stok = int(input("Masukkan Stok Barang : "))
            inp_harga = int(input("Masukkan Harga barang : "))
            inp_vendor = input('Masukkan Vendor Barang : ')
            new_dict = {
                'keys' : inp_pm,
                'name' : inp_nama,
                'stok' : inp_stok,
                'harga' : inp_harga,
                'vendor' : inp_vendor
            }
            inp_save = input('Apakah ingin menyimpan data baru? (y/n) : ') 
            if inp_save == 'y': 
                inventory.append(new_dict)
                list_code.append(inp_pm)
            else:
                add()
    elif inp_add == 2:
        main()
    else:
        add()
                        
def update(): # Fungsi Untuk Merubah Data
    list_update = [['1. Mengubah Data Barang'],
                   ['2. Kembali ke Menu Utama']]
    print_table(list_update,['Perintah'])
    inp_update = int(input('Silahkan Masukkan Perintah yang ingin Dijalankan : '))
    if inp_update == 1:
        inp_pm = int(input('Format kode = angka (max.4 Digit)\nMasukkan Data : '))
        inp_pm = check_pm(inp_pm)
        print(inp_pm)
        if inp_pm not in list_code:
            print("Data yang anda cari tidak ada")
            update()
        elif inp_pm in list_code:
            print_table([inventory[list_code.index(inp_pm)].values()])
            inp_save = input('Apakah ingin Mengubah data? (y/n) : ')
            if inp_save == 'y':
                inp_kolom = input('Nama || Stok || Harga || Vendor\nMasukkan kolom yang ingin di update : ')
                if inp_kolom.lower() == 'nama':
                    update_nama = input("Masukkan Nama Barang Baru : ")
                    inp_save = input('Apakah ingin Mengubah data? (y/n) : ')
                    if inp_save == 'y':
                        inventory[list_code.index(inp_pm)]['name'] = update_nama.capitalize()
                        print('Data Terupdate')
                        update()
                    else:
                        update()
                elif inp_kolom.lower() == "stok" :
                    update_stok = input("Masukkan Stok Barang Baru : ")
                    inp_save = input('Apakah ingin Mengubah data? (y/n) : ')
                    if inp_save == 'y':
                        inventory[list_code.index(inp_pm)]['stok'] = update_stok
                        print('Data Terupdate')
                        update()
                    else:
                        update()
                elif inp_kolom.lower() == 'harga':
                    update_harga = input("Masukkan Harga Barang Baru : ")
                    inp_save = input('Apakah ingin Mengubah data? (y/n) : ')
                    if inp_save == 'y':
                        inventory[list_code.index(inp_pm)]['harga'] = update_harga
                        print('Data Terupdate')
                        update()
                    else:
                        update()
                elif inp_kolom.lower() == 'vendor':
                    update_vendor = input("Masukkan Vendor Barang Baru : ")
                    inp_save = input('Apakah ingin Mengubah data? (y/n) : ')
                    if inp_save == 'y':
                        inventory[list_code.index(inp_pm)]['vendor'] = update_vendor
                        print('Data Terupdate')
                        update()
                    else:
                        update()
                else:
                    update()                 
     
def erase(): # Fungsi Untuk Menghapus Data
    list_erase = [['1. Hapus Data'],
                  ['2. Kembali ke Menu Utama']]
    print_table(list_erase,['Perintah'])
    inp_erase = int(input('Silahkan Masukan Perintah yang ingin dijalankan : '))
    if inp_erase == 1:
        inp_pm = int(input('Format kode = angka (max.4 Digit)\nMasukkan Data : '))
        inp_pm = check_pm(inp_pm)
        print(inp_pm)
        if inp_pm in list_code:
            print_table([inventory[list_code.index(inp_pm)].values()])
            inp_save = input('Apakah ingin menghapus data? (y/n) : ')
            if inp_save == 'y':
                del inventory[list_code.index(inp_pm)]
                del list_code[list_code.index(inp_pm)]
                print('Data Deleted')
            elif inp_save == 'n' :
                erase()
                
def main(): # Fungsi Untuk Menjalankan Program
    flag = True
    while flag:
        list_main = [['1. Tampilkan Data'],
                     ['2. Menambah Barang'],
                     ['3. Mengubah Data barang'],
                     ['4. Menghapus Barang'],
                     ['5. Keluar']]
        print_table(list_main,['Perintah'])
        inp = input('Masukkan Pilihan Menu : ')
        if inp == "1":
            show()
        elif inp == "2":
            add()
        elif inp == "3":
            update()
        elif inp == "4":
            erase()
        elif inp == "5":
            print('Terima Kasih!')
            exit()
        else:
            print('Pilihan yang anda masukkan salah, silahkan Mengulang')
            flag

main()
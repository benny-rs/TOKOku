import json
import datetime
import os
choose_file = ''
fee = 0
grand_total = 0

def menu():
    print('')
    print('{:^36}'.format('TOKOku'))
    print('{:^36}'.format('Pencatat Transaksi'))
    print('''
    +--------------------------+
    +      Data Transaksi      +
    +--------------------------+
    | 1. Buat File Baru        |
    | 2. Input Data Transaksi  |
    | 3. Lihat Data Transaksi  |
    | 4. Hapus Data Transaksi  |
    | 5. Update Data Transaksi |
    | 6. Keluar                |
    +--------------------------+
    *Gunakan pilihan "Buat File Baru" hanya jika ingin membuat file json baru!
    *Jika belum pernah membuat file json, pilih "Buat File Baru"!
    ''')
    global choose_file
    choose = input('Masukkan Pilihan : ')
    if choose == '1':
        newFile()
    elif choose == '2':
        os.system('cls')
        print('{:^38} \n'.format('INPUT DATA TRANSAKSI'))
        choose_file = input('Masukkan Nama File Yang Diinginkan : ')
        choose_file += '.json'
        looper_input()
    elif choose == '3':
        os.system('cls')
        print('{:^38} \n'.format('LIHAT DATA TRANSAKSI'))
        choose_file = input('Masukkan Nama File Yang Diinginkan : ')
        choose_file += '.json'
        view_log()
        return_to_menu()
    elif choose == '4':
        os.system('cls')
        print('{:^38} \n'.format('HAPUS DATA TRANSAKSI'))
        choose_file = input('Masukkan Nama File Yang Diinginkan : ')
        choose_file += '.json'
        looper_erase()
    elif choose == '5':
        os.system('cls')
        print('{:^38} \n'.format('UPDATE DATA TRANSAKSI'))
        choose_file = input('Masukkan Nama File Yang Diinginkan : ')
        choose_file += '.json'
        looper_update()
    elif choose == '6':
        keluar()
    else:
        os.system('cls')
        print('ERROR : Pilihan Tidak Tersedia!')
        menu()

def newFile():
    os.system('cls')
    print('{:^38} \n'.format('BUAT FILE BARU'))
    user_req_FileName = input('Masukkan Nama File Yang Diinginkan : ')
    user_req_FileName += '.json'
    with open(user_req_FileName, 'w',) as file_json:
        json.dump([], file_json)
        print('File Berhasil Dibuat!')
    return_to_menu()

def looper_input():
    global fee
    confirm = 'y'
    while True:
        try:
            fee = int(input('Masukkan besar keuntungan yang diinginkan : Rp '))
            break
        except ValueError:
            print('Hanya dapat memasukkan angka!')
            input('Enter untuk melanjutkan...')
            os.system('cls')
    while True:
        if confirm == 'y':
            input_trs()
        elif confirm == 'n':
            return_to_menu()
        confirm = input('Apakah masih ada transaksi yang ingin ditambahkan? (y/n) : ')

def input_trs():
    os.system('cls')
    view_data()
    local_templist = []
    jenis_item = input('Masukkan Jenis Item : ')
    nominal_item = int(input('Masukkan Nominal Item : '))
    hrg_item = nominal_item + fee
    jml_item = int(input('Masukkan Jumlah Item : '))
    total_hrg = hrg_item * jml_item
    wkt = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    local_tempdict = {'Waktu':wkt, 'Jenis':jenis_item, 'Nominal':nominal_item, 'Harga':hrg_item, 'Jumlah':jml_item, 'Total':total_hrg}
    with open(choose_file) as read_filejson:
        reader = json.load(read_filejson)
        for transaksi in reader:
            local_templist.append(transaksi)
    local_templist.append(local_tempdict)
    with open(choose_file,'w') as write_filejson:
        json.dump(local_templist, write_filejson, indent = 2)
    os.system('cls')
    view_data()
    print('Data Berhasil Ditambahkan!')

def view_log():
    view_data()
    print('Total Penjualan : Rp {:,}'.format(grand_total))

def view_data():
    global grand_total
    grand_total = 0
    os.system('cls')
    print('{0:^102} \n Nama File : '.format('DATA TRANSAKSI') + choose_file)
    print('+' + '-'*100 + '+')
    print('{0} {1:^4} {0} {2:^16} {0} {3:^17} {0} {4:^14} {0} {5:^11} {0} {6:^6} {0} {7:^12} {0} '.format('|', 'No', 'Waktu', 'Jenis Item', 'Nominal Item', 'Harga Item', 'Jumlah', 'Total Harga'))
    print('+' + '-'*100 + '+')
    with open(choose_file) as read_filejson:
        reader = json.load(read_filejson)
        for (num, trs) in enumerate(reader):
            grand_total += trs['Total']
            print('{0} {1:>4} {0} {2:^16} {0} {3:^17} {0} {8:^2} {4:>11} {0} {8:^2} {5:>8} {0} {6:>6} {0} {8:^2} {7:>9} {0} '.format('|', num+1, trs['Waktu'], trs['Jenis'], '{:,}'.format(trs['Nominal']),'{:,}'.format(trs['Harga']), trs['Jumlah'], '{:,}'.format(trs['Total']), 'Rp'))    
    print('+' + '-'*100 + '+')

def looper_erase():
    confirm = 'y'
    while True:
        if confirm == 'y':
            erase_data()
        elif confirm == 'n':
            return_to_menu()
        confirm = input('Apakah masih ada data transaksi yang ingin dihapus? (y/n) : ')

def erase_data():
    os.system('cls')
    view_data()
    local_templist = []
    try:
        nomor = int(input('Masukkan nomor yang akan dihapus : '))
        nomor -= 1
        try:
            with open (choose_file, 'r') as file_readjson:
                reader = json.load(file_readjson)
                for trs in reader:
                    local_templist.append(trs)
            local_templist.pop(nomor)
            with open (choose_file, 'w') as file_writejson:
                json.dump(local_templist, file_writejson, indent = 2)
        except IndexError:
            print('Data Tidak Ditemukan!')
            input('Enter untuk melanjutkan...')
    except ValueError:
        print('Hanya dapat memasukkan angka!')
        input('Enter untuk melanjutkan...')
    os.system('cls')
    view_data()

def looper_update():
    global fee
    confirm = 'y'
    while True:
        try:
            fee = int(input('Masukkan besar keuntungan yang diinginkan : Rp '))
            break
        except ValueError:
            print('Hanya dapat memasukkan angka!')
            input('Enter untuk melanjutkan...')
            os.system('cls')
    while True:
        if confirm == 'y':
            update_data()
        elif confirm == 'n':
            return_to_menu()
        confirm = input('Apakah masih ada data transaksi yang ingin diubah? (y/n) : ')

def update_data():
    os.system('cls')
    view_data()
    local_templist = []
    try:
        nomor = int(input('Masukkan nomor data yang akan diubah : '))
        nomor -= 1
        try:
            with open (choose_file, 'r') as read_filejson:
                reader = json.load(read_filejson)
                for trs in reader:
                    local_templist.append(trs)
            local_templist.pop(nomor)
            jenis_item = input('Masukkan Jenis Item : ')
            nominal_item = int(input('Masukkan Nominal Item : '))
            hrg_item = nominal_item + fee
            jml_item = int(input('Masukkan Jumlah Item : '))
            total_hrg = hrg_item * jml_item
            wkt = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
            local_tempdict = {'Waktu':wkt, 'Jenis':jenis_item, 'Nominal':nominal_item, 'Harga':hrg_item, 'Jumlah':jml_item, 'Total':total_hrg}
            local_templist.insert(nomor, local_tempdict)
            with open (choose_file, 'w') as write_filejson:
                json.dump(local_templist, write_filejson, indent = 2)
        except IndexError:
            print('Data Tidak Ditemukan!')
            input('Enter untuk melanjutkan...')
    except ValueError:
        print('Hanya dapat memasukkan angka!')
        input('Enter untuk melanjutkan...')     
    os.system('cls')
    view_data()

def keluar():
    while True:
        confirm_exit = input('Apakah anda yakin ingin keluar? (y/n) : ')
        if confirm_exit == 'y':
            os.system('cls')
            exit()
        elif confirm_exit == 'n':
            os.system('cls')
            menu()
        else:
            os.system('cls')
            print('Input Salah!')

def return_to_menu():
    while True:
        after_act = input('Apakah anda ingin kembali ke Menu Utama? (y/n) : ')
        if after_act == 'y':
            os.system('cls')
            menu()
        elif after_act == 'n':
            keluar()
        else:
            os.system('cls')
            print('Input Salah!')
menu()
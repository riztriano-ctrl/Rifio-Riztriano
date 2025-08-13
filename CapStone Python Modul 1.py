from tabulate import tabulate

listData = [
    [3101, 'Aldi Saputra', 'Laki', 30, 'Finance', 'Internship', 3500000],
    [3102, 'Budi Santoso', 'Laki', 28, 'HRD', 'Kontrak', 4200000],
    [3103, 'Citra Ayu', 'Perempuan', 26, 'Creative', 'Tetap', 5500000],
    [3104, 'Dewi Lestari', 'Perempuan', 32, 'Marketing', 'Kontrak', 4700000],
    [3105, 'Eko Prasetyo', 'Laki', 35, 'IT', 'Tetap', 6500000],
    [3106, "Farah Nabila", "Perempuan", 29, "Finance", "Internship", 3400000],
    [3107, "Gilang Ramadhan", "Laki", 27, "Sales", "Tetap", 5000000],
    [3108, "Hana Putri", "Perempuan", 31, "Customer Service", "Internship", 3600000]
]

# Table data
def print_table(listData):
    if not listData:
        print('\n\t\t\tData Kosong ')
        return
    else: 
        judul = ['ID', 'Nama', 'Gender', 'Umur', 'Divisi', 'Status','Gaji']
        print(tabulate(listData, headers=judul, tablefmt="fancy_grid"))
# menu 1 di dalam 1
def menampilkan_data():
    while True:
        pilihan = input('''
        ======= Menu Data Karyawan =======
                                      
        1. Tampilkan Semua Data
        2. Tampilkan Karyawan Tetap
        3. Tampilkan Karyawan Kontrak
        4. Tampilkan Karyawan Internship
        5. Kembali ke Menu Utama
                        
        Masukan Angka yang ingin di jalan kan : ''')

        if pilihan == '1':
            print_table(listData)
        elif pilihan == '2':
            tetap = []
            for x in listData:
                if x[5].capitalize() == 'Tetap':
                    tetap.append(x)
            print_table(tetap)
        elif pilihan == '3':
            kontrak = []
            for x in listData:
                if x[5].capitalize() == 'Kontrak':
                    kontrak.append(x)
            print_table(kontrak)
        elif pilihan == '4':
            intern = []
            for x in listData:
                if x[5].capitalize() == 'Internship':
                    intern.append(x)
            print_table(intern)
        elif pilihan == '5':
            break
        else:
            print('\n\tMasukan angka yang tersedia !!')
# ===============================================================
def tambah_1():
    # Input Id dengan pengecekan angka
    while True:
        id_input = input('\n\tMasukkan ID: ')
        if not id_input.isdigit():
            print('\tId harus angka.')
            continue
        id_karyawan = int(id_input)
        # Cek id
        id_sama = False
        for data in listData:
            if data[0] == id_karyawan:
                id_sama = True
                break
        if id_sama:
            print('\n\tId sudah ada.')
        else:
            break

    while True:
        nama = input('\tMasukkan Nama: ').title()
        if nama.replace(' ', '').isalpha():
            break
        print('\n\tHanya boleh berisi huruf')

    while True:
        gender = input('\tMasukkan Gender (Laki/Perempuan): ').capitalize()
        if gender in ['Laki', 'Perempuan']:
            break
        print('\n\tInput gender tidak valid.')

    # Input umur
    while True:
        umur_input = input('\tMasukkan Umur: ')
        if umur_input.isdigit() and 18 <= int(umur_input) <= 65:
            umur = int(umur_input)
            break
        print('\tUmur harus angka antara 18-65 tahun.')


    while True:
        divisi = input('\tMasukkan Divisi: ').title()
        if divisi.replace(' ', '').isalpha():
            break
        print('\tHanya boleh berisi huruf')

    while True:
        status = input('\tMasukkan Status (Tetap/Kontrak/Internship): ').capitalize()
        if status in ['Tetap', 'Kontrak','Internship']:
            break
        print('\tInput status tidak valid.')
    
    while True:
        gaji = input('\tMasukkan gaji : ')
        if gaji.isdigit() and int(gaji) > 0:
            gaji = int(gaji)
            break
        print('\tMasukan angka untuk gaji.')
    
    print(f'''
    Data yang di tambah
    Id      : {id_karyawan}
    Nama    : {nama}
    Gender  : {gender}
    Umur    : {umur}
    Divisi  : {divisi}
    Status  : {status}
    Gaji    : {gaji}''')
    while True:
        check = input('\nApakah anda yakin ingin menambah data di atas (Y/N) : ').strip().upper()
        if check in ['Y','N']:
            break
    if check == 'Y':
            listData.append([id_karyawan, nama, gender, umur, divisi, status, gaji])
            print_table(listData)
            print('\n\t\tData berhasil ditambahkan !!')
    else:
        print('\n\tData di batalkan.')
# menu 2 di dalam 2
def menambah_data():
    while True:
        pilihan = input('''
        === Menu Tambah Data ===
                        
        1. Tambah Satu Data
        2. Tambah Beberapa Data
        3. Kembali ke Menu Utama
                        
        Pilih menu angka: ''')

        if pilihan == '1':
            tambah_1()
        elif pilihan == '2':
            jumlah_data = (input('\n\tMasukan jumlah yang ingin ditambah data : '))
            if jumlah_data.isdigit():
                jumlah = int(jumlah_data)
                if jumlah > 0:
                    for _ in range(jumlah):
                        tambah_1()
                else:
                    print('\n\tAngka harus lebih dari 0.')
            else:
                print('\n\tmasukan angka yang benar.')
                    
        elif pilihan == '3':
            break
        else :
            print('\n\tMasukan angka yang tersedia.')
#================================================================            
def mengubah_data():
    
    while True:
        pilihan = input('''
        === Menu Ubah Data ===
        1. Ubah Nama
        2. Ubah Gender
        3. Ubah Umur
        4. Ubah Divisi
        5. Ubah Status
        6. ubah gaji
        7. Ubah Semua Data
        8. Kembali ke Menu Utama
        
        Pilih menu angka : ''')

        if pilihan == '8':
            break
        if pilihan not in ['1', '2', '3', '4', '5', '6', '7']:
            print('Pilihan tidak valid')
            continue
        if not listData:
            print("\n\t\t   Data karyawan kosong.")
            continue
        
        # # input Id
        while True:
            print_table(listData)
            id_input = input('\nMasukkan ID karyawan yang ingin diubah: ').strip()
            if not id_input.isdigit():
                print('\nID harus angka.')
                continue

            id_karyawan = int(id_input)
            index = -1
            for i in range(len(listData)):
                if listData[i][0] == id_karyawan:
                    index = i
                    break
            if index == -1:
                print('\nID tidak ditemukan. Coba lagi.')
                continue
            break  # ID valid
        
        print(f'Data lama: {listData[index]}')

        
        if pilihan == '1':
            while True:
                nama = input('Nama baru: ').title()
                if nama.replace(' ', '').isalpha():
                    if input(f"Yakin ubah nama menjadi '{nama}'? (Y/N): ").lower() == 'y':
                        listData[index][1] = nama
                        print_table(listData)
                        print("\n\t\t\tData berhasil diubah!")
                    else:
                        print("\n\t\t\tPerubahan dibatalkan.")
                    break
                print('\n\t\t\tHanya boleh berisi huruf')

        # Ubah Gender
        elif pilihan == '2':
            while True:
                gender = input('Gender baru (Laki/Perempuan): ').capitalize()
                if gender in ["Laki", "Perempuan"]:
                    if input(f"Yakin ubah gender menjadi '{gender}'? (Y/N): ").lower() == 'y':
                        listData[index][2] = gender
                        print_table(listData)
                        print("\n\t\t\tData berhasil diubah!")
                    else:
                        print("\n\t\t\tPerubahan dibatalkan.")
                    break
                print('\n\t\t\tInput gender tidak valid.')

        # Ubah Umur
        elif pilihan == '3':
            while True:
                umur_input = input('Masukkan Umur: ')
                if umur_input.isdigit() and 18 <= int(umur_input) <= 65:
                    if input(f"Yakin ubah umur menjadi {umur_input}? (Y/N): ").lower() == 'y':
                        listData[index][3] = int(umur_input)
                        print_table(listData)
                        print("\n\t\t\tData berhasil diubah!")
                    else:
                        print("\n\t\t\tPerubahan dibatalkan.")
                    break
                print('\n\t\t\tUmur harus angka antara 18-65 tahun.')

        # Ubah Divisi
        elif pilihan == '4':
            while True:
                divisi = input('Divisi baru: ').title()
                if divisi.replace(' ', '').isalpha():
                    if input(f"Yakin ubah divisi menjadi '{divisi}'? (Y/N): ").lower() == 'y':
                        listData[index][4] = divisi
                        print_table(listData)
                        print("\n\t\t\tData berhasil diubah!")
                    else:
                        print("\n\t\t\tPerubahan dibatalkan.")
                    break
                print('\n\t\t\tHanya boleh berisi huruf')

        # Ubah Status
        elif pilihan == '5':
            while True:
                status = input('Status baru (Tetap/Kontrak/Internship): ').capitalize()
                if status in ['Tetap', 'Kontrak', 'Internship']:
                    if input(f"Yakin ubah status menjadi '{status}'? (Y/N): ").lower() == 'y':
                        listData[index][5] = status
                        print_table(listData)
                        print("\n\t\t\tData berhasil diubah!")
                    else:
                        print("\n\t\t\tPerubahan dibatalkan.")
                    break
                print('\n\t\t\tInput status tidak valid.')

        # Ubah Gaji
        elif pilihan == '6':
            while True:
                gaji_input = input('Masukkan gaji baru: ')
                if gaji_input.isdigit() and int(gaji_input) > 0:
                    if input(f"Yakin ubah gaji menjadi {gaji_input}? (Y/N): ").lower() == 'y':
                        listData[index][6] = int(gaji_input)
                        print_table(listData)
                        print("\n\t\t\tData berhasil diubah!")
                    else:
                        print("\n\t\t\tPerubahan dibatalkan.")
                    break
                print('\n\t\t\tGaji harus berupa angka.')

        # Ubah Semua Data
        elif pilihan == '7':
            while True:
                # Nama
                while True:
                    nama = input('Nama baru: ').title()
                    if nama.replace(' ', '').isalpha():
                        break
                    print('\n\t\t\tNama hanya boleh huruf.')

                # Gender
                while True:
                    gender = input('Gender baru (Laki/Perempuan): ').capitalize()
                    if gender in ["Laki", "Perempuan"]:
                        break
                    print('\n\t\t\tGender tidak valid.')

                # Umur
                while True:
                    umur_input = input('Masukkan Umur: ')
                    if umur_input.isdigit() and 18 <= int(umur_input) <= 65:
                        umur = int(umur_input)
                        break
                    print('\n\t\t\tUmur harus angka antara 18-65 tahun.')

                # Divisi
                while True:
                    divisi = input('Divisi baru: ').title()
                    if divisi.replace(' ', '').isalpha():
                        break
                    print('\n\t\t\tDivisi hanya boleh huruf.')

                # Status
                while True:
                    status = input('Status baru (Tetap/Kontrak/Internship): ').capitalize()
                    if status in ["Tetap", "Kontrak", "Internship"]:
                        break
                    print('\n\t\t\tStatus tidak valid.')

                # Gaji
                while True:
                    gaji_input = input('Masukkan gaji baru: ')
                    if gaji_input.isdigit() and int(gaji_input) > 0:
                        gaji = int(gaji_input)
                        break
                    print('\n\t\t\tGaji harus angka.')

                # Konfirmasi akhir
                if input("Yakin ingin mengubah semua data? (Y/N): ").lower() == 'y':
                    listData[index] = [id_karyawan, nama, gender, umur, divisi, status, gaji]
                    print("\n\t\t\tData berhasil diubah!")
                else:
                    print("\n\t\t\tPerubahan dibatalkan.")
                break
#================================================================
def menghapus_data():
    while True:
        pilihan = input('''
        === Menu Hapus Data ===
        1. Hapus Berdasarkan ID
        2. Hapus Semua Data
        3. Kembali

        Pilih menu angka : ''').strip()

        if pilihan == '3':
            return

        elif pilihan == '1':
            if not listData:  # cek ulang sebelum proses
                print("\n\t\tData karyawan kosong.")
                continue

            print_table(listData)
            while True:
                id_input = input("\nMasukkan ID karyawan yang ingin dihapus (0 untuk batal): ").strip()

                if id_input == '0':
                    print("\n\t\tPenghapusan dibatalkan.")
                    break

                if not id_input.isdigit():
                    print('ID harus angka.')
                    continue

                id_karyawan = int(id_input)

                index = -1
                for i in range(len(listData)):
                    if listData[i][0] == id_karyawan:
                        index = i
                        break

                if index == -1:
                    print('\n\t\tId tidak ditemukan.')
                    continue

                print(f'Data yang akan dihapus: {listData[index]}')
                checker = input("Apakah anda yakin ingin menghapus data ini? (Y/N) : ").strip().lower()
                if checker == 'y':
                    del listData[index]
                    print_table(listData)
                    print("\n\t\tData berhasil dihapus.")
                else:
                    print("\n\t\tPenghapusan dibatalkan.")
                break

        elif pilihan == '2':
            if not listData:
                print("\n\t\t   Data karyawan kosong.")
                continue
            hapus_all = input("Apakah anda yakin ingin menghapus SEMUA data? (Y/N) : ").strip().lower()
            if hapus_all == 'y':
                listData.clear()
                print_table(listData)
                print("\n\t\tSemua data dihapus.")
                return  # langsung keluar supaya tidak balik ke menu hapus lagi
            else:
                print("\n\t\tPenghapusan semua data dibatalkan.")

        else:
            print("\n\t\tPilihan tidak valid. Coba lagi.")
# ===============================================================
def menu_utama():
    while True:
        pilihan = (input('''	
        ========== Data Karyawan Perusahaan ==========

        List Menu :
        1. Menampilkan Daftar Karyawan 
        2. Menambahkan Data Karyawan Baru
        3. Mengubah Data Karyawan
        4. Menghapus Data Karyawan
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : '''))
        print('\t==============================================')
        
        if pilihan == '1':
            menampilkan_data()
        elif pilihan == '2':
            menambah_data()
        elif pilihan == '3':
            mengubah_data()
        elif pilihan == '4':
            menghapus_data()
            print()
        elif pilihan == '5':
            print('\n\tProgram Selesai.')
            break
        else:
            print('\n\tMasukan angka tersedia !')

menu_utama()
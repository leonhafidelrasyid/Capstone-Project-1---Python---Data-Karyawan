data_karyawan = [
    {'ID': 2016010011001, 'Nama': 'Jordan Belfort','Jenis Kelamin': 'Pria', 'Usia': 72,  'Jabatan': 'Chief Executive Officer', 'Gaji': 200000000, 'Pendidikan': 'S3'},
    {'ID': 2016010011002, 'Nama': 'Gabriella Abigailina', 'Jenis Kelamin': 'Wanita', 'Usia': 61, 'Jabatan': 'Chief Marketing Officer', 'Gaji': 150000000, 'Pendidikan': 'S2'},
    {'ID': 2016010011003, 'Nama': 'Shani Indirani Nationi', 'Jenis Kelamin': 'Wanita', 'Usia': 55, 'Jabatan': 'Chief Human Resource Officer', 'Gaji': 150000000, 'Pendidikan': 'S2'},
    {'ID': 2016010011004, 'Nama': 'Marsha Lenati', 'Jenis Kelamin': 'Wanita', 'Usia': 45, 'Jabatan': 'Chief Finance Officer', 'Gaji': 150000000, 'Pendidikan': 'S2'},
    {'ID': 2016010011005, 'Nama': 'Chaterina Vallencinata', 'Jenis Kelamin': 'Wanita', 'Usia': 49, 'Jabatan': 'Chief Legal Officer', 'Gaji': 120000000, 'Pendidikan': 'S3'},
    {'ID': 2016010011006, 'Nama': 'Jeff Hammerbacher', 'Jenis Kelamin': 'Pria', 'Usia': 40, 'Jabatan': 'Chief Data Officer', 'Gaji': 200000000, 'Pendidikan': 'S3'},
    {'ID': 2023010012006, 'Nama': 'Yilong Ma', 'Jenis Kelamin': 'Wanita', 'Usia': 35, 'Jabatan': 'Data Analyst', 'Gaji': 7200000, 'Pendidikan': 'S1'},
    {'ID': 2023010012006, 'Nama': 'Tan Maliki', 'Jenis Kelamin': 'Wanita', 'Usia': 32, 'Jabatan': 'Data Analyst', 'Gaji': 7200000, 'Pendidikan': 'S1'},
    {'ID': 2023010012006, 'Nama': 'Lillian Chiu', 'Jenis Kelamin': 'Wanita', 'Usia': 35, 'Jabatan': 'Data Analyst', 'Gaji': 7200000, 'Pendidikan': 'S1'},
    {'ID': 2024010013007, 'Nama': 'Julia Fei', 'Jenis Kelamin': 'Wanita', 'Usia': 25, 'Jabatan': 'Data Scientist', 'Gaji': 15000000, 'Pendidikan': 'S1'},
    {'ID': 2024010013007, 'Nama': 'Gon Freecs', 'Jenis Kelamin': 'Pria', 'Usia': 25, 'Jabatan': 'Data Scientist', 'Gaji': 15000000, 'Pendidikan': 'S1'},
    {'ID': 2024010013007, 'Nama': 'Killua Zoldyck', 'Jenis Kelamin': 'Pria', 'Usia': 25, 'Jabatan': 'Data Scientist', 'Gaji': 15000000, 'Pendidikan': 'S1'},
    {'ID': 2024010013007, 'Nama': 'Leorio', 'Jenis Kelamin': 'Pria', 'Usia': 25, 'Jabatan': 'Data Scientist', 'Gaji': 15000000, 'Pendidikan': 'S1'},
    {'ID': 2024010014008, 'Nama': 'Sundas Khalid', 'Jenis Kelamin': 'Wanita', 'Usia': 45, 'Jabatan': 'Data Engineer', 'Gaji': 12000000, 'Pendidikan': 'S2'},
    {'ID': 2024010015009, 'Nama': 'Junaedi Asalam', 'Jenis Kelamin': 'Pria', 'Usia': 31, 'Jabatan': 'Cleaning Service', 'Gaji': 3000000, 'Pendidikan': 'SMA'},
    {'ID': 2024010015009, 'Nama': 'Surya Akasa', 'Jenis Kelamin': 'Pria', 'Usia': 31, 'Jabatan': 'Cleaning Service', 'Gaji': 3000000, 'Pendidikan': 'SMA'},
    {'ID': 2024010015010, 'Nama': 'Raymond Chun', 'Jenis Kelamin': 'Pria', 'Usia': 35, 'Jabatan': 'Finance Manager', 'Gaji': 30000000, 'Pendidikan': 'S2'},
    {'ID': 2024010013011, 'Nama': 'Anya Geraldine', 'Jenis Kelamin': 'Wanita', 'Usia': 33, 'Jabatan': 'Data Scientist', 'Gaji': 15000000, 'Pendidikan': 'S1'},
    {'ID': 2024010013012, 'Nama': 'Sella Rikabuming Rika', 'Jenis Kelamin': 'Wanita', 'Usia': 39, 'Jabatan': 'Senior Data Scientist', 'Gaji': 28000000, 'Pendidikan': 'S2'},
    {'ID': 2024010013012, 'Nama': 'Sony Pangarep', 'Jenis Kelamin': 'Pria', 'Usia': 29, 'Jabatan': 'Senior Data Analyst5', 'Gaji': 28000000, 'Pendidikan': 'S2'},
    {'ID': 2024010013014, 'Nama': 'Ojina Pangaraini', 'Jenis Kelamin': 'Wanita', 'Usia': 40, 'Jabatan': 'Human Resource Manager', 'Gaji': 30000000, 'Pendidikan': 'S2'},
    {'ID': 2024010013015, 'Nama': 'Timothy Donald Duck', 'Jenis Kelamin': 'Wanita', 'Usia': 25, 'Jabatan': 'Marketing Manager', 'Gaji': 50000000, 'Pendidikan': 'S2'},
    {'ID': 2024010015016, 'Nama': 'Sam Altboy', 'Jenis Kelamin': 'Pria', 'Usia': 44, 'Jabatan': 'Senior Machine Learning Engineer', 'Gaji': 80000000, 'Pendidikan': 'S3'}
]

from tabulate import tabulate
from collections import Counter

def display_menu():
    print("\nDatabase Karyawan PT. Singgasana Tbk")
    print("\nMenu:")
    print("1. Lihat Data Karyawan")
    print("2. Tambah Data Karyawan")
    print("3. Hapus Data")
    print("4. Update Data Karyawan")
    print("5. Statistik Karyawan")
    print("6. Keluar")

#Fitur lihat data karyawan
def lihat_data():
    while True:
        print("\nSub Menu Lihat Data Karyawan:")
        print("1. Lihat Semua Data Karyawan")
        print("2. Cari Karyawan")
        print("3. Kembali Ke Menu Utama")
        choice = input("Pilih sub menu: ")
        
        if choice == '1':
            print("\nData Karyawan PT.Singgasana Tbk:")
            headers = ["NIK", "Nama", "Jenis Kelamin", "Umur", "Pendidikan", "Jabatan", "Gaji/Bulan"]
            colalign = ("center", "center", "center", "center", "center", "center", "center")
            formatted_data = [[k['ID'], k['Nama'], k['Jenis Kelamin'], k['Usia'], k['Pendidikan'], k['Jabatan'], f"Rp {k['Gaji']:,}".replace(",", ".")] for k in data_karyawan]
            print(tabulate(formatted_data, headers, tablefmt="grid", colalign=colalign))
        
        elif choice == '2':
            print("\nSub Menu Cari Karyawan:")
            print("1. Cari Karyawan Berdasarkan Nama")
            print("2. Cari Karyawan Berdasarkan NIK")
            print("3. Kembali Ke Sub Menu Lihat Data Karyawan")
            sub_choice = input("Pilih sub menu: ")
            
            if sub_choice == '1':
                nama = input("Masukkan nama karyawan yang ingin dicari: ").lower()
                found = False
                for karyawan in data_karyawan:
                    if nama in karyawan['Nama'].lower():
                        headers = ["NIK", "Nama", "Jenis Kelamin", "Umur", "Pendidikan", "Jabatan", "Gaji/Bulan"]
                        colalign = ("center", "center", "center", "center", "center", "center", "center")
                        formatted_karyawan = [[karyawan['ID'], karyawan['Nama'], karyawan['Jenis Kelamin'], karyawan['Usia'], karyawan['Pendidikan'], karyawan['Jabatan'], f"Rp {karyawan['Gaji']:,}".replace(",", ".")]]
                        print(tabulate(formatted_karyawan, headers, tablefmt="grid", colalign=colalign))
                        found = True
                if not found:
                    print("Karyawan dengan nama tersebut tidak ditemukan.")
            
            elif sub_choice == '2':
                nik = input("Masukkan NIK karyawan yang ingin dicari: ")
                found = False
                for karyawan in data_karyawan:
                    if str(karyawan['ID']) == nik:
                        headers = ["NIK", "Nama", "Jenis Kelamin", "Umur", "Pendidikan", "Jabatan", "Gaji/Bulan"]
                        colalign = ("center", "center", "center", "center", "center", "center", "center")
                        formatted_karyawan = [[karyawan['ID'], karyawan['Nama'], karyawan['Jenis Kelamin'], karyawan['Usia'], karyawan['Pendidikan'], karyawan['Jabatan'], f"Rp {karyawan['Gaji']:,}".replace(",", ".")]]
                        print(tabulate(formatted_karyawan, headers, tablefmt="grid", colalign=colalign))
                        found = True
                        break
                if not found:
                    print("Karyawan dengan NIK tersebut tidak ditemukan.")
            
            elif sub_choice == '3':
                continue
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
#Fitur Menambah data
def tambah_data():
    while True:
        print("\nSub Menu Tambah Data Karyawan:")
        print("1. Tambah Data Karyawan")
        print("2. Kembali Ke Menu Utama")
        choice = input("Pilih sub menu: ")

        if choice == '1':
            try:
                new_nik = int(input("Masukkan NIK Karyawan yang ingin ditambahkan: "))
                for data in data_karyawan:
                    if data['ID'] == new_nik:
                        print(f"\nData karyawan ini sudah ada atas nama: {data['Nama']}")
                        return
                new_nama = input("Masukkan Nama Karyawan: ")
                new_jk = input(f"Masukkan Jenis Kelamin (Pria/Wanita) {new_nama}: ")
                new_umur = int(input("Masukan Umur Karyawan: "))
                new_posisi = input("Masukan Posisi Karyawan: ")
                new_gaji = int(input("Masukkan Gaji Karyawan: "))
                new_pendidikan = input("Masukkan Pendidikan Karyawan: ")

                print("\nData yang telah diinput:")
                new_data = {'ID': new_nik, 'Nama': new_nama, 'Jenis Kelamin': new_jk, 'Usia': new_umur, 'Jabatan': new_posisi, 'Gaji': new_gaji, 'Pendidikan': new_pendidikan}
                print(tabulate([new_data], headers="keys", tablefmt="grid"))

                confirm = input("Apakah data yang diinput sudah benar? (y/n): ")
                if confirm.lower() == 'y':
                    data_karyawan.append(new_data)
                    print(f"Karyawan dengan nama {new_nama} telah ditambahkan.")
                else:
                    print("Data tidak ditambahkan. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Pastikan NIK, umur, dan gaji adalah angka.")
        elif choice == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#Fitur menghapus data
def hapus_data():
    while True:
        print("\nSub Menu Hapus Data Karyawan:")
        print("1. Hapus Data Karyawan Berdasarkan NIK")
        print("2. Hapus Data Karyawan Berdasarkan Nama")
        print("3. Kembali Ke Menu Utama")
        choice = input("Pilih sub menu: ")
        
        if choice == '1':
            del_nik = int(input("Masukkan NIK Karyawan yang ingin dihapus: "))
            for data in data_karyawan:
                if data['ID'] == del_nik:
                    print("\nData Karyawan yang akan dihapus:")
                    print(tabulate([data.values()], headers=data.keys(), tablefmt="grid"))
                    confirm = input("Apakah Anda yakin ingin menghapus data karyawan ini? (y/n): ")
                    if confirm.lower() == 'y':
                        data_karyawan.remove(data)
                        print(f"Karyawan dengan NIK: {del_nik} atas nama: {data['Nama']} telah dihapus.")
                        return
                    else:
                        print("Penghapusan dibatalkan.")
                        return
            print(f"Karyawan dengan NIK {del_nik} tidak ditemukan.")
        
        elif choice == '2':
            del_nama = input("Masukkan Nama Karyawan yang ingin dihapus: ")
            for data in data_karyawan:
                if data['Nama'].lower() == del_nama.lower():
                    print("\nData Karyawan yang akan dihapus:")
                    print(tabulate([data.values()], headers=data.keys(), tablefmt="grid"))
                    confirm = input("Apakah Anda yakin ingin menghapus data karyawan ini? (y/n): ")
                    if confirm.lower() == 'y':
                        data_karyawan.remove(data)
                        print(f"Karyawan dengan nama: {del_nama} telah dihapus.")
                        return
                    else:
                        print("Penghapusan dibatalkan.")
                        return
            print(f"Karyawan dengan nama {del_nama} tidak ditemukan.")
        
        elif choice == '3':
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("Pilihan tidak valid. Silakan coba lagi.")

#Fitur mengupdate data
def ubah_data():
    while True:
        print("\nSub Menu:")
        print("1. Ubah data berdasarkan NIK")
        print("2. Ubah data berdasarkan Nama")
        print("3. Kembali ke menu utama")
        pilihan = int(input("Masukkan pilihan: "))
        
        if pilihan == 1:
            update_nik = int(input("Masukkan NIK Karyawan yang ingin diubah datanya: "))
            for data in data_karyawan:
                if data['ID'] == update_nik:
                    print("\nData Karyawan:")
                    print(tabulate([data.values()], headers=data.keys(), tablefmt="grid"))
                    
                    confirm = input("Apakah Anda yakin ingin mengupdate data karyawan ini? (y/n): ")
                    if confirm.lower() != 'y':
                        print("Pembaharuan data dibatalkan.")
                        return
                    
                    print("\nKolom yang bisa diubah:")
                    print("1. Nama")
                    print("2. Jenis Kelamin")
                    print("3. Umur")
                    print("4. Jabatan")
                    print("5. Gaji")
                    print("6. Pendidikan")
                    kolom = int(input("Masukkan nomor kolom yang ingin diubah: "))
                    
                    if kolom == 1:
                        new_value = input("Masukkan nama baru: ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah nama karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Nama'] = new_value
                        else:
                            print("Pembaharuan nama dibatalkan.")
                            return
                    elif kolom == 2:
                        new_value = input("Masukkan jenis kelamin baru (L/P): ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah jenis kelamin karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Jenis Kelamin'] = new_value
                        else:
                            print("Pembaharuan jenis kelamin dibatalkan.")
                            return
                    elif kolom == 3:
                        new_value = int(input("Masukkan umur baru: "))
                        confirm = input(f"Apakah Anda yakin ingin mengubah umur karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Usia'] = new_value
                        else:
                            print("Pembaharuan umur dibatalkan.")
                            return
                    elif kolom == 4:
                        new_value = input("Masukkan jabatan baru: ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah jabatan karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Jabatan'] = new_value
                        else:
                            print("Pembaharuan jabatan dibatalkan.")
                            return
                    elif kolom == 5:
                        new_value = int(input("Masukkan gaji baru: "))
                        confirm = input(f"Apakah Anda yakin ingin mengubah gaji karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Gaji'] = new_value
                        else:
                            print("Pembaharuan gaji dibatalkan.")
                            return
                    elif kolom == 6:
                        new_value = input("Masukkan pendidikan baru: ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah pendidikan karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Pendidikan'] = new_value
                        else:
                            print("Pembaharuan pendidikan dibatalkan.")
                            return
                    else:
                        print("Kolom tidak valid.")
                        return
                    
                    print(f"Data karyawan dengan NIK {update_nik} telah diubah.")
                    return
            print(f"Karyawan dengan NIK {update_nik} tidak ditemukan.")
        
        elif pilihan == 2:
            update_nama = input("Masukkan Nama Karyawan yang ingin diubah datanya: ")
            for data in data_karyawan:
                if data['Nama'].lower() == update_nama.lower():
                    print("\nData Karyawan:")
                    print(tabulate([data.values()], headers=data.keys(), tablefmt="grid"))
                    
                    confirm = input("Apakah Anda yakin ingin mengupdate data karyawan ini? (y/n): ")
                    if confirm.lower() != 'y':
                        print("Pembaharuan data dibatalkan.")
                        return
                    
                    print("\nKolom yang bisa diubah:")
                    print("1. Nama")
                    print("2. Jenis Kelamin")
                    print("3. Umur")
                    print("4. Jabatan")
                    print("5. Gaji")
                    print("6. Pendidikan")
                    kolom = int(input("Masukkan nomor kolom yang ingin diubah: "))
                    
                    if kolom == 1:
                        new_value = input("Masukkan nama baru: ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah nama karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Nama'] = new_value
                        else:
                            print("Pembaharuan nama dibatalkan.")
                            return
                    elif kolom == 2:
                        new_value = input("Masukkan jenis kelamin baru (L/P): ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah jenis kelamin karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Jenis Kelamin'] = new_value
                        else:
                            print("Pembaharuan jenis kelamin dibatalkan.")
                            return
                    elif kolom == 3:
                        new_value = int(input("Masukkan umur baru: "))
                        confirm = input(f"Apakah Anda yakin ingin mengubah umur karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Usia'] = new_value
                        else:
                            print("Pembaharuan umur dibatalkan.")
                            return
                    elif kolom == 4:
                        new_value = input("Masukkan jabatan baru: ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah jabatan karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Jabatan'] = new_value
                        else:
                            print("Pembaharuan jabatan dibatalkan.")
                            return
                    elif kolom == 5:
                        new_value = int(input("Masukkan gaji baru: "))
                        confirm = input(f"Apakah Anda yakin ingin mengubah gaji karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Gaji'] = new_value
                        else:
                            print("Pembaharuan gaji dibatalkan.")
                            return
                    elif kolom == 6:
                        new_value = input("Masukkan pendidikan baru: ")
                        confirm = input(f"Apakah Anda yakin ingin mengubah pendidikan karyawan ini menjadi {new_value}? (y/n): ")
                        if confirm.lower() == 'y':
                            data['Pendidikan'] = new_value
                        else:
                            print("Pembaharuan pendidikan dibatalkan.")
                            return
                    else:
                        print("Kolom tidak valid.")
                        return
                    
                    print(f"Data karyawan dengan nama {update_nama} telah diubah.")
                    return
            print(f"Karyawan dengan nama {update_nama} tidak ditemukan.")
        
        elif pilihan == 3:
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


#Fitur statistik karyawan
def statistik_karyawan():
    while True:
        print("\nStatistik Karyawan:")
        print("1. Gaji karyawan tertinggi")
        print("2. Gaji karyawan terendah")
        print("3. Rata-rata gaji seluruh karyawan")
        print("4. Jumlah karyawan berdasarkan pendidikan")
        print("5. Persentase jenis kelamin karyawan")
        print("6. Kembali ke menu utama")
        
        choice = input("Pilih submenu (1-6): ")
        
        if choice == '1':
            highest_salary = max(data_karyawan, key=lambda x: x['Gaji'])
            print(f"\nGaji tertinggi: Rp {highest_salary['Gaji']:,}".replace(',', '.'))
            print(f"NIK: {highest_salary['ID']}, Nama: {highest_salary['Nama']}, Jenis Kelamin: {highest_salary['Jenis Kelamin']}, Umur: {highest_salary['Usia']}, Jabatan: {highest_salary['Jabatan']}")
        elif choice == '2':
            lowest_salary = min(data_karyawan, key=lambda x: x['Gaji'])
            print(f"\nGaji terendah: Rp {lowest_salary['Gaji']:,}".replace(',', '.'))
            print(f"NIK: {lowest_salary['ID']}, Nama: {lowest_salary['Nama']}, Jenis Kelamin: {lowest_salary['Jenis Kelamin']}, Umur: {lowest_salary['Usia']}, Jabatan: {lowest_salary['Jabatan']}")
        elif choice == '3':
            rata_rata = sum(data['Gaji'] for data in data_karyawan) / len(data_karyawan)
            print(f"\nRata-rata gaji seluruh karyawan: Rp {rata_rata:,.0f}".replace(',', '.'))
        elif choice == '4':
            pendidikan_counter = Counter(data['Pendidikan'] for data in data_karyawan)
            print("\nJumlah karyawan berdasarkan pendidikan:")
            for pendidikan, jumlah in pendidikan_counter.items():
                print(f"{pendidikan}: {jumlah} karyawan")
        elif choice == '5':
            jenis_kelamin_counter = Counter(data['Jenis Kelamin'] for data in data_karyawan)
            total_karyawan = len(data_karyawan)
            persentase_pria = (jenis_kelamin_counter['Pria'] / total_karyawan) * 100
            persentase_wanita = (jenis_kelamin_counter['Wanita'] / total_karyawan) * 100
            print(f"\nPersentase jenis kelamin karyawan:")
            print(f"Pria: {persentase_pria:.2f}%")
            print(f"Wanita: {persentase_wanita:.2f}%")
        elif choice == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih submenu (1-11).")

def main():
    while True:
        display_menu()
        choice = input("Pilih menu (1-6): ")
        if choice == '1':       
            lihat_data()
        elif choice == '2':
            tambah_data()
        elif choice == '3':
            hapus_data()
        elif choice == '4':
            ubah_data()
        elif choice == '5':
            statistik_karyawan()      
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()


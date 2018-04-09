def pembayaran():
    print("\n===================================================")
    nama = input("\n\tMasukan Nama = ")
    nim = input("\tMasukan NIM = ")
    semester = input("\tMasukan Smester Saat ini = ")
    print("\n\t---Pilihan Pembayaran---")
    print("\t1. Pembayaran SPP")
    print("\t2. Pembayaran UTS")
    print("\t3. Pembayaran UAS")
    print("\t4. Pembayaran SPP & UTS")
    print("\t5. Pembayaran SPP & UAS")
    pilih = input("\n\tSilahkan Pilih: ")
    if pilih == "1":
        spp()
    elif pilih == "2":
        uts()
    elif pilih == "3":
        uas()
    elif pilih == "4":
        spp_uts()
    elif pilih == "5":
        spp_uas()
    else:
        exit
        tanya()

def spp():
    bulan = int(input("\n\tJumlah Bulan Yang Dibayarkan = "))
    bulan = float(bulan)
    total = 350000*bulan
    print("======================================================")
    print("\tTotal Bayar SPP Rp.350000*",bulan," = Rp.",total)
                  
def uas():
    matkul = int(input("\n\tJumlah Mata Kuliah = "))
    matkul = float(matkul)
    byr_uas = 50000*matkul
    print("=======================================================")
    print("\tTotal Bayar UAS Rp.5000*",matkul," = Rp.",byr_uas)

def uts():
    matkul_uts = int(input("\n\tJumlah Mata Kuliah = "))
    matkul_uts = float(matkul_uts)
    byr_uts = 25000*matkul_uts
    print("=======================================================")
    print("\tTotal Bayar UTS Rp.25000*",matkul_uts," = Rp.",byr_uts)

def spp_uas():
    bulan = int(input("\n\tJumlah Bulan Yang Dibayarkan= "))
    matkul = int(input("\n\tJumlah Mata Kuliah= "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 350000*bulan
    byr_uas = 50000*matkul
    total = total_spp + byr_uas + 5000
    print("\n\tTotal Bayar SPP Rp.350000*",bulan,"=Rp.",total_spp)
    print("\tTotal Bayar UAS Rp.50000*",matkul,"=Rp.",byr_uas)
    print("\tBiaya Tambahan Server Sebesar Rp.5000")
    print("========================================================")
    print("\tTotal Yang Harus Dibayar",total)

def spp_uts():
    bulan = int(input("\n\tJumlah Bulan Yang Dibayarkan= "))
    matkul = int(input("\n\tJumlah Mata Kuliah= "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 350000*bulan
    byr_uts = 25000*matkul
    total = total_spp + byr_uts + 5000
    print("\tTotal Bayar SPP Rp.350000*",bulan,"=Rp.",total_spp)
    print("\n\tTotal Bayar UTS Rp.25000*",matkul,"=Rp.",byr_uts)
    print("\tBiaya Tambahan Server Sebesar Rp.5000")
    print("========================================================")
    print("\tTotal Yang Harus Dibayar",total)

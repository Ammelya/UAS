import texttable as tt
import getpass
from DataMahasiswa.input_nilai import nilai_mahasiswa
from DataMahasiswa.pembayaran import pembayaran
from DataMahasiswa.cal import menu_cal


def menu() :
    print('\n\t=============================')
    print('\tProgram Pelita Bangsa 17.C1')
    print('\t=============================')
    print('\t1. Penilaian')
    print('\t2. Pembayaran')
    print('\t3. Kalkulator')
    print('\t=============================')
    print('\tSilahkan pilih 1-3')
    print(' ')
    pil = input('\tMasukan pilihan :')
    if pil == '1':
        nilai_mahasiswa()
    elif pil == '2':
        pembayaran()
    elif pil == '3':
        menu_cal()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali Ke Menu (y/t)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah Input...!!!")

username = input("\nUsername :")
password = getpass.getpass()
print("===========================================================")

if username == "ammel" and password == "ammelyas22":
	menu()

else:
	print ("Maaf password atau username anda salah........")
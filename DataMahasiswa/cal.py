def tambah ():
    print('\t1. Penjumlahan')
    a = int(input('\tMasukan nilai x= '))
    b = int(input('\tMasukan nilai y= '))
    c = a+b
    print ('\tx+y=',c)
    tanya ()
def kurang ():
    print('\t2. Pengurangan')
    a = int(input('\tMasukan nilai x= '))
    b = int(input('\tMasukan nilai y= '))
    c = a-b
    print ('\tx-y=',c)
    tanya ()
def bagi ():
    print('\t3. Pembagian')
    a = int(input('\tMasukan nilai x= '))
    b = int(input('\tMasukan nilai y= '))
    c = a/b
    print ('\tx/y=',c)
    tanya ()
def kali ():
    print('\t4. Perkalian')
    a = int(input('\tMasukan nilai x= '))
    b = int(input('\tMasukan nilai y= '))
    c = a*b
    print ('\tx*y=',c)
    tanya ()
    
def tanya():
    tanya = input("\n\tKembali ke menu kalkulator (y/t)? ")
    if tanya == "y":
        menu_cal()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...........!!!")
def menu_cal() :
    print('\n\t=============================')
    print('\tProgram Kalkulator Sederhana')
    print('\t=============================')
    print('\t1. Penjumlahan')
    print('\t2. Pengurangan')
    print('\t3. Pembagian')
    print('\t4. Perkalian')
    print('\t=============================')
    print('\tSilahkan pilih 1-4')
    print(' ')
    pil = input('\tMasukan pilihan :')
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else:
        print ('\tMaaf, input yang Anda masukan salah')
        print ('\tCoba ulangi kembali')
        tanya () 

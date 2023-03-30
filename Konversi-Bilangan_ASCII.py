try:
    print("===== Ujian Sekolah DP1-DP3 =====")
    print('Konversi dari :')
    print('1. Desimal')
    print('2. Biner')
    print('3. Oktal')
    print('4. Hexadecimal')
    print('5. ASCII')
    print('0. exit')

    masukan = int(input('Masukan Pilihan : '))
    print('')

    while masukan > 5 or masukan < 0:
        print('Silahkan Masukan Angka Yang Tersedia Di Menu.')
        masukan = int(input('Masukan Pilihan : '))
        print('')

    while masukan != 0:
        tampil = ''
        biner = 0
        hexa = 0
        pembalik = []
        cetak = []

        # KONVERSI DECIMAL
        if masukan == 1:
            print('')
            print('Konversi Ke :')
            print('1. Biner')
            print('2. Oktal')
            print('3. Hexadecimal')
            print('')
            menu = int(input('Masukan Pilihan : '))
            print('')

            while menu > 4 or menu < 0:
                print('Silahkan Masukan Angka Yang Tersedia Di Menu.')
                menu = int(input('Masukan Pilihan : '))
                print('')
            # DESIMAL - BINER
            if menu == 1:
                desimal = int(input('Masukan Angka Desimal:'))
                print('')
                while desimal != 0:
                    hasil = desimal % 2
                    cetak.insert(0, str(hasil))
                    desimal = desimal//2
                    if desimal == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)
                print('')
            # DESIMAL - OKTALL
            elif menu == 2:
                desimal = int(input('Masukan Angka Desimal : '))
                print('')
                while desimal != 0:
                    hasil = desimal % 8
                    cetak.insert(0, str(hasil))
                    desimal = desimal//8
                    if desimal == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)
                print('')
            # DESIMAL - HEX
            elif menu == 3:
                desimal = int(input('Masukan Angka Desimal : '))
                print('')
                while desimal != 0:
                    hasil = desimal % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    desimal = desimal//16
                    if desimal == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)
                print('')

        # KONVERSI BINER
        elif masukan == 2:
            print('Konversi Ke :')
            print('1. Desimal')
            print('2. Oktal')
            print('3. Hexadecimal')
            menu = int(input('Masukan Pilihan :'))
            print('')

            while menu > 4 or menu < 0:
                print('Silahkan Masukan Angka Yang Ada Pada Menu.')
                menu = int(input('Masukan Pilihan : '))
                print('')
            # BINER - DESIMAL
            if menu == 1:
                bin = input('Masukan Biner :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(2**i)
                print('Hasilnya Adalah : ', biner)
                print('')
            # BINER - OKTALL
            if menu == 2:
                bin = input('Masukan Biner :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(2**i)

                while biner != 0:
                    hasil = biner % 8
                    cetak.insert(0, str(hasil))
                    biner = biner//8
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)
                print('')
            # BINER - HEXA
            if menu == 3:
                bin = input('Masukan Biner :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(2**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)
                print('')

        # KONVERSI OKTAL
        elif masukan == 3:
            print('Konversi Ke :')
            print('1. Desimal')
            print('2. Biner')
            print('3. Hexadecimal')
            menu = int(input('Masukan Pilihan :'))
            print('')

            while menu > 4 or menu < 0:
                print('Silahkan Masukan Angka Yang Tersedia Di Menu.')
                menu = int(input('Masukan Pilihan : '))
                print('')
            # OKTALL - DESIMAL
            if menu == 1:
                bin = input('Masukan Oktal :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(8**i)
                print('Hasilnya Adalah : ', biner)
                print('')
            # OKTALL - BINER
            if menu == 2:
                bin = input('Masukan Oktal :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 2
                    cetak.insert(0, str(hasil))
                    biner = biner//2
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)
                print('')
            # OKTALL - HEXA
            if menu == 3:
                bin = input('Masukan Oktal :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)
                print('')

        # KONVERSI HEXADECIMAL
        elif masukan == 4:
            print('Konversi Ke :')
            print('1. Desimal')
            print('2. Biner')
            print('3. Oktal')
            menu = int(input('Masukan Pilihan :'))
            print('')

            while menu > 4 or menu < 0:
                print('Silahkan Masukan Angka Yang Tersedia Di Menu.')
                menu = int(input('Masukan Pilihan : '))
                print('')
            # HEXA - DESIMAL
            if menu == 1:
                hexa = input('Masukan Hexadesimal: ')
                decimal = 0
                for i in range(len(hexa)):
                    digit = hexa[i]
                    if digit.isdigit():
                        decimal += int(digit)*(16**(len(hexa)-i-1))
                    elif digit in ['a', 'A']:
                        decimal += 10*(16**(len(hexa)-i-1))
                    elif digit in ['b', 'B']:
                        decimal += 11*(16**(len(hexa)-i-1))
                    elif digit in ['c', 'C']:
                        decimal += 12*(16**(len(hexa)-i-1))
                    elif digit in ['d', 'D']:
                        decimal += 13*(16**(len(hexa)-i-1))
                    elif digit in ['e', 'E']:
                        decimal += 14*(16**(len(hexa)-i-1))
                    elif digit in ['f', 'F']:
                        decimal += 15*(16**(len(hexa)-i-1))
                    else:
                        print('Input tidak valid')
                        exit()
                print('Hasilnya adalah:', decimal)

            # HEXA - Biner
            if menu == 2:
                hexa = input('Masukkan heksadesimal: ')

                for digit in hexa:
                    if digit not in '0123456789ABCDEFabcdef':
                        print('Input tidak valid.')
                        exit()

                biner = ''
                for digit in hexa:
                    if digit in '0123456789':
                        biner += bin(int(digit))[2:].zfill(4)
                    else:
                        if digit in 'ABCDEF':
                            nilai = 10 + 'ABCDEF'.index(digit)
                        else:
                            nilai = 10 + 'abcdef'.index(digit)
                        biner += bin(nilai)[2:]

                biner = biner.lstrip("0")  # Menghapus nol di depan
                if not biner:  # Jika hasil biner kosong, beri nilai 0
                    biner = "0"

                print('Hasilnya Adalah:', biner)


            # HEXA - Oktal
            if menu == 3:
                hexa = input('Masukkan Bilangan Heksadesimal : ')
                tampil = ""
                cetak = []
                hexa_decimal = 0
                for i in range(len(hexa)):
                    if hexa[i] == 'A':
                        hasil = 10
                    elif hexa[i] == 'B':
                        hasil = 11
                    elif hexa[i] == 'C':
                        hasil = 12
                    elif hexa[i] == 'D':
                        hasil = 13
                    elif hexa[i] == 'E':
                        hasil = 14
                    elif hexa[i] == 'F':
                        hasil = 15
                    else:
                        hasil = int(hexa[i])
                    hexa_decimal += hasil * (16 ** (len(hexa)-i-1))

                while hexa_decimal != 0:
                    hasil = hexa_decimal % 8
                    cetak.insert(0, str(hasil))
                    hexa_decimal = hexa_decimal // 8
                    if hexa_decimal == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('Hasilnya Adalah : ', tampil)

        # KONVERSI ASCII
        elif masukan == 5:
            string = input("Masukkan string yang ingin dikonversi ke ASCII: ")

            # STRING - ASCII
            ascii_result = ""
            for char in string:
                ascii_result += str(ord(char)) + " "
            print("ASCII: ", ascii_result)

            # STRING - DESIMAL
            decimal_result = ""
            for char in string:
                decimal_result += str(ord(char)) + " "
            print("Desimal: ", decimal_result)

            # STRING - BINER
            binary_result = ""
            for char in string:
                binary_char = bin(ord(char))[2:].zfill(8) + " " # adding leading zeros with zfill()
                binary_result += binary_char
            print("Biner: ", binary_result)

            # STRING - OKTAL
            octal_result = ""
            for char in string:
                octal_result += oct(ord(char))[2:] + " "
            print("Oktal: ", octal_result)

            # STRING - HEXADESIMAL
            hex_result = ""
            for char in string:
                hex_result += hex(ord(char))[2:] + " "
            print("Hexadesimal: ", hex_result)

        print("===== Ujian Sekolah DP1-DP3 =====")
        print('Konversi dari :')
        print('1. Desimal')
        print('2. Biner')
        print('3. Oktal')
        print('4. Hexadecimal')
        print('5. ASCII')
        print('0. exit')
        masukan = int(input('masukan pilihan : '))
        print('')

except:
    print('Anda Memasukan Inputan Dilarang!. Maaf Program Terhenti:)')
    
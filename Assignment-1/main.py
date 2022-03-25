import os
from tabulate import tabulate
from graphrepresentation import graphrepresentation

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main(): 
    keepRun = 1
    while keepRun == 1:
        cls()
        print("==Graph Representation==")
        print("1. Lihat Daftar Nama")
        print("2. Tambahkan Nama")
        print("3. Atur Relasi")
        print("4. Tampilkan Adjacency Graph")
        print("5. Tampilkan Adjacency List")
        print("6. Tugas Pertama")
        print("0. EXIT")
        choose = str(input("pilihan --> "))
        if choose == "1":
            print("==Daftar Nama==")
            no = 1
            for nama in gp.getNama():
                print(no,". ", nama, end="\n")
                no += 1
            enter = input("press ENTER to continue ... ")
        elif choose == "2":
            for i in range(2):
                nama = str(input("nama ke-{} ".format(i+1)))
                gp.setNama(nama)
            addMore = str(input("ingin menambah nama lagi? (Y/n) -> "))
            if addMore == "Y" or "y":
                howMuch = int(input("berapa banyak -> "))
                for i in range(howMuch):
                    nama = str(input("nama ke-{} ".format(i+1)))
                    gp.setNama(nama)
            elif addMore == "N" or "n":
                pass
            else:
                pass
            enter = input("press ENTER to continue ... ")
        elif choose == "3":
            print("==Daftar Nama==")
            no = 1
            for nama in gp.getNama():
                print(no,". ", nama, end="\n")
                no += 1
            howMuch = int(input("berapa banyak relasi -> "))
            for i in range(howMuch):
                cls()
                print("==Daftar Nama==")
                no = 1
                for nama in gp.getNama():
                    print(no,". ", nama, end="\n")
                    no += 1
                name = str(input("nama -> "))
                teman = str(input("berteman dengan -> "))
                gp.setRelation(name, teman)
            
            enter = input("relasi telah dibuat, press ENTER to continue ... ")
        elif choose == "4":
            table = [[""]]
            for name in gp.getNama():
                table[0].append(name)
            relasi = []
            for i in range(len(gp.getNama())):
                relasi.append([gp.getNama()[i]])
            for i in range(len(relasi)):
                for j in range(len(gp.getRelation()[i])):
                    relasi[i].append(gp.getRelation()[i][j])
            for i in range(len(relasi)):
                table.append(relasi[i])

            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

            enter = input("press ENTER to continue ... ")

        elif choose == "5":
            table = [["vertex", "adjacent"]]
            row = []
            for i in range(len(gp.getNama())):
                row.append([])
                row[i].append(gp.getNama()[i])
                row[i].append([])
                
            for i in range(len(row)):
                notNull = 0
                for j in range(len(gp.getRelation()[i])):
                    if gp.getRelation()[i][j] == 1:
                        row[i][1].append(gp.getNama()[j])
                    else:
                        row[i][1].append("null")
            for i in range(len(row)):
                table.append(row[i])
            for i in range(len(row)):
                Null = 0
                for j in range(len(row[i][1])):
                    if row[i][1][j] == "null":
                        Null += 1
                    if Null == len(row[i][1]):
                        for k in range(len(row[i][1])):
                            row[i][1].pop(0)
                        row[i][1].append("null")
                if Null <= len(row[i][1])-1:
                    while row[i][1].count("null") > 0:
                        row[i][1].remove("null")

            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            
            enter = input("press ENTER to continue ... ")

        elif choose == "6":
            gp.setNama('Joko')
            gp.setNama('Susi')
            gp.setNama('Budi')
            gp.setNama('Yayuk')
            gp.setNama('Joni')
            gp.setRelation('Joko', 'Susi')
            gp.setRelation('Joko', 'Budi')
            gp.setRelation('Susi', 'Joko')
            gp.setRelation('Susi', 'Budi')
            gp.setRelation('Susi', 'Yayuk')
            gp.setRelation('Susi', 'Joni')
            gp.setRelation('Budi', 'Joko')
            gp.setRelation('Budi', 'Susi')
            gp.setRelation('Budi', 'Yayuk')
            gp.setRelation('Yayuk', 'Susi')
            gp.setRelation('Yayuk', 'Budi')
            gp.setRelation('Yayuk', 'Joni')
            gp.setRelation('Joni', 'Susi')
            gp.setRelation('Joni', 'Yayuk')

            enter = input("Tugas Selesai, press ENTER to continue ... ")

        elif choose == "0":
            keepRun += 1

        
if __name__ == "__main__":
    gp = graphrepresentation()
    main()
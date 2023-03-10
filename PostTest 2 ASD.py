import os
os.system("cls")

def LINEARSEARCH(array,xy):
    for l in range(len(array)):
        if type(array[l]) == list and v and a:
            searchdata = LINEARSEARCH(array[l],xy)
            if searchdata == -1:
                return -1
            else:
                print(xy, "ditemukan di indeks" ,l, "kolom" ,searchdata)
                exit()
        elif array[l] == xy:
            return l
    return -1

def LINIER():
    print("""
===============================================================
|Menampilkan Index Pada Setiap Data Yang Terdapat Pada List ^.^|
===============================================================
""")
    for y in range(len(array)):
        if array[y] == s:
            print(s, "di itemukan Di Index", y)
        elif array[y] == i:
            print(i, "di itemukan Di Index", y)
        elif array[y] == l:
            print(l, "di itemukan Di Index", y)
        else:
            for z in range(len(array)):
                if type(array[z]) == list and v and a:
                    searchdata = LINEARSEARCH(array[z], v)
                    print(v, "ditemukan di indeks" ,z, "kolom" ,searchdata)
                    searchdata = LINEARSEARCH(array[z], a)
                    print(a, "ditemukan di indeks" ,z, "kolom" ,searchdata)
                elif array[z] == v and a:
                    return z
            return -1

array = ["Arsel","Avivah","Daiva",["Wahyu","Wibi"]]
s = "Arsel"
i = "Avivah"
l = "Daiva"
v = "Wahyu"
a = "Wibi"

LINIER()
import numpy as np # magic square merupakan matriks, numpy digunakan untuk perhitungan aljabar
#Muhammad Fadhil_F55120068

def magic_square(matrix_ms):    #mendefinisikan fungsi magic square
    i_size = len(matrix_ms[0])
    sum_list = []

    for col in range(i_size): #untuk menentukan kode vertikal squarenya
        sum_list.append(sum(row[col] for row in matrix_ms))

        sum_list.extend([sum(lines) for lines in matrix_ms]) #untuk menentukan kode horizontal / sum untuk menjumlah list

        dl_result = 0                                               #data membuat list kosong untuk penyimpanan nilai
        for i in range(0, i_size):
            dl_result += matrix_ms[i][i]
        sum_list.append(dl_result)
        dl_result = 0
        for i in range(i_size-1, -1, -1):
            dl_result += matrix_ms[i][i]
        sum_list.append(dl_result)
        if len(set(sum_list)) > 1:
            return False
        return True


data = []  #untuk inisialisasikan data dengan data yang kosong
n = 9      #menentukan banyaknya inputan

for i in range(0, n): #untuk proses iterasi terhadap nilainya sampai nilai ke n
    ele = int(input("Enter nilai Square : "))
    data.append(ele)  #menambahkan data elemennya
print(data)           #untuk menampilkan data yang dimasukkan

data = np.reshape(data, (3, 3)) #untuk mengubah data vektor menjadi data array 3x3
print(data) #menampilkan data dari perhitungan diatas
print("\n Nilai Magic Square yang dimasukkan adalah", magic_square(data)) #menampilkan data dari fungsi def magic square
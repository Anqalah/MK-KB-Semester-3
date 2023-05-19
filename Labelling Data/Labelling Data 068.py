#Nama : Muhammad Fadhil
#NIM : F55120068
#Kelas : B

import numpy as np
from sklearn import preprocessing

# sample input labels
input_labels = ['AOV','Btom','Comet','Pisi','Ealah','Flawless','Good Game']

#Creating the label encoder
encoder = preprocessing.LabelEncoder()
#menormalisasi data dari input labels,
#input label disini menggunakan tipe data String, tapi sklearn hanya bisa membaca data numerik
encoder.fit(input_labels)

#encoding a set of labels
test_labels = ['Btom','AOV','Ealah']
#dimasukkan data sampel

encoded_values = encoder.transform(test_labels)
#.transform, mengubah data string menjadi angka
#utf-8 membaca data lebih kompleks
print("\nLabels =", test_labels) #kenapa test labels karena kita input
print("Encoded values =", list(encoded_values)) #data yang telah dinormalisasi akan muncul angka bukan string

#decoding a set of values
encoded_values = [5, 4, 3, 6,]
#mengembalikan nilai angka ke string

decoded_list = encoder.inverse_transform(encoded_values)
#dipanggil encoded, mengembalikan nilai yang telah dinormalisasi
print("\nEncoded values =", encoded_values)
print("\nDecoded labels =", list(decoded_list))
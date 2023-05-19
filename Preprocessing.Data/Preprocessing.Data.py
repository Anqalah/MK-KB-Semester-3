#Nama  : Muhammad Fadhil
#NIM   : F55120068
import numpy as np
from sklearn import preprocessing

#input data
input_data = np.array([[2.1, -1.9, 5.5], [-1.5, 2.4, 3.5], [0.5, -7.9, 5.6], [5.9, 2.3, -5.8]])
print(input_data)

#Binarisasi
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data)
print("\nBinarized Data:\n", data_binarized)

#Mean Removal
print("Mean =", input_data.mean(axis=0))
print("Std deviation =", input_data.std(axis=0))
data_scaled = preprocessing.scale(input_data)
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis=0))

#min max scalling
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)

#L1 normalisasi
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
print("\nl1 Normalized data:\n", data_normalized_l1)
#L2 normalisasi
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nl2 Normalized data:\n", data_normalized_l2)
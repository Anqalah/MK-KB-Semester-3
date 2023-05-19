# Nama  : Muhammad Fadhil
# NIM   : F55120068

from kanren import isvar, run, membero
from kanren.core import success, fail, condeseq, eq, var
from sympy.ntheory.generate import prime, isprime
import itertools as it

def prime_check(x): #fungsi untuk mengecek bilangan prima
    if isvar(x):
        return condeseq([(eq, x, p)] for p in map(prime, it.count(1)))
    else:
        return success if isprime(x) else fail

x = var() #fungsi untuk memasukkan data inputan
data = (12, 14, 15, 19, 20, 21, 22, 23, 29, 30, 41, 44, 52, 62, 65, 85)
print("Data:", data)

var_x = (membero, x, data) #pada variabel x yang telah terdapat data, membero untuk menampilkan data dari bilangan prima
member = run(0, x, var_x, (prime_check, x)) #di dalam var x terdapat data terus dicari bilangan primanya
fn = set(member) #di set member, untuk ditampilkan
print("Berikut adalah bilangan prima yang ada dalam data:", fn)

ten_prime = run(10, x, prime_check(x)) #fungsi untuk menampilkan 10 bilangan pertama
print('Sepuluh Bilangan Prima Pertama', ten_prime)
#Memecahkan Relasi Aljabar
from constraint import *
#Muhammad Fadhil_F55120068

problem = Problem()                 # untuk mendefinisikan dua fungsi pada variabel dibawah
problem.addVariable('a', range(15)) # nilainya dimulai dari 0 dan batasannya dibawah 10
problem.addVariable('b', range(15)) # range harus kelipatan 5 (untuk ganjil) atau 2 (untuk genap)

problem.addConstraint(lambda a, b: a * 2 == b) #untuk deklarasi variabel house, a=0 dikali 2

solutions = problem.getSolutions()
print(solutions)
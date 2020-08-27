#Soal 2 - List Spinner (30 Poin)
#fungsi buat rotasi matrix 90 derajat ccw
#list comperhension
#fungsi buat rotasi matrix 90 derajat ccw
def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
#m adalah yang menyatakan matriks. j dan i adalah yang menyatakan baris dan kolom
#for j in range(len(m)) adalah yang menyatakan inner loop yang sesuai dengan inputan(banyaknya data)
#for i in range(len(m[0])-1,-1,-1)adalah outerlooping berdasarkan data yang dimulai dari i = banyaknya elemen pada m[0] dikurang 1
#outer loop decrement, inner loop increments
#iter 1 i=2 j=0
# return [0][j] = m[0][2]=3
#iter 2 i=2 j=1
#return [0][1]=m[1][2]=6
# j nya sampai di loop baru i nya jadi i=1
matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]
matrix = rotate_matrix(matrix) #rotate 90 deg clockwise
print(matrix)
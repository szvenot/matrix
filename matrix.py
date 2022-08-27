# fuggveny 3 szam szorzatara
def threeunit (x,y,z):
	v = x * y * z
	return v
	 
# matrixunk listaval megadva stringkent
matrix1 = ['8',  '14', '6',  '25', '21', '54', '32']
matrix2 = ['12', '21', '32', '23', '54', '7' , '4' ]
matrix3 = ['32', '51', '14', '32', '23', '17', '35']
matrix4 = ['13', '21', '42', '52', '14', '32', '12']
matrix5 = ['54', '34', '25', '63', '91', '23', '42']
matrix6 = ['23', '42', '53', '23', '34', '53', '25']
matrix7 = ['32', '54', '34', '52', '34', '43', '65']

#globalis valtozok
lista = []

# nxn-es matrix merete
n = 7

# listak osszeillesztese
matrixall = matrix1 + matrix2 + matrix3 + matrix4 + matrix5 + matrix6 + matrix7

# stringek atalakitasa integerre
intmatrix = [int(x) for x in matrixall]

#lista feldarabolasa 7 db-s listakra
group = lambda t, j: zip(*[t[i::j] for i in range(j)])
matrix = group(intmatrix, n)

# a vizszintes 3-asok szozata
[[lista.append(threeunit (x[i], x[i+1], x[i+2])) for i in range(n-2)] for x in matrix]

# fuggoleges 3-asok szozata
[[lista.append(threeunit(matrix[i][j], matrix[i+1][j], matrix[i+2][j])) for j in range(n)] for i in range(0,n-2,1)]

# csokkeno atlok 3-as szorzatai
[[lista.append(threeunit(matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2])) for j in range(0,n-2,1)] for i in range(0,n-2,1)]

# a novekedo atlok 3-as szorzatai
[[lista.append(threeunit(matrix[i][j], matrix[i-1][j+1], matrix[i-2][j+2])) for j in range(0,n-2,1)] for i in range(2,n,1)]

print max(lista)

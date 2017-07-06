import struct
import hashlib
import csv
import os


#uf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
uf = {}
uf ['AC'] = 1
uf ['AL'] = 2
uf ['AP'] = 3
uf ['AM'] = 4
uf ['BA'] = 5
uf ['CE'] = 6
uf ['DF'] = 7
uf ['ES'] = 8
uf ['GO'] = 9
uf ['MA'] = 10
uf ['MT'] = 11
uf ['MS'] = 12
uf ['MG'] = 13
uf ['PA'] = 14
uf ['PB'] = 15
uf ['PR'] = 16
uf ['PE'] = 17
uf ['PI'] = 18
uf ['RJ'] = 19
uf ['RN'] = 20
uf ['RS'] = 21
uf ['RO'] = 22
uf ['RR'] = 23
uf ['SC'] = 24
uf ['SP'] = 25
uf ['SE'] = 26
uf ['TO'] = 27

f = open('201601_BolsaFamiliaFolhaPagamento.csv', 'r')
print(f.tell())
linha = f.readline()
f1 = open('bolsaTopicos.csv', 'w')
f1.write(linha)
f1.close()
#linha = f.readline().decode('latin1')
#count = 0
"""ufLinha = linha[0]+linha[1]
for i in uf:
	#print(i)
	count+=1
	if linha[0] == i[0] and linha[1] == i[1]:
		print(i)"""
"""while linha!="":
	if linha[0]=="U" and linha[1]=="F":
		print(linha)
print(linha)"""
"""
print(f.tell())
linha.append(f.readline().decode('latin1'))
print(f.tell())
linha.append(f.readline().decode('latin1'))
#print(linha[2])
print(f.tell())
i=0
for i in range (3):
	print(linha[i])"""
#count = 0
while True:
	linha = f.readline()
	if linha!="":
		#count+=1
		ufLinha = linha[0]+linha[1]
		#n = uf[ufLinha]
		f1 = open('bolsa'+ufLinha+'.csv','a')
		f1.write(linha)
		f1.close()
	else:
		break
#print(count)
f.close()
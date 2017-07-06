import struct
import hashlib
import os
import csv

fileName = "201601_BolsaFamiliaFolhaPagamento.csv"
indexName = "201601_bolsaFamilia-hash.csv"
dataFormat = "2s4s72s2s3s4s4s14s72s72s6s7s"  
encoding = "cp1252"
indexFormat = "14sLL"
keyColumnIndex = 7
hashSize = 14999999
recordSize = struct.calcsize(dataFormat)
counts = [0] * hashSize
#print struct.calcsize(indexFormat)
"""f = open(indexName, "rb")
f.seek(0, os.SEEK_END)
hashSize = f.tell()/struct.calcsize(indexFormat)
f.close()"""
#print hashSize

def h2(key):
    global hashSize
    return int(key)%hashSize

def h(key):
    global hashSize
    return int(hashlib.sha1(key).hexdigest(),16)%hashSize


colisoes = 0
tamanhoMaiorLista = 0
recordCount = 0
with open(fileName, "rb") as csvFile:
	r = csv.reader(csvFile, delimiter = "	")
	for row in r:
		p = h(row[keyColumnIndex])
		counts[p] += 1
		if counts[p] > 1:
			colisoes += 1
		if counts[p] > tamanhoMaiorLista:
			tamanhoMaiorLista = counts[p]
		recordCount += 1
csvFile.close()

"""f = open(fileName,"rb")
while True:
    line = f.read(recordSize)
    if line == "": # EOF
        break
    record = struct.unpack(dataFormat, line)
    p = h(record[keyColumnIndex])
    counts[p] += 1
    if counts[p] > 1:
        colisoes += 1
    if counts[p] > tamanhoMaiorLista:
        tamanhoMaiorLista = counts[p]
    recordCount += 1
f.close()"""

print "Numero Colisoes:", colisoes
print "Tamanho Maior Lista:", tamanhoMaiorLista

countOfCounts = [0] * (tamanhoMaiorLista+1)

for i in counts:
    countOfCounts[i] += 1

print countOfCounts

c = 0
media = 0
for j in countOfCounts:
    probabilidade = c*(float(j)/recordCount)
    print "Lista de tamanho", c, "probabilidade", probabilidade
    media += c*probabilidade
    c += 1

print "Media acesso", media

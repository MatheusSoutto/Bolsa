import struct
import hashlib
import os
import sys
import csv
import codecs


hashSize = 14999999
fileName = "201601_BolsaFamiliaFolhaPagamento.csv"
indexName = "201601_bolsaFamilia-hash.dat"
dataFormat = "2s4s72s2s3s4s4s14s72s72s6s7s"  
encoding = "cp1252"
indexFormat = "14sLL"
keyColumnIndex = 7

dataStruct = struct.Struct(dataFormat)
indexStruct = struct.Struct(indexFormat)

def h(key):
	global hashSize
	return int(hashlib.sha1(key).hexdigest(), 16)%hashSize

nis = []
if len(sys.argv) >= 2:
	if len(sys.argv[1]) == 11:
		nis.append('000')
	nis.append(sys.argv[1])
else:
	x = raw_input("Entre com o NIS: ")
	if len(x) == 11:
		nis.append('000')
	nis.append(x)
nisProcurado = ''.join(nis)

with open(fileName, "rb") as f:
	r = csv.reader(f, delimiter = "	")
	fi = open(indexName, "rb")
	p = h(nisProcurado)
	offset = p*indexStruct.size
	i = 1
	while True:
		fi.seek(offset, os.SEEK_SET)
		indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
		if indexRecord[0].find(nisProcurado) != -1:# == nisProcurado:
			print indexRecord
			line = 0
			record = ""
			for row in r:
				#print "for"
				if line == indexRecord[1]:
					print "if"
					record = "	".join(row)
					record = codecs.decode(record, encoding)
					break
				line += 1
			print record
			print i
			break
		else:
			offset = indexRecord[2]
			if offset == 0:
				break
			i += 1
	fi.close()



"""f = open(fileName, "rb")
fi = open(indexName,"r+b")

p = h(nisProcurado)
offset = p*indexStruct.size
i = 1
while True:
    fi.seek(offset,os.SEEK_SET)
    indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
    if indexRecord[0] == nisProcurado:
        f.seek(indexRecord[1]*dataStruct.size,os.SEEK_SET)
        record = dataStruct.unpack(f.read(dataStruct.size))
        print record
        print i
        break
    offset = indexRecord[2]
    if offset == 0:
        break
    i += 1
fi.close()
f.close()"""
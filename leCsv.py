import struct
import codecs
import csv
import os
import hashlib

hashSize = 14999999
fileName = "201601_BolsaFamiliaFolhaPagamento.csv"
indexName = "201601_bolsaFamilia-hash.csv"
dataFormat = "2s4s72s2s3s4s4s14s72s72s6s7s"  #o preco esta multipicado por 100
encoding = "cp1252"
indexFormat = "14sLL"
keyColumnIndex = 7

dataStruct = struct.Struct(dataFormat)
indexStruct = struct.Struct(indexFormat)

def h(key):
	global hashSize
	return int(hashlib.sha1(key).hexdigest(), 16)%hashSize

fi = open(indexName, "wb")
emptyIndexRecord = indexStruct.pack("", 0, 0)
for i in range (0, hashSize):
	fi.write(emptyIndexRecord)
fi.close()


fi = open(indexName, "r+b")
fi.seek(0, os.SEEK_END)
fileIndexSize = fi.tell()
print "Index File Size: ", fileIndexSize

#nis = 00019002755484
recordNumber = 0

with open(fileName, "rb") as csvFile:
	r = csv.reader(csvFile, delimiter='	')
	for row in r:
		if len(row) == 12:
			if row[keyColumnIndex] == "NIS Favorecido":
				continue
			#record = dataStruct.unpack(row)
			p = h(row[keyColumnIndex])
			fi.seek(p*indexStruct.size, os.SEEK_SET)
			indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
			fi.seek(p*indexStruct.size, os.SEEK_SET)
			if indexRecord[0][0] == "\0":
				fi.write(indexStruct.pack(row[keyColumnIndex], recordNumber, 0))
			else:
				nextPointer = indexRecord[2]
				fi.write(indexStruct.pack(indexRecord[0], indexRecord[1], fileIndexSize))
				fi.seek(0, os.SEEK_END)
				fi.write(indexStruct.pack(row[keyColumnIndex], recordNumber, nextPointer))
				fileIndexSize = fi.tell()
			recordNumber += 1
			"""for i in range (0, 12):
				if i < 11:
																	print codecs.decode(row[i], encoding) + '; ',
																else:
																	print codecs.decode(row[i], encoding)"""
csvFile.close()
fi.close()
			
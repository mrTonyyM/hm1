segFile = open(r'G:\00005262.segd','rb')
headerOne = segFile.read(32)
headerTwo = segFile.read(32)
headerThree = segFile.read(32)
# help (segFile)
# segFile.close()

ffid = headerOne[:2].hex()
formatCode = headerOne[2:4].hex()
commonConst = headerOne[4:10].hex()
year = headerOne[10:11].hex()
howMuchAddBlocks = (headerOne[11:12].hex())
day = headerOne[12:13].hex()
hour = headerOne[13:14].hex()
minutes = headerOne[14:15].hex()
sec = headerOne[15:16].hex()
codeProduction = headerOne[16:17].hex()
serialNumber = headerOne[17:19].hex()
bytesOnCadr = headerOne[19:22].hex()
intervalBaseCadr = headerOne[22:23].hex()
polarity = headerOne[23:24].hex()
recordType = headerOne[25:26].hex()
lengthRecord = headerOne[25:27].hex()
typeCadrOnReacord = headerOne[27:28].hex()
howMuchCadrs = headerOne[28:29].hex()
howMuchShifts = headerOne[29:30].hex()
howLengthAddHeader = headerOne[30:31].hex()
howLengthExHeader = headerOne[31:32].hex()

exFFID = int(headerTwo[0:3].hex(),16)
segFile.seek(32*howMuchCadrs) # TODO make cyckle for reading cadrs
headerAdd = segFile.read(32*howLengthAddHeader)
headerEX = segFile.read(32*howLengthExHeader)
how_much_traces =


print('номер файла ', ffid)
print('код формата ',formatCode)
print('общая постояная ',commonConst)
print('год ',year)
print('количество дополнительных блоков ',howMuchAddBlocks)
print('день от января ',day)
print('час ',hour)
print('минуты ',minutes)
print('секунды ',sec)
print('код продукта ',codeProduction)
print('номер серии ',serialNumber)
print('байтов на кадр ',bytesOnCadr)
print('интервал основного кадра ',intervalBaseCadr)
print('полярность ',polarity)
print('тип записи ',recordType)
print('длина записи ',lengthRecord)
print('тип кадра на запись ',typeCadrOnReacord)
print('как много 32х байтных кадров ',howMuchCadrs)
print('как много сдвигов ',howMuchShifts)
print('кол-во 32х байтных дополнительных заголовков ',howLengthAddHeader)
print('номер файла ',howLengthExHeader)
print('номер файла ',exFFID)


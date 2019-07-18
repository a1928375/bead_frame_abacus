def print_abacus(value):
    list=["|00000*****   |","|00000****   *|","|00000***   **|","|00000**   ***|","|00000*   ****|","|00000   *****|","|0000   0*****|","|000   00*****|","|00   000*****|","|0   0000*****|",]
    
    if len(str(value))<10:
        new_string=(10-len(str(value)))*"0"+str(value)
    
    for i in new_string:
        print list[int(i)]

print print_abacus(0)
print print_abacus(123)
print print_abacus(12345678)
print print_abacus(1337)
print print_abacus(232323)

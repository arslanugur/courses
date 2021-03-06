from itertools import permutations
for p in permutations("abcdef", 3):
    print("".join(p))
    
    
"""
OUTPUT
abc
abd
abe
abf
acb
acd
ace
acf
adb
adc
ade
adf
aeb
aec
aed
aef
afb
afc
afd
afe
bac
bad
bae
baf
bca
bcd
bce
bcf
bda
bdc
bde
bdf
bea
bec
bed
bef
bfa
bfc
bfd
bfe
cab
cad
cae
caf
cba
cbd
cbe
cbf
cda
cdb
cde
cdf
cea
ceb
ced
cef
cfa
cfb
cfd
cfe
dab
dac
dae
daf
dba
dbc
dbe
dbf
dca
dcb
dce
dcf
dea
deb
dec
def
dfa
dfb
dfc
dfe
eab
eac
ead
eaf
eba
ebc
ebd
ebf
eca
ecb
ecd
ecf
eda
edb
edc
edf
efa
efb
efc
efd
fab
fac
fad
fae
fba
fbc
fbd
fbe
fca
fcb
fcd
fce
fda
fdb
fdc
fde
fea
feb
fec
fed
"""


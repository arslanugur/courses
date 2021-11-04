#Here T=`tomato', B=`bell pepper', L=`lettuce', E=`eggplant'. You can run this code and observe the result.

from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))
   
#OUTPUT
"""
TTTTTTT
TTTTTTB
TTTTTTL
TTTTTTE
TTTTTBB
TTTTTBL
TTTTTBE
TTTTTLL
TTTTTLE
TTTTTEE
TTTTBBB
TTTTBBL
TTTTBBE
TTTTBLL
TTTTBLE
TTTTBEE
TTTTLLL
TTTTLLE
TTTTLEE
TTTTEEE
TTTBBBB
TTTBBBL
TTTBBBE
TTTBBLL
TTTBBLE
TTTBBEE
TTTBLLL
TTTBLLE
TTTBLEE
TTTBEEE
TTTLLLL
TTTLLLE
TTTLLEE
TTTLEEE
TTTEEEE
TTBBBBB
TTBBBBL
TTBBBBE
TTBBBLL
TTBBBLE
TTBBBEE
TTBBLLL
TTBBLLE
TTBBLEE
TTBBEEE
TTBLLLL
TTBLLLE
TTBLLEE
TTBLEEE
TTBEEEE
TTLLLLL
TTLLLLE
TTLLLEE
TTLLEEE
TTLEEEE
TTEEEEE
TBBBBBB
TBBBBBL
TBBBBBE
TBBBBLL
TBBBBLE
TBBBBEE
TBBBLLL
TBBBLLE
TBBBLEE
TBBBEEE
TBBLLLL
TBBLLLE
TBBLLEE
TBBLEEE
TBBEEEE
TBLLLLL
TBLLLLE
TBLLLEE
TBLLEEE
TBLEEEE
TBEEEEE
TLLLLLL
TLLLLLE
TLLLLEE
TLLLEEE
TLLEEEE
TLEEEEE
TEEEEEE
BBBBBBB
BBBBBBL
BBBBBBE
BBBBBLL
BBBBBLE
BBBBBEE
BBBBLLL
BBBBLLE
BBBBLEE
BBBBEEE
BBBLLLL
BBBLLLE
BBBLLEE
BBBLEEE
BBBEEEE
BBLLLLL
BBLLLLE
BBLLLEE
BBLLEEE
BBLEEEE
BBEEEEE
BLLLLLL
BLLLLLE
BLLLLEE
BLLLEEE
BLLEEEE
BLEEEEE
BEEEEEE
LLLLLLL
LLLLLLE
LLLLLEE
LLLLEEE
LLLEEEE
LLEEEEE
LEEEEEE
EEEEEEE
"""

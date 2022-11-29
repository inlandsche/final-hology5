from z3 import *

#flag = "hology5{b4s1c_b4by_VM?!}"
#valid = [b'686f6c6f', b'6779357b', b'62347331', b'635f6234', b'62795f56', b'4d3f217d']
k = [
  BitVec("k[0]", 32),
  BitVec("k[1]", 32),
  BitVec("k[2]", 32),
  BitVec("k[3]", 32),
  BitVec("k[4]", 32),
  BitVec("k[5]", 32)
]

s = Solver()
s.add((k[0] ^ k[2]) == 0x5e1f5b0a)
s.add(k[2] ^ k[5] == 0x4c520b2f)
s.add(k[1] - k[2] == 0x49c24505)
s.add(k[3] + k[5] == 0xb1839eb0)
s.add(k[4] ^ 0x23212019 == 0x757e597b)
s.add(k[0] - k[4] == 0x190cf606)

# for i in range(6):
#   for j in range(6):
#     v = Extract(8 * j + 7, 8 * j, k[i])
#     s.add(v >= 0x21, v <= 0x7e)


print(s.check())
m = s.model()
print(str("%.8x"%(m[k[0]].as_long())).decode("hex")[::-1] +
 str("%.8x"%(m[k[1]].as_long())).decode("hex")[::-1] +
 str("%.8x"%(m[k[2]].as_long())).decode("hex")[::-1] +
 str("%.8x"%(m[k[3]].as_long())).decode("hex")[::-1] +
 str("%.8x"%(m[k[4]].as_long())).decode("hex")[::-1] +
 str("%.8x"%(m[k[5]].as_long())).decode("hex")[::-1])

# print hex(m.eval(k[0] ^ k[3]).as_long())
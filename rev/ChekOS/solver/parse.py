from z3 import *

k = [
  BitVec("k[0]", 32),
  BitVec("k[1]", 32),
  BitVec("k[2]", 32),
  BitVec("k[3]", 32),
  BitVec("k[4]", 32),
  BitVec("k[5]", 32)
]

s = Solver()
s.add((k[0] ^ k[2]) == 0x0a5b1f5e)
s.add(k[2] ^ k[5] == 0x2f0b524c)
s.add(k[1] - k[2] == 0x0544c24a)
s.add(k[3] + k[5] == 0xb09e83b1)
s.add(k[4] ^ 0x19202123 == 0x7b597e75)
s.add(k[0] - k[4] == 0x05f60d19)

# for i in range(6):
#   for j in range(6):
#     v = Extract(8 * j + 7, 8 * j, k[i])
#     s.add(v >= 0x21, v <= 0x7e)


print(s.check())
m = s.model()
print(str("%.8x"%(m[k[0]].as_long())).decode("hex") +
 str("%.8x"%(m[k[1]].as_long())).decode("hex") +
 str("%.8x"%(m[k[2]].as_long())).decode("hex") +
 str("%.8x"%(m[k[3]].as_long())).decode("hex") +
 str("%.8x"%(m[k[4]].as_long())).decode("hex") +
 str("%.8x"%(m[k[5]].as_long())).decode("hex"))

# print hex(m.eval(k[0] ^ k[3]).as_long())
print('What is your character?')

i = input()
io = ord(i)
print(io)
ioa = int(io/2)
ior = io % 2
a = int(ioa/2)
ar = ioa % 2
b = int(a/2)
br = a%2
c = int(b/2)
cr = b%2
d = int(c/2)
dr = c%2
e = int(d/2)
er = d%2
f = int(e/2)
fr = e%2
g = int(f/2)
gr = f%2
rtpio = str(ior)
rtpar = str(ar)
rtpbr = str(br)
rtpcr = str(cr)
rtpdr = str(dr)
rtper = str(er)
rtpfr = str(fr)
rtpgr = str(gr)
rtp = rtpgr+rtpfr+rtper+rtpdr+rtpcr+rtpbr+rtpar+rtpio
print(rtp)

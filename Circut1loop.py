def oneBinary(text):
    io = ord(text)
    counter = 0
    r = 0
    binString=''
    while counter < 8:
        r = io%2
        io=int(io/2)
        binString = str(r) + binString
        counter+=1
    return binString
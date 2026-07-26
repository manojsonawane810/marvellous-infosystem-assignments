import hashlib

def calculateChecksum(filename):
    fObj = open(filename, "rb")

    hObj = hashlib.md5()
    buffer = fObj.read(1000)

    while (len(buffer) > 0):
        hObj.update(buffer)
        buffer = fObj.read(1000)

    fObj.close()

    return hObj.hexdigest() 
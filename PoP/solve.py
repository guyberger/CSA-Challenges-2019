import codecs
from itertools import permutations as prmt
N1 = 256
S, key, plain, cipher = [0 for i in range(N1)], [0 for i in range(15)], [], []
block1 = [214, 85, 173,9, 13, 217,126, 133, 241,98, 37, 11,50, 52, 8,18, 230, 22,122, 125, 160,86, 8, 226,17, 235, 234,154, 238, 250,210, 123, 171,178, 43, 98,237, 136, 68,184, 17, 74,113, 74, 138]

    
def restart():
    global S, key, plain, cipher
    S, key, plain, cipher = [0 for i in range(N1)], [0 for i in range(15)], [], []
def swap(i, j):
    global S
    S[i], S[j] = S[j], S[i]
def KSA():
    global key, S
    llen = 15
    j = 0
    S = [i for i in range(N1)]
    for i in range(N1):
        j = (j + S[i] + key[i % llen]) % N1
        swap(i, j)
def PRGA():
    global S, cipher, plain
    i, j, rr = 0, 0, ""
    for n in range(45):
        i = (i + 1) % N1
        j = (j + S[i]) % N1
        swap(i, j)
        rnd = S[(S[i] + S[j]) % N1]
        rr += chr(rnd)
        cipher[n] = rnd ^ plain[n]
def RC():
    global S, plain, cipher
    plain = block1
    cipher = ['!' for i in range(45)]
    S = [0 for i in range(N1)]
    KSA()
    PRGA()

def fillKey():
        global key
        key[0] = 9
        key[1] = 23
        key[2] = 6
        key[3] = 24
        key[4] = 18
        key[5] = 3
        key[6] = 3
        key[7] = 3
        key[8] = 5
        key[9] = 8
        key[10] = 24
        key[11] = 23
        key[12] = 3
        key[13] = 20
        key[14] = 3


for i in range(100):
        for j in range(100):
                out = ""
                restart()
                fillKey()
                key[11] = i
                key[5] = j
                RC()

                for c in cipher:
                        out += chr(c)
                if "CSA" not in out:
                        continue
                print("Cypher: {}, {}".format(i, j))
                print(out)



from os import listdir
from os.path import isfile, join
import hashlib

IV = 'a861f335d4d457a7c1d00640da380dc4'
prev = IV
mypath = './blocks'
def hashit(lst, s):
    if len(lst) <= 1:
        return lst
    nxtlst = []
    for i in range(0, len(lst), s):
        ins = ""
        for j in range(i, i + s):
            ins += lst[j]
        mm = hashlib.md5(ins.encode('utf-8'))
        nxtlst += [mm.hexdigest()]
    return nxtlst

def main():
    global prev
    files_lst = listdir(mypath)
    files_lst.sort()
    files_lst.sort(key=len)
    for fold in files_lst:    # fold: block_0-height_1-sons_2
        nxtpath = mypath + '/' + fold + '/'     # nxtpath leads to leaves of fold
        fold = fold.split("-")
        h = int((fold[1].split("_"))[1])
        s = int((fold[2].split("_"))[1])
        lst = []
        nxt_files_lst = listdir(nxtpath)
        nxt_files_lst.sort()
        nxt_files_lst.sort(key=len)
        for tx in nxt_files_lst:
            with open(nxtpath + tx, "r") as f:
                lst += [f.read()]
        # lst contains all the data leaves
        nodes_hashed = 0
        for i in range(len(lst)):
            lst[i] = hashlib.md5(lst[i].encode('utf-8')).hexdigest()
            nodes_hashed += 1
        while len(lst) > 1:
            lst = hashit(lst, s)

        # lst has only md5 of root
        ins = lst[0]
        prev = hashlib.md5((prev+ins).encode('utf-8')).hexdigest() 

    print(prev)


if __name__ == '__main__':
    main()

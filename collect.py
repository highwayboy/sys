def volume_collect(ID,username):
    fi=open("{}collect.txt".format(username),"a+",encoding="utf-8")
    fi.seek(0)
    if ID in fi.read():
        return
    fi.seek(2)
    fi.write(ID+",")
    fi.close()


def get_ID(username):
    fi=open("{}collect.txt".format(username),"r")
    t=fi.read()
    ls=t.split(",")
    del ls[-1]
    return ls
    fi.close()
get_ID(username)
        
        

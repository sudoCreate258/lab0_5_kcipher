# DO NOT UPDATE ANY CODE BELOW THIS LINE
import random as rand

def get_alpha_lst():
    ascii_A = 65
    alst = [chr(x) for x in range(ascii_A, ascii_A+26)]
    return alst

def get_plaintext():
    def fn():
        seed = rand.randint(-25,25)
        alst = get_alpha_lst()
        return alst[seed]
    return f"{fn()}{fn()}{fn()}"
    
def check_equals(ptext,ctext,flag=True):
    if flag:
        exp = ''.join([chr(ord(p)-3) for p in ptext])
        dxp = ''.join([chr(ord(p)+3) for p in exp])
    else:
        exp = ''.join([chr(ord(p)*3) for p in ptext])
        dxp = ''.join([chr(int(ord(p)/3)) for p in exp])
    assert ptext == dxp
    return exp == ctext

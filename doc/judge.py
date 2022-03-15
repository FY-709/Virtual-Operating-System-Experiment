import os
import subprocess as sp



def save(code,id):
    path = os.path.join(os.getcwd(),id+'.cpp')
    with open(path,'wb') as f:
        f.write(code)


def compile_code(id):
    r = sp.run(['g++',id+'.cpp','-o',id],stdout=sp.PIPE,stderr=sp.PIPE,universal_newlines=True)
    if r.stderr == None:
        return ['','']
    else:
        return [r.stderr,'']



def run_code(id):
    r = sp.run(['timeout','0.004','./'+id],stdout=sp.PIPE,stderr=sp.PIPE,universal_newlines=True)
    if r.stdout != None:
        return r.stdout
    else:
        return ''



    

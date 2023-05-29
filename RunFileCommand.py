import subprocess


#clasa comanda, in care am doua proprietati: file si language
class RunFileCommand(object):
    def __init__(self, file, exec):
        self.file = file
        self.exec = exec

#metoda execute pe care o apelez pentru a executa file ul
    def execute(self):
        subprocess.run([self.exec, self.file])

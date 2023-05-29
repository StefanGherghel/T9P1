from LanguageHandler import LanguageHandler
from RunFileCommand import  RunFileCommand
import subprocess


class PythonHandler(LanguageHandler):

    def __init__(succesor = None):
        super().__init__(succesor)

    def setSuccesor(self, succesor: LanguageHandler):
        self.__succesor = succesor

    def handle_it(self, file):
        contor_py_words = 0
        #mecanism de try and except, verific daca exista fisierul
        try:
            with  open(file, 'r') as python_file:
                continut = python_file.readlines()
                #verific daca am cuvinte cheie: __main, __name__, def
                for line in continut:
                    for word in line.split():
                        if word == '\'__main__\'':
                            contor_py_words = contor_py_words + 1
                        if word == '__name__':
                            contor_py_words = contor_py_words + 1
                        if word == 'def':
                            contor_py_words = contor_py_words + 1
                #daca nu le am, trimit task ul mai departe
                if contor_py_words == 0:
                    self.__succesor.handle_it(file)
                #daca le am, creez un obiect de tip RunFileCommand si apelez functia execute
                else:
                    self.exec = "python"
                    print('E python')
                    run_it = RunFileCommand(file, self.exec)
                    run_it.execute()
        except IOError:
            print('Fisierul nu exista!')




import os.path
import subprocess

from LanguageHandler import LanguageHandler
from RunFileCommand import RunFileCommand


class KotlinHandler(LanguageHandler):



    def __init__(succesor = None):
        super().__init__(succesor)

    def setSuccesor(self, succesor: LanguageHandler):
        self.__succesor = succesor

    def handle_it(self, file):
        contor_kt_words = 0
        try:
            with open(file, 'r') as kotlin_file:
                continut = kotlin_file.readlines()
                for line in continut:
                    for word in line.split():
                        word.replace('\ufeff', "")
                        if word == 'var':
                            contor_kt_words = contor_kt_words + 1
                        if word == 'main(args:':
                            contor_kt_words = contor_kt_words + 1
                        if word == 'fun':
                            contor_kt_words = contor_kt_words + 1
                if contor_kt_words == 0:
                    self.__succesor.handle_it(file)
                else:
                    self.exec = "java -jar"
                    print('E kotlin')
                    #run_it = RunFileCommand(file, "java -jar")
                    #run_it.execute()
                    name = os.path.splitext(file)
                    next_jar = name[0] + ".jar"
                    print(next_jar)
                    subprocess.run(["kotlinc Main.kt -include-runtime -d Main.jar"])
        except IOError:
            print('Fisierul nu exista!')





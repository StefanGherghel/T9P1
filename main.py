from KotlinHandler import KotlinHandler
from PythonHandler import PythonHandler

if __name__ == '__main__':

    py_handler = PythonHandler()
    kt_handler = KotlinHandler()

    py_handler.setSuccesor(kt_handler)

    #/home/student/AplicatiiPy/Laborator9/Aplicatie2/main.py
    #/home/student/AplicatiiPy/Laborator8/Aplicatie1/ChainAndFactory/src/Main.kt
    #/home/student/AplicatiiPy/Laborator9/Main.kt
    py_handler.handle_it("/home/student/AplicatiiPy/Laborator9/Main.kt")

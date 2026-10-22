from fastapi import FastAPI

def fence(func):
    def decorate():
        print ("+" * 10)
        func()
        print ("+" * 10)
    return decorate

@fence
def log():
    print ("Hello World!")

log()
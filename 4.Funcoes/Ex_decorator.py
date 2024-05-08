from datetime import datetime
import time

def meu_decorator(funcao):
    def controle():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return controle


@meu_decorator
def printa_loop():
    time.sleep(5)

printa_loop()




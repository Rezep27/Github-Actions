#src/main.py
import os

# obtener entrada y convertir a entero
num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit('El numero ingresado no es entero')
else:
    num = 1

# mostrar resultado en la consola

if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print("{0}={1}".format('result', num + 3), file = f)

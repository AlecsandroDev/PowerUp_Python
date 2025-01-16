from pynput.mouse import Listener
from pyautogui import position as pos

# Função responsável pelos comandos dos input do usuário
def on_click(x, y, button, pressed):
  # Imprimir os eixos X e Y do Mouse
  if pressed:
    print(pos())

    # Parar a execução
    if button.name == "right":
      return False

# Função responsável por ficar escuntado os input od usuárioss
with Listener(on_click=on_click) as listener:
  listener.join()
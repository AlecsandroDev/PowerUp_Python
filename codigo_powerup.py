from time import sleep as tm
import pyautogui as auto
import pandas as pd

# Site de exemplo para cadastro de Produtos
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Importação dos Dados do CSV para a variável
tabela = pd.read_csv(r"produtos.csv")

# Velocidade para executar as funções do pyautogui
auto.PAUSE = 0.2

# Função para abrir o Painel
def abrir_painel() -> None:
  auto.hotkey("win", "r")
  auto.hotkey("crtl", "backspace")
  auto.write(url)
  auto.press("enter")

  # Tempo para o site carregar
  tm(1.5)

  auto.click(x=479, y=343)

  auto.write("emaildesimulacao@gmail.com")
  auto.press("tab")

  auto.write("Emaildesimulacao123")
  auto.press("tab")
  auto.press("enter")

  importando_tabela()

  return None

# Função para acessar o valor da linha passada
def acessando_tabela(linha: str = '', nome_valor: str = '') -> None:
  texto = str(tabela.loc[linha, nome_valor])
  if texto != "nan": auto.write(texto) 
  auto.press("tab")

  return None

# Função para importar os valores do CSV para o Painel
def importando_tabela() -> None:
  for linha in tabela.index:
    auto.click(x=441, y=240)
    
    acessando_tabela(linha, "codigo")
    acessando_tabela(linha, "marca")
    acessando_tabela(linha, "tipo")
    acessando_tabela(linha, "categoria")
    acessando_tabela(linha, "preco_unitario")
    acessando_tabela(linha, "custo")
    acessando_tabela(linha, "obs")

    auto.press("enter")
    auto.press("home")

  return None

abrir_painel()
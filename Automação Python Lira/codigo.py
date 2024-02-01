#passo a passo do projeto 
import pyautogui #instalação pip install pyautogui
import time #ja vem instalado no python
pyautogui.PAUSE = 0.5
#passo 1 abrir o sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter') 
time.sleep(2)
pyautogui.click(x=716, y=510)
#passo 2 Fazer login 
pyautogui.write('helton.galant@python')
pyautogui.press('tab')
pyautogui.write('senhadeteste')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('tab')
#passo 3: importar a base de dados 
import pandas
tabela = pandas.read_csv('produtos.csv')
for linha in tabela.index:
    codigo = tabela.loc[linha,'codigo']
    pyautogui.write(str(tabela.loc[linha,'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')    
    obs = tabela.loc[linha,'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(50000)
    time.sleep(2) 
    pyautogui.click(x=654, y=385)



#%%
from selenium import webdriver
import sys
import time
import pandas as pd


#%%

driver = webdriver.Chrome(executable_path=r'C:\Users\gabri\OneDrive\Documentos\Documentos - Gabriel\EngenhariaDeDados\AulasHow\Aula006\src\chromedriver.exe')
def tem_item(xpath, driver = driver):
    try:
        driver.find_element(xpath)
        return True
    except:
        return False
time.sleep(5)
driver.implicitly_wait(40)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')


#%%
tb_filmes = '/html/body/div/div/div[1]/div[3]/main/div[2]/div[4]/div[1]/table[2]'

i = 0
while not tem_item(tb_filmes):
    i+=1
    if i >50:
        break
    pass

tabela = driver.find_element("xpath", '/html/body/div/div/div[1]/div[3]/main/div[2]/div[4]/div[1]/table[2]')
df = pd.read_html('<table>' + tabela.get_attribute('innerHTML') + '</table>')[0]

# %%

with open('print.png', 'wb') as f:
    f.write(driver.find_element("xpath", '/html/body/div').screenshot_as_png)



#%%
driver.close()
# %%

df[df['Ano']==1984]
# %%
df.to_csv('filmes_Nicolas_Cage.csv', sep=';')
# %%

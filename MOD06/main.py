#%%
from selenium import webdriver
import sys
import time
#%%
cep = sys.argv[1]

if cep:    
    driver = webdriver.Chrome(executable_path=r'C:\Users\gabri\OneDrive\Documentos\Documentos - Gabriel\EngenhariaDeDados\AulasHow\Aula006\src\chromedriver.exe')
    time.sleep(10)
    #%%
    #driver.get('https://howedu.com.br/')
    #driver.find_element("xpath", '//*[@id="page"]/div[1]/div/section/div/div[1]/div/div/div/a').click()
    #driver.find_element("xpath", '//*[@id="page"]/div[1]/div/section/div/div[2]/div/div/div/div/i[1]').click()
    #driver.find_element("xpath", '//*[@id="menu-2-739815d"]/li[2]/a').click()

    #%%
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')
    elem_cep = driver.find_element("name", 'endereco')

    #%%

    elem_cep.clear()
    #%%

    elem_cep.send_keys('09260250')
    # %%
    elem_cmb = driver.find_element("name", 'tipoCEP').click()
    driver.find_element("xpath", '//*[@id="tipoCEP"]/optgroup/option[6]').click()


    # %%
    driver.find_element("id", 'btn_pesquisar').click()
    time.sleep(3)

    logradouro = driver.find_element("xpath", '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]').text
    bairro = driver.find_element("xpath", '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    localidade = driver.find_element("xpath", '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text


    # %%

    #logradouro = driver.find_element("xpath", '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    #bairro = driver.find_element("xpath", '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    #localidade = driver.find_element("xpath", '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
    ## %%
    print("""
    Para o CEP {} temos:
    Endereço: {}
    Bairro: {}
    Localidade: {}
    """.format(
    cep,
    logradouro.split(' - ')[0],
    bairro,
    localidade
    ))
    # %%


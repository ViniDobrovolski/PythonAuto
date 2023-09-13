#Script desenvolvido com a ideia de automação de consulta de processos do INSS


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep



#entrar no site para consulta

driver = webdriver.Chrome()
driver.get('https://consultaprocessos.inss.gov.br/')
sleep(2)

#clicar no botão de pesquisar e abrir nova pagina 

btn_Pesquisa = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained jss9 MuiButton-containedPrimary MuiButton-fullWidth']")
btn_Pesquisa.click()
sleep(5)
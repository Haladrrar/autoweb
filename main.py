from selenium import webdriver
import time

option = webdriver.ChromeOptions()

#Эти два аргумента нужны чтобы сайт не видел что вместо нас заходит автоматизатор
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.2.108 Yowser/2.5 Safari/537.36")
option.add_argument("--disable-blink-features")

#Теперь заходим в браузер
driver = webdriver.Chrome(options = option)
#Сайт STC на который нам нужно зайти
driver.get("https://go.smarttradecoin.com/app/")

driver.find_element_by_id("l_username").send_keys("здесь логин")
driver.find_element_by_id("log_pass").send_keys("здесь")

driver.find_element_by_class_name("login").click()
#Тут стопаем программу на 3 секунды чтобы вы убрали рекламу, а иначе она код может не остановиться
time.sleep(3)

#Заходим в панель для инвестиций
driver.find_element_by_class_name("menu-flatico.icon-003-head").click()
driver.find_element_by_id("panel_trading_bot").click()

#Основная функция для запуска циклов покупки бота
def main():
	while True:
		try:
      #Здесь в двух таймслипах вы можете сами указать интервал в котором будет покупаться бот, я просто поставил интервал в одну минуту
			time.sleep(55)
			driver.find_element_by_id("buy_bot").click()

			time.sleep(5)
			driver.find_element_by_xpath('//button[@id="modal_buy_bot"]').click()
		except:
			pass

if __name__ == '__main__':
	main()

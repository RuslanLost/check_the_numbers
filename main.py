import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import telebot
import schedule


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--start-maximized')
options.add_argument("--window-size=1400,800")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

bot = telebot.TeleBot("6528485256:AAFr27qVMMB-A_Ig_YeX3DSK-kvWBr-TR3U")
chat_id = 479102451

url = ''

url_number_set = {(
'https://101internet.ru/belgorod', 'https://101internet.ru/barnaul', 'https://101internet.ru/chelyabinsk',
'https://101internet.ru/kirov', 'https://101internet.ru/vladimirskaya-oblast',
'https://101internet.ru/penza', 'https://101internet.ru/samara', 'https://101internet.ru/cheboksary',
'https://101internet.ru/perm', 'https://101internet.ru/nizhniy-novgorod',
'https://101internet.ru/irkutsk'): {"main" : '+7 (800) 302-32-76', "Ростелеком" : '+7(800)101-17-90', "МегаФон" : '+7(800)101-18-26'},

('https://101internet.ru/ekaterinburg',): {"main" : '+7 (343) 301-68-45', "Ростелеком" : '+7(800)101-17-90', "МТС " : '+7(800)101-17-95', "билайн" : '+7(800)101-17-81', "Дом.ру" : '+7(800)100-90-41'},

('https://101internet.ru/novosibirsk',): {"main" : '+7 (383) 382-99-85',  "Ростелеком" : '+7(800)101-17-90', "МТС " : '+7(800)101-17-95'},

('https://101internet.ru/krasnodar',): {"main" : '+7 (861) 238-72-94', "Ростелеком" : '+7(800)101-17-90', "ТТК" : '+7(800)707-60-52'},

('https://101internet.ru/tver',): {"main" : '+7 (482) 278-26-58', "Ростелеком" : '+7(800)101-17-90', "Дом.ру" : '+7(800)100-90-41'},

('https://101internet.ru/rostov-na-donu',): {"main" : '+7 (863) 310-39-61', "Ростелеком" : '+7(800)101-17-90', "Дом.ру" : '+7(800)100-90-41', "билайн" : '+7(800)101-17-81' },

('https://101internet.ru/omsk',): {"main" : '+7 (381) 229-01-37', "Ростелеком" : '+7(800)101-17-90', "билайн" : '+7(800)101-17-81'},

('https://www.moskvaonline.ru/', 'https://www.moskvaonline.ru/moskovskaya-oblast'): {"main" : '+7 (495) 085-76-54', "Ростелеком" : '+7(499)372-33-55', "МГТС" : '+7(495)106-82-09'},

('https://piter-online.net/', ): {"main" : '+7 (812) 635-33-61',"Ростелеком" : '+7(812)605-80-89', "Дом.ру" : '+7(812)605-80-75'},
('https://piter-online.net/leningradskaya-oblast', ): {"main" : '+7 (812) 635-33-61',"Ростелеком" : '+7(812)605-80-89', "Дом.ру" : '+7(800)100-90-41'},
}


url_number_set_2 = {(
'https://101internet.ru/belgorod',): {"main" : '+7 (800) 302-32-76', "Ростелеком" : '+7(800)101-17-90', "МегаФон" : '+7(800)101-18-26'},

('https://101internet.ru/ekaterinburg',): {"main" : '+7 (343) 301-68-45', "Ростелеком" : '+7(800)101-17-90', "МТС" : '+7(800)101-17-95', "билайн" : '+7(800)101-17-81', "Дом.ру" : '+7(800)100-90-41'},

('https://101internet.ru/novosibirsk',): {"main" : '+7 (383) 382-99-85',  "Ростелеком" : '+7(800)101-17-90', "МТС" : '+7(800)101-17-95'},

('https://101internet.ru/krasnodar',): {"main" : '+7 (861) 238-72-94', "Ростелеком" : '+7(800)101-17-90', "ТТК" : '+7(800)707-60-52'},

('https://101internet.ru/tver',): {"main" : '+7 (482) 278-26-58', "Ростелеком" : '+7(800)101-17-90', "Дом.ру" : '+7(800)100-90-41'},

('https://101internet.ru/rostov-na-donu',): {"main" : '+7 (863) 310-39-61', "Ростелеком" : '+7(800)101-17-90', "Дом.ру" : '+7(800)100-90-41', "билайн" : '+7(800)101-17-81' },

('https://101internet.ru/omsk',): {"main" : '+7 (381) 229-01-37', "Ростелеком" : '+7(800)101-17-90', "билайн" : '+7(800)101-17-81'},

('https://www.moskvaonline.ru/', 'https://www.moskvaonline.ru/moskovskaya-oblast'): {"main" : '+7 (495) 085-76-54', "Ростелеком" : '+7(499)372-33-55', "МГТС" : '+7(495)106-82-09'},

('https://piter-online.net/', ): {"main" : '+7 (812) 635-33-61',"Ростелеком" : '+7(812)605-80-89', "Дом.ру" : '+7(812)605-80-75'},
('https://piter-online.net/leningradskaya-oblast', ): {"main" : '+7 (812) 635-33-61',"Ростелеком" : '+7(812)605-80-89', "Дом.ру" : '+7(800)100-90-41'},}

url_adres = {
'https://101internet.ru/belgorod': {'Улица' : 'Мирная', "Дом" : '10'},

'https://101internet.ru/ekaterinburg': {'Улица' : 'Маршала Жукова', "Дом" : '10'},

'https://101internet.ru/novosibirsk': {'Улица' : 'Авиастроителей', "Дом" : '1'},

'https://101internet.ru/krasnodar': {'Улица' : 'Абрикосовая ул б', "Дом" : '543'},

'https://101internet.ru/tver': {'Улица' : 'Академика Туполева', "Дом" : '116к3'},

'https://101internet.ru/rostov-na-donu': {'Улица' : 'Автомобильный пер', "Дом" : '32а'},

'https://101internet.ru/omsk': {'Улица' : 'Архитекторов б', "Дом" : '1/1'},

'https://www.moskvaonline.ru/': {'Улица' : 'Вернандского проспект', "Дом" : '27к1'},

'https://piter-online.net/': {'Улица' : 'Англиская наб', "Дом" : '3к2'},
'https://piter-online.net/leningradskaya-oblast' : {'Улица' : 'Ольховая', "Дом" : '24'},
'https://www.moskvaonline.ru/moskovskaya-oblast': {'Улица' : 'Карбышева Бал', "Дом" : '13'}
}

def retry(max_attempts, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print(f"Function {func} failed after {max_attempts} attempts")
        return wrapper

    return decorator

def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print (f"Время выполнения функции: {time.time()-t}")
        return res

    return tmp



def find_css(selector):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))


def find_xpath(selector):
    return WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, selector)))

def find_xpath_loc(selector):
    return WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, selector)))


def header(url, number):
    if find_css('#HeaderMenu a div.roistat-phone').text == number:
        print('номер в хедере ок')
    else:
        bot.send_message(chat_id, f'на странице {url} в хедере не найден правильный номер')

def footer(url,number):
    if find_css('div[datatest="main_footer"] a.roistat-phone span._phone').text == number:
        print('номер в футере ок')
    else:
        bot.send_message(chat_id, f'на странице {url} в футере не найден правильный номер')

def ts( url_number, url_address):
    global t
    # try:
    for urls in url_number.keys():
        for url in urls:
            print('ts')
            driver.delete_all_cookies()
            driver.get(url)
            driver.maximize_window()
            driver.refresh()

            print('- главная открыта')
            input_street = find_xpath('//input[@datatest="main_input_street_home_new"]')
            print('- поле ввода улицы найдено')

            input_street.send_keys(url_address[url]['Улица'])
            time.sleep(2.5)
            input_street.send_keys(Keys.ENTER)
            print('- улица введена')
            input_house = find_css('div.app115 input[datatest="main_input_street_home_new"]')
            print('- поле дом найдено')
            input_house.click()
            input_house.send_keys(url_address[url]['Дом'])
            time.sleep(2)
            input_house.send_keys(Keys.ENTER)
            print('- Номер дома введен')
            drop_down = find_xpath('//li[text()= "В квартиру"]')
            drop_down.click()
            print(' - выбран элемент выпадающего списка')
            find_btn = find_xpath('//div[text() = "показать тарифы"]')
            print('- кнопка показать тарифы найдена')
            find_btn.click()
            print('- кнопка найти тарифы нажата')
            close_btn = find_css('div[datatest="close_popup1_from_quiz_input_tel"]')
            print('- кнопка закрыть найдена')
            close_btn.click()
            print('- кнопка закрыть нажата')
            #проверка номера в хедере
            url = url
            header(url, url_number[urls]['main'])
            footer(url, url_number[urls]['main'])
            for prov in url_number[urls].keys():
                if prov != 'main':
                    x = find_css('input[name="change_providers"]')
                    print('фильтр найден')
                    x.clear()
                    x.send_keys(Keys.BACKSPACE)
                    x.send_keys(prov)
                    print('значение ввел')

                    prov_filter = find_xpath('/html/body/div/div/div[10]/div[3]/div/div/div/ul/li')
                    print(prov_filter.text)
                    print('фильтр провайдера найден')
                    prov_filter.click()
                    x.clear()
                    print('-результат отфильтрован')
                    time.sleep(1)
                    tarif_btn = find_css('div[datatest="providers_form_inspect_connect_tariff_button"]')
                    print('- кнопка тарифа найдена')
                    tarif_btn.click()
                    print('- кнопка тарифа нажата')
                    #проверка номера

                    if find_xpath('/html/body/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/div[2]/div[2]/a').text == url_number[urls][prov]:
                        print('номер верный')
                    else:
                        bot.send_message(chat_id, f'В форме заявки на странице {url} не найден номер провайдера {prov}')

                    popup_close = find_xpath("/html/body/div/div/div[4]/div/div/div/div[2]/span")
                    popup_close.click()











def main(url_number):
    print('Проверка главной')
    for urls in url_number.keys():
        for url in urls:
            print(url)
            driver.get(url)
            header(url, url_number[urls]['main'])
            footer(url, url_number[urls]['main'])

# main(url_number_set)

@retry(2,2)
def rating(url_number):
    print('Cтраница рейтинга')
    for urls in url_number.keys():
        for url in urls:
            print(url)
            driver.get(f'{url}/rating')
            driver.refresh()
            header(url, url_number[urls]['main'])
            footer(url, url_number[urls]['main'])
            while True:
                try:
                    all_btns = driver.find_elements(By.CSS_SELECTOR, 'div[datatest="providers_form_inspect_connect_tariff_button"]')
                except:
                    print('нет тарифов с кнопкой подключения')
                    break
                finally:
                    break

            for btn in all_btns:
                if btn.is_displayed():

                    driver.execute_script("window.scrollBy(0,200)")

                    btn.click()
                    if len(driver.window_handles) == 1:

                        alt = find_xpath('/html/body/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/div[1]/img')
                        alt_attribute = alt.get_attribute("alt")
                        print(alt_attribute)
                        if alt_attribute in  url_number[urls].keys():

                            current_number = find_xpath('/html/body/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/div[2]/div[2]/a').text
                            if current_number == url_number[urls][alt_attribute]:

                                print('номер в заявке верный')
                                pop_up_close = find_xpath('/html/body/div/div/div[4]/div/div/div/div[2]/span')
                                pop_up_close.click()
                            else:
                                print(f'найден номер {current_number}')
                                bot.send_message(chat_id, f'В форме заявки на странице {driver.current_url} не найден номер провайдера {url_number[urls][alt_attribute]}')
                                pop_up_close = find_xpath('/html/body/div/div/div[4]/div/div/div/div[2]/span')
                                pop_up_close.click()
                        else:
                            pop_up_close = find_xpath('/html/body/div/div/div[4]/div/div/div/div[2]/span')
                            pop_up_close.click()
                    else:
                        current = driver.current_window_handle
                        for d in driver.window_handles:
                            if d != current:
                                driver.switch_to.window(d)
                                driver.close()
                                driver.switch_to.window(current)



@timer
def catalog(url_number):
    print('Каталог провайдера')
    for urls in url_number.keys():
        for url in urls:
            print(url)
            driver.get(f'{url}/providers')
            driver.refresh()
            header(url, url_number[urls]['main'])
            footer(url, url_number[urls]['main'])
            while True:
                try:
                    all_btns = driver.find_elements(By.CSS_SELECTOR,
                                                    'div[datatest="providers_form_inspect_connect_tariff_button"]')
                except:
                    print('нет тарифов с кнопкой подключения')
                    break
                finally:
                    break

            for btn in all_btns:
                if btn.is_displayed():

                    driver.execute_script("window.scrollBy(0,220)")

                    btn.click()
                    if len(driver.window_handles) == 1:

                        alt = find_xpath('/html/body/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/div[1]/img')
                        alt_attribute = alt.get_attribute("alt")
                        print(alt_attribute)
                        if alt_attribute in url_number[urls].keys():

                            current_number = find_xpath(
                                '/html/body/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/div[2]/div[2]/a').text
                            if current_number == url_number[urls][alt_attribute]:

                                print('номер в заявке верный')
                                pop_up_close = find_xpath('/html/body/div/div/div[4]/div/div/div/div[2]/span')
                                pop_up_close.click()
                            else:
                                print(f'найден номер {current_number}')
                                bot.send_message(chat_id,
                                                 f'В форме заявки на странице {driver.current_url} не найден номер провайдера {url_number[urls][alt_attribute]}')
                                pop_up_close = find_xpath('/html/body/div/div/div[4]/div/div/div/div[2]/span')
                                pop_up_close.click()
                        else:
                            pop_up_close = find_xpath('/html/body/div/div/div[4]/div/div/div/div[2]/span')
                            pop_up_close.click()
                    else:
                        current = driver.current_window_handle
                        for d in driver.window_handles:
                            if d != current:
                                driver.switch_to.window(d)
                                driver.close()
                                driver.switch_to.window(current)


def tohome(url_number):
    print('страница поиска по адресу')
    for urls in url_number.keys():
        for url in urls:
            print(url)
            driver.get(f'{url}/orders/tohome')
            header(url, url_number[urls]['main'])
            footer(url, url_number[urls]['main'])




provider_card = {('https://101internet.ru/belgorod/providers/rostelecom/', 'https://101internet.ru/barnaul/providers/rostelecom/', 'https://101internet.ru/chelyabinsk/providers/rostelecom/',
'https://101internet.ru/kirov/providers/rostelecom/', 'https://101internet.ru/vladimirskaya-oblast/providers/rostelecom/',
'https://101internet.ru/penza/providers/rostelecom/', 'https://101internet.ru/samara/providers/rostelecom/', 'https://101internet.ru/cheboksary/providers/rostelecom/',
'https://101internet.ru/perm/providers/rostelecom/', 'https://101internet.ru/nizhniy-novgorod/providers/rostelecom/',
'https://101internet.ru/irkutsk/providers/rostelecom/') : {'Ростелеком' : '+7(800)101-17-90'},('https://101internet.ru/ekaterinburg/providers/rostelecom/',) : { "Ростелеком" : '+7(800)101-17-90'},
                 ('https://101internet.ru/ekaterinburg/providers/mts/',): {"МТС ": '+7(800)101-17-95'}, ('https://101internet.ru/ekaterinburg/providers/beeline/',): {"билайн": '+7(800)101-17-81'},
                 ('https://101internet.ru/ekaterinburg/providers/dom-ru/',): {"ДомРу": '+7(800)100-90-41'}, ('https://101internet.ru/novosibirsk/providers/rostelecom',): {"Ростелеком" : '+7(800)101-17-90'},
                 ('https://101internet.ru/novosibirsk/providers/mts',): {"МТС": '+7(800)101-17-95'},('https://101internet.ru/krasnodar/providers/rostelecom',): { "Ростелеком" : '+7(800)101-17-90'},
('https://101internet.ru/krasnodar/providers/ttk',): {"ТТК" : '+7(800)707-60-52'},('https://101internet.ru/tver/providers/rostelecom',): {"Ростелеком" : '+7(800)101-17-90'},
('https://101internet.ru/rostov-na-donu/providers/dom-ru',): {"Дом.ру" : '+7(800)100-90-41'}, ('https://101internet.ru/omsk/providers/beeline',): {"билайн" : '+7(800)101-17-81'},
('https://www.moskvaonline.ru/providers/rostelecom/', 'https://www.moskvaonline.ru/moskovskaya-oblast/providers/rostelecom/'): {"Ростелеком" : '+7(499)372-33-55'},
('https://www.moskvaonline.ru/providers/mgts/', 'https://www.moskvaonline.ru/moskovskaya-oblast/providers/mgts/'): {"МГТС" : '+7(495)106-82-09'},
('https://piter-online.net/providers/rostelecom/','https://piter-online.net/leningradskaya-oblast/providers/rostelecom/' ): {"Ростелеком" : '+7(812)605-80-89'},


                 }

def provider_page(provider_url):
    print('Карточки провайдера')
    for urls in provider_url.keys():
        for url in urls:
            print(url)
            driver.get(url)
            cart_number = find_css('#provider_banner div.app99 a')
            text = cart_number.text.replace(" ","").strip()
            print(text)
            true_number = list(provider_url[urls].values())[0]
            if  text == true_number:
                print('Номер в карточке верный')

            else:
                print(f'найден номер {text}')
                bot.send_message(chat_id,
                                 f'В карточке провайдера на странице {driver.current_url} не найден номер провайдера {list(provider_url[urls].keys())[0]}')

            connect_btn = find_css('div[datatest="providers_form_inspect_connect_tariff_button"]')
            connect_btn.click()
            current_app_number = find_xpath('/html/body/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/div[2]/div[2]/a').text
            if current_app_number == true_number:
                print('Номер в заявке верный')
            else:
                bot.send_message(chat_id,
                                 f'В форме подключения провайдера на странице {driver.current_url} не найден номер провайдера {list(provider_url[urls].keys())[0]}')


@timer
def test():
    main(url_number_set)
    rating(url_number_set)
    provider_page(provider_card)
    tohome(url_number_set)
    catalog(url_number_set)
    ts(url_number=url_number_set_2, url_address=url_adres)


schedule.every(20).minutes.do(test)





while True:
    schedule.run_pending()
    time.sleep(1)















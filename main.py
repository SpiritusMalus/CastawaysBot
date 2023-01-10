import multiprocessing
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options as edge_option


def edge():
    # options = edge_option()
    # options.add_argument('--headless')
    driver = webdriver.Edge()
    driver.get('https://alpha.castaways.com/?s=hub42&r=90914')
    el = ActionChains(driver, duration=1)
    time.sleep(10)
    el.key_down('a').perform()
    time.sleep(5)
    el.key_up('a').perform()

    while True:
        el.key_down('a').perform()
        time.sleep(3)
        el.key_up('a').perform()

        el.key_down('w').perform()
        time.sleep(2)
        el.key_up('w').perform()

        el.key_down('d').perform()
        time.sleep(2)
        el.key_up('d').perform()

        el.key_down('s').perform()
        time.sleep(2)
        el.key_up('s').perform()


if __name__ == "__main__":
    # process1 = multiprocessing.Process(target=firefox)
    # process2 = multiprocessing.Process(target=chrome)
    process3 = multiprocessing.Process(target=edge)
    process4 = multiprocessing.Process(target=edge)
    process5 = multiprocessing.Process(target=edge)
    process6 = multiprocessing.Process(target=edge)
    process7 = multiprocessing.Process(target=edge)
    process8 = multiprocessing.Process(target=edge)
    # process9 = multiprocessing.Process(target=chrome)
    # process10 = multiprocessing.Process(target=chrome)
    # process11 = multiprocessing.Process(target=edge)
    # process12 = multiprocessing.Process(target=edge)

    # process1.start()
    # process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    # process9.start()
    # process10.start()
    # process11.start()
    # process12.start()

from UK_part import *
from DE_part import *
from CA_part import *
from IT_part import *
from US_part import *
from ES_part import *
from FR_part import *
from selenium import webdriver
from setting import *

from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import unquote
import requests,sys,os



max_page=0

def get_base_url(site):
    # site=input("请输入站点/US/UK/FR/ES/IT/CA/DE>>")
    if site=='US':
        url='https://www.amazon.com/'
    elif site=='UK':
        url='https://www.amazon.co.uk/'
    elif site=='FR':
        url='https://www.amazon.fr/'
    elif site=='ES':
        url='https://www.amazon.es/'
    elif site=='IT':
        url='https://www.amazon.it/'
    elif site=='CA':
        url='https://www.amazon.ca/'
    elif site=='DE':
        url='https://www.amazon.de/'
    else:
        print("请输入正确的内容>>")
        get_base_url(site)
    return [url,site]




def main():
    asin=input("请输入查询的aisn码>>")
    url=get_base_url()
    site=url[1]
    print("正在启动浏览器...")
    driver=webdriver.Chrome(CHROM_PATH)
    driver.get(url[0])
    page = 1

    # driver.find_elements_by_xpath("//input[@id='twotabsearchtextbox']")[0].send_keys('kw')
    amazon=input("操作完成后直接回车>>")
    # for s in range(60):
    #     time.sleep(1)
    #     print("剩余时间%s"%(30-s))
    html = driver.page_source
    print("当前页下载完成!,正在关闭当前浏览器...")
    driver.quit()

    if site == 'US':
        # page=1
        # html=driver.page_source
        print("当前正是:%s"%page)
        US_analysis(html,page,asin)
        driver.quit()
    elif site=='UK':
        UK_analysis(html,page,asin,url)
        # print(111)
    elif site=='FR':
        FR_analysis(html, page, asin,url)
    elif site=='ES':
        # url='https://www.amazon.es/'
        ES_analysis(html,page,asin,url)
    elif site=='IT':
        # url='https://www.amazon.it/'
        IT_analysis(html,page,asin,url)
    elif site=='CA':
        # url='https://www.amazon.ca/'
        CA_analysis(html,page,asin,url)
    elif site=='DE':
        # url='https://www.amazon.de/'
        DE_analysis(html,page,asin,url)
    else:
        print("请输入正确的内容>>")
        get_base_url()

    end = input("回车直接退出!\n重新查询请输入任意字符后回车\n没反应请多一次回车")
    if end=='':
        return [url,site]
    else:
        main()


def qt_mian(site,asin):
    url = get_base_url(site)
    # url = get_base_url()
    site = url[1]
    print("正在启动浏览器...")
    driver = webdriver.Chrome(CHROM_PATH)
    driver.get(url[0])
    page = 1

    # driver.find_elements_by_xpath("//input[@id='twotabsearchtextbox']")[0].send_keys('kw')
    amazon = input("操作完成后直接回车>>")
    # for s in range(60):
    #     time.sleep(1)
    #     print("剩余时间%s"%(30-s))
    html = driver.page_source

    print("当前页下载完成!,正在关闭当前浏览器...")
    driver.quit()

    return html

    # if site == 'US':
    #     # page=1
    #     # html=driver.page_source
    #     print("当前正是:%s" % page)
    #     US_analysis(html, page, asin)
    #     driver.quit()
    # elif site == 'UK':
    #     UK_analysis(html, page, asin, url)
    #     # print(111)
    # elif site == 'FR':
    #     FR_analysis(html, page, asin, url)
    # elif site == 'ES':
    #     # url='https://www.amazon.es/'
    #     ES_analysis(html, page, asin, url)
    # elif site == 'IT':
    #     # url='https://www.amazon.it/'
    #     IT_analysis(html, page, asin, url)
    # elif site == 'CA':
    #     # url='https://www.amazon.ca/'
    #     CA_analysis(html, page, asin, url)
    # elif site == 'DE':
    #     # url='https://www.amazon.de/'
    #     DE_analysis(html, page, asin, url)
    # else:
    #     print("请输入正确的内容>>")
    #     get_base_url()


def conti_main(site,html, page, asin, url):
    if site == 'US':
        # page=1
        # html=driver.page_source
        print("当前正是:%s" % page)
        US_analysis(html, page, asin)
        # driver.quit()
    elif site == 'UK':
        UK_analysis(html, page, asin, url)
        # print(111)
    elif site == 'FR':
        FR_analysis(html, page, asin, url)
    elif site == 'ES':
        # url='https://www.amazon.es/'
        ES_analysis(html, page, asin, url)
    elif site == 'IT':
        # url='https://www.amazon.it/'
        IT_analysis(html, page, asin, url)
    elif site == 'CA':
        # url='https://www.amazon.ca/'
        CA_analysis(html, page, asin, url)
    elif site == 'DE':
        # url='https://www.amazon.de/'
        DE_analysis(html, page, asin, url)
    else:
        print("请输入正确的内容>>")
        get_base_url()


# main()
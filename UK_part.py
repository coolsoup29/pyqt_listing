from bs4 import BeautifulSoup
from urllib.parse import unquote
import sys
from all_loader import *



from bs4 import BeautifulSoup
from urllib.parse import unquote
import sys
from all_loader import *




from bs4 import BeautifulSoup
from urllib.parse import unquote
import sys
from all_loader import *


def UK_get_sp(tag):
    try:
        xx = tag.parent.parent.contents[1].text
        # print(xx)
        if xx=='Sponsored':
            return "广告"
        else:
            return "非广告"
    except Exception as e:
        # print(e,111)
        return "非广告"

def UK_get_next(soup):
    try:
        next_page = 'https://www.amazon.co.uk' + soup.find_all('a', 'pagnNext')[0].attrs['href']
    except:
        # print(soup.find_all('li', 'a-last')[0].contents[0])
        next_page =  'https://www.amazon.co.uk' + soup.find_all('li', 'a-last')[0].contents[0].attrs['href']
        # print(next_page)
    if next_page=='Suivant':
        return 0
    return next_page


def current_page_get(html):
    try:
        soup=BeautifulSoup(html,'html.parser')
        tags=soup.find_all('li','a-selected')
        current_page=tags[0].contents[0].text
        print(current_page)
        return current_page
    except:
        return 1
def UK_analysis(html,page,search_asin,url):
    # page=1
    global max_page
    current_page=current_page_get(html)
    if page==1:
        soup=BeautifulSoup(html,'html.parser')
        try:
            max_page=soup.find_all('span','pagnDisabled')[0].text
        except Exception as e:
            try:
                max_page=soup.find_all('li','a-disabled')[1].text
            except Exception as e:
                max_page=100
        print(max_page)
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("\r当前进度是:%s/%s"%(page,max_page),end='')
    soup=BeautifulSoup(html,'html.parser')
    tags=soup.find_all('a','a-link-normal a-text-normal')
    # print(len(tags))
    if len(tags)==0:
        print('round 1')
        tags=soup.find_all('h5','a-color-base s-line-clamp-2')

        if len(tags)!=0:
            for tag in tags:
                # url = tag.contents[1].attrs['href']
                # print(url)
                sp=UK_get_sp(tag)
                url = tag.contents[1].attrs['href']
                url = unquote(url, 'utf-8')
                asin = url.split('/dp/')[1].split('/')[0]
                # print(asin,sp)
                if asin == search_asin:
                    # print(tag.parent.contents[1].text)
                    print('当前页数是', current_page, '排名:', tags.index(tag), "广告:", sp)
                    write_to_rank([asin,current_page,'英国'])
                    with open('test.html', 'w', encoding='utf-8') as f:
                        f.write(html)
                    sys.exit()
                    return 'GG'
        else:
            print('round 2')
            tags = soup.find_all('h5', 'a-color-base s-line-clamp-4')
            if len(tags)==0:
                print("be checked as robot,加载失败!,正在重新加载!")

                html = loader(url)
                UK_analysis(html, page, search_asin,url)
                # with open('test.html', 'w', encoding='utf-8') as f:
                #     f.write(html)
                # sys.exit()
                # return 'GG'

            for tag in tags:
                sp=UK_get_sp(tag)
                # url = tag.contents[1].attrs['href']
                # print(url)
                url = tag.contents[1].attrs['href']
                url = unquote(url, 'utf-8')
                asin = url.split('/dp/')[1].split('/')[0]
                # print(asin,sp)
                if asin == search_asin:
                    # print(tag.parent.contents[1].text)
                    print('当前页数是', current_page, '排名:', tags.index(tag)+1, "广告:", sp)
                    write_to_rank([asin,current_page,'英国'])
                    with open('test.html', 'w', encoding='utf-8') as f:
                        f.write(html)
                    sys.exit()
                    return 'GG'


        next_page = UK_get_next(soup)
        # print('next>>', next_page)
        page += 1
        if next_page == 0:
            print('全部抓取完成')
        else:
            html = loader(next_page)
            # html = selenium_loader(next_page)
            UK_analysis(html, page, search_asin,next_page)

    else:
        for tag in tags:


            try:
                sp=UK_get_sp(tag)
                # print(tag)
                url = tag.attrs['href']
                url=unquote(url,'utf-8')
                # print(url)
                asin=url.split('/dp/')[1].split('/')[0]
                print(asin)

                if asin==search_asin:
                    # print(tag.parent.contents.contents[1].text)
                    print('\r当前页数是',current_page,'排名:',tags.index(tag)+1,"广告:",sp,end='')
                    write_to_rank([asin,current_page,'英国'])
                    with open('test.html','w',encoding='utf-8') as f:
                        f.write(html)
                    sys.exit()
                    return 'GG'
            except Exception as e:
                print(e)
                continue
        try:
            next_page='https://www.amazon.co.uk'+soup.find_all('li','a-last')[0].contents[0].attrs['href']
        except Exception as e:
            # print(e)
            next_page='https://www.amazon.co.uk' + soup.find_all('a','pagnNext')[0].attrs['href']
            # print(next_page)
            # sys.exit()
        print('next>>',next_page)
        page+=1
        if next_page==0:
            print('全部抓取完成')
        else:
            html=loader(next_page)
            # html=selenium_loader(next_page)
            UK_analysis(html,page,search_asin,next_page)


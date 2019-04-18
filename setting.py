import time
import random as R



CHROM_PATH='/home/yice/Desktop/set_driver/chromedriver'










# user-agent
user_agent = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    ]

# the site of search
ref = ["http://www.yahoo.com",
        "http://www.yandex.ru",
        "http://www.bing.com",
        "http://www.google.com.hk",
        "http://www.naver.com",
        "http://www.rambler.ru",
        "http://www.goo.ne.jp",
        "http://www.go.com",
        "http://www.webcrawler.com",
        "http://www.tiscali.it",
        "http://www.excite.com",
        "http://www.meta.ua",
        "http://www.search.com",
        "http://saucenao.com",
        "http://www.cari.com.my",
        "http://www.looksmart.com",
        "http://www.lycos.com",
        "http://infospace.com",
        "http://www.wlw.de",
        "http://www.najdi.si",
        "http://www.ciao.es",
        "http://www.dmoz.org",
        "http://www.ceek.jp",
        "http://www.fireball.de",
        "http://www.jubii.dk",
        "http://www.hotbot.com",
        "http://www.sputtr.com",
        "http://www.splut.com",
        "http://www.hit-parade.com",
        "http://www.goto.com",
        "http://www.voila.fr",
        "http://www.altavista.com",
        "http://www.accoona.com",
        "http://www.all.by",
        "http://www.gogreece.com",
        "http://www.bellnet.de",
        "http://www.searchengine.com",
        "http://www.slider.com",
        "http://www.newmalaysia.com",
        "http://www.abrexa.co.uk",
        "http://www.kellysearch.com",
        "http://www.anzwers.com.au",
        "http://torrent-finder.info",
        "http://www.sunsteam.com",
        "http://www.blinde-kuh.ch",
        "http://www.godado.it",
        "http://www.apali.com",
        "http://www.buscapique.com",
        "http://www.walhello.com",
        "http://infoo.se",
        "http://www.akavita.by",
        "http://www.acoon.de",
        "http://www.helles-koepfchen.ch",
        "http://www.google.com",
        "http://www.yippy.com",
        "http://www.abacho.ch",
        "http://www.cnous.ch",
        "http://www.abacho.com",
        "http://www.cusco.pt",
        "http://www.yabba.com",
        ]



headers_img = {
                    # "Host":"https://www.amazon.com",
                    "User-Agent": R.choice(user_agent),
                    "Referer":R.choice(ref),
                    # 'cookie': 'session-id=260-2332126-7002167; i18n-prefs=EUR; ubid-acbfr=260-3347699-5251144; x-wl-uid=13Wv5jzhWUUweun3OxtBZNns5Vgah0vWAXKX5zyJP1XE1Re5olaHaUBuzavBkJZ+4mhg7wxMh8pQ=; session-token=27F6mKODwGVuSm/HLG+I9ru/q5ewqAUqURpmU1nmNrqa0T7nMQHj99oM7FKDV1D9VLiWyHPx3cOdUUU7fpiAohDhwceQ9YEEDk0/SBsTXKLemtPTboxOqriqvm3sPiblt/eJRvreKiVIeqE//sJejNzJVMpX7z1PaS+uVVM0eh1o9Y75sFiaUjIniTRJS/ZJ; session-id-time=2082754801l; csm-hit=tb:WJM43T88F4727FAWGWYR+s-0CD44XFT55CA2XFN6FW8|1554685931253&t:1554685931253&adb:adblk_n',
                    "Origin":"https://www.amazon.com",
                    "Content-Type":"text/plain;charset=UTF-8",
                    "Connection": 'close',
                    "accept":"*/*",
                    }


def write_to_rank(msg):
    # with open("rank.txt",'a',encoding='utf-8') as f:
    #     sql = '站点：'+ msg[2] +' ASIN：' + msg[0]+' 页数：' + msg[1] +" 时间："  + str(time.ctime()).replace(' ','-') + "\n"
    #     f.write(sql)
    #     print(sql)
    #     print("写入 rank.txt 文件中")

    import csv
    with open("rank.csv", "a", newline="") as datacsv:
            # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
            csvwriter = csv.writer(datacsv, dialect=("excel"))
            # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
            csvwriter.writerow([msg[2], msg[0], msg[1], str(time.ctime()).replace(' ','-')])







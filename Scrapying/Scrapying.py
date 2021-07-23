from datetime import date,timedelta
import json
import numpy as np
import requests
from bs4 import BeautifulSoup as BS

def get_data(start_date, end_date):
    URL = 'https://cn.investing.com/instruments/HistoricalDataAjax'
    headers = {
    'authority': 'cn.investing.com',
    'accept': 'text/plain, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://cn.investing.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://cn.investing.com/equities/apple-computer-inc-historical-data',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'PHPSESSID=qp85vakkesjpu3gi8he16f50ev; SideBlockUser=a^%^3A2^%^3A^%^7Bs^%^3A10^%^3A^%^22stack_size^%^22^%^3Ba^%^3A1^%^3A^%^7Bs^%^3A11^%^3A^%^22last_quotes^%^22^%^3Bi^%^3A8^%^3B^%^7Ds^%^3A6^%^3A^%^22stacks^%^22^%^3Ba^%^3A1^%^3A^%^7Bs^%^3A11^%^3A^%^22last_quotes^%^22^%^3Ba^%^3A1^%^3A^%^7Bi^%^3A0^%^3Ba^%^3A3^%^3A^%^7Bs^%^3A7^%^3A^%^22pair_ID^%^22^%^3Bs^%^3A4^%^3A^%^226408^%^22^%^3Bs^%^3A10^%^3A^%^22pair_title^%^22^%^3Bs^%^3A0^%^3A^%^22^%^22^%^3Bs^%^3A9^%^3A^%^22pair_link^%^22^%^3Bs^%^3A28^%^3A^%^22^%^2Fequities^%^2Fapple-computer-inc^%^22^%^3B^%^7D^%^7D^%^7D^%^7D; geoC=TW; adsFreeSalePopUp=1; adBlockerNewUserDomains=1627037954; StickySession=id.94392601784.095cn.investing.com; udid=3beef673c587a47e1a1043498c1490b7; smd=3beef673c587a47e1a1043498c1490b7-1627037953; __cflb=0H28uxmf5JNxjDUC6WDvQUEoJyvKUTrtxbDYP47PU7n; protectedMedia=2; __gads=ID=7a0cc87492427074:T=1627037955:S=ALNI_MaSoDDtif0CpbZonRHFa8fXeHvdzg; outbrain_cid_fetch=true; _ga=GA1.2.765852293.1627037954; _gid=GA1.2.1995928186.1627037957; _gat=1; _gat_allSitesTracker=1; nyxDorf=NzM0ZjFjNHYyZ2tjYi8zMGIyMWlheDoxMjM^%^3D; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1627037957; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1627037957; __cf_bm=0630e9079ad6db262f7e131c1c8f7c953c1cd671-1627037960-1800-AVNcdx7X5Xo4UcKjNVsrT/xUxIMpr4ZHiovZvmQLJ6pe0vCwFt7SVrwHQmMc/UZYpsWYJkmaRpG1YQBRV2CAi30a3TvB2KGuZ1ObdR+5lPFQ7VdeQNNmNzJfiDUAlcJluQ==; G_ENABLED_IDPS=google',
    }
    data = {
      'curr_id': '6408',
      'smlID': '1159963',
      'header': 'AAPL历史数据',
      'st_date': start_date,
      'end_date': end_date,
      'interval_sec': 'Daily',
      'sort_col': 'date',
      'sort_ord': 'DESC',
      'action': 'historical_data'
    }
    
    req = requests.post(URL, headers=headers, data=data)
    soup = BS(req.content, 'html.parser')
    t = soup.find_all('tr')
    result = {}
    for i in range(1,len(t)-1):
        content = t[i].find_all('td')
        val = []
        for j in range(1,len(content)):
            val.append(content[j].string)
        result[content[0].string] = val
    arr = ['最高','最低','差價','平均','漲跌幅']
    content = t[-1].find_all('span')
    for i in range(len(content)):
        result[arr[i]] = content[i].string
    result = json.dumps(result,ensure_ascii=False)
    
    return result
    
if __name__ == '__main__':
    print('input start date (yyyy/mm//dd)')
    start_date = input()
    print('input end date (yyyy/mm//dd)')
    end_date = input()
    result = get_data(start_date, end_date)
    print(result)
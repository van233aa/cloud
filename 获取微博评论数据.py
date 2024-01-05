import requests
import parsel
import csv

f=open('评论2.csv','a',encoding='utf-8-sig',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['id','screen_name','text_raw','source','like_counts','followers_count'])

headers={

    'Cookie':'SINAGLOBAL=3623229557425.0317.1625324086810; UOR=,,cn.bing.com; PC_TOKEN=b5b2fa254f; login_sid_t=ba60f9e75d6940e2edbeb783a9c70410; cross_origin_proto=SSL; _s_tentry=cn.bing.com; Apache=8362608304459.196.1704271259267; ULV=1704271259270:15:2:2:8362608304459.196.1704271259267:1704202651947; XSRF-TOKEN=yogNKDdT839ntf1iLbPKGdWi; WBStorage=267ec170|undefined; wb_view_log=1536*8641.25; crossidccode=CODE-gz-1RkWOP-3mNQxo-dzgyiCvIV8hUGVj4c93c0; SSOLoginState=1704271326; SUB=_2A25IkW2ODeRhGeBH41QV9CbKyTmIHXVr7-9GrDV8PUJbkNAbLVnSkW1NQbEgcHhHcsayyZU5oiLH9027vHcTLnig; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh1Jj_Ib3xXscpxvgD9kS255JpX5KzhUgL.Foq41hqXShnceo-2dJLoI0qLxKBLBonLB.2LxKBLB.zL1h5LxKBLBo.L1hnLxKqL1-eL1h.LxKBLB.2LB.2LxK-L1K2LBKzt; WBPSESS=P9Jsf0pjIDbGo9A5vjDc6WeRc5gJvkaPXwYfSHMWxrpDg2JSK7PwLLC1NoS9BefKIeyPH09mQlXWOXcZgn4eJgu7l5ni1sAF6Dphasq6Nz-_2GXzWN0YzTdKZJNLVHVPAiH33xVx3mRcuulC7satNA==',
    'Referer':'https://weibo.com/1749127163/NA8tbCaao',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}
def get_next(next='count=10'):
    url=f"https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4986123699095548&is_show_bulletin=2&is_mix=0&{next}&uid=1"
    response=requests.get(url=url)
    travel_data=response.json()
    list=travel_data['data']
    max_list=travel_data['max_id']
    for i in list:
        text_raw=i['text_raw']
        text=i['text']
        source=i['source']
        id=i['id']
        like_counts=i['like_counts']
        screen_name=i['user']['screen_name']
        followers_count=i['user']['followers_count']
        print(id,screen_name,text_raw,source,like_counts,followers_count)
        csv_writer.writerow([id,screen_name,text_raw,source,like_counts,followers_count])
    max_str="max_id="+str(max_list)
    get_next(max_str)
get_next()

import requests
import parsel
import csv

f=open('评论2.csv','a',encoding='utf-8-sig',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['id','screen_name','text_raw','source','like_counts','followers_count'])

headers={

    'Cookie':'.............................',
    'Referer':'.......................................',
    'User-Agent':'.........................................................',
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

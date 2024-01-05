import csv
from wordcloud import WordCloud
with open('评论2.csv','r',encoding='utf-8-sig')as f:
    reader=csv.reader(f)
    header=next(reader)
    column_index=2
    column_data=[row[column_index] for row in reader]

ea={'doge','n','good','http','cn','awsl','t'}
txt=column_data
newtxt=''.join(txt)


wordcloud=WordCloud(width=2000,
                    height=1080,
                    font_path='msyh.ttc',
                    background_color='white',
                    stopwords=ea,
                    ).generate(newtxt)
wordcloud.to_file('comment.png')
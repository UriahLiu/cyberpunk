def get_urls(max_page):
    start_url = 'http://news.cnstock.com/news/sns_yw/'
    urls = []
    for i in range(1,max_page+1):
        spec_url = start_url + str(i) if i>1 else start_url + 'index.html'
        source = pq(spec_url)
        urls += [item.attr('href') for item in source('.new-list li a').items()]
    return urls
def get_news(url):
    source = pq(url)  
    title = source('h1.title').text()
    date = source('span.timer').text()
    content = source('#qmt_content_div.content').text()
    if content:
        return {'URL': url, 'Title': title, 'Date': date, 'Content': content}
def save_txt(res):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f_name = news_date + '_' + res['Title']
    with codecs.open('securitynews/%s.txt'%f_name, 'w+', encoding='utf-8') as f:
        f.write('正文:' + res['Content'] + '\n')

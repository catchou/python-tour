from urllib import request
import re

class Spider:
    url = 'https://www.panda.tv/cate/pubg'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    title_pattern = '<span class="video-title" title="([\s\S]*?)">'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    name_pattern = '<span class="video-nickname" title="([\s\S]*?)"'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        #print(htmls)
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)

        for html in root_html:
            title = re.findall(Spider.title_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            name = re.findall(Spider.name_pattern, html)

            print('title:%s , number:%s, name:%s' % (title, number,name))
            print('-----------------------------')
    #Spider 的入口方法
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

spider = Spider()
spider.go()
#encoding:

import requests
import re
base_url = "https://qiushibaike.com/text/page/1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"}
root_pattern = "<div class=\"author clearfix\">([\s\S]*?)<div class=\"stats\">"
text_pattern = "<span>\n\n([\s\S]*?)\n</span>"
author_pattern = "<h2>\n([\s\S]*?)\n</h2>"
maxpage_pattern = "<span class=\"page-numbers\">([\s\S]*?)</span>"

r = requests.get(base_url,headers=headers)
base_str = r.text

# 获取各页面的内容
def get_contents():
    maxPage = int(re.findall(maxpage_pattern, base_str)[-1])
    for i in range(maxPage):
        url = "https://qiushibaike.com/text/page/%s" % (i+1)
        resp = requests.get(url, headers=headers)
        str = resp.text
        root_contents = re.findall(root_pattern, str)
        print("-------------------------------第%s页:-------------------------" % (i + 1))
        with open(r'E:\test\qiushibaike.txt', 'a') as f:
            f.write('-------------------------------第%s页:-------------------------\n' % (i + 1))
        for content in root_contents:
            author = re.findall(author_pattern, content)
            if(author == []):
                author = ['佚名']
            text = re.findall(text_pattern, content)
            with open(r'E:\test\qiushibaike.txt', 'a', encoding='gbk', errors='backslashreplace') as f:
                f.write('作者: %s\n' % author)
                f.write('内容: %s\n' % text[0][1:-1])

get_contents()

import requests
import re
base_url = "https://qiushibaike.com/text/page/1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"}
root_pattern = "<div class=\"author clearfix\">([\s\S]*?)<div class=\"stats\">"
text_pattern = "<span>\n\n([\s\S]*?)\n</span>"
author_pattern = "<h2>\n([\s\S]*?)\n</h2>"
maxpage_pattern = "<span class=\"page-numbers\">([\s\S]*?)</span>"

qiubai_patterns = {
    "root_pattern":"<div class=\"author clearfix\">([\s\S]*?)<div class=\"stats\">",
    "maxpage_pattern":" <span class=\"page-numbers\">([\s\S]*?)</span>",
    "text_pattern":"<span>\n\n([\s\S]*?)\n</span>",
    "author_pattern":"<h2>\n([\s\S]*?)\n</h2>"
}
r = requests.get(base_url,headers=headers)
base_str = r.text
root_texts = re.findall(root_pattern, base_str)
for text in root_texts:
    author = re.findall(author_pattern, text)
    if author==[]:
        author = ['佚名']
    content = re.findall(text_pattern, text)
    #print("作者：%s type:%s \n 内容: %s" % (author, type(author), content))

# 获取各页面的内容
def get_contents():
    maxPage = int(re.findall(maxpage_pattern, base_str)[-1])
    for i in range(maxPage):
        url = "https://qiushibaike.com/text/page/%s" % (i+1)
        resp = requests.get(url, headers=headers)
        str = resp.text
        root_contents = re.findall(root_pattern, str)
        #print("-------------------------------第%s页:-------------------------" % (i + 1))
        for content in root_contents:
            author = re.findall(author_pattern, content)
            if(author == []):
                author = ['佚名']
            text = re.findall(text_pattern, content)
            #print("作者：%s" % author)


get_contents()



# 提取各页面的数据
# @str root_contents 该页面的所有内容
# @dict 提取的规则。例：{"a_pattern":"pattern_contents"}
def analysis_contents(root_contents, *patterns):
    for pattern in patterns:
        print(pattern.items())
        #pass
    #print(type(patterns))


#get_contents()
analysis_contents(base_str, qiubai_patterns)
import xlrd
import xlwt
import jieba
from wordcloud import WordCloud, STOPWORDS
from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread
EXCELFILE = r'bili-紫罗兰永恒花园.xls'
BACKGROUNDIMG = ""
def doXmlSheet():
    readbook = xlrd.open_workbook(EXCELFILE)#读取excel文件
    sheets1 = readbook.sheet_by_index(0)
    sheets2 = readbook.sheet_by_index(1)
    strs = ""
    strs += doXmls(sheets1,strs)
    strs += doXmls(sheets2,strs)
    #print( " | ".join(jieba.cut(strs)))
    wordCl(strs)
def doXmls(sheets,strs):
    strr = ""
    for i in range(sheets.nrows):
        common = str(sheets.cell(i,3).value)
        strr += common
    return strr
        #print(common)
def wordCl(strs):
    stopwords = STOPWORDS.copy()
#     stopwords.add('感觉')
#     stopwords.add('第一集')
#     stopwords.add('已经')
#     stopwords.add('为什么')
#     stopwords.add('啊啊啊')
#     stopwords.add('不要')
#     stopwords.add('没有')
#     stopwords.add('？')
#     stopwords.add('觉得')
#     stopwords.add('时候')
#     stopwords.add('开始')
#     stopwords.add('一下')
#     stopwords.add('自己')
#     stopwords.add('就是')
#     stopwords.add('还有')
#     stopwords.add('但是')
#     stopwords.add('怎么')
#     stopwords.add('不要')
    word_list = [" ".join(jieba.cut(strs))]
    new_text = ' '.join(word_list)
    imagename = path.join(path.dirname(__file__), BACKGROUNDIMG)  # 背景图片路径
    coloring = imread(imagename)             # 读取背景图片 
    #fontname=path.join(path.dirname(__file__), "msyh.ttf")  # 使用的是微软雅黑字体   
    wordcloud = WordCloud(stopwords=stopwords,min_font_size=10,
        mask=coloring,font_path="msyh.ttf",scale=24, 
        background_color='white').generate(new_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

if __name__=='__main__':
    doXmlSheet()
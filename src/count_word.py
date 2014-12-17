#作者 ：赵鑫 高晓旸 at pku
#coding=utf-8
import  xml.dom.minidom;
import codecs;
import sys
sys.path.append("../")
import jieba;
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg;
#打开xml文档
#对训练集进行分词
def cut_train(filename):
    dom = xml.dom.minidom.parse(filename)
#seg_list = jieba.cut("我来到北京大学", cut_all=False)
#得到文档元素对象
    root = dom.documentElement;
    contents=root.getElementsByTagName('content');
    rates=root.getElementsByTagName('rating');
    fileHandle = codecs.open ( 'cut/cut_rate_20433139.txt', 'w',"utf-8" )
    for rate in rates:
            fileHandle.write (rate.firstChild.data+' ');  
    fileHandle.close() 
    fileHandle = codecs.open ( 'cut/cut_word_20433139.txt', 'w' ,"utf-8")   
    for content in contents:
        seg_list=pseg.cut(content.firstChild.data);
        result="";
        for lists in seg_list:
            if not lists.word.isspace():
                result+= str(lists.word)+"/"+str(lists.flag)+' ';
        fileHandle.write ( result+'\n' ) ; 
    fileHandle.close()
#对预测集进行分词  
def cut_predict(filename):
    dom = xml.dom.minidom.parse(filename)
#seg_list = jieba.cut("我来到北京大学", cut_all=False)
#得到文档元素对象
    root = dom.documentElement;
    contents=root.getElementsByTagName('content');
    fileHandle = codecs.open ( 'cut/pcut_word_20433139.txt', 'w' ,"utf-8")   
    for content in contents:
        seg_list=pseg.cut(content.firstChild.data);
        result="";
        for lists in seg_list:
            if not lists.word.isspace():
                result+= str(lists.word)+"/"+str(lists.flag)+' ';
        fileHandle.write ( result+'\n' ) ; 
    fileHandle.close()  
cut_train('20Movie/20433139.xml')
cut_predict('20predict/20433139.xml');
#stop.deal_stopword('mid_train_word.txt');
#print(rates[0].firstChild.data+contents[0].firstChild.data)

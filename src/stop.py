#作者 ：赵鑫 高晓旸 at pku
#coding=utf-8
import codecs;
#先过滤掉分词结果中的代词和冠词
def deal_v(filenames,flienames1):
    filename=codecs.open(filenames,'r','utf-8');
    readlist=filename.readlines();
    fileHandle = codecs.open ( flienames1, 'a' ,"utf-8")
    for eachline in readlist:
        text=eachline.rstrip().split(' ');
        result="";
        for t in text:
            if   t.find( '/r' )>0 or t.find( '/f' )>0:
                pass;
            else:
                re=t.split('/');
                result+=re[0]+' ';
          
        fileHandle.write ( result+'\n' ) ; 
    fileHandle.close() 
#过滤掉停用词
def deal_stopword(filenames,filenames1):
   stopwords = {}.fromkeys([ line.rstrip() for line in codecs.open ( '中文停用词表(比较全面_有1208个停用词).txt','r' ,"utf-8") ]);
   filename= codecs.open ( filenames, 'r',"utf-8" );
   fileHandle = codecs.open ( filenames1, 'w' ,"utf-8")
   readlist=filename.readlines();
   for eachline in readlist:
       texts=eachline.rstrip().split(' ');
       result="";
       for t in texts:
           if t not in stopwords:
               result+=t+" ";
         
       fileHandle.write ( result+'\n' ) ; 
   fileHandle.close() 
deal_v('cut/cut_word_20433139.txt','cut/end_train.txt');
deal_stopword('cut/end_train.txt','cut/word_20433139.txt') ;
deal_v('cut/pcut_word_20433139.txt','cut/pend_train.txt');
deal_stopword('cut/pend_train.txt','cut/pword_20433139.txt') ;
       

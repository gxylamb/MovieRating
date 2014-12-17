#作者 ：赵鑫 高晓旸 at pku
#coding=utf-8
import codecs;
#求出所有影评的df值和tf值
def tf(filenames,filenames1,filenames2):
    filename= codecs.open ( filenames, 'r',"utf-8" );
    readlist=filename.readlines();
    t=dict();df=dict();mid=dict();
    for lists in readlist:
        words=lists.strip().split(' ');
        for word in words:
            if word in t:
                t[word]+=1;
            else:
                t[word]=1;
            mid[word]=1;
        for k,x in mid.items():
            if k in df:
                df[k]+=1;
            else:
                df[k]=1;
        mid.clear();
    items=t.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    filename.close();
    filename=codecs.open(filenames1,'w','utf-8');
    for k in backitems:
        filename.write(k[1]+' '+str(k[0])+'\n');
    filename.close();
    backitems.clear();
    items=df.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    filename=codecs.open(filenames2,'w','utf-8');
    for key in backitems:
        filename.write(key[1]+' '+str(key[0])+'\n');
    filename.close();
tf('cut/word_20433139.txt','cut/word_20433139_tf.txt','cut/word_20433139_df.txt');
tf('cut/pword_20433139.txt','cut/pword_20433139_tf.txt','cut/pword_20433139_df.txt');

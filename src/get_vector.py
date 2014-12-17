#作者 ：赵鑫 高晓旸 at pku
import CHI;
import codecs;
import math;
def dict_df(filename,a):
    file=codecs.open(filename, 'r', 'utf-8');
    readlists=file.readlines();
    df=dict();l=len(readlists);print(l);
    for i in range(a):
        if a>=l:
            break;
        else:   
            re=readlists[i].strip().split(' '); 
            if len(re)==2:
                df[re[0]]=float(re[1]);
            else:
                print(re);
    return df;
#设置每类关键词选择的个数
def select_d(n):
    df=dict();t=dict();j=1;
    for i in range(5):
        t=dict_df('class_chi/class'+str(i+1)+'_df_chi.txt',n);
        for k,x in t.items():
            if k in df:
                df[k]+=x;
            else:
                df[k]=x;
        t.clear();
    print(len(df));
    t.clear();
    for k,x in df.items():
        t[k]=j;
        j+=1;
        print(str(j))
    return t;
#求出训练集的libsvm向量集
def tf_idf_v(dicts,filename,filename1,filename2,m):
    t=CHI.dict_df(filename);mid_dict=dict();
    file=codecs.open(filename1, 'r','utf-8');
    readline=file.readline().strip().split(' ');
    file1=codecs.open(filename2, 'r','utf-8');
    readlists=file1.readlines();
    l=len(readline);print(len(dicts))
    for i in range(l):
        texts=readlists[i].strip().split(' ');
        data=[0 for i in range(len(dicts)+1)];  
        l_word=len(texts);
        data[0]=int(readline[i]);
        for text in texts:
            if text in mid_dict:
                mid_dict[text]+=1;
            else:
                mid_dict[text]=1;
        for k,x in mid_dict.items():
            if k in dicts:
               tf=float(x)/l_word;
               idf=math.log(8000/float(t[k]));
               #print(dicts[k])
               data[int(dicts[k])]=tf*idf;
        l_word=0;
        #print(type(data[0]))
        if i<m:
            fileHandle = codecs.open ('train/train20433139.txt', 'a' ,"utf-8")
            for k,x in enumerate(data): 
                if k==0:
                    fileHandle.write(str(x)+' ');
                else:
                    fileHandle.write(str(k)+':'+str(x)+' ');
            fileHandle.write('\n');
            fileHandle.close() ;
        else:
            fileHandle = codecs.open ('train/predict20433139.txt', 'a' ,"utf-8")  
            for k,x in enumerate(data): 
                if k==0:
                    fileHandle.write(str(x)+' ');
                else:
                    fileHandle.write(str(k)+':'+str(x)+' ');
            fileHandle.write('\n');
            fileHandle.close() ;
#求出预测集的libsvm向量集
def tf_idf_predict_v(dicts,filename,filename1,filename2):
    t=CHI.dict_df(filename);mid_dict=dict();
    file1=codecs.open(filename1, 'r','utf-8');
    readlists=file1.readlines();
    l=len(readlists);
    print(len(dicts))
    for i in range(l):
        texts=readlists[i].strip().split(' ');
        data=[0 for i in range(len(dicts))];  
        l_word=len(texts);
        for text in texts:
            if text in mid_dict:
                mid_dict[text]+=1;
            else:
                mid_dict[text]=1;
        for k,x in mid_dict.items():
            if k in dicts:
               tf=float(x)/l_word;
               idf=math.log(8000/float(t[k]));
               #print(dicts[k])
               data[int(dicts[k])-1]=tf*idf;
        l_word=0;
        fileHandle = codecs.open (filename2, 'a' ,"utf-8")
        for k,x in enumerate(data): 
                fileHandle.write(str(k)+':'+str(x)+' ');
        fileHandle.write('\n');
        fileHandle.close() ;
dicts=select_d(30);
tf_idf_predict_v(dicts,'cut/pword_20433139_df.txt','cut/pword_20433139.txt','predict/predict20433139.txt');
tf_idf_v(dicts,'cut/word_20433139_df.txt','cut/cut_rate_20433139.txt','cut/word_20433139.txt',393);   
    
    
    
    
    

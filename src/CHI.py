#作者 ：赵鑫 高晓旸 at pku
#主要进行开放检验来提取特征值。
import codecs;
def dict_df(filename):
    file=codecs.open(filename, 'r', 'utf-8');
    readlists=file.readlines();
    df=dict();
    for readlist in readlists:
        re=readlist.strip().split(' '); 
        if len(re)==2:
            df[re[0]]=int(re[1]);
        else:
            print(re);
    return df;
def class_num(filename):
    file=codecs.open(filename, 'r', 'utf-8');
    readlists=file.readlines();
    return len(readlists);
#开放检验函数，参数值为还有所有词的df的文件，和只还有该分类的df的文件
def chi(filename,filename1):
    word_df=dict_df(filename);
    class_df=dict_df(filename1);
    i=0;
    print(len(class_df));
    strs=filename1.split('.');
    c_num=class_num(strs[0]+'.txt');
    c_word_sum=len(class_df);
    l=[[0 for col in range(2)] for row in range(c_word_sum)]  
    for k,x in class_df.items():
        a=x;
        c=c_num-a;
        b=word_df[k]-a;
        d=8000-c_num-b;
        z1=a*d-b*c;
        l[i][1]=k;
        l[i][0]=(z1 * z1 * float(8000)) /( (a+c)*(a+b)*(b+d)*(c+d) );
        i+=1;
    l.sort(reverse=True);
    for i in range(c_word_sum):
        fileHandle = codecs.open (strs[0]+'_chi.txt', 'a' ,"utf-8")  
        fileHandle.write ( l[i][1]+' '+str(l[i][0])+'\n') ; 
        fileHandle.close() ;
    print(len(l))
    print(l)
chi('cut/word_20433139_df.txt','class_chi/class1_df.txt');  
chi('cut/word_20433139_df.txt','class_chi/class2_df.txt'); 
chi('cut/word_20433139_df.txt','class_chi/class3_df.txt'); 
chi('cut/word_20433139_df.txt','class_chi/class4_df.txt'); 
chi('cut/word_20433139_df.txt','class_chi/class5_df.txt');       

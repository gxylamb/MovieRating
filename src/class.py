#作者 ：赵鑫 高晓旸 at pku
import codecs;
#将预处理后的影评分成5类
def file_make(filename,str):
    fileHandle = codecs.open (filename, 'a' ,"utf-8")  
    str.strip('\n');
    fileHandle.write ( str) ; 
    fileHandle.close() ;
#将影评分成类，参数为预处理后的影评文件和影评rating文件
def class_fire(filenames,filenames1):
    filename=codecs.open(filenames, 'r','utf-8');
    readlist=filename.readlines();
    filename1=codecs.open(filenames1,'r','utf-8');
    list=filename1.readline().strip().split(' ');
    num=len(list);
    for i in range(num):
        if int(list[i])==1:
            file_make('class_chi/class1.txt',readlist[i]);
        elif int(list[i])==2:
            file_make('class_chi/class2.txt',readlist[i]);
        elif int(list[i])==3:
            file_make('class_chi/class3.txt',readlist[i]);
        elif int(list[i])==4:
            file_make('class_chi/class4.txt',readlist[i]);
        else:
            file_make('class_chi/class5.txt',readlist[i]);
    print(type(list));print(type(readlist[0]));
#求每类的df值
def class_df(filename,df_filename):
    file=codecs.open(filename,'r','utf-8');
    readlists=file.readlines();
    df=dict();t=dict();
    for readlist in readlists:
        texts=readlist.strip().split(' ');
        for text in texts:
            t[text]=1;
        for k,x in t.items():
            if k in df:
                df[k]+=1;
            else:
                df[k]=1;
        t.clear();
    df_file=codecs.open(df_filename,'w','utf-8');
    items=df.items();
    array=[[v[1],v[0]] for v in items];
    array.sort();
    print(type(array));print(array[0][1]);print(type(array[0][0]))
    for key in array:
        df_file.write(key[1]+' '+str(key[0])+'\n');
    df_file.close();
class_fire('cut/word_20433139.txt','cut/cut_rate_20433139.txt');
class_df('class_chi/class1.txt','class_chi/class1_df.txt'); 
class_df('class_chi/class2.txt','class_chi/class2_df.txt');
class_df('class_chi/class3.txt','class_chi/class3_df.txt');
class_df('class_chi/class4.txt','class_chi/class4_df.txt');
class_df('class_chi/class5.txt','class_chi/class5_df.txt'); 

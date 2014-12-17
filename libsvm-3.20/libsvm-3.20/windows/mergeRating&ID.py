# -*- coding: utf-8 -*- 
import glob
import codecs;
files=codecs.open('predict_result.txt','a','utf-8');
for filename in glob.glob(r'C:\Users\gxy\Desktop\MovieRating\libsvm-3.20\libsvm-3.20\windows\*.con'):
    file=codecs.open(filename,'r','utf-8');
    readlists=file.readlines();
    texts=filename.strip().split('\\');
    text=texts[len(texts)-1].split('.')[0];
    for readlist in readlists:
        result="";
        result+=text+'\t'+readlist.strip('\n');
        files.write(result+'\n');
    
    
files.close();

        

  
        

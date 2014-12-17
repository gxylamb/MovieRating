count_word.py进行分词
cut_train('20Movie/20433139.xml')//对训练集进行分词结果写到cut/cut_rate_20433139.txt，cut/cut_word_20433139.txt中
cut_predict('20predict/20433139.xml');//对预测集进行分词结果写到cut/pcut_word_20433139.txt
stop.py进行预处理包括过滤停用词等
结果写到cut/word_20433139.txt(训练集)，cut/pword_20433139.txt（预测集）
tf-idf.py求词的df值,结果写到cut/word_20433139_df.txt，cut/pword_20433139_df.txt
class.py对评论按rating分成5类,结果写到class_chi/class1_df.txt中,当然总共有5个结果文件
CHI.py求取每类的开放检验结果写入到class_chi/class1_df_chi.txt中
get_vector.py用来的到libsvm所需的向量集。结果写到train/train20433139.txt，predict/predict20433139.txt
最后将train20433139.txt提供给libsvm进行建模，然后对predict20433139.txt进行预测并输出结果


from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import MeCab
import re
import os
#上記のコマンドでフォント入れるとGoogleColabだと以下のディレクトリに入ってるはず
FONT_PATH  = "ipaexg.ttf"
#TXT_NAME = "word_cloud"


#テキストを受け取り、名刺のみ抽出してくれる関数get_wordsを定義
def get_word_str(text):
    mecab = MeCab.Tagger()
    parsed = mecab.parse(text)
    lines = parsed.split('\n')#形態素解析したものをリスト化,要素を単語単位に仕分け
    lines = lines[0:-2]#いらない情報をカット
    word_list = []
 
    for line in lines:
        tmp = re.split('\t|,', line)#正規表現？\tと,で区切ってリスト化
 
        # 名詞のみ対象
        if tmp[1] in ["名詞"]:
            # さらに絞り込み
            if tmp[2] in ["一般", "固有名詞"]:
                word_list.append(tmp[0])#文章から固有名詞のみ抽出
                #print(word_list)
    #returnでword_list内の文字を半角空白で結合、一つの文字列を返す
    return " " . join(word_list)

# 文字列取得
def word_cloud(document,filename):
    picture_name = filename +".pdf"
    word_str = get_word_str(document)
    #wc = WordCloud(font_path=FONT_PATH,max_font_size=80).generate(word_str)
    #wc.to_file(picture_name)
    #return os.path.abspath(picture_name)
    return word_str
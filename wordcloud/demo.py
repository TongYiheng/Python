import jieba
import wordcloud

f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="MSYH.TTC", width=1000, height=700, background_color="white",
                        max_words=20, stopwords={"的", "和", "是", "在", "为", "要", "以", "把"})
w.generate(txt)
w.to_file("grwordcloud.png")

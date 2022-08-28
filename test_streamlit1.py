# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 00:44:10 2022

@author: 81708
"""


#起動させるときは、アナコンダプロンプトから下記コマンドを実行する。
#cd c:\00_App\_python
#streamlit run test_streamlit1.py
import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Streamlit Test10')


#テキストを追加する
st.write('Dataframe')

df = pd.DataFrame({
    '一列目': [1, 25, 3, 4],
    '二列目':[11, 12, 15, 14]
})

#Writeでも表示は可能だけど、細かい指定はできない
st.write(df)

#表の大きさを指定する
st.dataframe(df,width=200,height=200)

#各列の最大値を強調(各行の最大値を強調したい場合はaxis=1)
st.dataframe(df.style.highlight_max(axis=1))

#テーブルを表示(静的なテーブルを作る(ただ表だけを表示させたい))
st.table(df)

#バッククオーテーションは[Shift+@]
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#グラフの表示
df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#地図
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon']
)
st.map(df)

from PIL import Image
img = Image.open('_sampleImg.png')
st.image(img,caption='test',use_column_width=True)


#インタラクティブ　ウィジェット(UI)
#チェックボックス
if st.checkbox('Shoe Image'):
    img = Image.open('_sampleImg.png')
    st.image(img,caption='test',use_column_width=True)


#セレクトボックス
select = st.selectbox(label = "教えて", options = list(range(1,10)))
'あなたが選んだ数字は',select,'です。'

#テキストボックス
select = st.text_input("あなたの趣味は？")
'あなたの趣味は',select,'です。'

#スライダー
select = st.slider('あなたの点数は？',0,100,50)
'あなたの点数：',select



#テキストボックス
side = st.sidebar.text_input("[再度]あなたの趣味は？")
'あなたの趣味は',side,'です。'

#スライダー
side = st.sidebar.slider('[再度]あなたの点数は？',0,100,50)
'あなたの点数：',side

#１行に２つの列を作成する
l,r = st.columns(2) 
button = l.button('右に表示')
if(button == True):
    r.write('おしたな！')
else:
    r.write('初期状態')

#expandaで１括りの表示エリアを作って縮めたり表示したりできる
expanda1 = st.expander('問い合せ１')
expanda1.write("内容1")
expanda2 = st.expander('問い合せ２')
expanda2.write("内容2-1")
expanda2.write("内容2-2")
expanda3 = st.expander('問い合せ３')
expanda3.write("内容3-1")
expanda3.write("内容3-2")
expanda3.write("内容3-3")

#プログレスバー
st.write('プログレスバー')
'ｓたーと'

#表示用のテキストを作る
latestt = st.empty()
bar = st.progress(0)

for i in range(100):
    latestt.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

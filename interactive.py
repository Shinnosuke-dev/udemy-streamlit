# ここ見たら使い方わかる
# https://docs.streamlit.io/develop/api-reference

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title("Streamlit入門")

st.write("Interactive Widgets")

# チェックボックス
if st.checkbox('Show Image'): # checkboxはtrue/falseを返す
    img = Image.open("python_image.png")
    st.image(img, caption="python image", use_column_width=True) # 画面幅に画像を伸縮

# セレクトボックス
option_select = st.selectbox(
    'あなたが好きな数字を教えてください。', 
    list(range(1, 11)) # range([start], [stop])を意味し、stopの数値になるまで順に生成（stopmの数値は含まない）
)
'あなたの好きな数字は', option_select , 'ですね？'

# テキスト入力
input_text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', input_text

# スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition
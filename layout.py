# ここ見たら使い方わかる
# https://docs.streamlit.io/develop/api-reference

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title("Streamlit入門")

# # サイドバー表示：st.sidebar
# st.sidebar.write("Interactive Widgets")

# # テキスト入力
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# # スライダー
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション：', condition

# ---

# サイドバー表示：st.sidebar
st.write("Interactive Widgets")

left_column, right_column = st.columns(2) # udemyでは"beta_columns"としていたが、現在はベータ版ではなくなっていたため"columns"でいい

button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
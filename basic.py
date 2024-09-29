# ここ見たら使い方わかる
# https://docs.streamlit.io/develop/api-reference

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title("Streamlit入門")

st.write("DataFrame")

# df = pd.DataFrame({
#     "1列目": [1, 2, 3, 4],
#     "2列目": [10, 20, 30, 40]
# })

# # st.write(df) # dfを表示
# # st.dataframe(df, width=100, height=100) # dfを表示（引数の選択が可能）
# # st.dataframe(df.style.highlight_max(axis=0)) # dfを表示（引数の選択が可能）
# st.table(df.style.highlight_max(axis=0)) #静的な表を表示（上3つは動的）

# 以下markdown
""" 
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd


st.title("Streamlit入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})

# st.write(df) # dfを表示
# st.dataframe(df, width=100, height=100) # dfを表示（引数の選択が可能）
# st.dataframe(df.style.highlight_max(axis=0)) # dfを表示（引数の選択が可能）
st.table(df.style.highlight_max(axis=0)) #静的な表を表示（上3つは動的）
```

"""

df = pd.DataFrame(
    np.random.rand(20, 3), # 20×3の表を作成し、乱数（正規分布）を埋める
    columns=["a", "b", "c"] # 列名
)

st.line_chart(df) # 折れ線グラフ
st.area_chart(df) # 折れ線（中塗り）グラフ
st.bar_chart(df) # 棒グラフ

df_map = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70], # 新宿付近の緯度経度
    columns=["lat", "lon"]
)

st.write("新宿付近の緯度経度")
st.dataframe(df_map)
st.map(df_map) # 地図表示

st.write("Display Image")
img = Image.open("python_image.png")
st.image(img, caption="python image", use_column_width=True) # 画面幅に画像を伸縮

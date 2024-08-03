import streamlit as st
import numpy as np
from PIL import Image

# タイトルを表示
st.title("自然環境汚染")
# st.write('# headline1')
# st.markdown('# headline2')

# ローカルの画像ファイルを読み込む
image = Image.open("./GHS-pictogram/GHS-pictogram-Nature_polluting.png")

# 画像を30x30ピクセルにリサイズ
# resized_image = image.resize((30, 30))
# 画像を表示
# st.image(resized_image, caption="自然環境汚染", use_column_width=False)

# 高解像度のまま画像を表示
# st.image(image, caption="自然環境汚染", width=150)
st.image(image, width=150)

st.subheader('■リスク情報')
st.text('・水生生物に非常に強い毒性')

st.subheader('■安全対策')
st.text('・環境への放出を避けること。')
st.text('・内容物/容器を法令にしたがって廃棄すること。')

st.subheader('■応急措置')
st.text('・火災の場合：適切な消火剤又は水を用いて消火すること。')
st.text('・飲み込んだ場合：ただちに医師に連絡すること。/n口をすすぐこと。')
st.text('・眼に入った場合：水で数分間注意深く洗うこと。/nコンタクトレンズを使用していて容易に外せる場合は外すこと。/nその後も洗浄を続けること。/nただちに医師に連絡すること。')
st.text('・皮膚等に付着した場合：ただちに汚染された衣類を全て脱ぐこと。/n皮膚を多量の水と石けんで洗うこと。/n皮膚刺激が生じた場合、医師の手当てを受けること。')

def create_map_data():
    # マップ表示するランダムデータを作成
    data = {
        'lat': np.random.randn(100) / 100 + 35.68,
        'lon': np.random.randn(100) / 100 + 139.75,
    }
    # データをデータフレーム形式に変換
    map_data = pd.DataFrame(data)

    # マップの表示
    st.map(map_data)

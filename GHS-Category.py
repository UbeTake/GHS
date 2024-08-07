import streamlit as st
import numpy as np
from PIL import Image

import tensorflow as tf
import pandas as pd
from keras.src.utils import load_img

from geopy.geocoders import Nominatim
import streamlit_javascript as st_js

# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras import layers, models
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import os
import time

# Streamlit のキャッシュ機能を使用してモデルをロード
@st.cache_data
def load_model():
    with st.spinner('モデルを読み込んでいます...'):
        time.sleep(15)
        # トレーニング済みモデルの読み込み
        model = tf.keras.models.load_model('./my_model.h5')
    return model

# モデルをロード
model = load_model()
# モデルが正常に読み込まれたことを通知
st.success('モデルが正常に読み込まれました！')

# カメラ
picture = st.camera_input("Take a picture")
# 画像のアップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "png"])

# 画像のクラス名
classes = ['Corrosive',
           'Explosive',
           'Flammable',
           'Gases_under_pressure',
           'Harmful',
           'Hazardous_to_health',
           'Nature_polluting',
           'Oxidizing',
           'Toxic']

result_label = ""
lisk = "---"
safety = "---"
first_aid = "---"

if picture is not None or uploaded_file is not None:
    if uploaded_file is not None:
        # 画像の前処理
        img = load_img(uploaded_file, target_size=(150, 150))
        img = img.resize((150, 150))
        # x = image.img_to_array(img)
        x = np.array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0

    elif picture is not None:
        # 画像の前処理
        img = Image.open(picture)
        img = img.resize((150, 150))
        # x = image.img_to_array(img)
        x = np.array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0
    else:
        st.write("写真を撮るか画像ファイルをアップロードしてください。")

    # with st.spinner('予測中...'):
    #     try:
    #         predictions = model.predict(x)
    #         time.sleep(60)
    #         st.write(predictions)
    #     except Exception as e:
    #         st.error(f"予測中にエラーが発生しました: {e}")

    # 画像の分類
    predictions = model.predict(x)
    predicted_class = np.argmax(predictions[0])
    predicted_label = classes[predicted_class]

    # 結果の表示
    print(f'This image is classified as: {predicted_label}')

    # 条件分岐
    if predicted_label == "Corrosive":
        result_label = "腐食性"
        lisk = "・金属腐食のおそれ\n・重篤な皮膚の薬傷\n・重篤な眼の損傷"
        safety = "・他の容器に移し替えないこと。\n・吸入しないこと。\n・皮膚、眼に付けないこと。\n・取り扱い後は身体をよく洗うこと。\n・保護衣、保護手袋、保護眼鏡を着用すること。"
    elif predicted_label == "Explosive":
        result_label = "爆発物"
        lisk = "・爆発物：大量爆発危険性\n・爆発物：火災、爆風又は飛散危険性\n・熱すると爆発のおそれ"
        safety = "・禁煙。\n・高温、スパーク、火種を近づけないこと。\n・火災の場合は退避すること。\n・内容物/容器を法令にしたがって廃棄すること。"
    elif predicted_label == "Flammable":
        result_label = "可燃性"
        lisk = "・極めて可燃性/引火性の高いガス・エアゾール\n・引火性の高い液体および蒸気\n・可燃性固体\n・熱すると火災のおそれ\n・空気に触れると自然発火\n・水に触れると可燃性/引火性ガスを発生"
        safety = "・禁煙。\n・高温、スパーク、火種を近づけないこと。\n・喚起の良い場所で保管すること。"
    elif predicted_label == "Gases_under_pressure":
        result_label = "圧力下のガス"
        lisk = "・高圧ガス：熱すると爆発のおそれ\n・深冷液化ガス：凍傷又は傷害のおそれ"
        safety = "・日光から遮断し、喚起のよい場所で保管すること。\n・耐寒手袋および保護面または保護眼鏡を着用すること。"
    elif predicted_label == "Harmful":
        result_label = "有害"
        lisk = "・飲み込む、吸入する又は皮膚に接触すると有害\n・強い眼刺激、皮膚刺激\n・アレルギー制皮膚反応を起こすおそれ\n・呼吸器への刺激又は眠気やめまいのおそれ\n・オゾン層を破壊し、健康及び環境に有害"
        safety = "・吸入を避けること。\n・気分が悪い時は医師に連絡すること。\n・保護具を着用すること。\n・回収またはリサイクルに関する情報について製造者または供給者に問い合わせること。"
    elif predicted_label == "Hazardous_to_health":
        result_label = "健康に有害"
        lisk = "・遺伝性疾患のおそれ\n・発がんのおそれ\n・生殖能又は胎児への悪影響のおそれ\n・吸入するとアレルギー、喘息、呼吸困難を起こすおそれ\n・臓器への傷害のおそれ\n・誤えん性肺炎のおそれ"
        safety = "・皮膚に付けないこと。\n・吸入しないこと。\n・防じん・防毒マスク、保護手袋、保護衣、保護眼鏡を着用すること。\n・換気すること。\n・身体に異常が見られる、ばく露の懸念がある場合、医師の診察を受けること。"
    elif predicted_label == "Nature_polluting":
        result_label = "自然環境汚染"
        lisk = "・水生生物に非常に強い毒性"
        safety = "・環境への放出を避けること。\n・内容物/容器を法令にしたがって廃棄すること。"
    elif predicted_label == "Oxidizing":
        result_label = "酸化性"
        lisk = "・発火又は火災助長のおそれ\n・火災又は爆発のおそれ"
        safety = "・禁煙。\n・燃えるものから遠ざけること。\n・隔離して保管すること。"
    elif predicted_label == "Toxic":
        result_label = "有毒"
        lisk = "・飲み込む、吸入する又は皮膚に接触すると生命に危険あるいは有毒"
        safety = "・吸入しないこと。\n・口に入れたり、皮膚に付けないこと。\n・屋外または換気のよいところでのみ使用すること。\n・防じん・防毒マスク、保護衣、保護手袋、保護眼鏡を着用すること。\n・施錠して保管すること。"
    else:
        result_label = ""
        lisk = ""
        safety = ""
        first_aid = ""

    # タイトルの表示
    st.title(result_label)
    st.text(predicted_label)

    # ローカルの画像ファイルを読み込む
    #image = Image.open("./GHS-pictogram/GHS-pictogram-Nature_polluting.png")

    # 画像の表示
    # st.image(picture, width=150)

    # picture または uploaded_file を表示する
    # 両方の画像が存在する可能性がある場合に両方を表示したい場合
    if picture is not None:
        st.image(picture, width=150)
    if uploaded_file is not None:
        st.image(uploaded_file, width=150)
    if picture is None and uploaded_file is None:
        st.write("No image provided")

    first_aid = "[火災の場合]\n・適切な消火剤又は水を用いて消火すること。\n[飲み込んだ場合]\n・ただちに医師に連絡すること。\n・口をすすぐこと。\n[眼に入った場合]\n・水で数分間注意深く洗うこと。\n・コンタクトレンズを使用していて容易に外せる場合は外すこと。\n・その後も洗浄を続けること。\n・ただちに医師に連絡すること。\n[皮膚等に付着した場合]\n・ただちに汚染された衣類を全て脱ぐこと。\n・皮膚を多量の水と石けんで洗うこと。\n・皮膚刺激が生じた場合、医師の手当てを受けること。"

else:
    st.warning("Please take a picture with the camera or upload image file.")

st.subheader('■リスク情報')
st.text(lisk)
st.subheader('■安全対策')
st.text(safety)
st.subheader('■応急措置')
st.text(first_aid)

st.subheader('■GHSマップ')
# 緯度経度データ（10進数）
# pref_list = [
#   {"latitude":35.689521, "longitude":139.691704}, # 東京都
#   {"latitude":35.447753, "longitude":139.642514}, # 神奈川県
#   {"latitude":35.605058, "longitude":140.123308}, # 千葉県
#   {"latitude":35.857428, "longitude":139.648933}, # 埼玉県
# ]
# st.map(pref_list)

# 東京駅を中心に擬似的な位置情報データを生成する
lat, lon = 35.68184, 139.76718
df = pd.DataFrame(
    np.random.randn(30, 2) / [100, 100] + [lat, lon],
    columns=['lat', 'lon']
)
st.map(df)

# ボタンを横並びにレイアウト
col1, col2 = st.columns(2)
# 初期メッセージ
if not st.session_state.get("yes_button") and not st.session_state.get("no_button"):
    st.write("GHSピクトグラムを現在の位置情報にて地図上にマッピング追加しますか？")
# 「はい」ボタン
with col1:
    if st.button("はい", key="yes_button"):
        st.write("マッピング追加しました。")
# 「いいえ」ボタン
with col2:
    if st.button("いいえ", key="no_button"):
        st.write("キャンセルしました。")




# Function to get location data
def get_location():
    try:
        # Get the user's IP address
        ip_address = st.text_input("Enter your IP address:")

        # Use Nominatim to get location information based on the IP address
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(ip_address)

        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        st.error(f"Error retrieving location: {e}")
        return None, None




# タイトル
st.write("現在の位置情報を取得")

# JavaScriptを用いてブラウザの位置情報を取得
geolocation = st_js.st_javascript(
    """
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const { latitude, longitude } = position.coords;
            document.body.innerHTML = JSON.stringify({latitude, longitude});
        }
    )
    """
)

# 結果を表示
if geolocation:
    st.write(f"現在の位置情報:\n緯度: {geolocation['latitude']}\n経度: {geolocation['longitude']}")
    st.map({"lat": [geolocation['latitude']], "lon": [geolocation['longitude']]})
else:
    st.write("位置情報を取得できませんでした。ブラウザの設定を確認してください。")







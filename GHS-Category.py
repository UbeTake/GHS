import streamlit as st
import numpy as np
from PIL import Image

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import os
from tensorflow.keras.preprocessing import image

import matplotlib.image as mpimg

picture = st.camera_input("Take a picture")

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

# トレーニング済みモデルの読み込み
model = tf.keras.models.load_model('./my_model.h5')

# 画像のパス
#img_path = './sample.jpg'
img_path = picture

# 画像の前処理
img = image.load_img(img_path, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = x / 255.0

# 画像の分類
predictions = model.predict(x)
predicted_class = np.argmax(predictions[0])
predicted_label = classes[predicted_class]

# 結果の表示
print(f'This image is classified as: {predicted_label}')

# 条件分岐
result_label = ""
if predicted_label == "Corrosive":
    result_label = "腐食性"
elif predicted_label == "Explosive":
    result_label = "爆発物"
elif predicted_label == "Flammable":
    result_label = "可燃性"
elif predicted_label == "Gases_under_pressure":
    result_label = "圧力下のガス"
elif predicted_label == "Harmful":
    result_label = "有害"
elif predicted_label == "Hazardous_to_health":
    result_label = "健康に有害"
elif predicted_label == "Nature_polluting":
    result_label = "自然環境汚染"
elif predicted_label == "Oxidizing":
    result_label = "酸化性"
elif predicted_label == "Toxic":
    result_label = "有毒"
else:
    result_label = ""

# タイトルを表示
st.title(result_label)
st.text(predicted_label)

# ローカルの画像ファイルを読み込む
#image = Image.open(img_path)
#image = Image.open("./GHS-pictogram/GHS-pictogram-Nature_polluting.png")

# 画像の表示
#st.image(image, width=150)
#st.image(img_path, width=150)
st.image(picture, width=150)

st.subheader('■リスク情報')
st.text('・水生生物に非常に強い毒性')

st.subheader('■安全対策')
st.text('・環境への放出を避けること。')
st.text('・内容物/容器を法令にしたがって廃棄すること。')

st.subheader('■応急措置')
st.text('・火災の場合：適切な消火剤又は水を用いて消火すること。')
st.text('・飲み込んだ場合：ただちに医師に連絡すること。\n口をすすぐこと。')
st.text('・眼に入った場合：水で数分間注意深く洗うこと。\nコンタクトレンズを使用していて容易に外せる場合は外すこと。\nその後も洗浄を続けること。\nただちに医師に連絡すること。')
st.text('・皮膚等に付着した場合：ただちに汚染された衣類を全て脱ぐこと。\n皮膚を多量の水と石けんで洗うこと。\n皮膚刺激が生じた場合、医師の手当てを受けること。')

st.subheader('■マップ')
import streamlit as st

# 緯度経度データ（10進数）
pref_list = [
  {"latitude":35.689521, "longitude":139.691704}, # 東京都
  {"latitude":35.447753, "longitude":139.642514}, # 神奈川県
  {"latitude":35.605058, "longitude":140.123308}, # 千葉県
  {"latitude":35.857428, "longitude":139.648933}, # 埼玉県
]
st.map(pref_list)

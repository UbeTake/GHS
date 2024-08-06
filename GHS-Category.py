import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

# カメラ
picture = st.camera_input("Take a picture")
img_path = "./sample.jpg"

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

if img_path is not None:
    # 画像の読み込みと前処理
    img = Image.open(img_path)
    img = img.resize((150, 150))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # モデルのロード
    model = tf.keras.models.load_model('./my_model.h5')

    # 画像の分類
    # predictions = model.predict(x)
    # predicted_class = np.argmax(predictions[0])
    # predicted_label = classes[predicted_class]
    # st.write(f'Predicted class: {predicted_class}')
    # st.write(f'Predicted label: {predicted_label}')
    # 画像の表示
    st.image(img_path, width=150)
    # 結果の表示
    # print(f'This image is classified as: {predicted_label}')

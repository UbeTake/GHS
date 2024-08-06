import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# カメラ
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

if picture is not None:
    # 画像の読み込みと前処理
    img = Image.open(picture)
    img = img.resize((150, 150))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # predictions = []
    # predicted_class = 7
    # predicted_label = "test"

    # モデルのロード
    model = tf.keras.models.load_model('./my_model.h5')

    # 画像の分類
    predictions = model.predict(x)
    predicted_class = np.argmax(predictions[0])
    predicted_label = classes[predicted_class]

    st.write("分類結果:", predictions)
    st.write(f'Predicted class: {predicted_class}')
    st.write(f'Predicted label: {predicted_label}')

    # 画像の表示
    st.image(picture, width=150)
    # 結果の表示
    print(f'This image is classified as: {predicted_label}')

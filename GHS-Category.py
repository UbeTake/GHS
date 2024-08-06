import streamlit as st
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img

# カメラ
picture = st.camera_input("Take a picture")
img_path = "./sample.jpg"
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

if uploaded_file is not None:
    image = load_img(uploaded_file, target_size=(224, 224))
    st.image(image, caption='アップロードされた画像。', use_column_width=True)

    # 画像の読み込みと前処理
    img = Image.open(img_path)
    img = img.resize((150, 150))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # モデルのロード
    model = tf.keras.models.load_model('./my_model.h5')

    # 画像の分類
    st.write("分類処理中...")
    predictions = model.predict(x)
    predicted_class = np.argmax(predictions[0])
    predicted_label = classes[predicted_class]
    st.write(f'Predicted class: {predicted_class}')
    st.write(f'Predicted label: {predicted_label}')
    st.write("分類結果:", predictions)
    # 画像の表示
    st.image(img_path, width=150)
    # 結果の表示
    print(f'This image is classified as: {predicted_label}')

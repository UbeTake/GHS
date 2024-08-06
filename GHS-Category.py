import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
# from tensorflow.keras.preprocessing.image import load_img

# カメラ
picture = st.camera_input("Take a picture")
# img_path = "./sample.jpg"
# 画像のアップロード
# uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "png"])

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
    # image = load_img(uploaded_file, target_size=(224, 224))
    # st.image(image, caption='アップロードされた画像。', use_column_width=True)

    # 画像の読み込みと前処理
    img = Image.open(picture)
    img = img.resize((150, 150))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    predictions = []
    predicted_class = 7
    predicted_label = "test"
    try:
        # モデルのロード
        model = tf.keras.models.load_model('./my_model.h5')

        # 画像の分類
        predictions = model.predict(x)
        predicted_class = np.argmax(predictions[0])
        predicted_label = classes[predicted_class]
    except BrokenPipeError:
        print("BrokenPipeError: パイプが壊れちゃった。")

    st.write("分類結果:", predictions)
    st.write(f'Predicted class: {predicted_class}')
    st.write(f'Predicted label: {predicted_label}')

    # 画像の表示
    st.image(picture, width=150)
    # 結果の表示
    print(f'This image is classified as: {predicted_label}')

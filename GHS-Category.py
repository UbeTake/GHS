import streamlit as st
import numpy as np
from PIL import Image



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

# トレーニング済みモデルを保存したファイル名
model_filename = './my_model.h5'
# モデルの読み込み
model = tf.keras.models.load_model(model_filename)

# 画像のパス
# img_path = '/content/drive/MyDrive/Colab Notebooks/GHS/sample.jpg'
img_path = picture

# 必要なライブラリをインポートします
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 画像を表示する関数を定義します
def show(image_path):
  img = mpimg.imread(image_path)
  plt.imshow(img)
  plt.axis('off')  # 軸を非表示にする
  plt.show()

# 画像を表示します
show(img_path)

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

import keras.optimizers
from keras.models import load_model
import cv2

model = load_model('/home/greco/PycharmProjects/MemeDownloadScript/Predicting/my_meme_model.h5')

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

img = cv2.imread('/home/greco/PycharmProjects/MemeDownloadScript/Predicting/test20200214-223043-535063.png')

classes = model.predict_classes(img)

print(classes)


# -*- coding: utf-8 -*-
"""First_Deeplearning_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujWyGCOEzdEU0nqaNmEd5pcUNUWGlDPx
"""

import keras
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

keras.backend.backend()

"""## **Collect data**"""

fm = keras.datasets.fashion_mnist
(X_train, y_train), (X_test, y_test) = fm.load_data()

X_train.shape

X_test.shape

X_train[0]

"""##**Normalize training data before training the neural net**"""

X_train = X_train.reshape(60000,28,28,1)

X_train = X_train/255

X_test = X_test.reshape(10000,28,28,1)

X_test = X_test/255

"""##**Now bulid Sequential Model and add Layers into it**"""

from keras.models import Sequential
from keras.layers import Flatten, Dense ,Activation,Dropout, Conv2D,MaxPooling2D

model = Sequential() # here we choose sequencial model,there are other models also availble in documentation
model.add(Conv2D(32, (3,3), activation='relu',input_shape =(28,28,1)))
model.add(MaxPooling2D((2,2))) 
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(128,(3,3),activation='relu'))
model.add(Dropout(0.4))
model.add(Flatten()) # Flatten is converted 2D array in to 1D array
model.add(Dense(128,activation = 'relu')) # hidden layer with 100 neurons(It is base on try and error method to aassume neurons)
model.add(Dropout(0.3))
model.add(Dense(10,activation = 'softmax'))#activation Function is Softmax(Softmax is doing distributing set of number into just probabilities of your available classes )



model.summary()

"""## ***Compilation of model***"""

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
             metrics = ['accuracy'])

"""## **Fit the data in to model**"""

history = model.fit(X_train, y_train,
          batch_size=256,
          epochs=50,
          verbose=1,
          validation_data=(X_train, y_train))
score = model.evaluate(X_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])

"""## **Above shows accuracy score of 82.76%.The first parameter is loss**"""

plt.matshow(X_test[1])

y_predict = model.predict(X_test)

np.argmax(y_predict[0])

class_labels = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]

class_labels[np.argmax(y_predict[0])]

"""# Ploting training and validation accuracy as well as loss."""

accuracy = history.history['acc']
val_accuracy = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(accuracy))

plt.plot(epochs,accuracy,'bo',label='Training accuracy')
plt.plot(epochs,val_accuracy,'b',label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs,loss,'bo',label='Training loss')
plt.plot(epochs,val_loss,'b',label= 'Validation loss')
plt.title('Training and validation loss')                            
plt.legend()
plt.show()
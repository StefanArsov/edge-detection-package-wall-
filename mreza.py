# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:56:30 2019

@author: Stefan
"""

#import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten,Activation
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam


model = Sequential()

model.add(Conv2D(16, 3, 3, border_mode='same', input_shape=(5,5,3), activation='relu'))
model.add(Conv2D(16, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(1, 1)))

model.add(Conv2D(32, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(32, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(1, 1)))

model.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())

from keras.optimizers import RMSprop

model.add(Dense(2))
model.add(Activation('sigmoid'))
#loss='binary_crossentropy',
           # optimizer=RMSprop(lr=0.0001),
           #loss=categorical_crossentropy,
model.compile(loss='binary_crossentropy',
              optimizer=Adam(),
            metrics=['accuracy'])
history=model.fit(x1,y1,batch_size=500,epochs=100, validation_data=(xp_val,yp_val),shuffle=True, verbose=True)
h=model.predict(glavno)
h1=h.reshape(len(X1_test),140,172,2)
mse=0
n=0
#from sklearn.metrics import mean_squared_error
#mean_error=mean_squared_error(y_true, h1)


#for k in range(len(X_test)):
   #for i in range(140):
       #for j in range(172):
           #mse=mse+(y_true[k,i,j,0]-h1[k,i,j,0])**2+(y_true[k,i,j,1]-h1[k,i,j,1])**2
           #n=n+1

#mse=mse/n
import matplotlib.pyplot as plt
#plt.imshow(h1[1])
#model.predict()

# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
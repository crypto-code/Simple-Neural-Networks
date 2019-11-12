import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from keras.models import Sequential
from keras.layers import Dense, Dropout
from ann_visualizer.visualize import ann_viz
import numpy as np

X=np.array(([0,0,0],
            [0,0,1],
            [0,1,0],
            [0,1,1],
            [1,0,0],
            [1,0,1],
            [1,1,0],
            [1,1,1],), dtype=float)
y=np.array(([0],
            [1],
            [1],
            [0],
            [1],
            [0],
            [0],
            [1]), dtype=float)


#Model
model = Sequential()
model.add(Dense(64, input_dim=3, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, batch_size=1)
_, accuracy = model.evaluate(X, y)
print('\n\nAccuracy: %.2f' % (accuracy*100))

print('\n\n')

predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(8):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

ann_viz(model, title="Multi-Layer Preceptron", view=True)

from keras.models import Sequential
from keras.layers import Dense
from numpy import loadtxt

class NeuralNetworkService:

     def __init__(self, learning_file):
        dataset = loadtxt(learning_file, delimiter=',')
        # split into input (X) and output (y) variables
        # pdb.set_trace()
        X = dataset[:,0:115]
        y = dataset[:,115]
        
        # define the keras model
        model = Sequential()
        model.add(Dense(12, input_dim=115, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        
        # compile the keras model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        # fit the keras model on the dataset
        model.fit(X, y, epochs=150, batch_size=10)

        # evaluate the keras model
        _, accuracy = model.evaluate(X, y)
        print('Accuracy: %.2f' % (accuracy*100))


        dataset2 = loadtxt('file_to_evaluate.csv', delimiter=',')
        csv_to_evaluate = dataset2[:,0:115]
        # make class predictions with the model
        predictions = model.predict_classes(csv_to_evaluate)
        # summarize the first 5 cases
        for i in range(5):
           print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

NeuralNetworkService('zero_crossing_rate_info.csv')
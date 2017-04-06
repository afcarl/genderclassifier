from sklearn import tree,svm,linear_model
from sklearn.metrics import accuracy_score

#Height Weight Shoe size
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[179,70,40],[155,55,37],[171,75,42],[181,45,43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']



#defining models
clf = tree.DecisionTreeClassifier()
clf2 = svm.SVC()
clf3 = linear_model.SGDClassifier()
clf4 = linear_model.Perceptron()


#traning
clf = clf.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)
clf4 = clf4.fit(X,Y)
# inp = []
# height = input("Enter Height: ")
# inp.append(height)
# weight = input("Enter weight: ")
# inp.append(weight)
# shoeSize = input("Enter Shoe Size: ")

# inp.append(shoeSize)

#predict
prediction = clf.predict([180,60,44])
prediction2 = clf2.predict([180,60,44])
prediction3 = clf3.predict([180,60,44])
prediction4 = clf4.predict([180,60,44])

#To remove this error :-> ValueError: Found input variables with inconsistent numbers of samples: [11, 1]
xprediction = clf.predict(X)
xprediction2 = clf2.predict(X)
xprediction3 = clf3.predict(X)
xprediction4 = clf4.predict(X)

#calc accuracy
acc = accuracy_score(Y,xprediction)
acc2 = accuracy_score(Y,xprediction2)
acc3 = accuracy_score(Y,xprediction3)
acc4 = accuracy_score(Y,xprediction4)

print("From DTree")
print(prediction,acc)

print("from svm")
print(prediction2,acc2)

print('from SGDClassifier')
print(prediction3,acc3)

print('from perceptron')
print(prediction4,acc4)
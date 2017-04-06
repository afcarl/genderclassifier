from sklearn import tree

#Height Weight Shoe size
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[179,70,40],[155,55,37],[171,75,42],[181,45,43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']


#defining models
clf = tree.DecisionTreeClassifier()



#traning
clf = clf.fit(X,Y)

# inp = []
# height = input("Enter Height: ")
# inp.append(height)
# weight = input("Enter weight: ")
# inp.append(weight)
# shoeSize = input("Enter Shoe Size: ")

# inp.append(shoeSize)


prediction = clf.predict([180,60,44])

print("From DTree")
print(prediction)


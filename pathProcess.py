import pickle
Goal = 4


#for i in range(0,12):
file = open('./data/PathPoints/PathPointsGoal=' + str(Goal) + '.pkl', 'rb')
PathPoints_T = pickle.load(file)
file.close()
print(len(PathPoints_T))
PathPoints = []
CurX = int(PathPoints_T[0][0])
CurY = int(PathPoints_T[0][1])
for p in PathPoints_T:
    x = int(p[0])
    y = int(p[1])
    if x!=CurX or y!=CurY:
        PathPoints.append(p)
        CurX = x
        CurY = y
#print(PathPoints)
print(len(PathPoints))

file = open('./data/PathPointsFinal/PathPointsFinalGoal=' + str(Goal) + '.pkl', 'wb')  #save
pickle.dump(PathPoints, file)
file.close()

# Goal +=1
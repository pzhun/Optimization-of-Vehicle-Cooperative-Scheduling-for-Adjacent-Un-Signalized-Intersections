import pickle

goal = 4
file = open('./data/PathPointsFinal/PathPointsFinalGoal=' + str(goal) + '.pkl', 'rb')
PathPoints_T = pickle.load(file)
file.close()

PathPoints = []
CurX = int(PathPoints_T[0][0])
CurY = int(PathPoints_T[0][1])
for p in PathPoints_T:
        x = int(p[0])
        y = int(p[1])
        PathPoints.append([910-x,910-y,0])

#print(PathPoints)
print(len(PathPoints))

file = open('./data/PathPointsFinalGoal=' + '1' + '.pkl', 'wb')  #save
pickle.dump(PathPoints, file)
file.close()

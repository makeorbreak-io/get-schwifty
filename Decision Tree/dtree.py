from sklearn import tree
import numpy as np
import pickle

file = open('verificar.csv')
names = open('target_names1.csv')

target_list=[]
data_list=[]

check = 0
for line in file:
	if check > 0:
		line = line.strip()
		data = line.split(';')[2:52]
		nova_data =[]
		nova_data.extend(list(map(int,data[:])))
		print(data)


		target = line.split(';')[0:2]
		data_list.append(nova_data)
		target_list.append(target)
	else:
		check +=1

target_names=[]
for line in names:
	line = line.strip()
	line = line.split(';')[:]
	target_names.append(line)

file.close()
names.close()

data_list=data_list[1:]
target_list=target_list[1:]
target_names=target_names[1:]

print(target_list)

nova_target_list=[]
for target in target_list:
	target = target[0] + ' ' + target[1]
	nova_target_list.append(target)

nova_target_names=[]
for target in target_names:
	target = target[0] + ' ' + target[1]
	nova_target_names.append(target)

for i in list(range(0,len(nova_target_list))):
	if nova_target_list[i] in nova_target_names:
		nova_target_list[i] = nova_target_names.index(nova_target_list[i])



data_list_dt=np.array(data_list)
target_list_dt=np.array(nova_target_list)



arrayTrees=[]
numTrees=10

for index in range(0,numTrees):
	print("Tree index:", index)
	clf = tree.DecisionTreeClassifier(criterion = 'entropy')
	clf = clf.fit(data_list_dt, target_list_dt)
	arrayTrees.append(clf)


pickle.dump(arrayTrees, open('finalized_model.sav', 'wb'))


#ade = 'decisiontree.sav'
#pickle.dump(clf, open(ade, 'wb'))

def convertList(index, size):
	temp=[2]*size
	for i in range(1,size+1):
		if str(i) in loadedData[5]:
			temp[i-1]=1;
	return temp

def unwrap(loadedData):
	output=[]
	output.extend(list(map(int,loadedData[0:5])))
	output.extend(convertList(5,12))
	output.extend(convertList(6,8))
	output.extend(convertList(7,5))
	output.append(int(loadedData[8]))
	output.extend(convertList(9,11))
	output.append(int(loadedData[10]))
	output.append(int(loadedData[11]))
	output.extend(convertList(12,5))
	output.append(int(loadedData[13]))
	return output
##


filename='answersNY.sav'
loadedData= pickle.load(open(filename,'rb'))



out_ex=unwrap(loadedData)
out_ex = np.array(out_ex)
print(out_ex)
result = int(clf.predict([out_ex]))

print(nova_target_names[result])


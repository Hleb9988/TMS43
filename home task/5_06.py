# Создать список учеников
# подобной структуры.
# Определить средний балл
# оценок по всем предметам,
# и вывести сведения о
# студентах, средний балл
# которых больше 4. 


pupils = [
 {
 'firstname': 'Masha',
 'Group': 42,
 'physics': 3,
 'informatics': 10,
 'history': 5,
 'math': 1,
 },
  {
 'firstname': 'Pasha',
 'Group': 42,
 'physics': 7,
 'informatics': 3,
 'history': 2,
 },
  {
 'firstname': 'Misha',
 'Group': 42,
 'physics': 4,
 'informatics': 1,
 'history': 1,
 'phisic': 5,
 },
]

for i in range(len(pupils)):
	num=0
	sum=0
	for k,v in pupils[i].items():
		if k != 'firstname' and k != 'Group':
			sum+=pupils[i][k]
			num+=1
	pupils[i]['sr']=sum/num
	if pupils[i]['sr'] > 4:
		print(pupils[i]['firstname'])

print(pupils)
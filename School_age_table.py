# else if 
age = input('請輸入年齡:')
age = int(age)
if age < 6:
	print('幼稚園')
elif age >= 6 and age <= 10:
	print('國小')
elif age >= 11 and age <= 14:
	print('國中')
elif age >= 15 and age <= 17:
	print('高中')
elif age >= 18 and age <= 21:
	print('大學')
else:
	print('社會人士')
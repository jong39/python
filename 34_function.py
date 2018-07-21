def spam(eggs):
	eggs.append(1)  # 객체로 사용 될 경우 기존 argument(ham에) 추가가 되는 것이다. 	
	eggs = [2, 3] 
	print(eggs)  # 이것은 새로운 list(객체)를 만드는 것이기 때문에 ham과는 별도 이다.

ham = [0]
spam(ham)
print(ham)




def test(t):
	t = 20
	print(t)

x = 10
test(x)
print(x)
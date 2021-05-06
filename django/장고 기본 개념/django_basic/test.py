# class Smartphone:
#     """
#     Smartphone Class
#     """
#     # 클래스 변수
#     smartphone_count = 0
    
#     def __init__(self, brand, infomations):
#         self._brand = brand
#         self._infomations = infomations
#         Smartphone.smartphone_count += 1

#     def __str__(self):
#         return f'str : {self._brand} - {self._infomations}'

#     def __repr__(self):
#         return f'repr : {self._brand} - {self._infomations}'

#     def infomation(self):
#         print(f'Current Id : {id(self)}')
#         # print(f'Smartphone Detail Info : {self._brand} {self._infomations.get('price'))}'

#     def __del__(self):
#         Smartphone.smartphone_count -= 1
    
# Smartphone1 = Smartphone('Iphone', {'color' : 'White', 'price': 10000})
# Smartphone2 = Smartphone('Galaxy', {'color' : 'Black', 'price': 8000})
	
	
# print('1 : ',Smartphone.__dict__)
# print('2 : ',Smartphone1.__dict__)
# print('3 : ',Smartphone2.__dict__)
# print('4 : ',dir(Smartphone1))
	
# print(Smartphone1.smartphone_count)
# print(Smartphone.smartphone_count)
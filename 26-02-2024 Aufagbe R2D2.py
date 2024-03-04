young=int(10)
adult=int(10)
old=int(10)
circle=1
print('young', young, 'adult', adult ,'old', old)

while circle == 1 :
    new_young=int( (adult*4) + (old*2))
    
    new_adult=int(young / 2)
    
    old= int(adult / 3)
    young =new_young
    adult =new_adult
    print('young', young, 'adult', adult ,'old', old)
    print('do you want to continue?(press 1)')
    circle = int(input())
    
    
print('fina score : young', young, 'adult', adult,'old', old)

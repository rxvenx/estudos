#and
#or
#not

#tabela verdade

#   A  |   B  |   A and B   |   A or B
# false| false|    false    |   false
# false| true |    false    |   true
# true | false|    false    |   true
# true | true |    true     |   true

height = int(input('what is your height? (in centimeters)'))
credits = int(input('how many credits do you have?'))
with_taller_person = str(input('are you with a taller person than you?'))

if height >= 137 and credits >= 10:
    print('enjoy the ride!') 

elif height < 137: 
   
    if height < 100 or with_taller_person=='no' :
        print('you\'re not ready for this ride yet.')
    else:
        if height >= 100 and with_taller_person=='yes' :
            print('enjoy the ride!')
    
        
elif credits < 10:
    print('you do not have enough credits to ride')
    

else:
    print('invalid data')

    
#drink up, me hearties, yo-ho
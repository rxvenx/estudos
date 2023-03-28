# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin
print('Sorting Hat - simple version')
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


question_one = int(input('Q1) Do you like Dawn or Dusk? \n   1) Dawn \n   2) Dusk \n'))

if question_one == 1 :
    gryffindor = gryffindor +1 #gryffindor +=1 dá no mesmo
    ravenclaw = ravenclaw +1

elif question_one == 2 :
    hufflepuff = hufflepuff +1
    slytherin = slytherin +1
    
else:
    print('invalid input.')


question_two = int(input('Q2) When I’m dead, I want people to remember me as: \n   1)The Good \n   2)The Great \n   3)The Wise \n   4)The Bold \n'))

if question_two == 1 :
    hufflepuff = hufflepuff +2

elif question_two == 2 :
    slytherin = slytherin +2

elif question_two == 3 :
    ravenclaw = ravenclaw +2

elif question_two == 4 :
    gryffindor = gryffindor +2 #gryffindor +=2 dá no mesmo

else:
    print('invalid input.')

question_three = int(input('Q3) Which kind of instrument most pleases your ear? \n   1)The violin \n   2)The trumpet \n   3)The piano \n   4)The drum \n'))
if question_three == 1 :
    slytherin = slytherin +4

elif question_three == 2 :
    hufflepuff = hufflepuff +4

elif question_three == 3 :
    ravenclaw = ravenclaw +4

elif question_three == 4 :
    gryffindor = gryffindor +4 #gryffindor +=4 dá no mesmo

else:
    print('invalid input.')

print('Your final score:')
print(gryffindor, 'points to gryffindor')
print(slytherin, 'points to slytherin') 
print(ravenclaw, 'points to ravenclaw') 
print(hufflepuff, 'points to hufflepuff') 



# question_four = int(input('Q4) Do you like Dawn or Dusk?'))
# question_five = int(input('Q5) Do you like Dawn or Dusk?'))
# question_six = int(input('Q6) Do you like Dawn or Dusk?'))
# question_seven = int(input('Q7) Do you like Dawn or Dusk?'))
# question_eight = int(input('Q8) Do you like Dawn or Dusk?'))
# question_nine = int(input('Q9) Do you like Dawn or Dusk?'))
# question_ten =  int(input('Q10) Do you like Dawn or Dusk?'))


#1 yuan - 0.15 usd
#1 yen - 0,0076 usd
#1 won - 0,00077 usd


yuan = float(input("What do you have left in yuan? "))
yen = float(input("What do you have left in yen? "))
won = float(input("What do you have left in won? "))

yuan_usd = yuan*0.15
yen_usd = yen*0.0076
won_usd = won*0.00077

convert = yuan_usd + yen_usd + won_usd

print(convert)

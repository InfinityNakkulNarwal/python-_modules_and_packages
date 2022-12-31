# This script will generate random strong passwords.

import random
alp_cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alp_sml = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1','2', '3','4', '5', '6', '7', '8', '9', '0']
symb = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','*','/','?','>','<',':','"','{','}','[',']','\'',';','.','/','`','~']
gen_pwd = random.choice(alp_cap) +  random.choice(num) + random.choice(symb) + random.choice(alp_sml) + random.choice(num) + random.choice(symb) + random.choice(alp_cap) + random.choice(alp_cap) + random.choice(alp_sml) + random.choice(alp_sml) + random.choice(symb) + random.choice(num) + random.choice(symb) + random.choice(alp_sml) + random.choice(num) + random.choice(symb) + random.choice(alp_cap) + random.choice(alp_cap) + random.choice(alp_sml) + random.choice(alp_sml) + random.choice(symb) + random.choice(num)
print(gen_pwd)

import random


def get_random():
    nambers = list(range(3, 21))
    random_ = random.choice(nambers)
    return random_


def get_password(n):
    passbook = {}
    passbook.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534})
    passbook.update({8: 13172635, 9: 1218273645, 10: 141923283746})
    passbook.update({11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968})
    passbook.update({15: 1214114232133124115106978, 16: 1317115262143531341251161079})
    passbook.update({17: 11621531441351261171089, 18: 12151811724272163631545414513612711810})
    passbook.update({19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911})
    passbook.get(n)
    return passbook

n = get_random()
print("Случайная цифра:", n)

namb = list(range(1, n))
namb2 = list(range(1, n))
pair = []
result = ""
for i in namb:
    for j in namb2:
        if i >= j:
            continue
        else:
            multiple = n % (i + j)
            if multiple == 0:
               pair.append([i, j])
               result = result + str(i) + str(j)
print("Пары чисел:", pair)
print("Введите пароль:",result, " во второе окно" )





def open_account():
    print("새로운 계좌 생성")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money, commission):
    return balance ,money-commission, commission


balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
balance, money ,commission= withdraw_night(24000,4000,1000)
print("잔액은 {0}이고 출금액은 {1}이고, 수수료는 {2}입니다.".format(balance,money-commission,commission))
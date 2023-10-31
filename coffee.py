coins = [50, 20, 10, 5]
amount_due = 50
while amount_due > 0:
        print(f"Нужная сумма: {amount_due}")
        coin = int(input("Вставьте монету: "))
        if coin in coins:
            amount_due -= coin

change_owed = -amount_due
print(f"Ваша сдача: {change_owed}")
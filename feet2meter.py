def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
        v = v.replace("ft", "")  # удаление символов "ft"
        v = float(v)  # преобразование строки в число с плавающей запятой
        v = v * 0.3048  # перевод футов в метры
        return v

main()
def find_number_with_max_digit_sum():
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    while True:
        max_sum = 0
        number_with_max_sum = None

        while True:
            try:
                num = int(input("Введите целое число (для завершения введите 0): "))
                if num == 0:
                    break

                current_sum = sum_of_digits(num)
                if current_sum > max_sum:
                    max_sum = current_sum
                    number_with_max_sum = num
            except ValueError:
                print("Ошибка: введено не число. Пожалуйста, введите целое число.")

        if number_with_max_sum is not None:
            print(f"Число с максимальной суммой цифр: {number_with_max_sum}")
        else:
            print("Вы не ввели ни одного числа.")

        choice = input("Хотите начать заново? (да/нет): ")
        if choice.lower() != 'да':
            break

find_number_with_max_digit_sum()

# Костя подключен к мобильному оператору «Мобайл». Абонентская плата Кости составляет A рублей в месяц. 
# За эту стоимость Костя получает B мегабайт интернет-трафика. 
# Если Костя выйдет за лимит трафика, то каждый следующий мегабайт будет стоить ему C рублей.
# Костя планирует потратить D мегабайт интернет-трафика в следующий месяц. Помогите ему сосчитать, во сколько рублей ему обойдется интернет.

# input = input()
# tariff = list(map(int, input.split()))

# if tariff[3] < tariff[1]:
#     print(tariff[0])
# else:
#     diff = tariff[3] - tariff[1]
#     print(tariff[0] + (diff * tariff[2]))


# tariff = list(map(int, input().split()))

# if len(tariff) == 4:
#     tariff_code, initial_cost, cost_per_unit, units_consumed = tariff
    
#     if units_consumed < initial_cost:
#         final_cost = tariff_code
#     else:
#         final_cost = tariff_code + ((units_consumed - initial_cost) * cost_per_unit)

#     print(final_cost)
# else:
#     print("Недостаточно элементов в списке тарифов.")


try:
    tariff = list(map(int, input().split()))

    if len(tariff) == 4:
        tariff_code, initial_cost, cost_per_unit, units_consumed = tariff

        if units_consumed < initial_cost:
            final_cost = tariff_code
        else:
            final_cost = tariff_code + ((units_consumed - initial_cost) * cost_per_unit)

        print(final_cost)
    else:
        print("Неверное количество элементов в списке тарифов.")

except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целочисленные значения тарифов.")

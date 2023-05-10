import math
import random
import src.interface as interface
import src.connection_number_curr as connect
import src.rates_data as rates_data
import src.print_graph as print_graph
import src.graph as graph


# take the logarithms of the data in rates
def logarithm_convertor(rates):
    log_rates = [[-math.log(element) for element in row] for row in rates]
    return log_rates


# count money for one cycle
def earn_money(money, cycle, rates, chosen_currency):
    start = connect.currencies_to_numb[chosen_currency]
    end = cycle[0]
    for i in range(1, len(cycle) + 1):
        money *= rates[start][end]
        start = end
        if i < len(cycle):
            end = cycle[i]
    money *= rates[start][connect.currencies_to_numb[chosen_currency]]
    return money


def get_solution():
    print(interface.enter_curr)
    chosen_currency = input().upper()

    if chosen_currency.isdigit():
        chosen_currency = connect.numb_to_currencies[int(chosen_currency) - 1]

    print(interface.enter_amount, end=' ')
    money = int(input())

    count_v = len(connect.numb_to_currencies)
    random_time_stop = random.randrange(1, len(rates_data.arr_rates))

    for i in range(random_time_stop):
        rates = rates_data.arr_rates[i]
        log_rates = logarithm_convertor(rates)

        my_graph = graph.Graph(count_v)
        my_graph.fill_graph(log_rates)

        cycle = list(my_graph.find_negative_cycle(connect.currencies_to_numb[chosen_currency]))

        if my_graph.has_negative_cycle(connect.currencies_to_numb[chosen_currency]):
            print_graph.print_graf(rates, cycle, chosen_currency)
            money = earn_money(money, cycle, rates, chosen_currency)
        print(interface.next_cycle)
        answer = input()
        answer = answer.upper()
        if answer == 'NO':
            break
        elif answer == 'YES':
            continue
        else:
            print(interface.next_cycle)

    interface.print_balance(money, chosen_currency)

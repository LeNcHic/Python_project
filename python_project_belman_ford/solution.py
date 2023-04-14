import math
import random
import interface
import connection_number_curr as connect
import rates_data
import print_graph
import class_graph


# take the logarithms of the data in rates
def logarithm_convertor(rates):
    log_rates = [[math.log(element) for element in row] for row in rates]
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
    interface.print_choose_curr()
    chosen_currency = input().upper()

    if chosen_currency.isdigit():
        chosen_currency = connect.numb_to_currencies[int(chosen_currency) - 1]

    interface.print_enter_money()
    money = int(input())

    count_v = len(connect.numb_to_currencies)
    random_time_stop = random.randrange(1, len(rates_data.arr_rates))

    for i in range(random_time_stop):
        rates = rates_data.arr_rates[i]
        log_rates = logarithm_convertor(rates)

        graph = class_graph.Graph(count_v)
        graph.fill_graph(log_rates)

        cycle = list(graph.negative_cycle(connect.currencies_to_numb[chosen_currency]))

        if graph.is_negative_cycle(connect.currencies_to_numb[chosen_currency]):
            print_graph.print_graf(rates, cycle, chosen_currency)
            money = earn_money(money, cycle, rates, chosen_currency)
    interface.print_balance(money, chosen_currency)

edges = [
        ("GBP", "EUR"),
        ("GBP", "USD"),
        ("GBP", "RUB"),
        ("GBP", "BYN"),
        ("GBP", "CNY"),
        ("EUR", "USD"),
        ("EUR", "RUB"),
        ("EUR", "BYN"),
        ("EUR", "CNY"),
        ("USD", "RUB"),
        ("USD", "BYN"),
        ("USD", "CNY"),
        ("RUB", "BYN"),
        ("RUB", "CNY"),
        ("BYN", "CNY"),
    ]


def get_edge_labels(rates, currencies_to_numb):
    edge_labels = {
            ("GBP", "EUR"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["EUR"]]),
            ("GBP", "USD"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["USD"]]),
            ("GBP", "RUB"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["RUB"]]),
            ("GBP", "BYN"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["BYN"]]),
            ("GBP", "CNY"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["CNY"]]),
            ("EUR", "USD"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["USD"]]),
            ("EUR", "RUB"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["RUB"]]),
            ("EUR", "BYN"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["BYN"]]),
            ("EUR", "CNY"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["CNY"]]),
            ("USD", "RUB"): str(rates[currencies_to_numb["USD"]][currencies_to_numb["RUB"]]),
            ("USD", "BYN"): str(rates[currencies_to_numb["USD"]][currencies_to_numb["BYN"]]),
            ("USD", "CNY"): str(rates[currencies_to_numb["USD"]][currencies_to_numb["CNY"]]),
            ("RUB", "BYN"): str(rates[currencies_to_numb["RUB"]][currencies_to_numb["BYN"]]),
            ("RUB", "CNY"): str(rates[currencies_to_numb["RUB"]][currencies_to_numb["CNY"]]),
            ("BYN", "CNY"): str(rates[currencies_to_numb["BYN"]][currencies_to_numb["CNY"]]),
        }
    return edge_labels
import tabulate


def format_out(table, headers=None):
    return tabulate.tabulate(table, headers=headers, tablefmt="pretty")

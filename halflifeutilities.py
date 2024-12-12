from typing import List, Dict

import math

import radioactivenuclides as ran


def _sci_not_to_num(significand, exponent):

    return significand * 10 ** exponent


def printnuclides() -> None:

    """
    Print details of the the contents of
    radioactivenuclides as a table
    """

    print("-" * 71)

    print("| Key           ", end="")
    print("| Nuclide symbol ", end="")
    print("| Nuclide name   ", end="")
    print("| Half-life (years) |")

    print("-" * 71)

    for key, value in ran.radioactive_nuclides.items():

        print(f"| {key.ljust(14, ' ')}|", end="")

        print(f" {(str(value['atomicmass']) + value['elementsymbol']).ljust(15, ' ')}|", end="")

        print(f" {(value['element'] + ' ' + str(value['atomicmass'])).ljust(15, ' ')}|", end="")

        print(f" {(str(value['significand']) + '×10^' +str(value['exponent']) ).ljust(18, ' ')}|")

    print("-" * 71)


def decay_list(nuclidekey: str, halflives: int, startingvalue: int = 1048576) -> List:

    """
    For the specified nuclide creates a list of
    amounts remaining after each half-life has elapsed
    """

    dl = []

    nuclide = ran.radioactive_nuclides[nuclidekey]

    halflife = _sci_not_to_num(nuclide['significand'], nuclide['exponent'])

    for i in range(0, halflives + 1):

        remaining = 0.5**i

        dl.append({
                    "years_elapsed": halflife * i,
                    "remaining_decimal": remaining,
                    "remaining_amount": startingvalue * remaining
                  })

    return dl


def decay_table(nuclidekey: str, halflives: int, startingvalue: int = 1048576) -> None:

    """
    For specified nuclide prints table of half lives and years,
    and amounts remaining as decimals and amounts.
    """

    dl = decay_list(nuclidekey, halflives, startingvalue)

    tablewidth = 75

    nuclide = ran.radioactive_nuclides[nuclidekey]

    halflife = _sci_not_to_num(nuclide['significand'], nuclide['exponent'])

    print(f" {nuclide['element']} {nuclide['atomicmass']}\n")
    print(f" Half-Life {nuclide['significand']}×10^{nuclide['exponent']} years\n")

    print("-" * tablewidth)
    print("|          Elapsed              |                Remaining                |")
    print("-" * tablewidth)
    print("| Half-Lives ", end="")
    print("|    Years         ", end="")
    print("| Decimal             | Amount            |")

    print("-" * tablewidth)

    for index, item in enumerate(dl):

        print(f"| {index:<11d}|", end="")
        print(f" {item['years_elapsed']:<17e}|", end="")
        print(f" {item['remaining_decimal']:<19.12f} |", end="")
        print(f" {item['remaining_amount']:<17.8g} |")

    print("-" * tablewidth)


def at_time(nuclidekey: str, years: int, startingvalue: int = 1048576) -> Dict:

    """
    Calculates amount of nuclide remaining after
    specified number of years.
    Result is a dictionary with keys remaining_decimal
    and remaining_amount
    """

    nuclide = ran.radioactive_nuclides[nuclidekey]

    halflife = _sci_not_to_num(nuclide['significand'], nuclide['exponent'])

    exponent = -(years / halflife)

    remaining_decimal = 2**exponent

    remaining_amount = startingvalue * remaining_decimal

    return { "remaining_decimal": remaining_decimal, "remaining_amount": remaining_amount }


def time_to(nuclidekey: str, remaining_decimal: float) -> float:

    """
    Calculates the amount of time for a nuclide
    to decay to the specified proportion
    """

    nuclide = ran.radioactive_nuclides[nuclidekey]

    halflife = _sci_not_to_num(nuclide['significand'], nuclide['exponent'])

    factor = -(math.log2(remaining_decimal))

    return halflife * factor

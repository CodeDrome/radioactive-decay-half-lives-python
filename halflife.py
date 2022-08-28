import halflifeutilities as hlu
import radioactivenuclides as ran


def main():

    print("-------------------------------------")
    print("| codedrome.com                     |")
    print("| Half Life of Radioactive Nuclides |")
    print("-------------------------------------\n")

    hlu.printnuclides()

    # hlu.decay_table("uranium235", 8, 1048576)

    # nuclide = ran.radioactive_nuclides["tellurium128"]
    # halflife = nuclide['significand'] * 10 ** nuclide['exponent']
    # at = hlu.at_time("tellurium128", halflife * 0.5, 1048576)
    # print(at)

    # tt = hlu.time_to("tellurium128", 0.5)
    # print(f"{tt} Years")
    # print(f"{tt:,.0f} Years")
    # print(f"{tt / 1000000:,.0f} Million Years")
    # print(f"{tt / 1000000000:,.0f} Billion Years")
    # print(f"{tt / 1000000000000:,.0f} Trillion Years")


if __name__ == "__main__":

    main()

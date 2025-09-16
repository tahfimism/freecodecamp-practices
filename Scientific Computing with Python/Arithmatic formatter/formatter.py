

def arithmetic_arranger(problems, show_answers=False):

    prob = []
    # checking no. of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # checking for errors
    for problem in problems:
        if "+" in problem:
            n1 , n2 = problem.strip().split("+")
            op = "+"
        elif "-" in problem:
            n1 , n2 = problem.strip().split("-")
            op = "-"
        else:
            return "Error: Operator must be '+' or '-'."

        n1 = n1.strip()
        n2 = n2.strip()

        if not (n1.isdigit() and n2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(n1) > 4 or len(n2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # counting digit length and total length
        len1 = len(n1)
        len2 = len(n2)
        if len1 > len2 or len1 == len2:
            tlen = len1 + 2
        else:
            tlen = len2 + 2


        prob.append({"n1":n1 , "n2":n2, "len1":len1, "len2":len2, "tlen": tlen, "op":op})



    line1 = []
    line2 = []
    dash = []
    for p in prob:
        line1.append(" " * (p["tlen"]-p["len1"]) + p["n1"])
        line2.append(p["op"] + " " * (p["tlen"] - p["len2"] - 1) + p["n2"])
        dash.append("-"* p["tlen"])


    line1 = "    ".join(line1)
    line2 = "    ".join(line2)
    lined = "    ".join(dash)

    if show_answers:
        list3 = []

        for p in prob:
            if p["op"] == "+":
                ans = int(p["n1"]) + int(p["n2"])
            else:
                ans = int(p["n1"]) - int(p["n2"])
            ans = str(ans)

            lena = len(ans)

            list3.append(" " * (p["tlen"] - lena) + ans)
            line3 = "    ".join(list3)
        return f"{line1}\n{line2}\n{lined}\n{line3}"



    return f"{line1}\n{line2}\n{lined}"




print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')



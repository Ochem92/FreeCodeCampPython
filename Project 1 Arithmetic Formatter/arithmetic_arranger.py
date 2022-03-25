
def arithmetic_arranger(problems, display_results=False):
    topl = ''
    midl = ''
    linel = ''
    outputl = ''
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        lproblems = [problem.split(" ") for problem in problems]
        for problem in lproblems:
            if "*" in problem or "/" in problem:
                return "Error: Operator must be '+' or '-'."
            elif problem[0].isnumeric() is False or problem[2].isnumeric() is False:
                return "Error: Numbers must only contain digits."
            elif len(problem[0]) > 4 or len(problem[2]) > 4:
                return "Error: Numbers cannot be more than four digits."

            else:
                if problem[1] == "+":
                    output = str(int(problem[0]) + int(problem[2]))
                else:
                    output = str(int(problem[0]) - int(problem[2]))

            width = max(len(problem[0]), len(problem[2]))+2
            topl += problem[0].rjust(width) + "    "
            midl += problem[1] + problem[2].rjust(width-1) + "    "
            linel += ("-" * width) + "    "
            outputl += str(output).rjust(width) + "    "

    if display_results is True:
        arranged_problems = topl.rstrip()+"\n"+midl.rstrip()+"\n"+linel.rstrip()+"\n"+outputl.rstrip()
    else:
        arranged_problems = topl.rstrip()+"\n"+midl.rstrip()+"\n"+linel.rstrip()

    return arranged_problems
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))


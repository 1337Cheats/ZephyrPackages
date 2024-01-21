def var(var_name, var_value):
    assignment_statement = f"var {var_name} = {var_value}"
    exec(assignment_statement)


with open(__file__, "r") as file:
    file_contents = file.read()
    lines = file.readlines()
    for line in lines:
        if "var" in line:
            var_name = line.split(" ")[1]
            var_value = gtiq(line)
            var(var_name, var_value)

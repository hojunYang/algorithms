def convert_to_decimal(num_str, base):
    if num_str == "X":
        return "X"
    result = 0
    for i, d in enumerate(num_str[::-1]):
        if int(d) >= base: 
            return None
        result += int(d) * (base ** i)
    return result

def decimal_to_base(decimal_num, base):
    if decimal_num == 0:
        return "0"
    digits = []
    while decimal_num:
        digits.append(str(decimal_num % base))
        decimal_num //= base
    return "".join(digits[::-1])

def solution(expressions):
    answer = []
    possible_base = [i for i in range(2, 10)]
    
    # search possible base system 
    for expression in expressions:
        expression = expression.split(" ")
        
        for base in sorted(possible_base):
            first = convert_to_decimal(expression[0], base)
            second = convert_to_decimal(expression[2], base)
            result = convert_to_decimal(expression[4], base)
            if first is None or second is None or result is None:
                possible_base.remove(base)
                continue
            if result == "X":
                continue
            if expression[1] == "+":
                if first + second != result:
                    possible_base.remove(base)
                    continue
            elif expression[1] == "-":
                if first - second != result:
                    possible_base.remove(base)
                    continue
    
    for expression in expressions:
        expression = expression.split(" ")
        
        if expression[4] == "X":
            for base in sorted(possible_base):
                first = convert_to_decimal(expression[0], base)
                second = convert_to_decimal(expression[2], base)
                
                if expression[1] == "+":
                    result = decimal_to_base(first + second, base)
                    if expression[4] == "X":
                        expression[4] = result
                    elif expression[4] != result:
                        expression[4] = "?"
                        break
                
                elif expression[1] == "-":
                    result = decimal_to_base(first - second, base)
                    if expression[4] == "X":
                        expression[4] = result
                    elif expression[4] != result:
                        expression[4] = "?"
                        break
            expression[4] = str(expression[4])
            answer.append(" ".join(expression))
    
    return answer

print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"])) # 
print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
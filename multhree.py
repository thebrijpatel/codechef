for i in range(int(input())):
    num_of_digits, first_digit, second_digit = map(lambda x: int(x), input().split())

    if num_of_digits == 2:
        if (first_digit + second_digit) % 3 == 0:
            print("YES")
        else:
            print("NO")
        continue

    third_digit = (first_digit + second_digit)%10
    # the next digits are the 4 digits 2, 4, 6, 8 repeated in some order(unless they are 0)
    repeating_digits = [(2*third_digit)%10]
    for i in range(3):
        repeating_digits.append((2*repeating_digits[i])%10)
    #print(repeating_digits)
    current_sum = first_digit + second_digit + third_digit
    remaining_digits = num_of_digits - 3
    groups_of_four = int(remaining_digits/4)
    leftovers = remaining_digits%4
    current_sum += groups_of_four * sum(repeating_digits)
    current_sum += sum(repeating_digits[:leftovers])
    #print(current_sum)
    if current_sum % 3 == 0:
        print("YES")
    else:
        print("NO")
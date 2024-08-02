def convert_to_words(amount):
    amount = str(amount)
    in_words = ''
    digit_ones = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
        
    }
    digit_ten_nine= {
        "eleven": 1,
        "twelve": 2,
        "thirteen": 3,
        "fourteen": 4,
        "fifteen": 5,
        "sixteen": 6,
        "seventeen": 7,
        "eighteen": 8,
        "nineteen": 9

    }
    digit_tens = {
        'ten': 1,
        'twenty': 2,
        'thirty': 3,
        'forty': 4,
        'fifty': 5,
        'sixty': 6,
        'seventy': 7,
        'eighty': 8,
        'ninty': 9

    }

    if len(amount) == 3:
        for k, v in digit_ones.items():
            if int(amount[0]) == v:
                in_words += k + " hundred"

        if int(amount[1]) != 1:
            for k, v in digit_tens.items():
                if int(amount[1]) == v:
                    in_words += " and " + k
        else:
            for k, v in digit_ten_nine.items():
                if int(amount[2]) == v:
                    in_words += " and " + k
                    return in_words

        for k, v in digit_ones.items():
            if int(amount[2]) == v:
                in_words += " " + k

    return in_words


if __name__ == '__main__':
    amount_digt = int(input('Enter the Amount : '))
    print(convert_to_words(amount_digt))

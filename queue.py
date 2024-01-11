loopflag = True
loopflag2 = True
keywordlist_AND = []
keywordlist_OR = []
print(" Please enter the keywords you would like to do LitSearch on (To finish inputs - > done)")

while loopflag == True:

    if loopflag2 == True:

        while loopflag2:
            user_input_keyword_OR = input("Enter your OR-terms (Type done to exit the OR-term-selection)")
            if user_input_keyword_OR.lower() != "done":
                keywordlist_OR.append(user_input_keyword_OR)
                loopflag2 = True
            else:
                loopflag2 = False
    else:

        user_input_keyword = input()
        loopflag2 = False
        if user_input_keyword.lower() == "done":
            loopflag = False
        else:
            keywordlist_AND.append(user_input_keyword)

print(keywordlist_OR)
print(keywordlist_AND)

result_string_OR = 'OR'.join([' ' + word + ' ' for word in keywordlist_OR])
result_string_OR_finale = '(' + result_string_OR + ')'
print(result_string_OR_finale)

result_string_AND = 'AND'.join([' ' + word + ' ' for word in keywordlist_AND])
result_string_AND_finale = '(' + result_string_AND + ')'
print(result_string_AND_finale)

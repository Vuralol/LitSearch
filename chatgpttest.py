def query_finalizer(operation, given_string, string_list):
    if operation == "AND":
        result = 'AND'.join([' ' + word + ' ' for word in string_list])

    elif operation == "OR":
        result = " or ".join(string_list)

    elif operation == "NOT":
        result = " not ".join(string_list)

    else:
        # Default to returning the original list as a string if the operation is unknown
        result = " ".join(string_list)


    # Add the given string before and after the result
    result = f"{result}"
    #result = f"{result} {given_string}"

    return '(' + result + ')' + given_string


# Example usage:
input_strings = ["a", "b", "c", "d"]

and_result = query_finalizer("AND", "hurensohn", input_strings)
print("Result from AND operation:", and_result)

#or_result = perform_string_operations("OR", "or", input_strings)
#print("Result from OR operation:", or_result)

#not_result = perform_string_operations("NOT", "not", input_strings)
#print("Result from NOT operation:", not_result)

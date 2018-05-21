def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

assert count_upper_case("") == 0, "count_upper_case(\"\") should have returned 0, but didn't"
assert count_upper_case("A") == 1, "count_upper_case(\"A\") should have returned 1, but didn't"
assert count_upper_case("a") == 0, "count_upper_case(\"a\") should have returned 0, but didn't"
assert count_upper_case("£$%%^") == 0, "count_upper_case(\"£$%%^\") should have returned 0, but didn't"
assert count_upper_case("AbC") == 2, "count_upper_case(\"AbC\") should have returned 2, but didn't"


print("All the tests passed")
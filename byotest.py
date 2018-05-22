def assert_equal(actual, expected):
    assert expected == actual, "Expected {}, got {}".format(expected, actual)

def assert_not_equal(a, b):
    assert a != b, "Did not expect {}, but got {}".format(a, b)

def assert_is_in(collection, item):
    assert item in collection, "{} does not contain {}".format(collection, item)
    
def assert_is_not_in(collection, item):
    assert item not in collection, "{} contains {}, but was not supposed to!".format(collection, item)
    
# assert_is_not_in([1, 2, 3, 4, 5], 3) # Fails
# assert_not_equal(1, 1) # Fails
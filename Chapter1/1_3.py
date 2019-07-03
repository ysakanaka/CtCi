import unittest

def myurlify(s, l):
    s = s.replace("\s", "%20")
    return s

# O(N)
def urlify(string, length):
    '''fucntion replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in reversed(range(length)):
        print(string)
        if string[i] == ' ':
            # Replace spaces
            string[new_index -3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index -1] = string[i]
            new_index -= 1
        print(string)
    return string

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

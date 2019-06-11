import unittest
def pal_perm(s):
    s = (s.replace(" ", "")).lower()
    bitVector = 0
    for i in range(len(s)):
        mask = 1 << ord(s[i])-97
        print(ord(s[i])-97)
        print("mask", bin(mask))
        if (bitVector & mask) == 0:
            bitVector = bitVector | mask
        else:
            bitVector = bitVector & (~ mask)
        print(bin(bitVector))
    return ((bitVector & (bitVector -1)) == 0) or bitVector == 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            print(test_string, actual)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

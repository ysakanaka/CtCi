import unittest
def pal_perm(s):
    s = (s.lower()).replace(" ", "")
    d = {}
    for e in s:
        if e in d:
            d[e]+=1
        else:
            d[e] = 1

    if len(s)%2 == 0:
        for v in d.values():
            if v%2 !=0:
                return False

    else:
        flag = False
        for v in d.values():
            if v%2 == 1 and not flag:
                flag = True
            elif v%2 == 0:
                pass
            else:
                return False

    return True

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
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

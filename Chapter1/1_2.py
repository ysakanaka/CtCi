import unittest

def permstring(s1, s2):
    if len(s1) != len(s2):
        return False

    for s in s1:
        s2 = s2.replace(s, "", 1)
    if len(s2) > 0:
        return False
    else:
        return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = permstring(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = permstring(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

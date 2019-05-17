import unittest

def func(word):
    dict = {}
    for s in word:
        if s in dict:
            return False
        else:
            dict[s] = s

    return True

def func2(word):
    box = [""] * 128
    for s in word:
        if box[ord(s)] != "":
            return False
        else:
            box[ord(s)] = s
    return True

class Test(unittest.TestCase):
    dataT = [("abcd"), ("s4fad"), ("")]
    dataF = [("23ds2"), ("hb 627jh=j ()")]

    def test_unique(self):
        for test_string in self.dataT:
            actual = func2(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = func2(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

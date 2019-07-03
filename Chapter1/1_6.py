import unittest

def string_compression(s):
    count = 1
    ans = ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count +=1
        else:
            ans+=s[i]+str(count)
            count = 1
    ans += s[i]+str(count)
    if len(s) < len(ans):
        return s
    return ans

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

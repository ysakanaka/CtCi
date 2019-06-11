import unittest

def laven(s1, s2):
    table = [[0]*(len(s1)+1) for i in range(len(s2)+1)]
    for i in range(len(s1)+1):
        table[0][i] = i
    for i in range(len(s2)+1):
        table[i][0] = i

    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s1[j-1] == s2[i-1]:
                cost = 0
            else:
                cost = 1

            table[i][j] = min(min(table[i-1][j-1]+cost, table[i-1][j]+1), table[i][j-1]+1)
    print(table)
    return table[len(s2)][len(s1)] == 1 or table[len(s2)][len(s1)] == 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = laven(test_s1, test_s2)
            print(test_s1, test_s2, actual)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

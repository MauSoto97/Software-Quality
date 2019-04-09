import unittest
ans = "This program couns numbers, like 3 or 6 and tells you how many times the 3 and the 6 were in the text"

array1 = ans.split(" ")
numbers=[]
words=[]
new=[]

for a in array1:
    try:
        float(a)
    except:
        words.append(a)
    else:
        numbers.append(a)

for i in range(0, len(numbers)):
    if numbers[i] not in new:
        new.append(numbers[i])

for i in range(0, len(new)):
    print('Frequency of ', new[i], ' is :', numbers.count(new[i]))

class TestStringMethods(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(len(numbers), 4, "The array contains a different amount of elements than desired")
    def test_words(self):
        self.assertEqual(len(words), 19, "The array contains a different amount of elements than desired")
    def test_object(self):
        self.assertIs(new, list, "The element is not a List")
unittest.main()

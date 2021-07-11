class SimpleStringEncoder:
    
    """To get random letters from the letters
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.-_= "
    letters = list(letters)
    numpy.random.shuffle(letters)
    print(''.join(letters))
    """
    # all the required letters in random order
    letters = '_2F3x6RzZAByVq8rI9jg.fc0D1Ekb PLMUWdpaemvXn7ouYNQHJK-t=hsOCw4iGlT5S'
    def __init__(self, letters = letters):
        self.letters = letters

    # pass the string to encode it , pass the encoded sting to get back the decoded string
    def codec(self, string):
        result = ''
        for i in string:
            result += self.letters[-self.letters.index(i)]

        return result

class Reverse:
    
    def __init__(self , s):
        self.s = s
    
    def reverse_string(self):
        return self.s[::-1]

s = input("Enter a word: ")
reverse = Reverse(s)

print(f"Reversed String: {reverse.reverse_string()} ")
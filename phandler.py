import os

class prints_handler:
    def __init__(self, count_newline, ignore_errors):
        self.printing_array = ''
        self.count_newline = count_newline
        self.ignore_errors = ignore_errors
        self.end = None
    
    def flatten_string(self, args):
        text = ''
        for i in range(len(args)):
            text += str(args[i]) + (' ' if i != len(args) - 1 else '')
        return text

    def input(self, prompt):
        value = input(prompt)
        self.printing_array += prompt + value + '\n'
        return value

    def print(self, *args, **kwargs):
        text = self.flatten_string(args)

        self.printing_array += text + (kwargs['end'] if 'end' in kwargs else '\n')
        if 'end' not in kwargs: print(text)
        else: print(text, end=(kwargs['end']))

    def delete_line(self, line_number):
        printing_array_temp = self.printing_array.split('\n')

        if line_number <= len(printing_array_temp):
            os.system('cls')
            printing_array_temp.pop(len(printing_array_temp)-line_number-1)
            self.printing_array = '\n'.join(printing_array_temp[:-1])
            print(self.printing_array)

        elif self.ignore_errors:
            pass

        else:
            raise ValueError("Can't delete a line that does not exist")

    def clear(self, clear_screen):
        self.printing_array = []
        if clear_screen: os.system('cls')
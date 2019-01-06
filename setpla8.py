def snake_to_camel(word):
        import re
        return ''.join(X.capitalize() or "_" for X in word.split("_"))
print(snake_to_camel('Exercises'))

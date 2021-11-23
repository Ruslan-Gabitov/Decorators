nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


def logging_fun(function):
    def wrapped(*args, **kwargs):
        import time
        import os
        start =time.ctime()
        result_fun = function(*args, **kwargs)
        name_fun = function.__name__
        log_path = os.path.abspath('logger.txt')
        data = f'Start time: {start}\nFunction name: {name_fun}\nFunction arguments: *args: {args} *kwargs: {kwargs}\nResult function: {result_fun}\nLog file path: {log_path}\n\n'

        with open('logging.txt', 'a') as file:
            file.write(data)
        return result_fun  
    return wrapped

class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.count = 0
        self.result = None
        
    def __iter__(self):
        return self
    @logging_fun
    def __next__(self):
        try:
            self.result = sum(self.nested_list, [])[self.count] 
        except IndexError:
            raise StopIteration
        self.count += 1    
        return self.result
              
for item in FlatIterator(nested_list):
	print(item)

@logging_fun
def flat_generator(nested_list):
    count = 0
    data = True
    while data:
        try:
            data = sum(nested_list, [])[count]
            count += 1
            yield data
        except IndexError:
            data = False

for item in flat_generator(nested_list):
	print(item)
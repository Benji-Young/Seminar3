def sum_all(numbers):
    if isinstance(numbers,int):
        return numbers
    if isinstance(numbers,list):
        return sum(sum_all(n) for n in numbers)

print(sum_all([1,[],4,5]))
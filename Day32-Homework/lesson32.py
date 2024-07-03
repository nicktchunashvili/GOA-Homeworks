"""ასევე შეასრულეთ შემდეგი ამოცანები:"""

#ამოცანა N:1
def no_odds(values):
    return [i for i in values if i % 2 == 0]
    
#ამოცანა N:2
def sum_cubes(n):
    return sum(i**3 for i in range(0,n+1))

#ამოცანა N:3
def number_of_occurrences(element, sample):
    return sample.count(element)
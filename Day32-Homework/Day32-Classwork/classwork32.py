"""ყველამ შეასრულეთ classwork-ის ამოცანები:"""

#8 kyu:

#ამოცანა N:1

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."
    
#ამოცანა N:2

def find_difference(a, b):
	return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])

#ამოცანა N:3

def triple_trouble(one, two, three):
    ans = ''
    for i in range(len(one)):
        ans+=one[i]
        ans+=two[i]
        ans+=three[i]
    return ans

#7kyu:

#ამოცანა N:4

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / (b * 1.0)

#ამოცანა N:5

def in_asc_order(arr):
    return arr == sorted(arr)

#ამოცანა N:6

def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    else:
        counter = sum(range(n+1))
        return '+'.join(map(str, range(n+1))) + " = " + str(counter)
    

#6kyu:

#ამოცანა N:7

def transform_string(s):
    def transform_word(word):
        return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))

    return ' '.join(transform_word(word) for word in s.split())

input_string = "Hello World"
result = transform_string(input_string)
print(result)  

#ამოცანა N:8

def reverse_segments(data):
    segments = [data[i:i+8] for i in range(0, len(data), 8)]
    
    reversed_segments = segments[::-1]
    
    reversed_data = [bit for segment in reversed_segments for bit in segment]
    
    return reversed_data

input_data = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
reversed_result = reverse_segments(input_data)
print(reversed_result)
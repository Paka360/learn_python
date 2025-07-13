#Tuples
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

primes = (3,5,7,11,13,17,19,21,23)
print("Original Primes")
for prime in primes:
    print(prime)

primes = (23,29,31,37,41)
print("Modified Primes")
for prime in primes:
    print(prime)

#Practice Exercise
print('\nMenu')
buffets = ('tea', 'coffee', 'porrige', 'milk_shake', 'soakings', 'pudding')
for buffet in buffets:
    print(buffet.title())

buffets = ('waakye', 'fufu', 'kokonte', 'tuozaafi', 'rice')
print('\nRevised Menu.')
for buffet in buffets:
    print(buffet.title())


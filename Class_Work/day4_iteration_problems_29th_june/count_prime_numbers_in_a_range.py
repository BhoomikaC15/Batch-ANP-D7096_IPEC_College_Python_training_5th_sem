'''
------------------------------------------Count Prime Numbers in a Range---------------------------------------
Problem Statement 
Accept two integers representing the starting and ending values of a range. 
Display all prime numbers within the range and finally display the total number of prime numbers 
found.
----------------------------------------------------------------
Sample Input
Enter the starting value of the range: 10
Enter the ending value of the range: 50
----------------------------------------------------------------
Sample Output
Prime numbers in the range [10, 50]: 11 13 17 19 23 29 31 37 41 43
Total number of prime numbers found: 10
----------------------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
start = int(input("Enter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))

prime_count = 0

print(f"Prime numbers in the range [{start}, {end}]:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            prime_count += 1

print(f"\nTotal number of prime numbers found: {prime_count}")
#----------------------------------------------------------------------------------------------------------
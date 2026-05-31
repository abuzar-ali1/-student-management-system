def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        # Check if num is divisible by any smaller number up to its square root
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

if __name__ == "__main__":
    try:
        limit = int(input("Enter N to generate prime numbers up to N: "))
        if limit < 2:
            print("There are no prime numbers less than 2.")
        else:
            print(f"Prime numbers up to {limit}: {generate_primes(limit)}")
    except ValueError:
        print("Please enter a valid integer.")
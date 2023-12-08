#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def count_moves(primes, n):
        count = 0
        for prime in primes:
            if prime <= n:
                count += 1
        return count

    def can_make_move(primes, n):
        return count_moves(primes, n) > 0

    def get_winner(primes, n):
        if can_make_move(primes, n):
            return "Maria"
        else:
            return "Ben"

    most_wins = 0
    winner = None

    for n in nums:
        primes = get_primes(n)
        if get_winner(primes, n) == "Maria":
            most_wins += 1

    if most_wins > x - most_wins:
        return "Maria"
    elif most_wins < x - most_wins:
        return "Ben"
    else:
        return None

# Example usage
print("Winner: {}".format(isWinner(3, [4, 5, 1])))

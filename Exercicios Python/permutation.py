import itertools

if __name__ == '__main__':
    s = 'Joaozinho'
    
    nums = list(s)
    permutations = list(itertools.permutations(nums))

    # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    print([''.join(permutation) for permutation in permutations])
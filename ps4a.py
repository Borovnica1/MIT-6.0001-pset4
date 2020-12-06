# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    print(sequence)
    if len(sequence) == 1:
        return [sequence]
    
    perm_list = []
    
    for char in sequence:
        remaining_elements = [x for x in sequence if x != char]
        print('XXXXX',remaining_elements)
        z = get_permutations(remaining_elements) # permutations of sublist
        print('ZZZZZ ',z, char)
        for t in z:
            print(t)
            perm_list.append([char] + t)
            print('APPENDEDDDD ', perm_list)
    print('OUT OF LOOOOOOOOOOP')
    return perm_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    get_permutations('abc')
    pass #delete this line and replace with your code here


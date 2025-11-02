#Exercise 1.3: String Pattern Analyzer

# Problem Description:
# Create a program that analyzes a given text string and provides:
# 1. Character frequency count (case-insensitive)
# 2. Word count
# 3. Most common character (excluding spaces)
# 4. Palindrome check
# 5. Reverse the string

def string_pattern_analyzer():
    input_str = input("Enter a text string: ").lower()
    print(f"Input string: {input_str}")
    # Character frequency count
    char_freq = {}
    for char in input_str:  
        char_freq[char] = char_freq.get(char, 0) + 1
    print("Character frequency count (case-insensitive):")
    for char, freq in char_freq.items():
        print(f"'{char}': {freq}")
    print(f'Word count:{len(input_str.split(' '))}' )

    # Most common character (excluding spaces)
    char_freq.pop(' ', None)
    most_common_char = max(char_freq, key= lambda key: char_freq.get(key))
    print(f'fmost_common_char {most_common_char}')
    
    #Reverse the string
    reversed_str = input_str[::-1]
    print(f'Reversed String: {reversed_str}')

    # Palindrome check
    print(f'Palindrome check: {reversed_str == input_str}')


    

    



string_pattern_analyzer()


    
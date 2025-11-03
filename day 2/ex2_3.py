#Problem 3: File Line Generator (Generators - Beginner)

def read_file_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def strip_lines(lines):
    for line in lines:
        yield line.strip()

def number_lines(lines):
    for idx, line in enumerate(lines, start=1):
        yield f"{idx}: {line}"

def chunk_lines(lines, chunk_size):
    chunk = []
    for line in lines:
        chunk.append(line)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def reverse_lines(lines):
    buffer = list(lines)
    for line in reversed(buffer):
        yield line

# Write sample file
sample_content = "\nHello World\nPython Programming\nThis is a test\nPython is awesome\nFinal line\n"
file_path = 'sample.txt'
with open('file_path', 'w') as f:
    f.write(sample_content)
# Read file using generator
print("All lines:")
for line in read_file_lines(file_path):
    print(repr(line))
# Output:
# '\n'
# 'Hello World\n'
# 'Python Programming\n'
# 'This is a test\n'
# 'Python is awesome\n'
# 'Final line\n'
# Chain generators - filter and strip
print("\nFiltered lines (containing 'Python'):")
lines = read_file_lines(file_path)
filtered = filter_lines(lines, 'Python')
stripped = strip_lines(filtered)
for line in stripped:
    print(line)
# Output:
# Python Programming
# Python is awesome
# Number lines
print("\nNumbered lines:")
lines = read_file_lines(file_path)
stripped = strip_lines(lines)
numbered = number_lines(stripped)
for line in numbered:
    print(line)
# Output:
# 1:
# 2: Hello World
# 3: Python Programming
# 4: This is a test
# 5: Python is awesome
# 6: Final line
# Chunk lines
print("\nChunked lines (size 2):")
lines = read_file_lines(file_path)
stripped = strip_lines(lines)
chunked = chunk_lines(stripped, 2)
for chunk in chunked:
    print(chunk)
# Output:
# ['', 'Hello World']
# ['Python Programming', 'This is a test']
# ['Python is awesome', 'Final line']

reverse_lines(lines)
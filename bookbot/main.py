book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_by_key, sorted_by_value = count_each_character(text) 
    book_report = report(num_words, sorted_by_key, sorted_by_value, book_path)
    print(book_report)
 


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_each_character(words):
    counts = {}
    for word in words:
        for char in word:
            # Convert to lowercase and check if it's an alphabet letter
            if char.isalpha():
                char = char.lower()
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1

    # Sort by keys (alphabetically)
    sorted_by_key = dict(sorted(counts.items()))

    # Sort by values (# of letters)
    sorted_by_value = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    return sorted_by_key, sorted_by_value

def report(num_words, sorted_by_key, sorted_by_value, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for key, value in sorted_by_key.items():
        print(f"The '{key}' character was found {value} times") 
    return ("--- End report ---")
main()
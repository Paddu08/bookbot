from stats import spilt_words, char_counter, sort_counter
import sys 


if len(sys.argv)==1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
if len(sys.argv)>2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main(bookname):
    
    text = get_book_text(bookname)
    

        

    words = spilt_words(text)
    num_words = len(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookname}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
   

    counts = char_counter(text)
    sorted_list = sort_counter(counts)

    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

bookname=sys.argv[1]


main(bookname)

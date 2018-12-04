from typing import List


def is_palindrome(text: str, input_store: List) -> bool:
    """Returns true if the text is palindrome and takes a 
    record od last five entries
    false otherwise
    @type text:str
    @rtype: bool
    >>>store=[]
    >>> is_palindrom("ijeji",store)
    >>> True
    >>> is_palindrome("test",store")
    >>> False
    """

    input_store.append(text)
    if len(input_store) > 5:
        input_store.remove(input_store[0])
    if len(text) == 1 or text == "":
        return True
    text = text.replace(" ", "").lower()
    forward_count = 0
    end_index = len(text) - 1
    while forward_count < len(text):
        text[forward_count]
        if text[end_index - forward_count] != text[forward_count]:
            return False
        forward_count += 1
    return True


if __name__ == "__main__":
    records = []
    choice = ""
    while True:
        count = 0
        string = input("Enter a string: ")
        if is_palindrome(string, records):
            print("\n{} is a palindrome".format(string))
        else:
            print("\n{} is not a palindrome".format(string))
        print("\nThe previous entrie(s) you made are:")
        for entry in records:
            print("{}. {}".format(count+1, entry))
            count += 1
        choice = input("\nDo you want to continue Y/N? ")
        if choice.lower() == "n":
            print("\nGoodbye!")
            break
        while(choice.lower() != "n" and choice.lower() != "y"):
            print("\nPleas make correct choice from options given")
            choice = input("Do you want to continue Y/N? ")

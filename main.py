def sort_on(dict_item):
    #External solution #TODO Better understand how exactly does it work. Is it recursive? Hmm... 
    return next(iter(dict_item.values()))

def main():

    #local dir for source book for report
    reported_book = "books/frankenstein.txt"

    #dictionary var storing following: {key: "lower case letter", value: "amount of time such letter occuried in reported book"}
    letter_occurances_dict = {}

    #Reading file, changing all letters to lower case. words are list of strings
    with open(reported_book) as f:
        file_contents = f.read()
        file_contents_lower = file_contents.lower()
        words = file_contents_lower.split()

    #Populating letter_occurances_dict
    for word in words:
        for char in word:
            #Excluding all characters that are not party of alphabet
            if char.isalpha():
                if char in letter_occurances_dict:
                    letter_occurances_dict[char] += 1
                else:
                    letter_occurances_dict[char] = 1

    #list of dicts
    list_of_letter_dicts = []
    #sorted list of dicts
    sorted_list_of_letter_dicts = []

    #Populating list of dicts based on letter_occurances_dict
    for key, value in letter_occurances_dict.items():
        list_of_letter_dicts.append({key: value})

    #Sorting list of dicts, populating sorted list of dicts. #TODO Better understand how exactly does it work. key=sort_on is confusing. 
    sorted_list_of_letter_dicts = sorted(list_of_letter_dicts, key=sort_on, reverse=True)

    #Printing report
    print(f"--- Begin report of {reported_book} ---")
    #Itereting throught all element of list of letter dicts
    for list_element in sorted_list_of_letter_dicts:
        #Exposing key and value of list element dicts
        for key, value in list_element.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---") 

main()
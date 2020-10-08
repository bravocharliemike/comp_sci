data = [
{
"question": "In which year was Halley's Comet last visible from Earth?",
"answers": ["1986"],
"difficulty": 3
},
{
"question": "Where were the 2016 Summer Olympics held?", 
"answers": ["rio de janeiro", "rio", "brazil"], 
"difficulty": 2
},
{
"question": "Where were the 1946 Olympics held?",
"answers": ["Helsinki"],
"difficulty": 3
}
]

#def search_questions(data_list, query):


# Main body of program
def search_term(data_list, query):

    found = False
    for index, question in enumerate(data_list):
        question_text = question['question']
        if query in question_text.lower():
            found = True
            print(f"{index + 1}) {question_text}")
    if not found:
        print('No results found.')


def main():
    search_query = input('Enter search term: ').lower()
    search_term(data, search_query)

if __name__ == '__main__':
    main()

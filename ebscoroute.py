import collector



def text_tx():
    # 1. TX All Text
    keywordlist_and = []
    keywordlist_not = []
    given_string= "TX"
    # hier Deklarieren und Initialisiren wir alle Parameter die wir benötigen um unsere Queries zu schreiben bzgl. AND/OR/NOT

    print("Function fot TX All Text is called.")

    # Hier werden die OR-Queries genommen
    print("Enter the keywords that CAN to be in the article: Enter 'done' to end ")
    keywordlist_or = collector.termcollector()

    #Hier werden die AND-Keywords genommen
    user_decision_and = input("Do you want to search for terms that HAVE TO BE IN THE ARTICLE? Enter y or n")
    if  user_decision_and.lower() == 'y':
        print("Enter the keywords you want to search for they HAVE to be in the article: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

    #Hier werden die NOT-Keywords gesammelt
    user_decision = input("Do you want to exclude search terms? if so enter 'y' or 'n'")
    if user_decision == 'y':
        print("Enter the keyword(s) to exclude: (enter 'done' to end) ")
        keywordlist_not = collector.termcollector()
    else:
        pass

    # Diese Listen könnte man nun zum collector() rüberschicken um eben die redundanz des Codes zu vermindern bzw. um die Queries nun endlich zu gestalten
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))
def author_au():
    # 2.AU Author
    keywordlist_and = []
    keywordlist_not = []
    given_string = "AU"
    print("Function for AU Author is called.")

    author_string = print("Enter the name(s) of the scientists (Authors) that CAN be the Authors: (type 'done' to end) ")
    keywordlist_or = collector.termcollector()

    # Hier werden die AND-Keywords genommen
    user_decision_and = input("Enter the names of the scientists that HAVE TO BE the AUTHORS? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the Authors that HAVE TO BE the AUTHORS: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

        # Hier werden die NOT-Keywords gesammelt
    user_decision = input("Do you want to exclude AUTHORS? if so enter 'y' or 'n'")
    if user_decision == 'y':
            print("Enter the AUTHORS you want to exclude: (type 'done' to end) ")
            keywordlist_not = collector.termcollector()
    else:
        pass
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))
def title_ti():
    # 3.TI Title
    keywordlist_and = []
    keywordlist_not = []
    given_string = "TI"
    print("Function for TI Title is called.")

    author_string = print("Enter the titles that you want to search for: (type 'done' to end) ")
    keywordlist_or = collector.termcollector()

    # Hier werden die AND-Keywords genommen
    user_decision_and = input("Do you want to search for mandatory Titles? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the titles that HAVE TO BE in the TITLE: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

        # Hier werden die NOT-Keywords gesammelt
    user_decision = input("Do you want to exclude titles? if so enter 'y' or 'n'")
    if user_decision == 'y':
            print("Enter the titles you want to exclude: (type 'done' to end) ")
            keywordlist_not = collector.termcollector()
    else:
        pass
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))
def subject_term_su():
    # 4.SU Subject Terms

    given_string = "SU"
    keywordlist_and = []
    keywordlist_not = []
    print("Function for SU Subject Terms is called.")

    # AND - OR- verknüpfungen müssen hier abgefragt werden

    print("Enter the subject terms you want to search for: ")
    keywordlist_or = collector.termcollector()

    # Hier werden die AND-Keywords genommen
    user_decision_and = input("Do you want to search for mandatory Subject Terms? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the Subject terms that HAVE TO BE in the Article: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

    # Hier werden die NOT-Keywords genommen
    user_decision_and = input("Do you want to exclude Subject Terms? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the Subject Terms that you want to EXCLUDE: (type 'done' to end) ")
        keywordlist_not = collector.termcollector()
    else:
        pass
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))

def source_so():
    # 5. SO Source

    given_string = "SO"
    keywordlist_and= []
    keywordlist_not = []
    print("Function for SO Source is called.")

    # AND - OR- verknüpfungen müssen hier abgefragt werden

    print("Enter the Sources you want to search from: ")
    keywordlist_or = collector.termcollector()

    # Hier werden die AND-Keywords genommen
    user_decision_and = input("Do you want to search from MANDATORY Sources? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the Sources where the Article has to be searched from: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

    # Hier werden die NOT-Keywords genommen
    user_decision_and = input("Do you want to exclude Subject Terms? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the Subject Terms that you want to EXCLUDE: (type 'done' to end) ")
        keywordlist_not = collector.termcollector()
    else:
        pass
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))

def abstract_ab():
    # 6. AB Abstract

    given_string = "AB"
    keywordlist_and = []
    keywordlist_not = []

    print("Function for AB Abstract is called.")

    # AND - OR- verknüpfungen müssen hier abgefragt werden

    print("Enter the Sources you want to search from: ")
    keywordlist_or = collector.termcollector()

    # Hier werden die AND-Keywords genommen
    user_decision_and = input("Do you want to search from MANDATORY Sources? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the Sources where the Article has to be searched from: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

    # Hier werden die NOT-Keywords genommen
    user_decision_and = input("Do you want to exclude Subject Terms? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the Subject Terms that you want to EXCLUDE: (type 'done' to end) ")
        keywordlist_not = collector.termcollector()
    else:
        pass
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))

def issn_is():
    # 7. IS ISSN
    given_string = "ISSN"
    keywordlist_and= []
    keywordlist_not = []
    print("Function for IS ISSN is called.")

    # AND - OR- verknüpfungen müssen hier abgefragt werden

    print("Enter the ISSN you want to search from: ")
    keywordlist_or = collector.termcollector()

    # Hier werden die AND-Keywords genommen
    user_decision_and = input("Do you want to search for MANDATORY ISSN'S? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the ISSN where the Article has to be searched from: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

    # Hier werden die NOT-Keywords genommen
    user_decision_and = input("Do you want to exclude ISSN's? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the ISSNs that you want to EXCLUDE: (type 'done' to end) ")
        keywordlist_not = collector.termcollector()
    else:
        pass
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))


def isbn_is():
    # 8. ISBN

    given_string = "ISBN"
    keywordlist_and= []
    keywordlist_not = []
    print("Function for 8 is called.")

    # AND - OR- verknüpfungen müssen hier abgefragt werden

    print("Enter the ISBN you want to search from: ")
    keywordlist_or = collector.termcollector()

    # Hier werden die AND-Keywords genommen
    user_decision_and = input("Do you want to search for MANDATORY ISBN's? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the ISBN where the Article has to be searched from: (type 'done' to end) ")
        keywordlist_and = collector.termcollector()
    else:
        pass

    # Hier werden die NOT-Keywords genommen
    user_decision_and = input("Do you want to exclude ISBN's? Enter y or n")
    if user_decision_and.lower() == 'y':
        print("Enter the ISBN that you want to EXCLUDE: (type 'done' to end) ")
        keywordlist_not = collector.termcollector()
    else:
        pass
    print(collector.query_finalizer("OR", given_string, keywordlist_or))
    print(collector.query_finalizer("AND", given_string, keywordlist_and))
    print(collector.query_finalizer("NOT", given_string, keywordlist_not))



# Get user input
print("The following list is an enumeration of the searchable fields. Choose any you desire via inputs")
print("1 text_tx,"
      "2 author_au,"
      "3 title_ti,"
      "4 subject_term_tu,"
      "5 source_so,"
      "6 abstract_ab,"
      "7 issn_is,"
      "8 isbn_is")
user_input = input("Enter numbers between 1 and 8 separated by commas: ")

# Split the input into a list of numbers
numbers = [int(num) for num in user_input.split(',')]

# Define a dictionary to map numbers to functions
function_mapping = {
    1: text_tx,
    2: author_au,
    3: title_ti,
    4: subject_term_su,
    5: source_so,
    6: abstract_ab,
    7: issn_is,
    8: isbn_is,
    #doi search
}

# Call the appropriate function for each number
for number in numbers:
    if 1 <= number <= 8:
        # Call the function using the dictionary
        function_mapping[number]()
    else:
        print(f"Ignoring {number} as it is not between 1 and 8.")

# End of the program
print("End of the program.")

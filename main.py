def orkeywords():
    loopflag_or = True
    or_keywordlist = []
    while loopflag_or:
        user_input = input()

        if user_input == "done":
            loopflag_or = False
        else:
            loopflag_or = True
            or_keywordlist.append(user_input)

    or_keywordlist_or = 'OR'.join([' ' + word + ' ' for word in or_keywordlist])
    or_keywordlist_finale = '(' + or_keywordlist_or + ')'
    return or_keywordlist_finale


def andkeywords():
    loopflag_and = True
    and_keywordlist = []
    while loopflag_and:
        user_input = input()

        if user_input == "done":
            loopflag_and = False
        else:
            loopflag_and = True
            and_keywordlist.append(user_input)

    and_keywordlist_and = 'AND'.join([' ' + word + ' ' for word in and_keywordlist])
    and_keywordlist_finale = '(' + and_keywordlist_and + ')'
    return and_keywordlist_finale


def ebscoroute():
    table_of_terms = (" 1. TX All Text 2. AU Author 3. TI Title 4. SU Subjects (Descriptors) "
                      "5. AB Abstract 6. KW Keywords 7. RW Book Reviews 8. CO Company 9. CN Conference"
                      "10. CA Corporate Author 11. Country of Publicatio 12. GE Geographic Subject 13. IS ISSN"
                      "14. IB ISBN 15. LA Language 16. OL Language of Origin 17. PE Person/Team 18. PS Products"
                      "19. PB Publisher 20. RE Report Number 21. SO Source")
    table_of_terms_angemeldet = (" 1. TX All Text, 2.AU Author, 3.TI Title, 4.SU Subject Terms, 5. SO Source, 6. AB Abstract , 7. IS ISSN , 8. ISBN ")
    print("Which of these criteria has to be searched for? (e.g. 1,16,18,2,4) ")
    print(table_of_terms)


Programloop = True
print("Please insert the keywords that you WANT to search for (OR):")
print("Type done to exit")
zu_zeigen = orkeywords()
print("Please insert the keywords that you HAVE TO be searched for (AND): ")
print("Type done to exit")
zu_zeigen2 = andkeywords()
print(zu_zeigen)
print(zu_zeigen2)

# (teaching OR learning OR studying)
# AND (hackathon OR devcamp OR dev camp OR hack week)

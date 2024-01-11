from pipes import quote

keyword = input("Enter the keyword: ")
author = input("Enter the author's name: ")

processed_keyword = quote(keyword)
processed_author = quote(author)

print(processed_author)
print(processed_keyword)

import keyword

# Get the list of keywords
keywords = keyword.kwlist

# Save output in the current folder
with open("keywords_output.txt", "w") as file:
    for index, word in enumerate(keywords, start=1):
        file.write(f"{index}. {word}\n")

print("Output saved to 'keywords_output.txt' in the current folder.")


# To save file in Current Directory

# PS C:\Users\DELL\Desktop\Python\15_Keywords> python write.py
# Output saved to 'keywords_output.txt' in the current folder.
# PS C:\Users\DELL\Desktop\Python\15_Keywords> 
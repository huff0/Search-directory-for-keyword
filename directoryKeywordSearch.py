""""
Description: This is a script to search all files within a directory for keywords

TODO: Add GUI + ability to select different keyword lists

Author: huff

"""

import os

def searchDirectory(directory, keywords):

    # Create an empty list to store the paths of the files that contain any of the keywords
    filesContainingKeywords = []
    
    # Iterate files in directory
    for file in os.listdir(directory):

        # Get the full path of the file
        filePath = os.path.join(directory, file)
        
        # If the file is a subfolder then recursively search
        if os.path.isdir(filePath):
            filesContainingKeywords += searchDirectory(filePath, keywords)
        else:
            # Open the file and read its contents
            with open(filePath, 'r') as f:
                contents = f.read()
            
            # Iterate keywords
            for word in keywords:
                # Check (case insensitively) if the keyword is in the file 
                if word.lower() in contents.lower():
                    # If keyword is in file, add the file's path to the list
                    filesContainingKeywords.append(filePath)
                    break
    
    return filesContainingKeywords

# Change and add keywords
keywords = ['secret', 'words'] 

# Add path to the directory 
files = searchDirectory('/path/to/directory/', keywords) 

# Output file name(s) which contains keyword(s)
print(files)



    
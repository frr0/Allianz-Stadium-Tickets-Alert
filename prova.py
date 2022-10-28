# Python program to read
# file word by word

# opening the text file
with open('data.txt','r') as file:

    # reading each line	
    for line in file:

        # reading each word		
        for word in line.split():

            # displaying the words		
            # print(word)

            if(word == "ticket" or word == "tickets" or word == "ticket." or word == "tickets." or word == "tickets." or word == "tickets." or word == "ticket," or word == "tickets," or word == "ticket!" or word == "tickets!" or word == "ticket?" or word == "tickets?"):
                Line = line
                print(line)

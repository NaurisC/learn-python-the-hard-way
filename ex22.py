import sys
script, input_encoding, error = sys.argv #command line argument that takes 3 inputs. what is error = sys.argv?

#in this secxction we are only defining functions. Not running anything yet
def main(language_file, encoding, errors):
     line = language_file.readline() #reads line from the file and assigns it to the variable line 
     
     if line: #tests if there is something in the line of the document. If True is returned next 2 lines are executed until empty line is reached
        print_line(line, encoding, errors) 
        return main(language_file, encoding, errors) #calling the main function again, effectively looping itself until False is reached
        
        
def print_line(line, encoding, errors):
    next_lang = line.strip() #strip() trims the whitespace from the string, 
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
# Here we are done with defining stuff and are ready to execute

languages = open("languages.txt", encoding="utf-8") # so we open the file languages.txt and assign it's contents to the variable languages. Set the encoding to utf-8 and assign it to the variable encoding

main(languages, input_encoding, error) #call the main function with the arguments languages, input_encoding, and error


#this script is taking bytes written inside the b'' (byte string) and converting them to the UTF-
#8 (or other) encoding specified
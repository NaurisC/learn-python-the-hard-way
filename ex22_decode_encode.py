def main(language_file, encoding):
     line = language_file.readline() #reads line from the file and assigns it to the variable line 
     
     if line: #tests if there is something in the line
        print_line(line, encoding) #if line 8 returns true, this is executed
        return main(language_file, encoding) #and this. If line 8 returns False, 9 and 10 are not executed
        
        
def print_line(line, encoding):
    next_lang = line.strip() #strip() trims the whitespace from the string, 
    raw_bytes = next_lang.encode(encoding)
    cooked_string = raw_bytes.decode(encoding,)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8") #open the file languages.txt and assign it's contents to the variable languages. Set the encoding to utf-8 and assign it to the variable encoding
input_encoding = "utf-8"

main(languages, input_encoding) #call the main function with the arguments languages, input_encoding, and error


#this script is taking bytes written inside the b'' (byte string) and converting them to the UTF-
#8 (or other) encoding specified



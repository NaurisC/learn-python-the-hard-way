def main(language_file, encoding):
     line = language_file.readline() #reads line from the file and assigns it to the variable line 
     
     if line.strip(): #tests if there is something in the line
        print(line.encode(encoding))

language_file = open("languages.txt") 

main(language_file, encoding = "utf-8")
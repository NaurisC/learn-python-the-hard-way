#just playing around with code elements from ex22.py

languages = open("languages.txt", encoding="utf-8")
encoding = "utf-8"

def main(languages, encoding):
    line = (languages.readline())
    
    
    if line:
        print(languages.readline())
        return main(languages, encoding)

main(languages, "utf-8")
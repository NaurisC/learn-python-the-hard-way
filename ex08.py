formatter = "{} {} {} {}" #if you add {} it will print the same number of times you have {} in the formatter. you can\t have less {} than in the lists below
print(formatter.format(1, 2, 3, 4)) #if you add more numbers than {} it will not print the extra numbers
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Hail onto thee",
    "Who art Hathor in your triumphing",
    "Even unto thee",
    "Who art Hathor in your beauty",
    "Who travellest over the heavens in thy bark at the midcourse of the Sun", #will not print this line
    "Tahuti standeth in his splendour at the prow",#will not print this line
    "And Ra-Hoor abideth at the helm",#will not print this line
    "Hail unto thee from the abodes of the morning"#will not print this line

))
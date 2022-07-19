import gender_guesser.detector as gender

# The result will be one of
# unknown (name not found),
# andy (androgynous),
# male,
# female,
# mostly_male,
# or mostly_female.
#
# The difference between andy and unknown is that the "andy" is found to have the same probability to be male
# than to be female, while the "unknown" means that the name was not found in the database.

d = gender.Detector()

print("\n== First names randomly selected from CTF and Grobid XMLs ==\n")
names = [u"Adeline", u"Arya", u"Amalesh", u"Aner", u"Casta", u"Hongjun", u"Jani", u"Magda", u"Ritwik",  u"Saima"]

for name in names:
    print(name + " - " + d.get_gender(name))



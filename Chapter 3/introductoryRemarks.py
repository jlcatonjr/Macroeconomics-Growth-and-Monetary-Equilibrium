

ryanThompson = "Ryan goes to NDSU. He is from Lakota. He grew up on a farm. He has a dog \
named Hurley. Ryan loves wheat."

adamSeidler = "Adam is from Garrison. He grew up on a farm. Adam loves wheat too... \
Adam has a dog named Zeus. Adam does not believe in Greek mythology. He loves elephants."

coleHanson = "Cole is from Minot. He grew up in Minot. He likes to snowboard. \
Cole is winning the dog game. Their names are Jaxon, Oliver, and Piper."

jessicaFleck = "Jessica is from Mandan. She grew up on a ranch. She hates cows. \
She has three dogs that she love; thus she and Cole are tied. Two Australian sheperds \
red healer cross and one Australian sheperd blue healer cross. They are named Sadie, \
Dixie, and Kota. Jessica's favorite condiment is ranch."

markSimonson = "Mark is from Fargo. He has two cats. One is named Max and the other \
is named Cuddles. Mark is a city boy, never doin any of that ag stuff! Mark is interested \
in finance. He also likes to watch movies. His favorite kind of movie is tied between \
comedy and horror. He might like the combination of the two."

coleGoetz = "Cole is from Mandan. He did not grow up on a farm or a ranch. Cole doesn't \
do much in Mandan. His girlfriend has two cats. She also left Mandan. Cole is a simple kind \
of man. He likes the Twins!"

maxCossette = "Max is from a farm just outside of Fargo. His farm grows alot of soy and \
some barley. He likes to wake surf and snowmobile. He wakesurfs at Crystal Lake. Max is \
interested in precision ag. He is really into hardcore sports. He likes to ride dirtbikes! \
beerrraahhppp!!!"

ekremErgun = "Ekrem is from Turkey. He grew in Ankara, which is the capital of Turkey. \
Ekrem liked to eat kabob in Turkey. He likes to play video games. He likes DOTA on Warcraft III. \
Ekrem plays soccer (you know, because in the U.S. we don't call it football...). \
Ekrem was busy sleeping during the World Cup 2018."

khadeejaMahmood = "Khadeeja is from Pakistan. She moved a lot when she was growing up. \
Her father was in the military. She likes sports and used to play basketball. She likes \
to watch cricket. Her favorite animal is a dog, but she like many kinds of animals."

print(ryanThompson, adamSeidler, coleHanson, jessicaFleck)
print()
print(ryanThompson)
print()
print(adamSeidler)
print()
print(coleHanson)
print()
print(jessicaFleck)

"""make a dictionary for introductions"""
students = {}
students["Ryan Thompson"] = [ryanThompson]
students["Adam Seidler"] = [adamSeidler]
students["Cole Hanson"] = [coleHanson]
students["Jessica Fleck"] = [jessicaFleck]
students["Mark Simonson"] = [markSimonson]
students["Cole Goetz"] = [coleGoetz]
students["Max Cossette"] = [maxCossette]
students["Ekrem Ergun"] = [ekremErgun]
students["Khadeeja Mahmood"] = [khadeejaMahmood]

print(students)

for student in students:
    print()
    print(students[student])
    
import pandas as pd

studentsDF = pd.DataFrame(students).T
studentsDF = studentsDF.rename(columns = {studentsDF.columns[0]:"Cool Stuff about Student"})
studentsDF.index.names = ['Student Name']

print(studentsDF)
studentsDF.to_csv("Student Introductions.csv")
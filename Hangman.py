import random, time

print("Hello! Welcome to hangman!\n")

time.sleep(2)

movies = ["avatar", "titanic", "toy story", "spiderman"]
famous_people = ["barakobama", "jamesbond", "brandoncole", "tiaracarbin", "averybrown"]
bible_books = ["genisis", "exodus", "revelations", "kings", "songs" "pslams", "mathew", "numbers", "judges", "brandon"]

category_list = {}
category_list["movies"] = movies
category_list["famous people"] = famous_people
category_list["bible books"] = bible_books
key_list = [key for key in category_list]

print("Choose from these categories below!\n")
time.sleep(1)
for keys in key_list:
    print(str(key_list.index(keys) + 1) + ".", keys)

print("")

cat = input("Enter choice here: ")

choice = random.sample(category_list[cat], 1)
word = choice[0]

word.lower()
blank = ("_ " * len(word))
print(blank + "\n")
num_trys = 6
char_list = set()


while "_" in blank:
    
    char = input("Guess your letter: ")
    
    if char not in word:
        print("Incorrect!\n")
        
        if char in char_list:
            num_trys = num_trys
        
        if char not in char_list:
            num_trys -= 1
    
    elif char in word:
        blank = blank.split()
        indexes = [i for i in range(0,len(word)) if word[i] == char]
        for i in range(0,len(indexes)):
            blank[indexes[i]] = char
        blank = " ".join(blank)

    char_list.add(char)
    print(blank + "\n")
    print("You have", num_trys, "trys left\n")

    if num_trys == 0:
        print("Game over!")
        time.sleep(1)
        print("The word was", word)
        break

word = input("Press enter to exit program")


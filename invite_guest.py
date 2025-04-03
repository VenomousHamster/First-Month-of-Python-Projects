
list_of_letters = []

with open("C:././Names/invited_names.txt", "r") as file:
    lines = file.readlines()
    names = [line.strip() for line in lines]

with open("C:././Names/invited_names.txt", "w") as file:
    file.write("\n".join(names))

with open("C:././Letters/starting_letter.txt", "r") as file:
           letter = file.read()

for name in range(len(names)):
    current_letter = letter.replace("name", names[name])
    list_of_letters.append(current_letter)

for i in range(len(names)):
    with open(f"C:././ReadyToSend/{names[i]}.text", "w") as file:
        file.write(list_of_letters[i])

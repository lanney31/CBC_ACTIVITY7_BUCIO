
def about_me():
    with open('about_me.txt', 'w') as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        hobby = input("Enter your favorite hobby: ")
        
       
        file.write("Name: " + name + "\n")
        file.write("Age: " + age + "\n")
        file.write("Hobby: " + hobby + "\n")
        
    print("Your details have been written to 'about_me.txt'.")


def read_about_me():
    try:
        with open('about_me.txt', 'r') as file:
            content = file.read()
            print("\nDetails from 'about_me.txt':")
            print(content)
    except FileNotFoundError:
        print("The file 'about_me.txt' does not exist.")


about_me()  
read_about_me()

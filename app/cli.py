from app.models import create_emotions_table, add_emotion

# this small cli helps the user interact with the app in the terminal
def main():
    print("welcome to the emotion management assistant 💭")
    print("1. create table")
    print("2. add an emotion and advice")
    print("3. exit")

    choice = input("choose an option: ")

    if choice == "1":
        create_emotions_table()
    elif choice == "2":
        emotion = input("enter emotion: ")
        advice = input("enter advice for this emotion: ")
        add_emotion(emotion, advice)
    elif choice == "3":
        print("goodbye! stay emotionally balanced 🌱")
    else:
        print("invalid option, please try again.")

if __name__ == "__main__":
    main()

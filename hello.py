from helper import Message

def main():
    msg = input("Enter the message to print in develop: ")
    Message.greeting(msg)


if __name__ == "__main__":
    main()
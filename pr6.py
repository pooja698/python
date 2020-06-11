def string_alternative():
    str = 'Good Evening'
    for i in range(0,len(str),2) :
        print(str[i], end="")


def main():
    string_alternative()


if __name__ == "__main__":
    main()
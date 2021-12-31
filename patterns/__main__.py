from patterns import behavioral, creational, structural

types = {"creational": creational, "behavioral": behavioral, "structural": structural}


def main():
    print("Welcome to the design patterns CLI.\n")
    while True:
        pattern_type: str = input(f"Which type? ({', '.join(types.keys())}): ")
        try:
            types[pattern_type].main()
        except KeyError:
            print(f"Type {pattern_type} not found. Finishing software.")
            break


if __name__ == "__main__":
    main()

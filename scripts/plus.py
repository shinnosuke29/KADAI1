import sys

def main():
    total = 0
    for line in sys.stdin:
        try:
            total += int(line.strip())
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.", file=sys.stderr)
            sys.exit(1)
    print(total)

if __name__ == "__main__":
    main()

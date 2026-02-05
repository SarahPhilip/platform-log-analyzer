import sys


def analyze_log(filename):
    errors = []

    try:
        with open(filename) as f:
            for line in f:
                if "ERROR" in line:
                    errors.append(line.strip())
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]

    errors = analyze_log(log_file)

    with open("report.txt", "w") as f:
    	f.write(f"Total errors: {len(errors)}\n")

    	for e in errors:
        	f.write(e + "\n")

    print("Report saved to report.txt")

    for e in errors:
        print(e)


if __name__ == "__main__":
    main()


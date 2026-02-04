def analyze_log(filename):
    errors = []
    with open(filename) as f:
        for line in f:
            if "ERROR" in line:
                errors.append(line.strip())

    return errors


def main():
    log_file = "sample.log"
    errors = analyze_log(log_file)

    print(f"Total errors: {len(errors)}")
    for e in errors:
        print(e)


if __name__ == "__main__":
    main()

def log(message: str, filename: str = "log.txt"):
    with open(filename, "a") as f:
        f.write(message + "\n")

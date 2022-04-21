import os

def main(filename) :
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + ".csv")

if __name__ == "__main__":
    main('Jmeter_log1.jtl')
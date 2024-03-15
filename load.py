import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: python load.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    subprocess.run(["python3", "dpre.py", file_path])

if __name__ == "__main__":
    main()

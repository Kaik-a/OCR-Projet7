"""Main python file to execute"""
from app.main import app


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
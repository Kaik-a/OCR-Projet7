"""Main python file to execute"""
from app.main import APP  # pylint: disable=cyclic-import


def main():
    """Main method"""
    APP.run(debug=True)


if __name__ == "__main__":
    main()

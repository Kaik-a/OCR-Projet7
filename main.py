"""Main python file to execute"""
from maps import maps
from wiki import wiki


def main():
    print(wiki.get_info_on_loc(maps.get_location("tour eiffel")))


if __name__ == "__main__":
    main()

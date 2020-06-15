"""Main python file to execute"""
from app import app, maps, wiki, parser


def main():
    question = input("Search ? ")
    #
    coordonates = maps.get_location(parser.prepare(question))
    #
    print(wiki.endow(wiki.get_info_on_loc(coordonates)))

    #app.run(debug=True)


if __name__ == "__main__":
    main()

#import re and (optionally) sys
#def main
#def parse
    #takes str of html as input
    #identifies any YouTube URL that is the src value of an iframe element
    #return a shorter youtu.be url as a str

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<iframe (?:width="\d*" height="\d*" )?src="https?://(?:www\.)?(?:youtube\.com|youtu\.be)/embed/(\w*)"(?: title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>', s):
        URL = (f"https://youtu.be/{matches.group(1)}")
        return(URL)
    else:
        return(None)


if __name__ == "__main__":
    main()

#revisit and improve parse function
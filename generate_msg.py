import argparse
import markovify


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--sentences", type=int,
        help="how many sentenses to generate")
    ap.add_argument("-w", "--words", type=int,
        help="how many words in sentence")
    args = vars(ap.parse_args())

    with open("./data/corpus.txt", encoding='utf-8') as f:
        text = f.read()

    text_model = markovify.Text(text, well_formed=False)
    text_model = text_model.compile(inplace=True)

    for _ in range(args["sentences"]):
        print(text_model.make_short_sentence(args["words"]))


if __name__ == "__main__":
    main()

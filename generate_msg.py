import markovify


def main():
    with open("messages.txt", encoding='utf-8') as f:
        text = f.read()

    text_model = markovify.Text(text, well_formed=False)
    text_model = text_model.compile(inplace=True)

    for i in range(1):
        print(text_model.make_short_sentence(100))


if __name__ == "__main__":
    main()

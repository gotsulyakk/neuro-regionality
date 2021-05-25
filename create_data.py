import json


def main():
    with open('channel_messages.json') as f:
        raw_data = json.load(f)
    
    text = ""
    for elem in raw_data:
        if "message" in elem:
            text += str(elem["message"] + "\n")

    with open("messages.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()

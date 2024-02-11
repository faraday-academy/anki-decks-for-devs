import genanki
import json
import os
import sys

from anki_model import simple_qa_model


def load_json_data(json_file_path):
    with open(json_file_path, "r") as file:
        return json.load(file)


def create_deck_from_json(data):
    deck = genanki.Deck(data["deck_id"], data["deck_name"])

    for card in data["cards"]:
        note = genanki.Note(model=simple_qa_model, fields=[card["front"], card["back"]])
        note.tags = card["tags"]
        deck.add_note(note)

    return deck


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <json_deck_file>")
        sys.exit(1)

    json_file_name = sys.argv[1]
    json_file_path = os.path.join("./", json_file_name)

    if not os.path.exists(json_file_path):
        print(f"File {json_file_path} not found.")
        sys.exit(1)

    data = load_json_data(json_file_path)

    deck = create_deck_from_json(data)

    output_dir = "generated_apkg_files"
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = os.path.join(
        output_dir, f"{data['deck_name'].replace(' ', '_')}.apkg"
    )

    if os.path.exists(output_file_path):
        overwrite = (
            input(f"The file {output_file_path} already exists. Overwrite? (y/n): ")
            .strip()
            .lower()
        )
        if overwrite != "y":
            print("Operation cancelled.")
            sys.exit(0)

    genanki.Package(deck).write_to_file(output_file_path)
    print(f"Deck generated successfully: {output_file_path}")


if __name__ == "__main__":
    main()

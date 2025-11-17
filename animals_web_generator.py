import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info():
    try:
        output = ''  # define an empty string

        # Read the JSON file
        animals_data = load_data('animals_data.json')

        # Process each animal
        for animal in animals_data:
            print("-" * 30)
            output += "<li class=\"cards__item\">"

            # Print name if it exists
            if 'name' in animal:
                print(f"Name: {animal['name']}")
                output += f"<strong>Name:</strong> {animal['name']}<br/>\n"

            # Print diet if it exists (nested under characteristics)
            if 'characteristics' in animal and 'diet' in animal['characteristics']:
                print(f"Diet: {animal['characteristics']['diet']}")
                output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

            # Print first location if locations list exists and is not empty
            if 'locations' in animal and animal['locations']:
                print(f"Location: {animal['locations'][0]}")
                output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

            # Print type if it exists (using taxonomy class as type)
            if 'taxonomy' in animal and 'class' in animal['taxonomy']:
                print(f"Type: {animal['taxonomy']['class']}")
                output += f"<strong>Type:</strong> {animal['taxonomy']['class']}<br/>\n"

            output += "</li>"

        print(output)
    except FileNotFoundError:
        print("Error: animals_data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    print_animal_info()

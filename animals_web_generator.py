import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info():
    try:
        # Read the JSON file
        animals_data = load_data('animals_data.json')

        # Process each animal
        for animal in animals_data:
            print("-" * 30)

            # Print name if it exists
            if 'name' in animal:
                print(f"Name: {animal['name']}")

            # Print diet if it exists (nested under characteristics)
            if 'characteristics' in animal and 'diet' in animal['characteristics']:
                print(f"Diet: {animal['characteristics']['diet']}")

            # Print first location if locations list exists and is not empty
            if 'locations' in animal and animal['locations']:
                print(f"Location: {animal['locations'][0]}")

            # Print type if it exists (using taxonomy class as type)
            if 'taxonomy' in animal and 'class' in animal['taxonomy']:
                print(f"Type: {animal['taxonomy']['class']}")

    except FileNotFoundError:
        print("Error: animals_data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    print_animal_info()

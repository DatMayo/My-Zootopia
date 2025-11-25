import json


def load_data(file_path):
    """Load and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file to be loaded.
        
    Returns:
        dict: Parsed JSON data as a Python dictionary.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def write_to_html(file_path, content):
    """Write content to an HTML file.

    Args:
        file_path (str): Path where the HTML file will be created or overwritten.
        content (str): HTML content to be written to the file.

    Note:
        This will overwrite the file if it already exists.
    """
    with open(file_path, "w") as handle:
        handle.write(content)



def print_animal_info():
    """Process and display animal information from a JSON file.
    
    This function reads animal data from 'animals_data.json', extracts key information
    including name, diet, location, and animal type, then prints this information
    to both the console and formats it as HTML list items.
    
    The function handles several error cases:
    - Missing or inaccessible file
    - Invalid JSON format
    - Other unexpected errors
    
    Note:
        The HTML output is currently printed to console but not saved to a file.
        Consider using write_to_html() to save the output.
    """
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
        write_to_html("animals_template.html", output)
    except FileNotFoundError:
        print("Error: animals_data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    print_animal_info()

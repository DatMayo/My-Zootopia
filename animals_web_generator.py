import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class Animal:
    """Represents an animal with its properties."""
    name: str
    diet: Optional[str] = None
    location: Optional[str] = None
    animal_type: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'Animal':
        """Create an Animal instance from a dictionary.
        
        Args:
            data: Dictionary containing animal data
            
        Returns:
            Animal: A new Animal instance
        """
        return cls(
            name=data.get('name', 'Unknown'),
            diet=data.get('characteristics', {}).get('diet'),
            location=data.get('locations', [None])[0] if data.get('locations') else None,
            animal_type=data.get('taxonomy', {}).get('class')
        )

    def to_console(self) -> str:
        """Format animal data for console output."""
        lines = [f"Name: {self.name}"]
        if self.diet:
            lines.append(f"Diet: {self.diet}")
        if self.location:
            lines.append(f"Location: {self.location}")
        if self.animal_type:
            lines.append(f"Type: {self.animal_type}")
        return "\n".join(lines)

    def to_html(self) -> str:
        """Format animal data as an HTML list item."""
        html_parts = [f"<li class=\"cards__item\">"]
        html_parts.append(f"<strong>Name:</strong> {self.name}<br/>")

        if self.diet:
            html_parts.append(f"<strong>Diet:</strong> {self.diet}<br/>")
        if self.location:
            html_parts.append(f"<strong>Location:</strong> {self.location}<br/>")
        if self.animal_type:
            html_parts.append(f"<strong>Type:</strong> {self.animal_type}<br/>")

        html_parts.append("</li>")
        return "\n".join(html_parts)


def load_animals(file_path: str) -> List[Animal]:
    """Load and parse animal data from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing animal data.
        
    Returns:
        List[Animal]: List of Animal objects.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return [Animal.from_dict(animal) for animal in data]


def generate_html_content(animals: List[Animal]) -> str:
    """Generate HTML content from a list of animals.
    
    Args:
        animals: List of Animal objects to include in the HTML.
        
    Returns:
        str: Formatted HTML content.
    """
    header = """<!DOCTYPE html>
    <html>
    <head>
        <title>Animal Information</title>
        <style>
            @gray-darker:               #444444;
            @gray-dark:                 #696969;
            @gray:                      #999999;
            @gray-light:                #cccccc;
            @gray-lighter:              #ececec;
            @gray-lightest:             lighten(@gray-lighter,4%);
    
    
            html {
              background-color: #ffe9e9;
            }
    
            h1 {
                text-align: center;
                font-size: 40pt;
                font-weight: normal;
            }
    
            body {
              font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
              font-style: normal;
              font-weight: 400;
              letter-spacing: 0;
              padding: 1rem;
              text-rendering: optimizeLegibility;
              -webkit-font-smoothing: antialiased;
              -moz-osx-font-smoothing: grayscale;
              -moz-font-feature-settings: "liga" on;
              width: 900px;
              margin: auto;
            }
    
            .cards {
              list-style: none;
              margin: 0;
              padding: 0;
            }
    
            .cards__item {
              background-color: white;
              border-radius: 0.25rem;
              box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
              overflow: hidden;
              padding: 1rem;
              margin: 50px;
            }
    
            .card__title {
              color: @gray-dark;
              font-size: 1.25rem;
              font-weight: 300;
              letter-spacing: 2px;
              text-transform: uppercase;
            }
    
            .card__text {
              flex: 1 1 auto;
              font-size: 0.95rem;
              line-height: 2;
              margin-bottom: 1.25rem;
            }
        </style>
    </head>
    <body>
        <h1>Animal Information</h1>
        <ul style="list-style: none; padding: 0; display: flex; flex-wrap: wrap;">"""

    footer = """
        </ul>
    </body>
    </html>"""

    content = "\n".join(animal.to_html() for animal in animals)
    return f"{header}{content}{footer}"


def main():
    """Main function to process and display animal information."""
    try:
        # Configuration
        input_file = Path("animals_data.json")
        output_file = Path("animals.html")

        # Load and process data
        animals = load_animals(input_file)

        # Output to console
        for animal in animals:
            print("-" * 30)
            print(animal.to_console())

        # Generate and save HTML
        html_content = generate_html_content(animals)
        output_file.write_text(html_content, encoding='utf-8')
        print(f"\nHTML output has been saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()

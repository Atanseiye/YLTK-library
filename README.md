# Yoruba Language Took Kit

The Yoruba language toolkit was developed as a tool for processing and preprocessing Yoruba language.
In the similitude of how the NLTK works, where stopwords, stem, lemmas are handle while processing languages, the YLTK is also equipped with various tools ranging from the stopwords in Yoruba and other things are under development.

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Installation
Clone the repository:
   ```bash
   git clone https://github.com/username/project-name.git
   ```
Activate virtual environment
   ```bash
    YLTK\Scripts\activate
   ```
Install requirement
   ```bash
    pip install -r requirements.txt
   ```

Add you API_KEY
```bash
   export API_KEY='your-api-key-here'
   ```

## Usage
Run the script:
   ```bash
    python detect.py --url https://example.com
   ```

## Features
- Batch processing of large text to extract Yoruba texts alone with the method `extract_yoruba_words`.
- Frequency count for each words with the method `word_frequency_count`.
- Generate Stop words that is higher than a specified frequency with the method `stop_words`.
- Batch Stop words removal from a large Yoruba text using the method `remove_stopwords`

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature-name"`.
4. Push the branch: `git push origin feature-name`.
5. Submit a pull request.

## Testing
Run the tests using:
   ```bash
   pytest tests/
   ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Authors
1. Kolade Atanseiye: koladeatanseiye@gmail.com

from concurrent.futures import ThreadPoolExecutor, as_completed
import openai
from collections import Counter
import os
import re

# Load the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set!")

# Replace with your OpenAI API key
openai.api_key = api_key

class YLTK:
    def __init__():
        return 1
    

    
    # Getting the frequecy of words
    def word_frequency_count(text):

        # Helper function to count word frequencies for a chunk of text
        def count_words(text_chunk):
            # Preprocess the text: remove punctuation, convert to lowercase
            cleaned_text = re.sub(r'[^\w\s]', '', text_chunk).lower()

            # Split the text into words
            words = cleaned_text.split()

            # Use Counter to count occurrences of each word
            return Counter(words)

        # Split the text into smaller chunks for parallel processing
        chunk_size = len(text) // 4  # Adjust the number of chunks as needed
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

        # Use ThreadPoolExecutor to process the chunks in parallel
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(count_words, chunks))

        # Combine all word counts from each chunk
        total_word_counts = Counter()
        for result in results:
            total_word_counts.update(result)

        return dict(total_word_counts)

    # Generating the list of stop words
    def stop_words(file: dict):
        # Helper function to check if a word's frequency is greater than or equal to 5
        def check_word(word_item):
            word, count = word_item
            if count >= 5:
                return word
            return None

        # Get the maximum number of workers (CPU cores)
        max_workers = os.cpu_count()

        # Use ThreadPoolExecutor to process the word count items in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(check_word, file.items()))

        # Filter out the None values (words that don't meet the condition)
        list_of_stopWords = [word for word in results if word is not None]

        return list_of_stopWords
    
    def remove_stopwords(list_a, document_b):
        """
        Removes any text in list_a from document_b and returns the remaining text in document_b.

        :param list_a: List of strings to be removed
        :param document_b: The document (string) from which the text will be removed
        :return: The remaining text in document_b as a string
        """
        # Convert document_b into a list of words
        document_b_words = document_b.split()

        # Create a set from list_a for efficient lookup
        list_a_set = set(list_a)

        # Filter words in document_b that are not in list_a
        remaining_words = [word for word in document_b_words if word not in list_a_set]

        # Join the remaining words back into a single string
        return " ".join(remaining_words)
    